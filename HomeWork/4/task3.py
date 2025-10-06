"""CLI для додавання витрат і прибутків у базу даних."""

import sqlite3
import os


def initialize_db():
    """Створює або оновлює таблицю з полем type."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "expenses.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Створюємо таблицю, якщо її ще немає
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            purpose TEXT NOT NULL,
            amount REAL NOT NULL,
            type TEXT CHECK(type IN ('витрата', 'прибуток')) NOT NULL DEFAULT 'витрата',
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    conn.commit()
    conn.close()


def add_record(purpose, amount, record_type):
    """Додає новий запис (витрату або прибуток) у таблицю."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "expenses.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (purpose, amount, type)
        VALUES (?, ?, ?)
    """,
        (purpose, amount, record_type),
    )

    conn.commit()
    conn.close()
    print(f"✅ {record_type.capitalize()} успішно додано!")


def main():
    """Консольний інтерфейс для введення витрат і прибутків."""
    initialize_db()
    print("=== Додавання витрат і прибутків ===")

    while True:
        record_type = (
            input("Введіть тип запису (витрата/прибуток або 'exit' для виходу): ")
            .strip()
            .lower()
        )
        if record_type == "exit":
            print("👋 Вихід із програми.")
            break
        if record_type not in ("витрата", "прибуток"):
            print("❌ Невірний тип. Введіть 'витрата' або 'прибуток'.")
            continue

        purpose = input("Введіть призначення: ").strip()
        try:
            amount = float(input("Введіть суму: "))
        except ValueError:
            print("❌ Помилка: введіть числове значення суми.")
            continue

        add_record(purpose, amount, record_type)


if __name__ == "__main__":
    main()
