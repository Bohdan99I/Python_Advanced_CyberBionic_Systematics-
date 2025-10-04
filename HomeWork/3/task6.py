"""
Модуль для створення функції користувача,
яка конкатенує необмежену кількість полів для таблиці 'materials'.
"""

import sqlite3

# Підключення до бази
conn = sqlite3.connect("materials.db")
cursor = conn.cursor()


# Функція користувача для конкатенації полів
def concat_fields(*args):
    """
    Приймає необмежену кількість аргументів і повертає їх як одну конкатеновану стрічку.
    """
    return " ".join(str(arg) for arg in args if arg is not None)


# Реєстрація функції в SQLite
conn.create_function("concat_fields", -1, concat_fields)

# Приклад використання: об'єднати ідентифікатор та вага матеріалу
cursor.execute("SELECT concat_fields(id, weight) FROM materials")
results = cursor.fetchall()

for row in results:
    print(row[0])

conn.close()
