"""Завдання 1.
Порівняння синхронного (requests) та асинхронного (aiohttp) виконання HTTP-запитів
із логуванням у базу даних SQLite.
"""

import asyncio
import sqlite3
from datetime import datetime
import requests
import aiohttp


def setup_db():
    """Створює базу даних і таблиці для логів."""
    conn = sqlite3.connect("logs.db")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS logs_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event TEXT
        )
    """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS logs_aiohttp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def log_event(table: str, message: str):
    """Записує подію в таблицю бази даних."""
    conn = sqlite3.connect("logs.db")
    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO {table} (timestamp, event) VALUES (?, ?)",
        (datetime.now().isoformat(), message),
    )
    conn.commit()
    conn.close()


def fetch_with_requests(urls: list[str]):
    """Виконує HTTP-запити до списку URL за допомогою бібліотеки requests."""
    for url in urls:
        log_event("logs_requests", f"Початок запиту до {url}")
        try:
            response = requests.get(url, timeout=10)
            log_event(
                "logs_requests",
                f"Відповідь від {url} отримано зі статусом {response.status_code}",
            )
        except requests.RequestException as e:
            log_event("logs_requests", f"Помилка при запиті до {url}: {e}")


async def fetch_url(session: aiohttp.ClientSession, url: str):
    """Виконує один асинхронний HTTP-запит і логування."""
    log_event("logs_aiohttp", f"Початок запиту до {url}")
    try:
        async with session.get(url, timeout=10) as response:
            log_event(
                "logs_aiohttp",
                f"Відповідь від {url} отримано зі статусом {response.status}",
            )
    except aiohttp.ClientError as e:
        log_event("logs_aiohttp", f"Помилка при запиті до {url}: {e}")
    except asyncio.TimeoutError:
        log_event("logs_aiohttp", f"Таймаут при запиті до {url}")


async def fetch_with_aiohttp(urls: list[str]):
    """Асинхронно виконує HTTP-запити до списку URL за допомогою aiohttp."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)


def main():
    """Основна функція: створення бази, запуск двох варіантів запитів і логування."""
    setup_db()

    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://httpbin.org/get",
        "https://www.google.com",
    ]

    print("=== Виконання через requests ===")
    fetch_with_requests(urls)
    print("Готово! Логи збережено в таблиці logs_requests.\n")

    print("=== Виконання через aiohttp ===")
    asyncio.run(fetch_with_aiohttp(urls))
    print("Готово! Логи збережено в таблиці logs_aiohttp.\n")


if __name__ == "__main__":
    main()
