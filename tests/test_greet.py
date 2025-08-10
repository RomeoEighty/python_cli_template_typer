from typer.testing import CliRunner

from python_cli_template_typer.cli import app

runner = CliRunner()

def test_hello():
    result = runner.invoke(app, ["greet", "hello", "Alice", "--count", "2"])
    assert result.exit_code == 0
    assert result.stdout.count("Hello, Alice!") == 2
