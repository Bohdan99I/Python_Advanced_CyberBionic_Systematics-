"""
Модуль для розрахунку швидкості автомобіля.
Містить функцію calculate_speed() і тести з використанням assert.
"""


def calculate_speed(distance_km: float, time_h: float) -> float:
    """
    Обчислює швидкість автомобіля (км/год).
    Формула: швидкість = відстань / час

    :param distance_km: довжина шляху у кілометрах
    :param time_h: тривалість шляху у годинах
    :return: швидкість у км/год
    """
    if not isinstance(distance_km, (int, float)) or not isinstance(
        time_h, (int, float)
    ):
        raise TypeError("Відстань і час повинні бути числами")

    if distance_km < 0 or time_h <= 0:
        raise ValueError("Відстань має бути невід'ємною, а час — більшим за нуль")

    return round(distance_km / time_h, 2)


if __name__ == "__main__":
    assert calculate_speed(100, 2) == 50.00
    assert calculate_speed(150, 3) == 50.00
    assert calculate_speed(90, 1.5) == 60.00
    assert calculate_speed(0, 1) == 0.00
    assert calculate_speed(120.5, 2.5) == 48.2

    try:
        calculate_speed(-10, 2)
    except ValueError:
        print("✅ Перевірка негативної відстані пройдена")

    try:
        calculate_speed(100, 0)
    except ValueError:
        print("✅ Перевірка ділення на нуль (час = 0) пройдена")

    try:
        calculate_speed("100", 2)
    except TypeError:
        print("✅ Перевірка текстового вводу пройдена")

    print("✅ Усі тести пройдено успішно!")
