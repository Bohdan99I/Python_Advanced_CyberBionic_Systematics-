"""
Завдання 3
Робота з базою даних і SMTP.
"""

import sqlite3
import smtplib
from email.mime.text import MIMEText
from datetime import date


class User:
    """
    Клас, який описує користувача системи.
    Містить ім’я, прізвище, по батькові, дату народження та email.
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        middle_name: str,
        birthday: date,
        email: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birthday = birthday
        self.email = email

    def get_full_name(self) -> str:
        """Повертає повне ім'я користувача."""
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_short_name(self) -> str:
        """Повертає коротке ім'я користувача."""
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    def get_age(self) -> int:
        """Обчислює вік користувача."""
        today = date.today()
        return (
            today.year
            - self.birthday.year
            - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        )

    def __str__(self):
        return f"{self.get_full_name()} ({self.birthday})"


def init_db():
    """Ініціалізує базу даних."""
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            middle_name TEXT,
            birthday TEXT,
            email TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def add_user_to_db(user: User):
    """Додає користувача до бази."""
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO users (first_name, last_name, middle_name, birthday, email)
        VALUES (?, ?, ?, ?, ?)
    """,
        (
            user.first_name,
            user.last_name,
            user.middle_name,
            str(user.birthday),
            user.email,
        ),
    )
    conn.commit()
    conn.close()
    print(f"✅ Користувача {user.get_full_name()} додано до бази даних.")


def find_user_in_db(keyword: str):
    """Пошук користувачів за частиною імені або email."""
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(
        """
        SELECT first_name, last_name, middle_name, birthday, email FROM users
        WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ?
    """,
        (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"),
    )
    results = cur.fetchall()
    conn.close()
    return results


def send_thank_you_email(user: User):
    """
    Надсилає тестовий лист подяки користувачу (заглушка).
    Для реального запуску потрібно вказати справжні дані SMTP.
    """

    sender_email = "example@gmail.com"
    recipient_email = user.email
    subject = "Дякуємо за реєстрацію!"
    body = f"Привіт, {user.first_name}! Дякуємо за реєстрацію у нашій системі."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    print(f"📧 Імітація надсилання листа на {recipient_email}...")

    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        # smtp.login("your_email", "your_password")
        # smtp.send_message(msg)
        smtp.quit()
        print("✅ Лист подяки надіслано (заглушка).")
    except smtplib.SMTPException as e:
        print(f"⚠️ Помилка SMTP під час надсилання листа: {e}")


def register_user(user: User):
    """Реєстрація користувача з надсиланням листа."""
    add_user_to_db(user)
    send_thank_you_email(user)


if __name__ == "__main__":
    init_db()

    new_user = User(
        "Ігор", "Петров", "Сергійович", date(1990, 5, 14), "test@example.com"
    )
    register_user(new_user)

    print("\n🔍 Пошук користувача за іменем 'Ігор':")
    found = find_user_in_db("Ігор")
    for row in found:
        print(row)
