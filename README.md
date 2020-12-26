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

Spawn a shell inside the poetry environment, then call pytest:

```sh
poetry shell
pytest
```