import pandas as pd
import ast
from deviousutils.hf import pull_parquet_from_hf
from deviousutils.claude import create_cache_dir, run_claude_with_cache
# from constants import TASK_MAP
import concurrent.futures
from tqdm import tqdm

from olmo_eval.evals.tasks.common import list_tasks, list_variants
from pull_results import get_olmo_eval_results

TASK_MAP = [
    {
        "old_tasks": [
            "arc_challenge:mc::xlarge",
            "arc_easy:mc::xlarge",
        ],
        "new_tasks": [
            "arc_challenge:mc::olmo3base",
            "arc_easy:mc::olmo3base",
        ],
    }
]


def get_olmo_eval_tasks():
    """Get implemented tasks in olmo-eval, e.g. "medqa_en::olmo3base" """
    tasks = list_tasks()
    task_variant_pairs = []

    for task in tasks:
        variants = list_variants(task)[task]
        for variant in variants:
            task_variant_pairs.append(f"{task}::{variant}")

    return task_variant_pairs


def get_unimplemented_tasks():
    olmo_eval_tasks = get_olmo_eval_tasks()
    unimplemented_task_map = []

    for entry in TASK_MAP:
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
    # task_alias = task_alias.replace('gen2mc:xlarge', 'gen2mc') # manual fix: the example is the same
    filtered = df[df["task_alias"] == task_alias].copy()
    filtered["doc"] = filtered["doc"].apply(ast.literal_eval)
    filtered = filtered.sort_values("instance_id")
    docs = filtered["doc"].tolist()
    example_doc = docs[0]
    if "query" not in example_doc:
        raise RuntimeError(
            f"Docs in '{task_alias}' do not have 'query'!: {example_doc}"
        )
    example_query = example_doc["query"]
    return example_query


def create_migrate_prompt(oe_eval_task_names, new_task_names, example_query_str):
    prompt = read_prompt("prompts/migrate_task.md")

    new_task_str = " ".join([f"-t {task}" for task in new_task_names])

    print("Migrating task:\n\t" + f"olmo-eval run -m mock {new_task_str} --inspect")

    prompt = (
        prompt.replace("{OE_EVAL_TASK_NAME}", ", ".join(oe_eval_task_names))
        .replace("{NEW_TASK_STR}", new_task_str)
        .replace("{EXAMPLE_QUERY}", example_query_str)
    )


def create_debug_prompt(oe_eval_task_names, new_task_names, example_query_str):
    prompt = read_prompt("prompts/debug_task.md")

    # olmo-eval-internal
    olmo_eval_results = get_olmo_eval_results(
        dashboard="olmo-3-parity", 
        tasks=new_task_names
    )

    print(olmo_eval_results)
    raise

    # oe-eval-internal
    oe_eval_results = get_cookbook_results(
        dashboard="olmo3-paper-main",
        tasks=oe_eval_task_names,
        models=["Olmo-3-1025-7B:main"],
    )

    # TODO: get example inputs/outputs from dataframes if applicable


def execute_task(prompt):
    cache_dir = prepare_claude_env()

    # Execute prompt
    result, cache_dir = run_claude_with_cache(
        prompt,
        cache_dir=cache_dir,
        model_name="claude-opus-4-6",
        verbose=False,
        show_spinner=True,
    )
    rollout_dir = cache_dir / "rollout"

    return rollout_dir


def _migrate_and_return(args):
    oe_eval_task_names, new_task_names, example_queries_df = args

    example_query_str = ""
    for task in oe_eval_task_names:
        try:
            query = get_example_query(example_queries_df, task_alias=task)
        except Exception as e:
            raise RuntimeError(task)
        example_query_str += f"{task}\n```\n{query}\n```\n\n"

    # prompt = create_migrate_prompt(
    #     oe_eval_task_names,
    #     new_task_names,
    #     example_query_str
    # )

    prompt = create_debug_prompt(oe_eval_task_names, new_task_names, example_query_str)

    rollout_dir = execute_task(prompt)

    return rollout_dir


def main():
    task_map = get_unimplemented_tasks()

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

"""
olmo-eval beaker launch \
    -n "davidh-debug" -m allenai/Olmo-3-1025-7B -H default \
    -c h100 -w ai2/olmo-eval-debug -B ai2/oe-base --inspect --store -y \
    -g olmo-3-parity \
    --gpus 4 \
    -t arc_challenge:mc::olmo3base@urgent \
    -t arc_easy:mc::olmo3base@urgent \
    -t coqa:gen::olmo3base@urgent \
    -t csqa:mc::olmo3base@urgent \
    -t csqa:rc::olmo3base@urgent \
    -t drop:gen::olmo3base@urgent \
    -t hellaswag:rc::olmo3base@urgent \
    -t jeopardy:gen::olmo3base@urgent \
    -t lab_bench_dbqa::olmo3base@urgent \
    -t lab_bench_protocolqa::olmo3base@urgent \
    -t lambada::olmo3base@urgent \
    -t medmcqa:mc::olmo3base@urgent \
    -t medmcqa:rc::olmo3base@urgent \
    -t piqa:mc::olmo3base@urgent \
    -t piqa:rc::olmo3base@urgent \
    -t qasper_yesno:rc::olmo3base@urgent \
    -t sciq:mc::olmo3base@urgent \
    -t sciriff_yesno:rc::olmo3base@urgent \
    -t socialiqa:mc::olmo3base@urgent \
    -t socialiqa:rc::olmo3base@urgent \
    -t squad:gen::olmo3base@urgent \
    -t medqa_en:mc::olmo3base@urgent \
    -t medqa_en:rc::olmo3base@urgent

olmo-eval results query -G olmo-3-parity
"""
