### Task parity debugging from in olmo-eval-internal

I'm trying to get parity with the oe-eval-internal task(s) {OE_EVAL_TASK_NAME} in the new olmo-eval-internal.

The old task config is located here:

```sh
{CWD}/oe-eval-internal/oe_eval/configs/models.py
```

And the new task is located in a file in this folder:

```sh
{CWD}/olmo-eval-internal/src/olmo_eval/evals/tasks
```

However, when I ran the results from the new task I implemented on the Olmo 3 7B LLM, the scores are different!

### results in oe-eval-internal (old suite)

Here are the results when running on the legacy task suite:

```json
{OE_EVAL_RESULTS}
```

### results in olmo-eval-internal (new suite)

The tasks in the new eval suite (denoted by `{NEW_TASK_STR}`), can be run using this command:

```sh
# Run evals on new suite. Please use this command!
olmo-eval beaker launch \
    -n "claude-code-debugging" -m allenai/Olmo-3-1025-7B -H default \
    -c h100 -p urgent -B ai2/oe-base --inspect --store -y \
    -g olmo-3-parity-mar30 \
    -w ai2/olmo-3-evals \
    --gpus 4 \
    {NEW_TASK_STR}
```

This will launch and execute an remote eval command with GPUs. It uses Beaker Gantry, and requires **changes to be committed to Git in order to run**.

### your task

Can you debug the task? 

First, can you run the `olmo-eval beaker launch` command to get the current results from olmo-eval-internal? Then, modify the implementation and rerun `olmo-eval beaker launch`. Repeat until you reach parity.

Ensure the implementation is the EXACT SAME between libraries. Please run scripts when applicable to check this.

### things to double-check

- Are the number of instances the same between the two sets?
- Is the prompt formatting for the input the same?
- Is the pool of instances (train/val/test splits) the same? Are they ordered the same?
- Is the random seed the same?
- Are the in-context examples / ICL selection the same?
- Are the metrics the same? (BPB, F1, Exact Match, RC vs. MC Accuracy, ...)


### final reminders

Please begin by running the `olmo-eval beaker launch` command! Then, look at the results and debug from there. The `olmo-eval` command should take 5-30 minutes. After each change, please commit the change in `olmo-eval-internal/` GitHub.