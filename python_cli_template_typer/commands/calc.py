import typer
from python_cli_template_typer.utils import ensure_nonzero

# Sub-app for calculation commands
app = typer.Typer()

@app.command()
def add(a: int, b: int):
    """
    Add two numbers and print the result.
    """
    typer.echo(f"{a} + {b} = {a + b}")

@app.command()
def div(
    a: float = typer.Argument(..., help="Dividend"),
    b: float = typer.Argument(..., help="Divisor", callback=ensure_nonzero),
):
    """Divide a by b and print the result."""
    typer.echo(f"{a} / {b} = {a / b}")
