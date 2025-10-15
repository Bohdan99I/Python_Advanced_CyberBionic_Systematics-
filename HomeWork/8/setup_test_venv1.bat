@echo off
echo ==========================================
echo 🔧 Створення віртуального оточення test_venv
echo ==========================================

REM Перевіряємо, чи встановлено virtualenv
pip show virtualenv >nul 2>&1
if errorlevel 1 (
    echo ⚙️ Встановлюємо virtualenv...
    pip install virtualenv
)

REM Створюємо оточення
virtualenv test_venv

REM Активуємо оточення
call test_venv\Scripts\activate

echo ==========================================
echo 📦 Встановлення пакетів
echo ==========================================
pip install "django==3.2"
pip install "beautifulsoup4==4.12.3"
pip install "pillow==2.3.0"

echo ==========================================
echo ✅ Перевірка встановлених пакетів
echo ==========================================
pip list

echo ==========================================
echo 🚪 Деактивація оточення
echo ==========================================
deactivate

echo ✅ Готово! Оточення test_venv створено й деактивовано.
