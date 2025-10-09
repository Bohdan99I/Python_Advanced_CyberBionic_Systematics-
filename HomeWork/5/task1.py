"""
Модуль для демонстрації багатопотокового обчислення факторіала.
Порівнює швидкість виконання через Thread та ThreadPoolExecutor.
"""

import math
import threading
import time
import sys
from concurrent.futures import ThreadPoolExecutor

# Дозволяє конвертувати великі числа у рядки
sys.set_int_max_str_digits(10000000)


def calculate_factorial(n: int) -> int:
    """Обчислює факторіал числа n."""
    return math.factorial(n)


def run_with_threads(numbers):
    """Запускає обчислення факторіалів через Thread."""
    threads = []
    results = []

    def worker(num):
        """Виконує обчислення факторіала для одного числа."""
        result = calculate_factorial(num)
        results.append((num, result))

    start = time.time()
    for num in numbers:
        t = threading.Thread(target=worker, args=(num,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    end = time.time()

    print("\nРезультати через Thread:")
    for num, result in results:
        print(f"{num}! має {len(str(result))} цифр")
    print(f"Час виконання (Thread): {end - start:.5f} секунд")


def run_with_threadpool(numbers):
    """Запускає обчислення факторіалів через ThreadPoolExecutor."""
    start = time.time()
    results = []

    with ThreadPoolExecutor(max_workers=len(numbers)) as executor:
        future_to_num = {
            executor.submit(calculate_factorial, num): num for num in numbers
        }
        for future in future_to_num:
            num = future_to_num[future]
            result = future.result()
            results.append((num, result))

    end = time.time()

    print("\nРезультати через ThreadPoolExecutor:")
    for num, result in results:
        print(f"{num}! має {len(str(result))} цифр")
    print(f"Час виконання (ThreadPoolExecutor): {end - start:.5f} секунд")


def main():
    """Основна функція, що запускає обчислення для заданих чисел."""
    numbers = [10000, 15000, 20000, 25000]
    print("=== Запуск через Thread ===")
    run_with_threads(numbers)

    print("\n=== Запуск через ThreadPoolExecutor ===")
    run_with_threadpool(numbers)


if __name__ == "__main__":
    main()
