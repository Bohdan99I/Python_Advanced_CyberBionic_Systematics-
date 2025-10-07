import sqlite3
import os
from datetime import datetime
import requests


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "exchange_rates.db")


def create_table():
    """Створює таблицю для зберігання курсів валют до USD."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS exchange_rate_to_usd (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_name TEXT,
            currency_value REAL,
            current_date TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def fetch_usd_rates():
    """Отримує поточні курси валют до USD з API Monobank."""
    url = "https://api.monobank.ua/bank/currency"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [item for item in data if item.get("currencyCodeA") == 980]  # 980 = UAH
    except requests.RequestException as e:
        print(f"[ERROR] Помилка при отриманні даних: {e}")
        return []


def save_usd_rates(data):
    """Зберігає отримані курси валют у базу даних."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for item in data:
        cursor.execute(
            """
            INSERT INTO exchange_rate_to_usd (currency_name, currency_value, current_date)
            VALUES (?, ?, ?)
            """,
            (
                "UAH",
                item.get("rateSell") or item.get("rateCross") or item.get("rateBuy"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ),
        )
    conn.commit()
    conn.close()


def show_last_3_rates():
    """Виводить останні 3 збережені записи курсів USD."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, currency_name, currency_value, current_date
        FROM exchange_rate_to_usd
        ORDER BY id DESC
        LIMIT 3
    """
    )
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("\nОстанні 3 збережені курси USD:")
        for row in rows:
            print(f"ID: {row[0]}, Валюта: {row[1]}, Курс: {row[2]}, Дата: {row[3]}")
    else:
        print("Записів у базі ще немає.")


def main():
    """Головна функція для створення таблиці, отримання та збереження курсів USD."""
    create_table()
    rates = fetch_usd_rates()
    if rates:
        save_usd_rates(rates)
        print("Курси валют успішно збережено.")
        show_last_3_rates()
    else:
        print("Курсів не отримано.")


if __name__ == "__main__":
    main()
