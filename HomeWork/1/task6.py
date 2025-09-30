"""
Завдання 6: Функція-генератор чисел Фібоначчі з декоратором, що залишає лише парні числа.
"""

from typing import Generator, Callable


def only_even(generator_func: Callable) -> Callable:
    """
    Декоратор, який фільтрує послідовність, залишаючи лише парні числа.
    """

    def wrapper(*args, **kwargs) -> Generator[int, None, None]:
        for value in generator_func(*args, **kwargs):
            if value % 2 == 0:
                yield value

    return wrapper


@only_even
def fibonacci(n: int) -> Generator[int, None, None]:
    """
    Генератор чисел Фібоначчі.

    Аргументи:
        n (int): Кількість чисел Фібоначчі для генерації.

    Повертає:
        Генератор, що видає числа Фібоначчі.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# Приклад використання
for num in fibonacci(20):
    print(num)
