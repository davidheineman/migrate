import subprocess
import os
import json
import re

OLMO_EVAL_VENV_BIN = "~/ai2/migrate/olmo-eval-internal/.venv/bin"

_ANSI_RE = re.compile(r'\x1b\[[^a-zA-Z]*[a-zA-Z]')


def load_json_safe(raw: str) -> dict:
    """Parse JSON from a string that may contain ANSI escape sequences."""
    clean = _ANSI_RE.sub('', raw)
    json_start = clean.index('{')
    json_end = clean.rindex('}') + 1
    return json.loads(clean[json_start:json_end])


def get_olmo_eval_results(dashboard, tasks):
    venv_bin = os.path.expanduser(OLMO_EVAL_VENV_BIN)
    
    cmd = [
        os.path.join(venv_bin, "olmo-eval"),
        "results",
        "query",
        "-G", dashboard,
        "-f", "json"
    ]

    for task in tasks:
        cmd.extend(["-t", task])

    try:
        print(f"\033[94m{' '.join(cmd)}\033[0m")

        process = subprocess.run(
            cmd, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )

        results_json = load_json_safe(process.stdout)
        
        return results_json
    except subprocess.CalledProcessError as e:
        if "ConnectionTimeout" in (e.stderr or ""):
            raise RuntimeError("Please connect to AWS exit node on Tailscale")
        raise RuntimeError(f"Error running olmo-eval results query: {e.stderr}")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Error parsing JSON output from olmo-eval: {e}\nRaw stdout: {repr(process.stdout)}")


def make_score_summary(results):
    """E.g. ['minerva_math_flex: 0.534', 'exact_match_flex: 0.474', 'exact_match_flex: 0.152']"""

    # Collect all metric name: score pairs in results and print them as a list
    metric_score_list = []

    for model in results.get('models', []):
        for task in model.get('tasks', []):
            metrics = task.get('metrics', {})
            # metrics is usually like {'accuracy': {'exact_match_flex': 0.474}}
            for group, names_to_scores in metrics.items():
                if isinstance(names_to_scores, dict):
                    for metric_name, score in names_to_scores.items():
                        metric_score_list.append(f"{metric_name}: {score}")
                elif isinstance(names_to_scores, (int, float)):
                    metric_score_list.append(f"{group}: {names_to_scores}")
    
    return metric_score_list


if __name__ == '__main__':
    results = get_olmo_eval_results(
        dashboard="math-benchmarks",
        tasks=["math500"]
    )

    metric_score_list = make_score_summary(results)

    print(metric_score_list)
