"""
Скрипт для веб-скрапінгу сайту books.toscrape.com.
Збирає інформацію про книги (назва, ціна, рейтинг, наявність)
з перших 10 сторінок та зберігає її у форматі CSV.
"""

import csv
import re
import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

MAX_PAGES_TO_SCRAPE = 10

BASE_URL = "http://books.toscrape.com/"
START_URL = "http://books.toscrape.com/catalogue/page-1.html"
OUTPUT_FILE = "books_data.csv"

RATING_MAP = {
    "One": "One",
    "Two": "Two",
    "Three": "Three",
    "Four": "Four",
    "Five": "Five",
}


def fetch_html(url):
    """Виконує HTTP GET-запит і повертає HTML-контент."""
    try:
        # Додаємо невелику затримку для ввічливості
        time.sleep(0.5)

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        response.encoding = "utf-8"

        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Помилка при запиті URL {url}: {e}")
        return None


def parse_book_data(html_content):
    """Парсить HTML, вилучає дані про книги та посилання на наступну сторінку."""
    soup = BeautifulSoup(html_content, "html.parser")
    all_books_data = []

    products = soup.find_all("article", class_="product_pod")

    for book in products:
        # 1. Назва (Title)
        title_tag = book.h3.a
        title = (
            title_tag["title"] if title_tag and "title" in title_tag.attrs else "N/A"
        )

        # 2. Ціна (Price)
        price_tag = book.select_one(".price_color")
        raw_price = price_tag.get_text(strip=True) if price_tag else "£0.00"

        clean_price = re.sub(r"[^\d.]", "", raw_price)

        try:
            price_float = float(clean_price)
        except ValueError:
            print(f"Помилка перетворення ціни: '{raw_price}'. Використовуємо 0.00.")
            price_float = 0.00

        # 3. Рейтинг (Rating)
        rating_tag = book.select_one(".star-rating")
        raw_rating_class = (
            rating_tag["class"][-1]
            if rating_tag and "class" in rating_tag.attrs
            else "Unknown"
        )
        rating_word = RATING_MAP.get(raw_rating_class, "Unknown")

        # 4. Наявність на складі (Availability)
        availability_tag = book.select_one(".instock")
        is_available = (
            "In stock" in availability_tag.get_text() if availability_tag else False
        )

        all_books_data.append(
            {
                "Назва": title,
                "Ціна": price_float,
                "Рейтинг": rating_word,
                "Наявність": is_available,
            }
        )

    # --- Навігація: пошук наступної сторінки ---
    next_tag = soup.select_one("li.next > a")
    next_page_url = None
    if next_tag and "href" in next_tag.attrs:
        next_page_url = urljoin(BASE_URL, "catalogue/" + next_tag["href"])

    return all_books_data, next_page_url


def save_to_csv(data):
    """Зберігає зібрані дані у CSV-файл."""
    if not data:
        print("Немає даних для збереження.")
        return

    fieldnames = ["Назва", "Ціна", "Рейтинг", "Наявність"]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"\n✅ Дані успішно збережено у файл: {OUTPUT_FILE}")
    print(f"   Зібрано {len(data)} записів.")


def main_scraper():
    """Головна функція для керування скрапінгом з обмеженням сторінок."""
    all_scraped_data = []
    current_url = START_URL
    page_count = 0

    print(f"Початок скрапінгу з: {START_URL}")
    print(f"Обмеження: перші {MAX_PAGES_TO_SCRAPE} сторінок.")

    while current_url and page_count < MAX_PAGES_TO_SCRAPE:
        page_count += 1
        print(
            f"--> Обробка сторінки #{page_count}/{MAX_PAGES_TO_SCRAPE}: {current_url}"
        )

        html = fetch_html(current_url)
        if not html:
            break

        book_data, next_url = parse_book_data(html)
        all_scraped_data.extend(book_data)

        current_url = next_url

    print(f"\nСкрапінг завершено. Зібрано дані з {page_count} сторінок.")
    save_to_csv(all_scraped_data)


if __name__ == "__main__":
    main_scraper()
