import typer
from python_cli_template_typer.utils import ensure_nonzero
from python_cli_template_typer.core.mathops import add as add_fn, div as div_fn

# Sub-app for calculation commands
app = typer.Typer()

@app.command()
def add(a: int, b: int):
    """
    Add two numbers and print the result.
    """
    typer.echo(f"{a} + {b} = {add_fn(a, b)}")

@app.command()
def div(
    a: float = typer.Argument(..., help="Dividend"),
    b: float = typer.Argument(..., help="Divisor", callback=ensure_nonzero),
):
    """Divide a by b and print the result."""
    # b is non-zero here thanks to Typer callback; delegate to pure function
    result = div_fn(a, b)
    typer.echo(f"{a} / {b} = {result}")
