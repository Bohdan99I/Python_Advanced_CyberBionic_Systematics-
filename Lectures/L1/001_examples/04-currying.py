"""Приклад карирування функції"""


def ordinary_add(x, y):
    """Звичайна функція"""
    return x + y


def curryied_add(x):
    """Карирована функція"""
    def do_add(y):
        return x + y

    return do_add


# Виконання звичайної функції вимагає всіх аргументів прямо тут і зараз"
print(ordinary_add(2, 3))
print()
# Карування дозволяє передавати аргументи у функцію поступово: спочатку перший аргумент, потім другий
print(curryied_add(2)(3))
print()
# Карування робить легким часткове застосування функцій
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))
print()

# У вигляді лямбда-виразів
ordinary_add = lambda x, y: x + y
curryied_add = lambda x: lambda y: x + y

print(ordinary_add(2, 3))
print(curryied_add(2)(3))
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))
