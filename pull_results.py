import subprocess
import os
import json

OLMO_EVAL_VENV_BIN = "~/ai2/migrate/olmo-eval-internal/.venv/bin"

def get_olmo_eval_results(dashboard, tasks):
    venv_bin = os.path.expanduser(OLMO_EVAL_VENV_BIN)
    
    cmd = [
        os.path.join(venv_bin, "olmo-cookbook-eval"),
        "results",
        "-d", dashboard,
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
        # Parse resulting JSON
        results_json = json.loads(process.stdout)
        return results_json
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error running olmo-eval results query: {e.stderr}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error parsing JSON output from olmo-eval: {e}")
