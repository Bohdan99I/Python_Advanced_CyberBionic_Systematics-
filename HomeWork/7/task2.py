"""
Завдання 2:
Створіть два класи Directory (тека) і File (файл) з типами (анотацією).
"""

from __future__ import annotations
from typing import List, Optional


class File:
    """
    Клас File представляє файл із назвою та посиланням на теку.
    """

    def __init__(self, name: str, directory: Optional[Directory] = None) -> None:
        self.name: str = name
        self.directory: Optional[Directory] = directory

    def __str__(self) -> str:
        return f"Файл: {self.name}, Тека: {self.directory.name if self.directory else 'Немає'}"


class Directory:
    """
    Клас Directory представляє теку з підтеками та файлами.
    """

    def __init__(self, name: str, root: Optional[Directory] = None) -> None:
        self.name: str = name
        self.root: Optional[Directory] = root
        self.files: List[File] = []
        self.sub_directories: List[Directory] = []

    def add_sub_directory(self, sub_dir: Directory) -> None:
        """
        Додає підкаталог до поточної теки.
        """
        sub_dir.root = self
        self.sub_directories.append(sub_dir)

    def remove_sub_directory(self, sub_dir: Directory) -> None:
        """
        Видаляє підкаталог із поточної теки.
        """
        if sub_dir in self.sub_directories:
            sub_dir.root = None
            self.sub_directories.remove(sub_dir)

    def add_file(self, file: File) -> None:
        """
        Додає файл у поточну теку.
        """
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File) -> None:
        """
        Видаляє файл із поточної теки.
        """
        if file in self.files:
            file.directory = None
            self.files.remove(file)

    def __str__(self) -> str:
        """
        Повертає читабельне представлення теки.
        """
        sub_dirs = ", ".join([d.name for d in self.sub_directories]) or "Немає"
        files = ", ".join([f.name for f in self.files]) or "Немає"
        return f"Тека: {self.name}\n  Підтеки: {sub_dirs}\n  Файли: {files}"


if __name__ == "__main__":
    # Створюємо головну теку
    root_dir = Directory("Root")

    # Створюємо підтеки
    documents = Directory("Documents")
    images = Directory("Images")

    # Додаємо підтеки в Root
    root_dir.add_sub_directory(documents)
    root_dir.add_sub_directory(images)

    # Створюємо файли
    file1 = File("resume.docx")
    file2 = File("photo.jpg")
    file3 = File("notes.txt")

    # Додаємо файли до тек
    documents.add_file(file1)
    documents.add_file(file3)
    images.add_file(file2)

    # Виводимо інформацію про структуру
    print(root_dir)
    print(documents)
    print(images)

    # Видаляємо підтеку та файл для демонстрації
    root_dir.remove_sub_directory(images)
    documents.remove_file(file3)

    print("\nПісля видалення:")
    print(root_dir)
    print(documents)

