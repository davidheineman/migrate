from cookbook.eval.results import (
    make_dashboard_table,
    find_missing_tasks,
    make_results_from_dashboard
)

def get_cookbook_results(dashboard, tasks, models):
    add_data = {}

    if isinstance(dashboard, str):
        dashboard = [dashboard]

    for _dashboard in dashboard:
        # we get the metrics table from the datalake
        dashboard_table = make_dashboard_table(
            dashboard=_dashboard,
            force=False,
            skip_on_fail=True,
        )

        # we subselect the right tasks and models, plus expand named tasks
        results = make_results_from_dashboard(
            dashboard_table=dashboard_table,
            tasks=tasks,
            models=models,
        )

        # we find missing tasks in the results
        missing_tasks = find_missing_tasks(results=results)

        data = results._data

        # Load results into dict
        for eval_key, model_dict in data.items():
            if eval_key not in add_data:
                add_data[eval_key] = {}
            for model_name, results in model_dict.items():
                if model_name not in add_data[eval_key]:
                    add_data[eval_key][model_name] = results

    return add_data