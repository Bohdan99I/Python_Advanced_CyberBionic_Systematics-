"""
UDP-сервер, який очікує повідомлення від клієнтів
і виводить у консоль ідентифікатори нових пристроїв.
"""

import socket


def start_udp_server():
    """
    Запускає UDP-сервер, який очікує повідомлення від клієнтів
    і виводить у консоль ідентифікатори нових пристроїв.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 12345))

    print("UDP-сервер запущений. Очікування з'єднань...")

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"Новий пристрій: {message.decode()} від {client_address}")


if __name__ == "__main__":
    start_udp_server()
