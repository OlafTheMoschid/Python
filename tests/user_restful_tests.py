import pytest
import datetime
from requests import get, post, delete

# Tests for user RESTful edition

# GETTING


def test_show_user_all():
    x = get('http://127.0.0.1:8080/api/v2/users')
    assert x.status_code == 200


def test_show_user_correct_id():
    x = get('http://127.0.0.1:8080/api/v2/users/1')
    assert x.status_code == 200


def test_show_user_wrong_id():
    x = get('http://127.0.0.1:8080/api/v2/users/10')
    assert x.status_code == 200


def test_show_user_string_id():
    x = get('http://127.0.0.1:8080/api/v2/users/number')
    assert x.status_code == 200

# ADDING


def test_add_user_correct():
    user = {
        'nickname': 'test_nickname',
        'email': 'blahblah@goooo.com',
        'password': 'password_20'
    }
    x = post('http://127.0.0.1:8080/api/v2/users', json=user)
    assert x.status_code == 200


def test_add_user_not_enough_data():
    # Недостаточно переданных параметров
    # Обязательные параметры: ['nickname', 'email', 'password']
    user = {
        'nickname': 'test_nickname'
    }
    x = post('http://127.0.0.1:8080/api/v2/users', json=user)
    assert x.status_code == 200


def test_add_user_exists():
    # Уже существует пользователь с таким емайлом
    user = {
        'nickname': 'test_nickname_2',
        'email': 'blahblah@goooo.com',
        'password': 'password_8'
    }
    x = post('http://127.0.0.1:8080/api/v2/users', json=user)
    assert x.status_code == 200


def test_add_user_type_data():
    # Неверные типы данных
    user = {
        'nickname': 12345,
        'email': 'blahblah@goooo.com',
        'password': 'password_8'
    }
    x = post('http://127.0.0.1:8080/api/v2/users', json=user)
    assert x.status_code == 200
