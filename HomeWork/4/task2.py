"""CLI для додавання нових записів у таблицю особистих витрат."""

import sqlite3
import os


def add_expense(purpose, amount):
    """Додає новий запис у таблицю витрат."""
    # Знаходимо базу у тій самій папці, де розташований цей файл
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "expenses.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (purpose, amount)
        VALUES (?, ?)
    """,
        (purpose, amount),
    )

    conn.commit()
    conn.close()
    print("✅ Новий запис успішно додано!")


def main():
    """Консольний інтерфейс для введення витрат."""
    print("=== Додавання особистих витрат ===")
    while True:
        purpose = input("Введіть призначення витрати (або 'exit' для виходу): ").strip()
        if purpose.lower() == "exit":
            print("👋 Вихід із програми.")
            break

        try:
            amount = float(input("Введіть суму витрати: "))
        except ValueError:
            print("❌ Помилка: введіть числове значення суми.")
            continue

        add_expense(purpose, amount)


if __name__ == "__main__":
    main()
