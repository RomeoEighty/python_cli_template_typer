import typer
from python_cli_template_typer.commands import greet, calc

# Main Typer app
app = typer.Typer(help="My Typer-based CLI application")

# Register subcommands from separate modules
app.add_typer(greet.app, name="greet", help="Greeting commands")
app.add_typer(calc.app, name="calc", help="Calculation commands")

@app.command()
def version():
    """Show the CLI version."""
    from python_cli_template_typer import __version__
    typer.echo(__version__)

if __name__ == "__main__":
    app()
