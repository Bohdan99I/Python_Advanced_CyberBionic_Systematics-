"""
Модуль для роботи з CSV-файлом користувачів.
Можливості: створення, додавання, читання, конвертація в JSON та XML.
"""

import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

CSV_FILE = Path("people.csv")


def write_csv(overwrite=True):
    """
    Створює або перезаписує CSV-файл на основі введених користувачем даних.
    :param overwrite: True - перезапис, False - додавання нових рядків
    """
    mode = "w" if overwrite else "a"
    with open(CSV_FILE, mode, newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if overwrite:
            writer.writerow(["Name", "Surname", "Birthdate", "City"])
        while True:
            name = input("Введіть ім'я (або Enter для завершення): ")
            if not name:
                break
            surname = input("Введіть прізвище: ")
            birthdate = input("Введіть дату народження (YYYY-MM-DD): ")
            city = input("Введіть місто проживання: ")
            writer.writerow([name, surname, birthdate, city])
            print("Дані додані.\n")


def read_csv():
    """Читає CSV-файл рядок за рядком і виводить на консоль."""
    if not CSV_FILE.exists():
        print("CSV-файл ще не створений.")
        return

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def csv_to_json():
    """Конвертує CSV у JSON та повертає словник."""
    if not CSV_FILE.exists():
        print("CSV-файл ще не створений.")
        return []

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    json_file = CSV_FILE.with_suffix(".json")
    with open(json_file, "w", encoding="utf-8") as jf:
        json.dump(data, jf, ensure_ascii=False, indent=4)

    print(f"Дані збережено у {json_file}")
    return data


def csv_to_xml():
    """Конвертує CSV у XML та повертає ElementTree."""
    if not CSV_FILE.exists():
        print("CSV-файл ще не створений.")
        return None

    data = csv_to_json()  # Використовуємо готовий JSON
    root = ET.Element("People")

    for person in data:
        person_elem = ET.SubElement(root, "Person")
        for key, value in person.items():
            ET.SubElement(person_elem, key).text = value

    tree = ET.ElementTree(root)
    xml_file = CSV_FILE.with_suffix(".xml")
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"Дані збережено у {xml_file}")
    return tree


if __name__ == "__main__":
    while True:
        print("\nВиберіть дію:")
        print("1 - Створити/перезаписати CSV")
        print("2 - Додати нові рядки до CSV")
        print("3 - Прочитати CSV")
        print("4 - Конвертувати CSV у JSON")
        print("5 - Конвертувати CSV у XML")
        print("0 - Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            write_csv(overwrite=True)
        elif choice == "2":
            write_csv(overwrite=False)
        elif choice == "3":
            read_csv()
        elif choice == "4":
            csv_to_json()
        elif choice == "5":
            csv_to_xml()
        elif choice == "0":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

    print("До побачення!")
