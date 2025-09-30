"""
Завдання 3:
Програма виводить 25 перших чисел Фібоначчі:
1. Без кешу
2. З кешем довільної довжини (власна реалізація)
3. З кешем з functools.lru_cache(maxsize=10)
4. З кешем з functools.lru_cache(maxsize=16)
"""

from functools import lru_cache


# 1. Фібоначчі без кешу
def fib_no_cache(n: int) -> int:
    """Фібоначчі без кешу."""
    if n < 2:
        return n
    return fib_no_cache(n - 1) + fib_no_cache(n - 2)


# 2. Фібоначчі з кешем (власна реалізація словником)
fib_cache = {}


def fib_with_dict_cache(n: int) -> int:
    """Фібоначчі з кешем у словнику."""
    if n in fib_cache:
        return fib_cache[n]
    if n < 2:
        fib_cache[n] = n
    else:
        fib_cache[n] = fib_with_dict_cache(n - 1) + fib_with_dict_cache(n - 2)
    return fib_cache[n]


# 3. Фібоначчі з functools.lru_cache(maxsize=10)
@lru_cache(maxsize=10)
def fib_lru_10(n: int) -> int:
    """Фібоначчі з functools.lru_cache(maxsize=10)."""
    if n < 2:
        return n
    return fib_lru_10(n - 1) + fib_lru_10(n - 2)


# 4. Фібоначчі з functools.lru_cache(maxsize=16)
@lru_cache(maxsize=16)
def fib_lru_16(n: int) -> int:
    """Фібоначчі з functools.lru_cache(maxsize=16)."""
    if n < 2:
        return n
    return fib_lru_16(n - 1) + fib_lru_16(n - 2)


if __name__ == "__main__":
    print("Фібоначчі без кешу:")
    print([fib_no_cache(i) for i in range(25)])

    print("\nФібоначчі з кешем (dict):")
    print([fib_with_dict_cache(i) for i in range(25)])

    print("\nФібоначчі з lru_cache (maxsize=10):")
    print([fib_lru_10(i) for i in range(25)])

    print("\nФібоначчі з lru_cache (maxsize=16):")
    print([fib_lru_16(i) for i in range(25)])
