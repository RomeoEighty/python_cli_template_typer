from typer.testing import CliRunner

from python_cli_template_typer.cli import app

runner = CliRunner()

def test_add_ok():
    r = runner.invoke(app, ["calc", "add", "2", "3"])
    assert r.exit_code == 0
    assert "2 + 3 = 5" in r.stdout

def test_div_ok():
    r = runner.invoke(app, ["calc", "div", "6", "3"])
    assert r.exit_code == 0
    assert "6.0 / 3.0 = 2.0" in r.stdout

def test_div_zero_rejected():
    r = runner.invoke(app, ["calc", "div", "1", "0"])
    # Typer/Click uses exit code 2 for BadParameter by default
    assert r.exit_code == 2
    assert "Divisor must be non-zero" in r.stdout
