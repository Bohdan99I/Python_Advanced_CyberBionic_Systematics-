"""Модуль тестів для функції calculate_bmi з використанням pytest."""

import pytest
from task2 import calculate_bmi


def test_valid_bmi():
    """Перевірка правильних розрахунків BMI."""
    assert calculate_bmi(70, 1.75) == 22.86
    assert calculate_bmi(90, 1.9) == 24.93
    assert calculate_bmi(50, 1.6) == 19.53


def test_invalid_negative_values():
    """Перевірка від’ємних значень."""
    with pytest.raises(ValueError):
        calculate_bmi(-70, 1.8)
    with pytest.raises(ValueError):
        calculate_bmi(70, -1.8)


def test_invalid_zero_values():
    """Перевірка нульових значень."""
    with pytest.raises(ValueError):
        calculate_bmi(0, 1.8)
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)


def test_invalid_data_type():
    """Перевірка неправильних типів даних."""
    with pytest.raises(ValueError):
        calculate_bmi("70", 1.8)
    with pytest.raises(ValueError):
        calculate_bmi(70, "1.8")
