import pytest
from reverse import reverse


def test_empty():
    assert reverse('') == ''


def test_single():
    assert reverse('a') == 'a'


def test_palindrom():
    assert reverse('level') == 'level'


def test_usual_str():
    assert reverse('Hello') == 'olleH'


def test_wrong_type_not_iter():
    with pytest.raises(TypeError):
        reverse(55)


def test_wrong_type_iter():
    with pytest.raises(TypeError):
        reverse(['He', 'll', 'o!'])
