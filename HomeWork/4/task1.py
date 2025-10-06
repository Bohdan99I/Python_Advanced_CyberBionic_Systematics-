"""Модуль для створення таблиці особистих витрат у базі даних SQLite."""

import sqlite3
import os


def create_expenses_table():
    """Створює таблицю для збереження особистих витрат у поточній папці."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "expenses.db")

    # Підключення до бази даних
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Створення таблиці
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            purpose TEXT NOT NULL,
            amount REAL NOT NULL,
            time DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    conn.commit()
    conn.close()
    print(f"✅ Таблицю створено або вже існує. Шлях до бази: {db_path}")


if __name__ == "__main__":
    create_expenses_table()
