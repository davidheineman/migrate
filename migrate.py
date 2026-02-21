import pandas as pd
import ast
from deviousutils.hf import pull_parquet_from_hf
from deviousutils.claude import create_cache_dir, run_claude_with_cache
from constants import TASK_MAP

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
    path = pull_parquet_from_hf(
        repo_id="allenai/olmo-3-eval-questions",
        split_name="instances"
    )

    df = pd.read_parquet(path)

    return df


def get_example_query(df, task_alias):
    filtered = df[df["task_alias"] == task_alias].copy()
    filtered["doc"] = filtered["doc"].apply(ast.literal_eval)
    filtered = filtered.sort_values("instance_id")
    docs = filtered["doc"].tolist()
    example_query = docs[0]["query"]
    return example_query


def migrate_task(oe_eval_task_names, new_task_names, example_queries_df):
    prompt = read_prompt("migrate_task.md")

    new_task_str = ' '.join([f'-t {task}' for task in new_task_names])

    example_query_str = ""
    for task in oe_eval_task_names:
        query = get_example_query(example_queries_df, task_alias=task)
        example_query_str += f"{task}\n```\n{query}\n```\n\n"

    print("Migrating task:\n\t" + f"olmo-eval run -m mock {new_task_str} --inspect")

    prompt = (
        prompt
        .replace("{OE_EVAL_TASK_NAME}", ', '.join(oe_eval_task_names))
        .replace("{NEW_TASK_STR}", new_task_str)
        .replace("{EXAMPLE_QUERY}", example_query_str)
    )

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
    old_tasks, new_tasks, df = args
    return migrate_task(
        oe_eval_task_names=old_tasks,
        new_task_names=new_tasks,
        example_queries_df=df
    )


def main():
    import concurrent.futures
    from tqdm import tqdm

    df = load_example_queries()

    task_pairs = [(entry["old_tasks"], entry["new_tasks"], df.copy()) for entry in TASK_MAP]

    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        results = list(
            tqdm(
                executor.map(_migrate_and_return, task_pairs),
                total=len(task_pairs),
                desc="Migrating tasks"
            )
        )


if __name__ == '__main__':
    main()

"""
olmo-eval beaker launch \
    -n "davidh-debug" -m allenai/Olmo-3-1025-7B -H default -t "piqa:mc:olmo3base@urgent" -t "piqa:rc:olmo3base@urgent" \
    -c h100 -w ai2/olmo-eval-debug -B ai2/oe-base --inspect -y
"""