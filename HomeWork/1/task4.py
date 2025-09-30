"""
task4.py
Програма для порівняння швидкості виконання обчислення чисел Фібоначчі
з різними підходами до кешування.
"""

import functools
import time


def timer(func):
    """
    Декоратор для замірювання часу виконання функції.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функція {func.__name__} виконалася за {end - start:.6f} сек.")
        return result

    return wrapper


def fib_no_cache(n: int) -> int:
    """
    Обчислення числа Фібоначчі без кешу.
    """
    if n <= 1:
        return n
    return fib_no_cache(n - 1) + fib_no_cache(n - 2)


_cache = {}


def fib_with_dict_cache(n: int) -> int:
    """
    Обчислення числа Фібоначчі з кешем на основі словника.
    """
    if n in _cache:
        return _cache[n]
    if n <= 1:
        _cache[n] = n
    else:
        _cache[n] = fib_with_dict_cache(n - 1) + fib_with_dict_cache(n - 2)
    return _cache[n]


@functools.lru_cache(maxsize=10)
def fib_lru_10(n: int) -> int:
    """
    Обчислення числа Фібоначчі з lru_cache (maxsize=10).
    """
    if n <= 1:
        return n
    return fib_lru_10(n - 1) + fib_lru_10(n - 2)


@functools.lru_cache(maxsize=16)
def fib_lru_16(n: int) -> int:
    """
    Обчислення числа Фібоначчі з lru_cache (maxsize=16).
    """
    if n <= 1:
        return n
    return fib_lru_16(n - 1) + fib_lru_16(n - 2)


@timer
def test_fib_no_cache():
    """
    Тест: обчислення 25 чисел Фібоначчі без кешу.
    """
    return [fib_no_cache(i) for i in range(25)]


@timer
def test_fib_with_dict_cache():
    """
    Тест: обчислення 25 чисел Фібоначчі зі словниковим кешем.
    """
    return [fib_with_dict_cache(i) for i in range(25)]


@timer
def test_fib_lru_10():
    """
    Тест: обчислення 25 чисел Фібоначчі з lru_cache (maxsize=10).
    """
    return [fib_lru_10(i) for i in range(25)]


@timer
def test_fib_lru_16():
    """
    Тест: обчислення 25 чисел Фібоначчі з lru_cache (maxsize=16).
    """
    return [fib_lru_16(i) for i in range(25)]


if __name__ == "__main__":
    print("Тест без кешу:")
    test_fib_no_cache()

    print("\nТест з кешем (dict):")
    test_fib_with_dict_cache()

    print("\nТест з lru_cache(maxsize=10):")
    test_fib_lru_10()

    print("\nТест з lru_cache(maxsize=16):")
    test_fib_lru_16()
