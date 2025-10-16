@echo off
echo ============================================
echo   Створення віртуального оточення test_poetry
echo ============================================

:: Перевіряємо, чи встановлено Poetry
poetry --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Poetry не встановлено. Встановлюю...
    pip install poetry
)

:: Ініціалізація нового проєкту (якщо ще не існує)
if not exist pyproject.toml (
    echo Ініціалізація нового проекту...
    poetry init --no-interaction
)

:: Вказуємо потрібну версію Python
echo Налаштовую Python 3.9...
poetry env use python3.9

:: Створюємо та активуємо середовище
echo Створюю середовище test_poetry...
poetry shell

:: Встановлюємо потрібні пакети
echo Встановлюю Django 3.1, BeautifulSoup4 та Pillow 2.7.0...
poetry add django==3.1 beautifulsoup4 pillow==2.7.0

:: Відображаємо список встановлених пакетів
echo ============================================
echo   Встановлені пакети:
echo ============================================
poetry show

:: Деактивація середовища
echo Деактивація середовища...
deactivate

echo ============================================
echo   Середовище test_poetry створено та вимкнено
echo ============================================
pause
