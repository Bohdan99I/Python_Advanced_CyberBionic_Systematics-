"""Приклад використання функції partial модуля functools"""

from functools import partial

# Часткове застосування функції
print_with_comma = partial(print, sep=', ')

print_with_comma(2, 3, 5)
