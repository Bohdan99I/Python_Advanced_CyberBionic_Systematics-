"""
HTTP-клієнт, який приймає URL, метод та дані, виконує запит та виводить результат.
"""

import requests


def http_request(target_url: str, http_method: str = "GET", payload: dict = None):
    """
    Виконує HTTP-запит за заданим URL і методом.

    :param target_url: URL ресурсу
    :param http_method: HTTP-метод ('GET', 'POST', 'PUT', 'DELETE' тощо)
    :param payload: Словник з даними для передачі (опціонально)
    """
    try:
        method = http_method.upper()
        if method == "GET":
            response = requests.get(target_url, params=payload, timeout=10)
        elif method == "POST":
            response = requests.post(target_url, json=payload, timeout=10)
        elif method == "PUT":
            response = requests.put(target_url, json=payload, timeout=10)
        elif method == "DELETE":
            response = requests.delete(target_url, timeout=10)
        else:
            print(f"[ERROR] Метод {method} не підтримується.")
            return

        # Вивід результатів
        print(f"Status code: {response.status_code}")
        print("Headers:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
        print("Body:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Помилка при виконанні запиту: {e}")


if __name__ == "__main__":
    # Введення даних користувачем
    input_url = input("Введіть URL: ")
    input_method = input("Введіть метод (GET, POST, PUT, DELETE): ")
    input_data = input(
        "Введіть дані у форматі ключ=значення через кому (опціонально): "
    )

    # Створення словника даних для запиту
    user_data = None
    if input_data:
        user_data = dict(
            item.split("=") for item in input_data.split(",")
        )  # pylint: disable=C0103

    http_request(input_url, input_method, user_data)

    input("Натисніть Enter для виходу...")

    # Завершення програми
