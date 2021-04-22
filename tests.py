import requests

get = requests.get("http://127.0.0.1:8000/api/v2/notes").json()
print(get)

get = requests.get("http://127.0.0.1:8000/api/v2/notes/1").json()
print(get)

post = requests.post("http://127.0.0.1:8000/api/v2/notes", params={"api_key": 'pbkdf2:sha256:150000$4Mm3oOth$8df713f755b7180f38cb4625475dfe6e76cdd69520422ab6273d2847ed3eaf1a',
                                                                   "content": "Ого я снова супер админ"}).json()
print(post)

delete = requests.delete("http://127.0.0.1:8000/api/v2/notes/7", params={"api_key": 'pbkdf2:sha256:150000$4Mm3oOth$8df713f755b7180f38cb4625475dfe6e76cdd69520422ab6273d2847ed3eaf1a'}).json()
print(delete)
