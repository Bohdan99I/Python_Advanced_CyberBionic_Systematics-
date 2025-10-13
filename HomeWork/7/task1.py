"""
Завдання 1:
"""

from typing import List


def convert_int_list_to_str_list(numbers: List[int]) -> List[str]:
    """
    Приймає список чисел (int) і повертає список рядкових значень (str).
    """
    return [str(num) for num in numbers]


if __name__ == "__main__":
    original_numbers = [10, 25, 33, 47, 100]
    string_numbers = convert_int_list_to_str_list(original_numbers)

    print("Оригінальний список:", original_numbers)
    print("Список у вигляді рядків:", string_numbers)
