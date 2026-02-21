Migrate tasks from oe-eval -> olmo-eval-internal with claude code

### setup

```sh
uv pip install deviousutils pandas tqdm
```

### migrate

The task alias mapping is defined in constants.py. Modify that, then run:

```sh
python migrate.py
```