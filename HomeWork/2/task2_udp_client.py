"""
UDP-клієнт для надсилання унікального ідентифікатора пристрою на сервер.
"""

import socket
import uuid


def send_device_id():
    """
    Надсилає унікальний ідентифікатор пристрою на UDP-сервер,
    повідомляючи про присутність клієнта в мережі.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 12345)

    device_id = str(uuid.uuid4())
    client_socket.sendto(device_id.encode(), server_address)
    print(f"Відправлено ідентифікатор: {device_id}")

    client_socket.close()


if __name__ == "__main__":
    send_device_id()
