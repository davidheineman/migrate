TASK_MAP_SET_1 = [
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
            "sciq:mc::xlarge",
        ],
        "new_tasks": [
            "sciq:mc::olmo3base",
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
    {
        "old_tasks": [
            "mmlu_stem:mc",
            "mmlu_humanities:mc",
            "mmlu_social_sciences:mc",
            "mmlu_other:mc",
        ],
        "new_tasks": [
            "mmlu:stem:mc::olmo3base",
            "mmlu:humanities:mc::olmo3base",
            "mmlu:social_sciences:mc::olmo3base",
            "mmlu:other:mc::olmo3base",
        ],
    },
]

TASK_MAP_SET_2 = [
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
            "qasper_yesno:rc::olmes",
        ],
        "new_tasks": [
            "qasper_yesno:rc::olmo3base",
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
]

# These are not yet implemented
TASK_MAP_SET_3 = [
    {
        "old_tasks": [
            "coqa:mc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "coqa:mc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "drop:mc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "drop:mc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "jeopardy:mc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "jeopardy:mc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "naturalqs:mc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "naturalqs:mc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "squad:mc::gen2mc:xlarge",
        ],
        "new_tasks": [
            "squad:mc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "winogrande:rc::xlarge",
        ],
        "new_tasks": [
            "winogrande:rc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_arithmetic:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_arithmetic:rc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_coding:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_coding:rc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_common_knowledge:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_common_knowledge:rc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_logical_reasoning:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_logical_reasoning:rc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_string_operations:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_string_operations:rc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_pattern:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_pattern:rc::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "gsm8k::olmo3:n8:v2",
        ],
        "new_tasks": [
            "gsm8k::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "gsm_symbolic::olmo3:n8:v2",
        ],
        "new_tasks": [
            "gsm_symbolic::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "gsm_symbolic:p1::olmo3:n8:v2",
        ],
        "new_tasks": [
            "gsm_symbolic:p1::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "gsm_symbolic:p2::olmo3:n8:v2",
        ],
        "new_tasks": [
            "gsm_symbolic:p2::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_algebra::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_algebra::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_counting_and_probability::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_counting_and_probability::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_geometry::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_geometry::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_intermediate_algebra::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_intermediate_algebra::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_number_theory::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_number_theory::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_prealgebra::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_prealgebra::olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_precalculus::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_precalculus::olmo3base",
        ]
    },
]

# This set should be implemented, but may not have RC task configs
TASK_MAP_SET_4 = [
    {
        "old_tasks": [
            "arc_challenge:rc::xlarge"
        ], 
        "new_tasks": [
            "arc_challenge:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "arc_easy:rc::xlarge"
        ], 
        "new_tasks": [
            "arc_easy:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "mmlu_stem:rc"
        ], 
        "new_tasks": [
            "mmlu:stem:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "mmlu_humanities:rc"
        ], 
        "new_tasks": [
            "mmlu:humanities:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "mmlu_other:rc"
        ], 
        "new_tasks": [
            "mmlu:other:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "mmlu_social_sciences:mc"
        ], 
        "new_tasks": [
            "mmlu:social_sciences:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "csqa:rc::olmes:full"
        ], 
        "new_tasks": [
            "csqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "hellaswag:rc::olmes:full"
        ], 
        "new_tasks": [
            "hellaswag:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "winogrande:rc::olmes:full"
        ], 
        "new_tasks": [
            "winogrande:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "socialiqa:rc::olmes:full"
        ], 
        "new_tasks": [
            "socialiqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "piqa:rc::olmes:full"
        ], 
        "new_tasks": [
            "piqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "coqa:rc::gen2mc:xlarge"
        ], 
        "new_tasks": [
            "coqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "drop:rc::gen2mc:xlarge"
        ], 
        "new_tasks": [
            "drop:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "jeopardy:rc::gen2mc:xlarge"
        ], 
        "new_tasks": [
            "jeopardy:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "naturalqs:rc::gen2mc:xlarge"
        ], 
        "new_tasks": [
            "naturalqs:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "squad:rc::gen2mc:xlarge"
        ], 
        "new_tasks": [
            "squad:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "sciq:rc::olmo3"
        ], 
        "new_tasks": [
            "sciq:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "qasper_yesno:rc::olmes"
        ], 
        "new_tasks": [
            "qasper_yesno:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_arithmetic:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_arithmetic:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_coding:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_coding:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_common_knowledge:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_common_knowledge:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_logical_reasoning:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_logical_reasoning:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_string_operations:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_string_operations:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_pattern:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_pattern:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lab_bench_dbqa"
        ], 
        "new_tasks": [
            "lab_bench_dbqa::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lab_bench_protocolqa"
        ], 
        "new_tasks": [
            "lab_bench_protocolqa::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lambada"
        ], 
        "new_tasks": [
            "lambada",
        ],
    },
    {
        "old_tasks": [
            "medmcqa:rc::none"
        ], 
        "new_tasks": [
            "medmcqa:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "medqa_en:rc::none"
        ], 
        "new_tasks": [
            "medqa_en:rc::olmo3base",
        ],
    },
    {
        "old_tasks": [
            "sciriff_yesno:rc::olmes"
        ], 
        "new_tasks": [
            "sciriff_yesno:rc::olmo3base",
        ],
    }
]

TASK_MAP_SET_5 = [
    # This will have QA and Math BPB sets.
]

TASK_MAP_SET_6 = [
    # This will have Code Gen sets (should be more challenging b/c of execution)
]