"""
Модуль для створення користувацької агрегатної функції,
яка обчислює середнє значення ваги матеріалів і округляє його до цілого.
"""

import sqlite3

# Підключення до бази
conn = sqlite3.connect("materials.db")
cursor = conn.cursor()


# Користувацька агрегатна функція
class AverageWeight:
    """
    Агрегатна функція для підрахунку середнього значення ваги матеріалів.
    """

    def __init__(self):
        self.values = []

    def step(self, value):
        """Додає нове значення ваги."""
        if value is not None:
            self.values.append(value)

    def finalize(self):
        """Обчислює середнє значення та округляє його до цілого."""
        if not self.values:
            return None
        return round(sum(self.values) / len(self.values))


# Реєстрація функції в SQLite
conn.create_aggregate("avg_weight", 1, AverageWeight)

# Приклад вибірки
cursor.execute("SELECT avg_weight(weight) FROM materials")
result = cursor.fetchone()[0]

print(f"Середнє значення ваги (округлене): {result}")

conn.close()
