"""
Завдання 3:
Створення власних діалектів для CSV, робота з ними при записі та читанні файлів.
"""

import csv

# Реєстрація власних діалектів
csv.register_dialect(
    "semicolon_dialect",
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
)

csv.register_dialect(
    "pipe_dialect",
    delimiter="|",
    quotechar="'",
    quoting=csv.QUOTE_ALL,
)

# Дані для прикладу
data = [
    ["Ім'я", "Прізвище", "Вік"],
    ["Іван", "Петренко", 25],
    ["Олена", "Шевченко", 30],
    ["Марія", "Коваль", 28],
]

# Запис у CSV з діалектом semicolon_dialect
with open("people_semicolon.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, dialect="semicolon_dialect")
    writer.writerows(data)

print("✅ Файл people_semicolon.csv створено")

# Запис у CSV з діалектом pipe_dialect
with open("people_pipe.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, dialect="pipe_dialect")
    writer.writerows(data)

print("✅ Файл people_pipe.csv створено")

# Читання з CSV з використанням діалектів
print("\n📖 Читання з people_semicolon.csv:")
with open("people_semicolon.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, dialect="semicolon_dialect")
    for row in reader:
        print(row)

print("\n📖 Читання з people_pipe.csv:")
with open("people_pipe.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, dialect="pipe_dialect")
    for row in reader:
        print(row)
