from requests import post

user = {
     'nickname': 'test_name',
     'email': 'testemail@test.com',
     'hashed_password': 'password_1'
}

print(post('http://127.0.0.1:8080/api/v2/users', json=user).json())
