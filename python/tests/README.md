# Running the Python test suite

This package ships its own tests under `python/tests/`. The suite expects
optional Heather parsing dependencies and the development toolchain to be
installed before invoking `pytest`.

## Set up an environment

1. From the repository root, create or activate a Python 3.12+ virtual environment in
   the `python/` directory.
2. Install the package with the development and Heather extras so the parser and
   test tooling are available:
   ```bash
   pip install .[dev,heather]
   ```
3. Ensure imports resolve to the local sources by running tests from inside the
   `python/` directory (or export `PYTHONPATH=src`).

## Run all tests

From `python/`, run:
```bash
pytest
```

## Run only the Heather parsing tests

The Heather parsing fixtures live in `tests/dialects/heather/parsing`. To run only
those tests:
```bash
pytest tests/dialects/heather/parsing
```

## Run an individual parsing scenario

Each `.hat` fixture (for example, `ex_fn01.hat`) is consumed by
`test_parse_with_ir.py`. To target a single case, use `-k` with the relevant
parameter name. For `ex_fn01.hat`, run:
```bash
pytest tests/dialects/heather/parsing/test_parse_with_ir.py -k ex_fn01
```

If you need to preserve the generated temporary project files for debugging,
comment out the `shutil.rmtree` call near the end of `test_parse_with_ir.py`.
