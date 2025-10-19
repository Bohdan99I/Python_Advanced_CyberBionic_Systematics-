"""Тести для перевірки валідності класу Student."""

import unittest
from task3 import Student


class TestStudent(unittest.TestCase):
    """Перевірка роботи класу Student."""

    def test_valid_student(self):
        """Перевірка правильності створення студента."""
        student = Student("Іван", "Петренко", 20, 85.5)
        self.assertEqual(student.first_name, "Іван")
        self.assertEqual(student.last_name, "Петренко")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.average_grade, 85.5)

    def test_invalid_name(self):
        """Перевірка некоректного ім'я."""
        with self.assertRaises(ValueError):
            Student("", "Петренко", 20, 85.5)

    def test_invalid_last_name(self):
        """Перевірка некоректного прізвища."""
        with self.assertRaises(ValueError):
            Student("Іван", "", 20, 85.5)

    def test_invalid_age_type(self):
        """Перевірка некоректного типу віку."""
        with self.assertRaises(ValueError):
            Student("Іван", "Петренко", "двадцять", 85.5)

    def test_negative_age(self):
        """Перевірка негативного віку."""
        with self.assertRaises(ValueError):
            Student("Іван", "Петренко", -5, 85.5)

    def test_invalid_grade_type(self):
        """Перевірка некоректного типу середнього балу."""
        with self.assertRaises(ValueError):
            Student("Іван", "Петренко", 20, "відмінно")

    def test_grade_out_of_range_low(self):
        """Перевірка негативного середнього балу."""
        with self.assertRaises(ValueError):
            Student("Іван", "Петренко", 20, -1)

    def test_grade_out_of_range_high(self):
        """Перевірка негативного середнього балу."""
        with self.assertRaises(ValueError):
            Student("Іван", "Петренко", 20, 101)


if __name__ == "__main__":
    unittest.main()
