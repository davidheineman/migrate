Migrate tasks from oe-eval -> olmo-eval-internal with claude code

### setup

Install deps:

```sh
uv sync

# GIT_LFS_SKIP_SMUDGE=1 pip install git+https://github.com/allenai/olmo-3-eval-analysis.git@main

GIT_LFS_SKIP_SMUDGE=1 git clone --no-recurse-submodules https://github.com/allenai/olmo-3-eval-analysis.git /tmp/olmo-3-eval-analysis && pip install /tmp/olmo-3-eval-analysis
```

Clone both repos:

```sh
git clone https://github.com/allenai/oe-eval-internal
git clone https://github.com/allenai/olmo-eval-internal
```

### migrate

The task alias mapping is defined in constants.py. Modify that, then run:

```sh
python migrate.py
```