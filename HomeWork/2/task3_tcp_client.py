"""
TCP-клієнт для надсилання двох чисел на сервер
та отримання їхньої суми.
"""

import socket


def send_numbers(num1, num2):
    """
    Надсилає два числа на сервер, отримує суму у відповідь.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12346))

    message = f"{num1},{num2}"
    client_socket.sendall(message.encode())

    response = client_socket.recv(1024).decode()
    print("Відповідь сервера:", response)

    client_socket.close()


if __name__ == "__main__":
    send_numbers(5, 7)
