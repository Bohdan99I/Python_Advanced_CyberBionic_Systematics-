"""
Скрипт для парсингу веб-сторінки: отримує заголовок (title)
та вміст усіх тегів <div> з вказаного URL.
"""

import requests
from bs4 import BeautifulSoup

# URL-адреса для парсингу
URL = "https://edu.cbsystematics.com/ua"

try:
    # 1. Отримання HTML-коду сторінки
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    # 2. Парсинг HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # --- A. Читання Title ---
    page_title = soup.title.string

    print("=========================================")
    print(f"Заголовок сторінки (Title): {page_title}")
    print("=========================================")

    # --- B. Читання всіх тегів <div> ---
    div_tags = soup.find_all("div")

    print(f"\nЗнайдено {len(div_tags)} тегів <div>. Друк вмісту:")
    print("-----------------------------------------")

    # 3. Роздруківка тегів <div> через цикл for
    for index, div in enumerate(div_tags, 1):
        # Отримання тексту тега <div>
        div_content = div.get_text(strip=True)

        print(f"DIV #{index}:")
        print(div_content)
        print("-----------------------------------------")

except requests.exceptions.RequestException as e:
    print(f"Помилка при отриманні сторінки: {e}")
except AttributeError:
    print("Помилка: Не вдалося знайти тег <title> на сторінці.")
except (IOError, OSError) as e:
    print(f"Виникла неочікувана помилка: {e}")

print("\nРобота скрипта завершена.")
print ("=========================================")
