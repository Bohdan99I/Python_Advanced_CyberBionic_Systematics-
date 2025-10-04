"""
Завдання 2:
- створення XML-файлу з вкладеними елементами,
- використання XPath для пошуку даних.
"""

import xml.etree.ElementTree as ET

# Ім'я файлу
file_path = "library.xml"

# Створюємо XML структуру
library = ET.Element("library")

book1 = ET.SubElement(library, "book", attrib={"id": "1"})
ET.SubElement(book1, "title").text = "Мистецтво війни"
ET.SubElement(book1, "author").text = "Сунь-цзи"
ET.SubElement(book1, "year").text = "500 до н.е."

book2 = ET.SubElement(library, "book", attrib={"id": "2"})
ET.SubElement(book2, "title").text = "Кобзар"
ET.SubElement(book2, "author").text = "Тарас Шевченко"
ET.SubElement(book2, "year").text = "1840"

book3 = ET.SubElement(library, "book", attrib={"id": "3"})
ET.SubElement(book3, "title").text = "Майстер і Маргарита"
ET.SubElement(book3, "author").text = "Михайло Булгаков"
ET.SubElement(book3, "year").text = "1967"

# Записуємо XML у файл
tree = ET.ElementTree(library)
tree.write(file_path, encoding="utf-8", xml_declaration=True)

print(f"✅ XML файл збережено у {file_path}")

# Завантаження XML з файлу
tree = ET.parse(file_path)
root = tree.getroot()

# Пошук усіх книг
print("\n📚 Усі книги в бібліотеці:")
for book in root.findall("book"):
    title = book.find("title").text
    author = book.find("author").text
    print(f"- {title} ({author})")

# Пошук книги за автором
print("\n🔎 Книги Тараса Шевченка:")
for book in root.findall("book"):
    if book.find("author").text == "Тарас Шевченко":
        print(book.find("title").text)

# Пошук книги, де рік > 1900
print("\n📖 Книги після 1900 року:")
for book in root.findall("book"):
    try:
        year = int(book.find("year").text.split()[0])
        if year > 1900:
            print(book.find("title").text)
    except ValueError:
        pass
