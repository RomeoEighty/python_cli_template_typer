# python_cli_template_typer

A sample command-line application built with [Typer](https://typer.tiangolo.com/) and managed with [Poetry](https://python-poetry.org/).

## Project Setup

```bash
# Install both production and development dependencies
poetry install

# Run the CLI (script mode)
poetry run python_cli_template_typer --help
poetry run python_cli_template_typer greet hello Bob --count 3

# Run the CLI (module mode)
poetry run python -m python_cli_template_typer version
```

## Shell Completion

To enable shell completion (bash/zsh/fish):

```bash
poetry run python_cli_template_typer --install-completion
```

## Running Tests

```bash
poetry run pytest -q
```

## Export Requirements (for pip environments)

```bash
# Production requirements
poetry export -f requirements.txt -o requirements.txt --without-hashes

# Development requirements (includes dev dependencies)
poetry export -f requirements.txt -o requirements-dev.txt --with dev --without-hashes
```

