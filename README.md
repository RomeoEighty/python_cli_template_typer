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

## Install with pip

You can also install this CLI without Poetry using pip.

From source (local path):
```bash
pip install .
```

From a Git repository:
```bash
pip install git+https://github.com/yourusername/mycli.git
```

From requirements.txt (exported from Poetry):
```bash
pip install -r requirements.txt
```

After installation, the `mycli` command will be available in your shell (ensure your Python bin path is in `PATH`).

## Uninstall

If you installed this project in a Poetry-managed virtual environment:
```bash
poetry env remove python
```

If you added it as a dependency to another Poetry project:
```bash
poetry remove mycli
```

If you installed it via pip:
```bash
pip uninstall mycli
```

