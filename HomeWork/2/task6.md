# Завдання 6: Робота з API https://jsonplaceholder.typicode.com/

## Основні поняття

- **API** – інтерфейс для взаємодії програм з серверами.
- **JSONPlaceholder** – тестовий REST API для практики, який надає ресурси:
  - `/posts`, `/comments`, `/albums`, `/photos`, `/todos`, `/users`
- **HTTP-методи**:
  - `GET` – отримання даних
  - `POST` – створення нових даних
  - `PUT` – повне оновлення ресурсу
  - `PATCH` – часткове оновлення
  - `DELETE` – видалення ресурсу

---

## Приклад використання **urllib**

```python
import urllib.request
import json

# GET-запит
url = "https://jsonplaceholder.typicode.com/posts/1"
with urllib.request.urlopen(url) as response:
    data = json.load(response)
    print(data)

# POST-запит
import urllib.parse

url = "https://jsonplaceholder.typicode.com/posts"
post_data = urllib.parse.urlencode({
    "title": "foo",
    "body": "bar",
    "userId": 1
}).encode()
req = urllib.request.Request(url, data=post_data, method="POST")
with urllib.request.urlopen(req) as response:
    data = json.load(response)
    print(data)
```

## Приклад використання requests

```python
import requests

# GET-запит
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())

# POST-запит
payload = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
print(response.json())

# PUT-запит
payload = {"id": 1, "title": "updated", "body": "updated body", "userId": 1}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=payload)
print(response.json())

# DELETE-запит
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
```
