"""Приклад використання функції модуля lru_cache functools"""

from functools import lru_cache

# Тут функцію обчислення чисел Фібоначчі записано рекурсивно, але по
# продуктивності та витрати пам'яті вона буде порівнянна з нерекурсивною


@lru_cache(maxsize=None)
def fibonacci(index):
    if index < 2:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)


for i in range(1, 100):
    print(fibonacci(i))

