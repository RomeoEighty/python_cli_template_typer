import pytest
from python_cli_template_typer.core.mathops import add, div

@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 3), (-1, 5, 4), (2.5, 0.5, 3.0)],
)
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [(6, 3, 2.0), (7.5, 2.5, 3.0)],
)
def test_div(a, b, expected):
    assert div(a, b) == expected
    # sanity: result type is float
    assert isinstance(div(a, b), float)

def test_div_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
