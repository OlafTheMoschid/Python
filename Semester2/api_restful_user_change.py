from requests import post

user = {
    'nickname': 'changed_nickname',
    'email': 'newmail@mail.com'
    }

print(post('http://127.0.0.1:8080/api/v2/users/2', json=user).json())
