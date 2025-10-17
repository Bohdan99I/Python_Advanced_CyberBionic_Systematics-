@echo off
echo ============================================
echo     Створення середовища test_conda
echo ============================================

:: Перевірка, чи встановлено conda
conda --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Помилка: Conda не знайдено. Будь ласка, встановіть Anaconda або Miniconda.
    pause
    exit /b
)

:: Створюємо середовище test_conda з Python 3.10
echo Створення середовища test_conda з Python 3.10...
conda create -n test_conda python=3.10 -y

:: Активуємо середовище
echo Активую середовище test_conda...
call conda activate test_conda

:: Встановлюємо потрібні пакети
echo Встановлюю Django 4, BeautifulSoup4 та Pillow 8.4.0...
pip install "Django==4.*" "beautifulsoup4" "Pillow==8.4.0"

:: Відображаємо список встановлених пакетів
echo ============================================
echo     Встановлені пакети у test_conda:
echo ============================================
pip list

:: Деактивуємо середовище
echo Деактивація середовища...
call conda deactivate

echo ============================================
echo     Середовище test_conda створено і вимкнено
echo ============================================
pause
