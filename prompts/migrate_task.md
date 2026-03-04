### Task migration from oe-eval-internal -> olmo-eval-internal

I'm trying to get parity with the oe-eval-internal task(s) {OE_EVAL_TASK_NAME} in the new olmo-eval-internal.

The old task config is located here:

```sh
/Users/dhei/ai2/migrate/oe-eval-internal/oe_eval/configs/models.py
```

Please add the new task config to olmo-eval-internal:

```sh
/Users/dhei/ai2/migrate/olmo-eval-internal/src/olmo_eval/evals/tasks
```

And, if relevant, add the corresponding task suite to the task suite registy:

```sh
/Users/dhei/ai2/migrate/olmo-eval-internal/src/olmo_eval/evals/suites
```

### Example query

When you test your changes, you will see an example request (labeled "Request")

Here's an example request from oe-eval-internal:

{EXAMPLE_QUERY}

PLEASE MAKE SURE THE MOCK REQUEST MATCHES THIS ONE!!

### Testing your changes

You can test the task with a mock solver here:

```sh
olmo-eval run -m mock {NEW_TASK_STR} --inspect
```

After you implement, please run the mock solver and make sure everything runs, and that the output looks reasonable.

### Additional Notes

- **Style:** Do NOT write any docstrings unless absolutely necessary
- **Style:** Do NOT write any comment delinators (e.g. `# =========`) unless absolutely necessary
- **Parity:** Often the spacing for the answer is off (or wrong). For instance, ending with "Answer: " instead of "Answer:". Please double check with the example query vs. your mock request, to make sure yours is correct!!
- **Parity:** Often oe-eval-internal manually specifies few-shot examples. If this is applicable to that config, make sure they are used!
- **Completeness**: Make sure to implement EVERY task variant that I ask for!