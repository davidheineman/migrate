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
    },
    {
        "old_tasks": [
            "coqa::xlarge",
        ],
        "new_tasks": [
            "coqa:gen::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "csqa:mc::xlarge",
            "csqa:rc::olmes:full",
        ],
        "new_tasks": [
            "csqa:mc::olmo3base",
            "csqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "drop::xlarge",
        ],
        "new_tasks": [
            "drop:gen::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "hellaswag:rc::xlarge",
        ],
        "new_tasks": [
            "hellaswag:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "jeopardy::xlarge",
        ],
        "new_tasks": [
            "jeopardy:gen::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lab_bench_dbqa",
        ],
        "new_tasks": [
            "lab_bench_dbqa::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lab_bench_protocolqa",
        ],
        "new_tasks": [
            "lab_bench_protocolqa::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lambada",
        ],
        "new_tasks": [
            "lambada::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "medmcqa:mc::none",
            "medmcqa:rc::none",
        ],
        "new_tasks": [
            "medmcqa:mc::olmo3base",
            "medmcqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "piqa:mc::xlarge",
            "piqa:rc::olmes:full",
        ],
        "new_tasks": [
            "piqa:mc::olmo3base",
            "piqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "qasper_yesno:rc::olmes",
        ],
        "new_tasks": [
            "qasper_yesno:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "sciq:mc::xlarge",
        ],
        "new_tasks": [
            "sciq:mc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "sciriff_yesno:rc::olmes",
        ],
        "new_tasks": [
            "sciriff_yesno:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "socialiqa:mc::xlarge",
            "socialiqa:rc::olmes:full",
        ],
        "new_tasks": [
            "socialiqa:mc::olmo3base",
            "socialiqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "squad::xlarge",
        ],
        "new_tasks": [
            "squad:gen::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "medqa_en:mc::none",
            "medqa_en:rc::none",
        ],
        "new_tasks": [
            "medqa_en:mc::olmo3base",
            "medqa_en:rc::olmo3base",
        ],
    },
]


# The datalake did not save example queries for these tasks
TASK_MAP_NO_EXAMPLES = [
    {
        "old_tasks": [
            "winogrande:rc::xlarge",
        ],
        "new_tasks": [
            "winogrande:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "naturalqs::xlarge",
            "naturalqs:mc::gen2mc:xlarge",
            "naturalqs:rc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "naturalqs:gen::olmo3base",
            "naturalqs:mc::olmo3base",
            "naturalqs:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_arithmetic:rc::olmes",
            "basic_skills_coding:rc::olmes",
            "basic_skills_common_knowledge:rc::olmes",
            "basic_skills_logical_reasoning:rc::olmes",
            "basic_skills_pattern:rc::olmes",
            "basic_skills_string_operations:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_arithmetic:rc::olmo3base",
            "basic_skills_coding:rc::olmo3base",
            "basic_skills_common_knowledge:rc::olmo3base",
            "basic_skills_logical_reasoning:rc::olmo3base",
            "basic_skills_pattern:rc::olmo3base",
            "basic_skills_string_operations:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "coqa:mc::gen2mc:xlarge",
            "coqa:rc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "coqa:mc::olmo3base",
            "coqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "drop:mc::gen2mc:xlarge",
            "drop:rc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "drop:mc::olmo3base",
            "drop:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "jeopardy:mc::gen2mc:xlarge",
            "jeopardy:rc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "jeopardy:mc::olmo3base",
            "jeopardy:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "sciq:rc::olmo3",
        ],
        "new_tasks": [
            "sciq:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "squad:mc::gen2mc:xlarge",
            "squad:rc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "squad:mc::olmo3base",
            "squad:rc::olmo3base",
        ],
    },
]
