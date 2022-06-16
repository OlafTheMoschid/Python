from requests import delete

print(delete('http://127.0.0.1:8080/api/v2/users/2').json())
