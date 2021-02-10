# Example Usage

First download the dependencies using poetry:

```sh
pip install poetry
poetry install
```

Then run the CLI:

```sh
poetry run memorizer --path data/test.json --count 3
```

# Running The Tests

Make sure to first download the dependencies using poetry:

```sh
pip install poetry
poetry install
```

Then spawn a shell inside the poetry environment and call pytest:

```sh
poetry shell
pytest
```