Migrate tasks from oe-eval -> olmo-eval-internal with claude code

### setup

Clone both repos:

```sh
git clone https://github.com/allenai/oe-eval-internal
git clone https://github.com/allenai/olmo-eval-internal
```

Install deps:

```sh
uv sync
```

### migrate

The task alias mapping is defined in constants.py. Modify that, then run:

```sh
python migrate.py
```