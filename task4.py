import pytest
from rectangle import Rectangle

@pytest.fixture
def rectangle():
    return Rectangle(5, 10)


def test_area(rectangle):
    assert rectangle.get_area() == 50


def test_perimeter(rectangle):
    assert rectangle.get_perimeter() == 30


def test_float_area(rectangle):
    rectangle.__init__(1.5, 5)
    assert rectangle.get_area() == 7.5


def test_float_perimeter(rectangle):
    rectangle.__init__(1.5, 5)
    assert rectangle.get_perimeter() == 13


def test_negative_value(rectangle):
    with pytest.raises(ValueError):
        rectangle.__init__(-5, 10)


def test_wrong_type(rectangle):
    with pytest.raises(TypeError):
        rectangle.__init__('-5', [10])
