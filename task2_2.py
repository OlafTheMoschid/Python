import pytest
from math import sqrt
from roots import roots


def test_a_iszero():
    assert roots(0, 1, 2) == None


def test_b_iszero():
    assert roots(2, 0, -8) == (-2, 2)


def test_b_iszero_err():
    assert roots(2, 0, 8) == None


def test_c_iszero():
    assert roots(1, -4, 0) == (0, 4)


def test_discriminant_iszero():
    assert roots(1, 2, 1) == (-1, -1)


def test_discriminant_isnegative():
    assert roots(1, 2, 6) == None


def test_some_nums_are_float():
    x1 = (5 - 2 * sqrt(15)) / 7
    x2 = (5 + 2 * sqrt(15)) / 7
    assert roots(2.1, -3, -1.5) == (x1, x2)


def test_output_float():
    x1 = (14 - 16) / 6
    x2 = (14 + 16) / 6
    assert roots(3, -14, -5) == (x1, x2)


def test_wrong_type():
    assert roots('1', [4], 3) == None
