### Task parity debugging from in olmo-eval-internal

I'm trying to get parity with the oe-eval-internal task(s) {OE_EVAL_TASK_NAME} in the new olmo-eval-internal.

The old task config is located here:

```sh
/Users/dhei/ai2/migrate/oe-eval-internal/oe_eval/configs/models.py
```

And the new task is located in a file in this folder:

```sh
/Users/dhei/ai2/migrate/olmo-eval-internal/src/olmo_eval/evals/tasks
```

However, when I ran the results from the new task I implemented on the Olmo 3 7B LLM, the scores are different!

### results in oe-eval-internal (old suite)

CSQA MC       & 75.3 
HellaSwag RC  & 77.7 
MedMCQA MC    & 48.3 

### results in olmo-eval-internal (new suite)

                         Results Summary                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Task                    ┃ Status  ┃ Metric           ┃ Result ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ csqa:mc::olmo3base      │ Success │ accuracy:logprob │ 0.7715 │
│ hellaswag:rc::olmo3base │ Success │ accuracy:logprob │ 0.5616 │
│ medqa_en:mc::olmo3base  │ Success │ accuracy:logprob │ 0.4156 │
└─────────────────────────┴─────────┴──────────────────┴────────┘

### your task

Can you debug the task? Ensure the implementation is the EXACT SAME between libraries. Please run scripts when applicable to check this.

### things to double-check

- Are the number of instances the same between the two sets?
- Is the prompt formatting for the input the same?