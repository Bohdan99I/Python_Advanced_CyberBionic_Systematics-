"""
Демонстрація роботи з HTTP у Python за допомогою urllib та requests.
"""

import urllib.request
import urllib.parse
import requests


def urllib_example():
    """
    Виконує HTTP-запит GET і POST за допомогою urllib.
    """
    print("=== urllib приклад ===")

    # GET-запит
    url = "https://jsonplaceholder.typicode.com/posts/1"
    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8")
        print("GET (urllib) ->", data[:100], "...")  # обрізаємо для зручності

    # POST-запит
    url = "https://jsonplaceholder.typicode.com/posts"
    post_data = urllib.parse.urlencode(
        {"title": "foo", "body": "bar", "userId": 1}
    ).encode("utf-8")

    req = urllib.request.Request(url, data=post_data, method="POST")
    with urllib.request.urlopen(req) as response:
        data = response.read().decode("utf-8")
        print("POST (urllib) ->", data)


def requests_example():
    """
    Виконує HTTP-запит GET і POST за допомогою requests.
    """
    print("\n=== requests приклад ===")

    # GET-запит
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url, timeout=5)
    print("GET (requests) ->", response.json())

    # POST-запит
    url = "https://jsonplaceholder.typicode.com/posts"
    post_data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=post_data, timeout=5)
    print("POST (requests) ->", response.json())


if __name__ == "__main__":
    urllib_example()
    requests_example()
