"""Завдання 2.
Розробіть сокет-сервер на основі бібліотеки asyncio.
"""

import asyncio
from datetime import datetime


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    """Обробляє підключення клієнта."""
    addr = writer.get_extra_info("peername")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Підключено клієнта: {addr}")

    try:
        while True:
            data = await reader.readline()
            if not data:
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] Клієнт {addr} відключився."
                )
                break

            message = data.decode().strip()
            print(
                f"[{datetime.now().strftime('%H:%M:%S')}] Отримано від {addr}: {message}"
            )

            if message.lower() in ("exit", "quit", "bye"):
                writer.write("Вихід із сервера...\n".encode())
                await writer.drain()
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] Клієнт {addr} завершив сесію."
                )
                break

            response = f"Сервер ({datetime.now().strftime('%H:%M:%S')}): отримано -> {message}\n"
            writer.write(response.encode())
            await writer.drain()

    except ConnectionResetError:
        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] Підключення з {addr} розірвано."
        )

    writer.close()
    await writer.wait_closed()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] З'єднання з {addr} закрито.")


async def main():
    """Запускає асинхронний сервер на порту 8888."""
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8888)
    addr = server.sockets[0].getsockname()
    print(f"Сервер запущено на {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nСервер зупинено вручну.")
