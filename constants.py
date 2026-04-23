TASK_MAP_SET_1 = [
    {
        "old_tasks": [
            "arc_challenge:mc::xlarge",
            "arc_easy:mc::xlarge",
        ],
        "new_tasks": [
            "arc_challenge:mc:olmo3base",
            "arc_easy:mc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "coqa::xlarge",
        ],
        "new_tasks": [
            "coqa:gen:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "csqa:mc::xlarge",
            "csqa:rc::olmes:full",
        ],
        "new_tasks": [
            "csqa:mc:olmo3base",
            "csqa:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "drop::xlarge",
        ],
        "new_tasks": [
            "drop:gen:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "hellaswag:rc::xlarge",
        ],
        "new_tasks": [
            "hellaswag:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "jeopardy::xlarge",
        ],
        "new_tasks": [
            "jeopardy:gen:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lambada",
        ],
        "new_tasks": [
            "lambada:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "medmcqa:mc::none",
            "medmcqa:rc::none",
        ],
        "new_tasks": [
            "medmcqa:mc:olmo3base",
            "medmcqa:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "piqa:mc::xlarge",
            "piqa:rc::olmes:full",
        ],
        "new_tasks": [
            "piqa:mc:olmo3base",
            "piqa:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "sciq:mc::xlarge",
        ],
        "new_tasks": [
            "sciq:mc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "socialiqa:mc::xlarge",
            "socialiqa:rc::olmes:full",
        ],
        "new_tasks": [
            "socialiqa:mc:olmo3base",
            "socialiqa:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "squad::xlarge",
        ],
        "new_tasks": [
            "squad:gen:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "medqa_en:mc::none",
            "medqa_en:rc::none",
        ],
        "new_tasks": [
            "medqa_en:mc:olmo3base",
            "medqa_en:rc:olmo3base",
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
            "mmlu:stem:mc:olmo3base",
            "mmlu:humanities:mc:olmo3base",
            "mmlu:social_sciences:mc:olmo3base",
            "mmlu:other:mc:olmo3base",
        ],
    },
]

TASK_MAP_SET_2 = [
    {
        "old_tasks": [
            "lab_bench_dbqa",
        ],
        "new_tasks": [
            "lab_bench_dbqa:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lab_bench_protocolqa",
        ],
        "new_tasks": [
            "lab_bench_protocolqa:olmo3base",
        ],
    },

    {
        "old_tasks": [
            "qasper_yesno:rc::olmes",
        ],
        "new_tasks": [
            "qasper_yesno:rc:olmo3base",
        ],
    },

    {
        "old_tasks": [
            "sciriff_yesno:rc::olmes",
        ],
        "new_tasks": [
            "sciriff_yesno:rc:olmo3base",
        ],
    },
]

# These are not yet implemented
TASK_MAP_SET_3 = [
    {
        "old_tasks": [
            "coqa:mc::gen2mc", # (not :xlarge!)
        ],
        "new_tasks": [
            "coqa:mc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "drop:mc::gen2mc", # (not :xlarge!)
        ],
        "new_tasks": [
            "drop:mc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "jeopardy:mc::gen2mc", # (not :xlarge!)
        ],
        "new_tasks": [
            "jeopardy:mc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "naturalqs:mc::gen2mc", # (not :xlarge!)
        ],
        "new_tasks": [
            "naturalqs:mc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "squad:mc::gen2mc", # (not :xlarge!)
        ],
        "new_tasks": [
            "squad:mc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "winogrande:rc::xlarge",
        ],
        "new_tasks": [
            "winogrande:rc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_arithmetic:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_arithmetic:rc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_coding:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_coding:rc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_common_knowledge:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_common_knowledge:rc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_logical_reasoning:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_logical_reasoning:rc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_string_operations:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_string_operations:rc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "basic_skills_pattern:rc::olmes",
        ],
        "new_tasks": [
            "basic_skills_pattern:rc:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "gsm8k::olmo3:n8:v2",
        ],
        "new_tasks": [
            "gsm8k:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "gsm_symbolic::olmo3:n8:v2",
        ],
        "new_tasks": [
            "gsm_symbolic:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "gsm_symbolic:p1::olmo3:n8:v2",
        ],
        "new_tasks": [
            "gsm_symbolic:p1:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "gsm_symbolic:p2::olmo3:n8:v2",
        ],
        "new_tasks": [
            "gsm_symbolic:p2:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_algebra::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_algebra:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_counting_and_probability::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_counting_and_probability:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_geometry::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_geometry:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_intermediate_algebra::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_intermediate_algebra:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_number_theory::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_number_theory:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_prealgebra::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_prealgebra:olmo3base",
        ]
    },
    {
        "old_tasks": [
            "minerva_math_precalculus::olmes:n4:v2",
        ],
        "new_tasks": [
            "minerva_math_precalculus:olmo3base",
        ]
    },
]

# This set should be implemented, but may not have RC task configs
TASK_MAP_SET_4 = [
    {
        "old_tasks": [
            "arc_challenge:rc::olmes:full"
        ], 
        "new_tasks": [
            "arc_challenge:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "arc_easy:rc::olmes:full"
        ], 
        "new_tasks": [
            "arc_easy:rc:olmo3base",
        ],
    },
    # {
    #     "old_tasks": [
    #         "mmlu_stem:rc"
    #     ], 
    #     "new_tasks": [
    #         "mmlu:stem:rc:olmo3base",
    #     ],
    # },
    # {
    #     "old_tasks": [
    #         "mmlu_humanities:rc"
    #     ], 
    #     "new_tasks": [
    #         "mmlu:humanities:rc:olmo3base",
    #     ],
    # },
    # {
    #     "old_tasks": [
    #         "mmlu_other:rc"
    #     ], 
    #     "new_tasks": [
    #         "mmlu:other:rc:olmo3base",
    #     ],
    # },
    # {
    #     "old_tasks": [
    #         "mmlu_social_sciences:rc"
    #     ], 
    #     "new_tasks": [
    #         "mmlu:social_sciences:rc:olmo3base",
    #     ],
    # },
    {
        "old_tasks": [
            "mmlu:rc"
        ], 
        "new_tasks": [
            "mmlu:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "csqa:rc::olmes:full"
        ], 
        "new_tasks": [
            "csqa:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "hellaswag:rc::olmes:full"
        ], 
        "new_tasks": [
            "hellaswag:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "winogrande:rc::olmes:full"
        ], 
        "new_tasks": [
            "winogrande:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "socialiqa:rc::olmes:full"
        ], 
        "new_tasks": [
            "socialiqa:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "piqa:rc::olmes:full"
        ], 
        "new_tasks": [
            "piqa:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "coqa:rc::gen2mc" # no :xlarge !
        ], 
        "new_tasks": [
            "coqa:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "drop:rc::gen2mc" # no :xlarge !
        ], 
        "new_tasks": [
            "drop:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "jeopardy:rc::gen2mc" # no :xlarge !
        ], 
        "new_tasks": [
            "jeopardy:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "naturalqs:rc::gen2mc" # no :xlarge !
        ], 
        "new_tasks": [
            "naturalqs:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "squad:rc::gen2mc" # no :xlarge !
        ], 
        "new_tasks": [
            "squad:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "sciq:rc::olmo3"
        ], 
        "new_tasks": [
            "sciq:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "qasper_yesno:rc::olmes"
        ], 
        "new_tasks": [
            "qasper_yesno:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_arithmetic:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_arithmetic:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_coding:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_coding:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_common_knowledge:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_common_knowledge:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_logical_reasoning:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_logical_reasoning:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_string_operations:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_string_operations:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "basic_skills_pattern:rc::olmes"
        ], 
        "new_tasks": [
            "basic_skills_pattern:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lab_bench_dbqa"
        ], 
        "new_tasks": [
            "lab_bench_dbqa:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "lab_bench_protocolqa"
        ], 
        "new_tasks": [
            "lab_bench_protocolqa:olmo3base",
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
            "medmcqa:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "medqa_en:rc::none"
        ], 
        "new_tasks": [
            "medqa_en:rc:olmo3base",
        ],
    },
    {
        "old_tasks": [
            "sciriff_yesno:rc::olmes"
        ], 
        "new_tasks": [
            "sciriff_yesno:rc:olmo3base",
        ],
    }
]

# This will have QA and Math BPB sets.
TASK_MAP_SET_5 = [
    {
        "old_tasks": [
            "arc_challenge:bpb::olmes:full",
        ],
        "new_tasks": [
            "arc_challenge:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "arc_easy:bpb::olmes:full",
        ],
        "new_tasks": [
            "arc_easy:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mmlu:bpb",
        ],
        "new_tasks": [
            "mmlu:bpb"
        ]
    },
    {
        "old_tasks": [
            "csqa:bpb::olmes:full",
        ],
        "new_tasks": [
            "csqa:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "hellaswag:bpb::olmes:full",
        ],
        "new_tasks": [
            "hellaswag:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "winogrande:bpb::olmes:full",
        ],
        "new_tasks": [
            "winogrande:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "socialiqa:bpb::olmes:full",
        ],
        "new_tasks": [
            "socialiqa:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "piqa:bpb::olmes:full",
        ],
        "new_tasks": [
            "piqa:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "coqa:bpb::gen2mc", # no :xlarge !
        ],
        "new_tasks": [
            "coqa:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "drop:bpb::gen2mc", # no :xlarge !
        ],
        "new_tasks": [
            "drop:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "jeopardy:bpb::gen2mc", # no :xlarge !
        ],
        "new_tasks": [
            "jeopardy:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "naturalqs:bpb::gen2mc", # no :xlarge !
        ],
        "new_tasks": [
            "naturalqs:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "squad:bpb::gen2mc", # no :xlarge !
        ],
        "new_tasks": [
            "squad:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "sciq:bpb::olmo3",
        ],
        "new_tasks": [
            "sciq:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "qasper_yesno:bpb::olmes",
        ],
        "new_tasks": [
            "qasper_yesno:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "basic_skills_arithmetic:bpb::olmes",
        ],
        "new_tasks": [
            "basic_skills_arithmetic:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "basic_skills_coding:bpb::olmes",
        ],
        "new_tasks": [
            "basic_skills_coding:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "basic_skills_common_knowledge:bpb::olmes",
        ],
        "new_tasks": [
            "basic_skills_common_knowledge:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "basic_skills_logical_reasoning:bpb::olmes",
        ],
        "new_tasks": [
            "basic_skills_logical_reasoning:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "basic_skills_string_operations:bpb::olmes",
        ],
        "new_tasks": [
            "basic_skills_string_operations:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "basic_skills_pattern:bpb::olmes",
        ],
        "new_tasks": [
            "basic_skills_pattern:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "lab_bench_dbqa:bpb",
        ],
        "new_tasks": [
            "lab_bench_dbqa:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "lab_bench_protocolqa:bpb",
        ],
        "new_tasks": [
            "lab_bench_protocolqa:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "lambada:bpb",
        ],
        "new_tasks": [
            "lambada:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "medmcqa:bpb::none",
        ],
        "new_tasks": [
            "medmcqa:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "medqa_en:bpb::none",
        ],
        "new_tasks": [
            "medqa_en:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "sciriff_yesno:bpb::olmes",
        ],
        "new_tasks": [
            "sciriff_yesno:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "minerva_math_algebra:bpb::olmes",
        ],
        "new_tasks": [
            "minerva_math_algebra:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "minerva_math_counting_and_probability:bpb::olmes",
        ],
        "new_tasks": [
            "minerva_math_counting_and_probability:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "minerva_math_geometry:bpb::olmes",
        ],
        "new_tasks": [
            "minerva_math_geometry:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "minerva_math_intermediate_algebra:bpb::olmes",
        ],
        "new_tasks": [
            "minerva_math_intermediate_algebra:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "minerva_math_number_theory:bpb::olmes",
        ],
        "new_tasks": [
            "minerva_math_number_theory:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "minerva_math_prealgebra:bpb::olmes",
        ],
        "new_tasks": [
            "minerva_math_prealgebra:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "minerva_math_precalculus:bpb::olmes",
        ],
        "new_tasks": [
            "minerva_math_precalculus:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "codex_humaneval:3shot:bpb::none",
        ],
        "new_tasks": [
            "codex_humaneval:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mbpp:3shot:bpb::none",
        ],
        "new_tasks": [
            "mbpp:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:bash",
        ],
        "new_tasks": [
            "mt_mbpp_bash:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:c",
        ],
        "new_tasks": [
            "mt_mbpp_c:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:cpp",
        ],
        "new_tasks": [
            "mt_mbpp_cpp:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:csharp",
        ],
        "new_tasks": [
            "mt_mbpp_csharp:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:go",
        ],
        "new_tasks": [
            "mt_mbpp_go:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:haskell",
        ],
        "new_tasks": [
            "mt_mbpp_haskell:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:java",
        ],
        "new_tasks": [
            "mt_mbpp_java:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:javascript",
        ],
        "new_tasks": [
            "mt_mbpp_javascript:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:matlab",
        ],
        "new_tasks": [
            "mt_mbpp_matlab:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:php",
        ],
        "new_tasks": [
            "mt_mbpp_php:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:python",
        ],
        "new_tasks": [
            "mt_mbpp_python:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:r",
        ],
        "new_tasks": [
            "mt_mbpp_r:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:ruby",
        ],
        "new_tasks": [
            "mt_mbpp_ruby:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:rust",
        ],
        "new_tasks": [
            "mt_mbpp_rust:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:scala",
        ],
        "new_tasks": [
            "mt_mbpp_scala:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:swift",
        ],
        "new_tasks": [
            "mt_mbpp_swift:bpb:olmo3base"
        ]
    },
    {
        "old_tasks": [
            "mt_mbpp_v2fix:typescript",
        ],
        "new_tasks": [
            "mt_mbpp_typescript:bpb:olmo3base"
        ]
    }
]

TASK_MAP_SET_6 = [
    {
        "old_tasks": ["arc_challenge:mc::xlarge"],
        "new_tasks": ["arc_challenge:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["arc_easy:mc::xlarge"],
        "new_tasks": ["arc_easy:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["mmlu_stem:mc"],
        "new_tasks": ["mmlu:stem:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["medmcqa:mc::none"],
        "new_tasks": ["medmcqa:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["medqa_en:mc::none"],
        "new_tasks": ["medqa_en:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["sciq:mc::xlarge"],
        "new_tasks": ["sciq:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["mmlu_humanities:mc"],
        "new_tasks": ["mmlu:humanities:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["mmlu_other:mc"],
        "new_tasks": ["mmlu:other:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["mmlu_social_sciences:mc"],
        "new_tasks": ["mmlu:social_sciences:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["csqa:mc::xlarge"],
        "new_tasks": ["csqa:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["piqa:mc::xlarge"],
        "new_tasks": ["piqa:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["socialiqa:mc::xlarge"],
        "new_tasks": ["socialiqa:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["coqa:mc::gen2mc"],
        "new_tasks": ["coqa:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["drop:mc::gen2mc"],
        "new_tasks": ["drop:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["jeopardy:mc::gen2mc"],
        "new_tasks": ["jeopardy:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["naturalqs:mc::gen2mc"],
        "new_tasks": ["naturalqs:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["squad:mc::gen2mc"],
        "new_tasks": ["squad:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["hellaswag:rc::xlarge"],
        "new_tasks": ["hellaswag:rc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["lambada"],
        "new_tasks": ["lambada"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["winogrande:rc::xlarge"],
        "new_tasks": ["winogrande:rc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["basic_skills_arithmetic:rc::olmes"],
        "new_tasks": ["basic_skills_arithmetic:rc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["basic_skills_coding:rc::olmes"],
        "new_tasks": ["basic_skills_coding:rc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["basic_skills_common_knowledge:rc::olmes"],
        "new_tasks": ["basic_skills_common_knowledge:rc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["basic_skills_logical_reasoning:rc::olmes"],
        "new_tasks": ["basic_skills_logical_reasoning:rc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["basic_skills_string_operations:rc::olmes"],
        "new_tasks": ["basic_skills_string_operations:rc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["basic_skills_pattern:rc::olmes"],
        "new_tasks": ["basic_skills_pattern:rc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["drop::xlarge"],
        "new_tasks": ["drop:gen:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["jeopardy::xlarge"],
        "new_tasks": ["jeopardy:gen:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["squad::xlarge"],
        "new_tasks": ["squad:gen:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["coqa::xlarge"],
        "new_tasks": ["coqa:gen:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["gsm8k::olmo3:n8:v2"],
        "new_tasks": ["gsm8k:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["gsm_symbolic::olmo3:n8:v2"],
        "new_tasks": ["gsm_symbolic:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["gsm_symbolic:p1::olmo3:n8:v2"],
        "new_tasks": ["gsm_symbolic:p1:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["gsm_symbolic:p2::olmo3:n8:v2"],
        "new_tasks": ["gsm_symbolic:p2:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["minerva_math_algebra::olmes:n4:v2"],
        "new_tasks": ["minerva_math_algebra:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["minerva_math_counting_and_probability::olmes:n4:v2"],
        "new_tasks": ["minerva_math_counting_and_probability:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["minerva_math_geometry::olmes:n4:v2"],
        "new_tasks": ["minerva_math_geometry:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["minerva_math_intermediate_algebra::olmes:n4:v2"],
        "new_tasks": ["minerva_math_intermediate_algebra:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["minerva_math_number_theory::olmes:n4:v2"],
        "new_tasks": ["minerva_math_number_theory:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["minerva_math_prealgebra::olmes:n4:v2"],
        "new_tasks": ["minerva_math_prealgebra:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["minerva_math_precalculus::olmes:n4:v2"],
        "new_tasks": ["minerva_math_precalculus:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["arc_challenge:rc::olmes:full"],
        "new_tasks": ["arc_challenge:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["arc_easy:rc::olmes:full"],
        "new_tasks": ["arc_easy:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mmlu:rc"],
        "new_tasks": ["mmlu:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["csqa:rc::olmes:full"],
        "new_tasks": ["csqa:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["hellaswag:rc::olmes:full"],
        "new_tasks": ["hellaswag:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["winogrande:rc::olmes:full"],
        "new_tasks": ["winogrande:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["socialiqa:rc::olmes:full"],
        "new_tasks": ["socialiqa:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["piqa:rc::olmes:full"],
        "new_tasks": ["piqa:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["coqa:rc::gen2mc"],
        "new_tasks": ["coqa:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["drop:rc::gen2mc"],
        "new_tasks": ["drop:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["jeopardy:rc::gen2mc"],
        "new_tasks": ["jeopardy:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["naturalqs:rc::gen2mc"],
        "new_tasks": ["naturalqs:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["squad:rc::gen2mc"],
        "new_tasks": ["squad:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["sciq:rc::olmo3"],
        "new_tasks": ["sciq:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["qasper_yesno:rc::olmes"],
        "new_tasks": ["qasper_yesno:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_arithmetic:rc::olmes"],
        "new_tasks": ["basic_skills_arithmetic:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_coding:rc::olmes"],
        "new_tasks": ["basic_skills_coding:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_common_knowledge:rc::olmes"],
        "new_tasks": ["basic_skills_common_knowledge:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_logical_reasoning:rc::olmes"],
        "new_tasks": ["basic_skills_logical_reasoning:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_string_operations:rc::olmes"],
        "new_tasks": ["basic_skills_string_operations:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_pattern:rc::olmes"],
        "new_tasks": ["basic_skills_pattern:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["lab_bench_dbqa"],
        "new_tasks": ["lab_bench_dbqa:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["lab_bench_protocolqa"],
        "new_tasks": ["lab_bench_protocolqa:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["lambada"],
        "new_tasks": ["lambada"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["medmcqa:rc::none"],
        "new_tasks": ["medmcqa:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["medqa_en:rc::none"],
        "new_tasks": ["medqa_en:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["sciriff_yesno:rc::olmes"],
        "new_tasks": ["sciriff_yesno:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["arc_challenge:bpb::olmes:full"],
        "new_tasks": ["arc_challenge:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["arc_easy:bpb::olmes:full"],
        "new_tasks": ["arc_easy:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mmlu:bpb"],
        "new_tasks": ["mmlu:bpb"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["csqa:bpb::olmes:full"],
        "new_tasks": ["csqa:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["hellaswag:bpb::olmes:full"],
        "new_tasks": ["hellaswag:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["winogrande:bpb::olmes:full"],
        "new_tasks": ["winogrande:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["socialiqa:bpb::olmes:full"],
        "new_tasks": ["socialiqa:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["piqa:bpb::olmes:full"],
        "new_tasks": ["piqa:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["coqa:bpb::gen2mc"],
        "new_tasks": ["coqa:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["drop:bpb::gen2mc"],
        "new_tasks": ["drop:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["jeopardy:bpb::gen2mc"],
        "new_tasks": ["jeopardy:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["naturalqs:bpb::gen2mc"],
        "new_tasks": ["naturalqs:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["squad:bpb::gen2mc"],
        "new_tasks": ["squad:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["sciq:bpb::olmo3"],
        "new_tasks": ["sciq:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["qasper_yesno:bpb::olmes"],
        "new_tasks": ["qasper_yesno:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_arithmetic:bpb::olmes"],
        "new_tasks": ["basic_skills_arithmetic:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_coding:bpb::olmes"],
        "new_tasks": ["basic_skills_coding:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_common_knowledge:bpb::olmes"],
        "new_tasks": ["basic_skills_common_knowledge:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_logical_reasoning:bpb::olmes"],
        "new_tasks": ["basic_skills_logical_reasoning:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_string_operations:bpb::olmes"],
        "new_tasks": ["basic_skills_string_operations:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["basic_skills_pattern:bpb::olmes"],
        "new_tasks": ["basic_skills_pattern:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["lab_bench_dbqa:bpb"],
        "new_tasks": ["lab_bench_dbqa:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["lab_bench_protocolqa:bpb"],
        "new_tasks": ["lab_bench_protocolqa:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["lambada:bpb"],
        "new_tasks": ["lambada:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["medmcqa:bpb::none"],
        "new_tasks": ["medmcqa:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["medqa_en:bpb::none"],
        "new_tasks": ["medqa_en:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["sciriff_yesno:bpb::olmes"],
        "new_tasks": ["sciriff_yesno:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["minerva_math_algebra:bpb::olmes"],
        "new_tasks": ["minerva_math_algebra:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["minerva_math_counting_and_probability:bpb::olmes"],
        "new_tasks": ["minerva_math_counting_and_probability:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["minerva_math_geometry:bpb::olmes"],
        "new_tasks": ["minerva_math_geometry:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["minerva_math_intermediate_algebra:bpb::olmes"],
        "new_tasks": ["minerva_math_intermediate_algebra:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["minerva_math_number_theory:bpb::olmes"],
        "new_tasks": ["minerva_math_number_theory:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["minerva_math_prealgebra:bpb::olmes"],
        "new_tasks": ["minerva_math_prealgebra:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["minerva_math_precalculus:bpb::olmes"],
        "new_tasks": ["minerva_math_precalculus:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["codex_humaneval:3shot:bpb::none"],
        "new_tasks": ["codex_humaneval:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mbpp:3shot:bpb::none"],
        "new_tasks": ["mbpp:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:bash"],
        "new_tasks": ["mt_mbpp_bash:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:c"],
        "new_tasks": ["mt_mbpp_c:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:cpp"],
        "new_tasks": ["mt_mbpp_cpp:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:csharp"],
        "new_tasks": ["mt_mbpp_csharp:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:go"],
        "new_tasks": ["mt_mbpp_go:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:haskell"],
        "new_tasks": ["mt_mbpp_haskell:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:java"],
        "new_tasks": ["mt_mbpp_java:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:javascript"],
        "new_tasks": ["mt_mbpp_javascript:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:matlab"],
        "new_tasks": ["mt_mbpp_matlab:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:php"],
        "new_tasks": ["mt_mbpp_php:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:python"],
        "new_tasks": ["mt_mbpp_python:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:r"],
        "new_tasks": ["mt_mbpp_r:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:ruby"],
        "new_tasks": ["mt_mbpp_ruby:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:rust"],
        "new_tasks": ["mt_mbpp_rust:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:scala"],
        "new_tasks": ["mt_mbpp_scala:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:swift"],
        "new_tasks": ["mt_mbpp_swift:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["mt_mbpp_v2fix:typescript"],
        "new_tasks": ["mt_mbpp_typescript:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    }
]

TASK_MAP_SET_7 = [
    {
        "old_tasks": ["bigcodebench:3shot::olmo3:v2"],
        "new_tasks": ["bigcodebench:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["codex_humaneval:3shot::olmo3:n32:v2"],
        "new_tasks": ["humaneval:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["deepseek_leetcode::olmo3:n32:v2"],
        "new_tasks": ["deepseek_leetcode:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["ds1000:3shot::olmo3:v2"],
        "new_tasks": ["ds1000:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["mbpp:3shot::olmo3:n32:v2"],
        "new_tasks": ["mbpp:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["multipl-e-humaneval:n32:v2"],
        "new_tasks": ["multipl_humaneval:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["multipl-e-mbpp:n32:v2"],
        "new_tasks": ["multipl_mbpp:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["codex_humanevalfim_single::olmo3"],
        "new_tasks": ["humaneval_fim_single:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["codex_humanevalfim_multi::olmo3"],
        "new_tasks": ["humaneval_fim_multi:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["codex_humanevalfim_random::olmo3"],
        "new_tasks": ["humaneval_fim_random:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    }
]

TASK_MAP_SET_8 = [
    {
        "old_tasks": ["socialiqa:mc::xlarge"],
        "new_tasks": ["socialiqa:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["winogrande:rc::xlarge"],
        "new_tasks": ["winogrande:rc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["winogrande:bpb::olmes:full"],
        "new_tasks": ["winogrande:bpb:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["arc_challenge:mc::xlarge"],
        "new_tasks": ["arc_challenge:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["csqa:mc::xlarge"],
        "new_tasks": ["csqa:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["piqa:mc::xlarge"],
        "new_tasks": ["piqa:mc:olmo3base"],
        "parity_model": "allenai/Olmo-3-1025-7B"
    },
    {
        "old_tasks": ["lab_bench_dbqa"],
        "new_tasks": ["lab_bench_dbqa:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
    {
        "old_tasks": ["medmcqa:rc::none"],
        "new_tasks": ["medmcqa:rc:olmo3base"],
        "parity_model": "allenai/OLMo-2-0425-1B"
    },
]

TASK_MAP_SET_9 = [
    {
        "results": """\
{
    "harmbench":
    {
        "inverted_functional_category_asr_lower": {
            "contextual": 0.485
        }
    }
}

(you only need to ensure parity with this contextual subtask result)
""",
        "old_tasks": ["harmbench:wildguard_reasoning_answer"],
        "new_tasks": ["harmbench:wg_judge_thinking"],
        "parity_model": "swiss-ai/Apertus-8B-Instruct-2509"
    }
]