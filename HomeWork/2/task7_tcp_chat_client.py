"""
Простий TCP-клієнт для підключення до чату.
"""

import socket
import threading


def receive_messages(client_socket):
    """Отримує повідомлення від сервера та виводить їх на консоль."""
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(message)
        except (OSError, ConnectionResetError) as e:
            print(f"[ERROR] {e}")
            client_socket.close()
            break


def main():
    """Запуск клієнта та підключення до сервера."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        try:
            msg = input()
            if msg.lower() == "exit":
                client_socket.close()
                break
            client_socket.send(msg.encode("utf-8"))
        except (OSError, ConnectionResetError) as e:
            print(f"[ERROR] {e}")
            client_socket.close()
            break


if __name__ == "__main__":
    main()
