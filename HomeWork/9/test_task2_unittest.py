"""Модуль тестів для функції calculate_bmi з використанням unittest."""

import unittest
from task2 import calculate_bmi


class TestBMICalculation(unittest.TestCase):
    """Тести функції calculate_bmi."""

    def test_valid_values(self):
        """Перевірка правильних розрахунків."""
        self.assertEqual(calculate_bmi(70, 1.75), 22.86)
        self.assertEqual(calculate_bmi(60, 1.6), 23.44)
        self.assertEqual(calculate_bmi(90, 1.9), 24.93)

    def test_invalid_values(self):
        """Перевірка некоректних числових значень."""
        with self.assertRaises(ValueError):
            calculate_bmi(-70, 1.8)
        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.8)
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.8)

    def test_invalid_data_type(self):
        """Перевірка неправильних типів даних."""
        with self.assertRaises(ValueError):
            calculate_bmi("70", 1.8)
        with self.assertRaises(ValueError):
            calculate_bmi(70, "1.8")


if __name__ == "__main__":
    unittest.main()
    print("✅ Усі тести через unittest пройдено успішно!")
