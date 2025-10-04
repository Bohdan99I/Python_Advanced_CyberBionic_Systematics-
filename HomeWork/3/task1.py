"""
Модуль для демонстрації роботи з JSON у Python.

Завдання 1:
- створення словників,
- конвертація у JSON,
- збереження у файл у папці "3",
- завантаження даних з файлу.
"""

import json

# Створюємо словники
person1 = {"name": "Іван", "age": 25, "city": "Київ"}
person2 = {"name": "Олена", "age": 30, "city": "Львів"}

# Об'єднуємо у список
people = [person1, person2]

# Збереження у JSON файл
with open("people.json", "w", encoding="utf-8") as f:
    json.dump(people, f, ensure_ascii=False, indent=4)

print("✅ Дані збережено у файл people.json")

# Завантаження з JSON файлу
with open("people.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("📂 Дані, завантажені з файлу:")
print(loaded_data)
