"""
Модуль для розрахунку індексу маси тіла (ІМТ) людини.
Формула: ІМТ = маса (кг) / (зріст (м))²
"""


def calculate_bmi(weight: float, height: float) -> float:
    """
    Обчислює індекс маси тіла (BMI).

    :param weight: маса в кілограмах (float)
    :param height: зріст у метрах (float)
    :return: значення BMI (float)
    :raises ValueError: якщо weight або height некоректні
    """
    if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Введені дані мають бути числами.")
    if weight <= 0 or height <= 0:
        raise ValueError("Маса та зріст мають бути додатними числами.")

    return round(weight / (height**2), 2)


# --- Тестування через assert ---
def test_asserts():
    """Тести функції calculate_bmi через оператор assert."""
    assert calculate_bmi(70, 1.75) == 22.86
    assert calculate_bmi(50, 1.6) == 19.53
    assert calculate_bmi(90, 1.9) == 24.93
    assert calculate_bmi(100, 2.0) == 25.0
    assert calculate_bmi(60, 1.5) == 26.67

    try:
        calculate_bmi(-70, 1.8)
    except ValueError:
        pass
    else:
        raise AssertionError("Мала бути помилка для від’ємної маси")

    try:
        calculate_bmi(70, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Мала бути помилка для нульового зросту")

    try:
        calculate_bmi("70", 1.8)
    except ValueError:
        pass
    else:
        raise AssertionError("Мала бути помилка для текстового вводу")


if __name__ == "__main__":
    test_asserts()
    print("✅ Усі тести через assert пройдено успішно!")
