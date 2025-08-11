from __future__ import annotations

def add(a: int | float, b: int | float) -> int | float:
    return a + b

def div(a: int | float, b: int | float) -> float:
    if b == 0:
        # Pure function: raise a normal Python error (easy to test)
        raise ZeroDivisionError("division by zero")
    return a / b
