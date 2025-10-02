"""
TCP-сервер, який приймає два числа, розділені комою,
обчислює їхню суму та повертає результат клієнту.
"""

import socket


def start_tcp_server():
    """
    Запускає TCP-сервер, що слухає повідомлення від клієнтів,
    виконує обчислення та повертає результат.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12346))
    server_socket.listen(1)

    print("TCP-сервер запущено. Очікування з'єднань...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Підключився клієнт: {addr}")

        data = conn.recv(1024).decode()
        if not data:
            break

        try:
            num1_str, num2_str = data.split(",")
            num1, num2 = int(num1_str.strip()), int(num2_str.strip())
            result = num1 + num2
            response = f"Сума: {result}"
        except ValueError:
            response = "Помилка: потрібно надіслати два числа через кому."
        except IndexError:
            response = "Помилка: формат повідомлення неправильний."

        conn.sendall(response.encode())
        conn.close()


if __name__ == "__main__":
    start_tcp_server()
