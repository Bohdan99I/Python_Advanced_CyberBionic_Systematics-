"""
Завдання 7: Звичайна функція множення, карирова функція та часткове застосування.
"""

from functools import partial
from typing import Callable


def multiply(a: int, b: int) -> int:
    """
    Звичайна функція множення двох чисел.

    Аргументи:
        a (int): перше число
        b (int): друге число

    Повертає:
        int: добуток a і b
    """
    return a * b


def curry_multiply(a: int) -> Callable[[int], int]:
    """
    Карирова функція множення.

    Аргументи:
        a (int): перше число

    Повертає:
        Функцію, яка приймає друге число і повертає добуток
    """

    def inner(b: int) -> int:
        return a * b

    return inner


# Часткове застосування за допомогою functools.partial
partial_multiply_by_2 = partial(multiply, 2)  # перший аргумент зафіксований як 2
partial_multiply_by_3_and_4 = partial(multiply, 3, 4)  # обидва аргументи зафіксовані

# Приклади використання
print("Звичайна функція:", multiply(5, 6))  # 30
print("Карирова функція:", curry_multiply(5)(6))  # 30
print("Часткове застосування (2*7):", partial_multiply_by_2(7))  # 14
print("Часткове застосування (3*4):", partial_multiply_by_3_and_4())  # 12
