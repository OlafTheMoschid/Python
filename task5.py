import pytest


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@pytest.mark.parametrize("test_input,expected", [(1, 1), (2, 1), (3, 2), (4, 3), (5, 6), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)])
def test_fib(test_input, expected):
    assert fib(test_input) == expected
