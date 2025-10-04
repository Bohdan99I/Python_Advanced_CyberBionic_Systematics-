"""
Модуль для роботи з таблицею 'materials', яка містить
ідентифікатор, вагу, висоту та додаткові характеристики матеріалів.
"""

import sqlite3
import json

# Підключення до бази
conn = sqlite3.connect("materials.db")
cursor = conn.cursor()

# Створення таблиці
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    weight REAL,
    height REAL,
    extra_features TEXT
)
"""
)


def add_material(weight, height, features):
    """
    Додає матеріал у таблицю.

    :param weight: вага матеріалу
    :param height: висота матеріалу
    :param features: список кортежів з характеристиками (назва, значення)
    """
    features_json = json.dumps(features, ensure_ascii=False)
    cursor.execute(
        "INSERT INTO materials (weight, height, extra_features) VALUES (?, ?, ?)",
        (weight, height, features_json),
    )
    conn.commit()


def get_materials():
    """
    Виводить всі матеріали з таблиці.
    """
    cursor.execute("SELECT * FROM materials")
    rows = cursor.fetchall()
    for row in rows:
        material_id, weight, height, features_json = row
        features = json.loads(features_json)
        print(f"ID: {material_id}, Вага: {weight}, Висота: {height}")
        print("Характеристики:")
        for name, value in features:
            print(f"  - {name}: {value}")
        print("-" * 30)


# Демонстрація роботи
add_material(12.5, 3.2, [("Колір", "Червоний"), ("Щільність", "1.2 г/см3")])
add_material(7.8, 2.5, [("Твердість", "Висока"), ("Прозорість", "Низька")])

get_materials()

conn.close()
