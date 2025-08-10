import typer

# Sub-app for greeting related commands
app = typer.Typer()

@app.command()
def hello(name: str, count: int = 1, verbose: bool = False):
    """
    Greet the given name multiple times.
    """
    if verbose:
        typer.echo(f"[greet] name={name}, count={count}")
    for _ in range(count):
        typer.echo(f"Hello, {name}!")
