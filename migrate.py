import os
import pandas as pd
import ast
from deviousutils.hf import pull_parquet_from_hf
from deviousutils.claude import create_cache_dir, run_claude_with_cache
from constants import TASK_MAP_SET_1, TASK_MAP_SET_2, TASK_MAP_SET_3, TASK_MAP_SET_4, TASK_MAP_SET_5
import concurrent.futures
from tqdm import tqdm
from termcolor import cprint

from olmo_eval.evals.tasks.common import list_tasks, list_variants
from pull_olmo_eval import get_olmo_eval_results
from pull_cookbook import get_cookbook_results

# MODE = "implement"
MODE = "debug"

# PARITY_MODEL_ALIAS = "allenai/Olmo-3-1025-7B"
PARITY_MODEL_ALIAS = "allenai/OLMo-2-0425-1B"

# TASK_MAP = TASK_MAP_SET_3
TASK_MAP = TASK_MAP_SET_4
# TASK_MAP = TASK_MAP_SET_5


def get_olmo_eval_tasks():
    """Get implemented tasks in olmo-eval, e.g. "medqa_en::olmo3base" """
    tasks = list_tasks()
    task_variant_pairs = []

    for task in tasks:
        variants = list_variants(task)[task]
        for variant in variants:
            task_variant_pairs.append(f"{task}::{variant}")

    return task_variant_pairs


def get_unimplemented_tasks(task_map):
    olmo_eval_tasks = get_olmo_eval_tasks()
    unimplemented_task_map = []

    for entry in task_map:
        new_tasks = entry["new_tasks"]
        # If ANY new_task in new_tasks is not in olmo_eval_tasks, add entry to unimplemented_task_map
        if any(new_task not in olmo_eval_tasks for new_task in new_tasks):
            unimplemented_task_map += [entry]

    return unimplemented_task_map


def prepare_claude_env():
    # Create rollout dir
    cache_dir = create_cache_dir()
    rollout_dir = cache_dir / "rollout"
    rollout_dir.mkdir(parents=True, exist_ok=True)

    ### (add logic here!)

    return cache_dir


def read_prompt(prompt_path):
    # Load prompt
    with open(prompt_path, "r") as f:
        prompt_template = f.read()

    return prompt_template


def load_example_queries():
    # Base easy inputs
    base_easy_path = pull_parquet_from_hf(
        repo_id="davidheineman/olmo-3-eval-questions",
        split_name="olmo3_paper_pstar",
    )

    # Base main inputs
    base_main_path = pull_parquet_from_hf(
        repo_id="davidheineman/olmo-3-eval-questions",
        split_name="olmo3_paper_main",
    )

    df_easy = pd.read_parquet(base_easy_path)
    df_main = pd.read_parquet(base_main_path)
    df = pd.concat([df_easy, df_main], ignore_index=True)

    return df


def get_example_query(df, task_alias):
    # manual task remappings for examples:
    if task_alias == "mmlu_stem:rc":
        task_alias = "mmlu_college_computer_science:rc::olmes"
    elif task_alias == "mmlu_humanities:rc":
        task_alias = "mmlu_human_sexuality:rc::olmes"
    elif task_alias == "mmlu_other:rc":
        task_alias = "mmlu_nutrition:rc::olmes"
    elif task_alias == "mmlu_social_sciences:rc":
        task_alias = "mmlu_high_school_us_history:rc::olmes"
    
    # task_alias = task_alias.replace('gen2mc:xlarge', 'gen2mc') # manual fix: the example is the same
    filtered = df[df["task_alias"] == task_alias].copy()
    filtered["doc"] = filtered["doc"].apply(ast.literal_eval)
    filtered = filtered.sort_values("instance_id")
    docs = filtered["doc"].tolist()
    example_doc = docs[0]
    if "query" not in example_doc:
        cprint(f"Docs in '{task_alias}' do not have 'query'!: {example_doc}", "red")
        example_query = "This doc has no example query! Please complete the task without this."
    else:
        example_query = example_doc["query"]
    return example_query


def create_migrate_prompt(oe_eval_task_names, new_task_names, example_query_str):
    prompt = read_prompt("prompts/migrate_task.md")

    new_task_str = " ".join([f"-t {task}" for task in new_task_names])

    cprint("Migrating: " + f"olmo-eval run -m mock {new_task_str} --inspect", "green")

    prompt = (
        prompt.replace("{OE_EVAL_TASK_NAME}", ", ".join(oe_eval_task_names))
        .replace("{NEW_TASK_STR}", new_task_str)
        .replace("{EXAMPLE_QUERY}", example_query_str)
    )

    cprint(prompt, "blue")

    return prompt


def create_debug_prompt(oe_eval_task_names, new_task_names):
    prompt = read_prompt("prompts/debug_task.md")

    # # olmo-eval results query -G olmo-3-parity
    # # olmo-eval-internal
    # olmo_eval_results = get_olmo_eval_results(
    #     dashboard="olmo-3-parity-mar30", 
    #     tasks=new_task_names
    # )
    # print(olmo_eval_results)
    # raise

    # oe-eval-internal
    if PARITY_MODEL_ALIAS == "allenai/Olmo-3-1025-7B":
        # olmo-cookbook-eval results -d olmo3-paper-main -t winogrande:rc::xlarge -m Olmo-3-1025-7B:main
        oe_eval_results = get_cookbook_results(
            dashboard="olmo3-paper-main",
            tasks=oe_eval_task_names,
            models=["Olmo-3-1025-7B:main"],
        )
    elif PARITY_MODEL_ALIAS == "allenai/OLMo-2-0425-1B":
        # olmo-cookbook-eval results -d olmo-3-baseline -t mmlu:rc -m OLMo-2-0425-1B --skip-on-fail
        oe_eval_results = get_cookbook_results(
            dashboard="olmo-3-baseline",
            tasks=oe_eval_task_names,
            models=["OLMo-2-0425-1B"],
        )
    else:
        raise ValueError(PARITY_MODEL_ALIAS)

    cprint(f"{oe_eval_task_names} -> " + str(oe_eval_results), "green")

    if not oe_eval_results:
        raise RuntimeError(f"olmo-cookbook returned an empty dict for {oe_eval_task_names}!")

    new_task_str = " ".join([f"-t {task}" for task in new_task_names])

    prompt = (
        prompt
        .replace("{CWD}", os.getcwd())
        .replace("{OE_EVAL_TASK_NAME}", ", ".join(oe_eval_task_names))
        .replace("{OE_EVAL_RESULTS}", str(oe_eval_results))
        .replace("{NEW_TASK_STR}", new_task_str)
        .replace("{MODEL_ALIAS}", PARITY_MODEL_ALIAS)
    )

    cprint(prompt, "blue")

    return prompt


def execute_task(prompt):
    cache_dir = prepare_claude_env()

    # Execute prompt
    result, cache_dir = run_claude_with_cache(
        prompt,
        cache_dir=cache_dir,
        model_name="claude-opus-4-6",
        # verbose=False,
        # show_spinner=True,
        verbose=True,
        show_spinner=False,
    )
    rollout_dir = cache_dir / "rollout"

    return rollout_dir


def _migrate_and_return(args):
    oe_eval_task_names, new_task_names, example_queries_df = args

    if MODE == "implement":
        example_query_str = ""
        for task in oe_eval_task_names:
            try:
                query = get_example_query(example_queries_df, task_alias=task)
            except Exception as e:
                raise RuntimeError(task)
            example_query_str += f"{task}\n```\n{query}\n```\n\n"

        prompt = create_migrate_prompt(
            oe_eval_task_names,
            new_task_names,
            example_query_str
        )
    
    elif MODE == "debug":
        prompt = create_debug_prompt(
            oe_eval_task_names, 
            new_task_names
        )

    rollout_dir = execute_task(prompt)

    return rollout_dir


def main():
    if MODE == "implement":
        task_map = get_unimplemented_tasks(TASK_MAP)
    elif MODE == "debug":
        task_map = TASK_MAP
    else:
        raise ValueError(MODE)
    
    df = load_example_queries()

    task_pairs = [
        (entry["old_tasks"], entry["new_tasks"], df.copy()) for entry in task_map
    ]

    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        results = list(
            tqdm(
                executor.map(_migrate_and_return, task_pairs),
                total=len(task_pairs),
                desc="Migrating tasks",
            )
        )


if __name__ == "__main__":
    main()
