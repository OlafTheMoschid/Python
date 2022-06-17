from requests import post

user = {
    'nickname': 'changed_nick',
    'email': 'newmail@mail.com'
    }

print(post('http://127.0.0.1:8080/api/v2/users/4', json=user).json())
