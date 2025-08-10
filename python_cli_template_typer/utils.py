import typer

def ensure_positive(n: int) -> int:
    """
    Ensure that the given number is non-negative.
    Raise ValueError if the number is negative.
    """
    if n < 0:
        raise ValueError("Value must be non-negative")
    return n

def ensure_nonzero(n: float) -> float:
    """Ensure the value is not zero (for divisors)."""
    if n == 0:
        raise typer.BadParameter("Divisor must be non-zero.")
    return n
