"""
Модуль містить приклад декоратора для заміру часу виконання функції.
"""

import time
from functools import wraps


def measure_time(func):
    """
    Декоратор для заміру часу виконання функції.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # старт заміру
        result = func(*args, **kwargs)
        end = time.perf_counter()  # кінець заміру
        print(f"Функція '{func.__name__}' виконалась за {end - start:.6f} секунд")
        return result

    return wrapper


@measure_time
def slow_function():
    """
    Функція для тестування декоратора.
    Виконує обчислення суми чисел від 0 до 10_000_000.
    """
    total = 0
    for i in range(10_000_000):
        total += i
    return total


if __name__ == "__main__":
    print(slow_function())
