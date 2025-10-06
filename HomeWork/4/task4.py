"""Завдання 4. Агрегатні функції для підрахунку витрат і прибутків за місяць."""

import sqlite3
from datetime import datetime
import os


# --- Ініціалізація бази даних ---
def init_db():
    """Створює базу даних і таблицю, якщо її ще немає."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "expenses.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            purpose TEXT NOT NULL,
            amount REAL NOT NULL,
            type TEXT CHECK(type IN ('витрата', 'прибуток')) NOT NULL,
            time TEXT NOT NULL
        )
    """
    )

    conn.commit()
    conn.close()


# --- Додавання запису ---
def add_record(purpose, amount, record_type):
    """Додає новий запис до таблиці."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "expenses.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (purpose, amount, type, time) VALUES (?, ?, ?, ?)",
        (purpose, amount, record_type, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    )

    conn.commit()
    conn.close()
    print("✅ Запис успішно додано!")


# --- Агрегатна функція для підрахунку ---
def calculate_totals(month):
    """Обчислює загальні суми прибутків і витрат за вказаний місяць."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "expenses.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Вибірка витрат
    cursor.execute(
        """
        SELECT SUM(amount) FROM expenses
        WHERE type='витрата' AND strftime('%m', time)=?
    """,
        (month,),
    )
    total_expenses = cursor.fetchone()[0] or 0

    # Вибірка прибутків
    cursor.execute(
        """
        SELECT SUM(amount) FROM expenses
        WHERE type='прибуток' AND strftime('%m', time)=?
    """,
        (month,),
    )
    total_income = cursor.fetchone()[0] or 0

    conn.close()
    return total_expenses, total_income


# --- Головне меню ---
def main():
    """Головна функція, що забезпечує роботу CLI для підрахунку витрат і прибутків."""
    init_db()

    while True:
        print("\n=== Меню фінансового обліку ===")
        print("1. Додати запис")
        print("2. Порахувати витрати та прибутки за місяць")
        print("3. Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            purpose = input("Введіть призначення: ")
            amount = float(input("Введіть суму: "))
            record_type = input("Введіть тип (витрата / прибуток): ").strip().lower()
            if record_type not in ("витрата", "прибуток"):
                print("❌ Невірний тип. Використовуйте 'витрата' або 'прибуток'.")
                continue
            add_record(purpose, amount, record_type)

        elif choice == "2":
            month = input("Введіть номер місяця (наприклад, 03 для березня): ")
            expenses, income = calculate_totals(month)
            print(f"\n📅 Результати за місяць {month}:")
            print(f"Загальні витрати: {expenses:.2f} грн")
            print(f"Загальний прибуток: {income:.2f} грн")
            print(f"Баланс: {income - expenses:.2f} грн")

        elif choice == "3":
            print("👋 Вихід із програми.")
            break
        else:
            print("❌ Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
