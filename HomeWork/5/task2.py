"""
Завдання 2.
Програма перевіряє наявність файлу і шукає рядок "Wow!".
Якщо знайдено — генерується подія, і інший потік видаляє файл.
"""

import os
import time
import threading

# Подія, яку згенерує перша функція при знаходженні "Wow!"
file_event = threading.Event()

# Ім'я файлу для перевірки
FILENAME = "test_file.txt"


def check_file_for_wow(filename: str):
    """Функція перевіряє наявність файлу та рядка 'Wow!'."""
    while True:
        if not os.path.exists(filename):
            print("[INFO] Файл не знайдено. Очікування 5 секунд...")
            time.sleep(5)
            continue

        print("[INFO] Файл знайдено. Перевірка вмісту...")

        try:
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                if any("Wow!" in line for line in lines):
                    print("[SUCCESS] Знайдено рядок 'Wow!' у файлі!")
                    file_event.set()
                    break
                else:
                    print(
                        "[INFO] Рядка 'Wow!' не знайдено. Перевірка знову через 5 секунд..."
                    )
                    time.sleep(5)
        except Exception as e:
            print(f"[ERROR] Помилка при читанні файлу: {e}")
            time.sleep(5)


def delete_file_on_event(filename: str):
    """Функція очікує подію та видаляє файл."""
    print("[WAITING] Очікування сигналу для видалення файлу...")
    file_event.wait()
    try:
        os.remove(filename)
        print(f"[DELETED] Файл '{filename}' видалено після знаходження 'Wow!'")
    except FileNotFoundError:
        print("[WARNING] Файл вже видалено або не існує.")


def create_file_if_not_exists(filename: str):
    """Допоміжна функція — створює файл, якщо його немає."""
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Тут буде щось цікаве...\n")
        print(f"[INFO] Створено файл '{filename}' без рядка 'Wow!'")


def main():
    """Основна функція, що запускає потоки."""
    create_file_if_not_exists(FILENAME)

    # Створюємо два потоки
    checker_thread = threading.Thread(target=check_file_for_wow, args=(FILENAME,))
    deleter_thread = threading.Thread(target=delete_file_on_event, args=(FILENAME,))

    # Запускаємо обидва
    checker_thread.start()
    deleter_thread.start()

    # Очікуємо завершення
    checker_thread.join()
    deleter_thread.join()

    print("[DONE] Програма завершила роботу.")


if __name__ == "__main__":
    main()
