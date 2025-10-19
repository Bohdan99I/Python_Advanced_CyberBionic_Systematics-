"""Модуль для зберігання даних про студентів."""


class Student:
    """Клас Student з атрибутами ім'я, прізвище, вік та середній бал."""

    def __init__(self, first_name: str, last_name: str, age: int, average_grade: float):
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("Ім'я має бути непорожнім рядком.")
        if not isinstance(last_name, str) or not last_name:
            raise ValueError("Прізвище має бути непорожнім рядком.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Вік має бути додатним числом.")
        if not isinstance(average_grade, (int, float)) or not (
            0 <= average_grade <= 100
        ):
            raise ValueError("Середній бал має бути числом від 0 до 100.")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, {self.age} років, середній бал {self.average_grade})"


# створення 10 студентів
students = [
    Student("Іван", "Петренко", 20, 85.5),
    Student("Марія", "Іваненко", 19, 91.2),
    Student("Олег", "Сидоренко", 22, 76.8),
    Student("Наталія", "Коваль", 21, 88.3),
    Student("Андрій", "Шевченко", 23, 95.0),
    Student("Оксана", "Лисенко", 20, 82.1),
    Student("Богдан", "Ткачук", 19, 79.5),
    Student("Катерина", "Мельник", 21, 90.0),
    Student("Юрій", "Гнатюк", 24, 70.3),
    Student("Ірина", "Романюк", 22, 92.7),
]
