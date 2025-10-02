"""
Простий TCP-сервер для чату з можливістю підключення кількох клієнтів.
"""

import socket
import threading

clients = []  # Список активних клієнтів


def handle_client(client_socket):
    """Обробка повідомлень від клієнта."""
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                broadcast(message, client_socket)
        except (OSError, ConnectionResetError) as e:
            print(f"[ERROR] {e}")
            remove_client(client_socket)
            break


def broadcast(message, sender_socket):
    """Відправляє повідомлення всім клієнтам, крім відправника."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except (OSError, ConnectionResetError):
                remove_client(client)


def remove_client(client_socket):
    """Видаляє клієнта з списку активних."""
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()


def main():
    """Запуск TCP-сервера та очікування підключень."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen()
    print("[STARTED] Сервер TCP запущено на порті 5555")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"[CONNECTED] Клієнт підключився: {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    main()
