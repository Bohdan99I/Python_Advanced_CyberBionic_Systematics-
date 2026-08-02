import csv

with open('data/example1.csv', 'r') as f:
    # передаємо у reader файловий дескриптор
    reader = csv.reader(f)
    print('Line nums', reader.line_num)
    # друкуємо dialect, який відповідає правила парсингу CSV файлу.
    print('Dialect', reader.dialect)
    # запуск циклу та ітеруємося по кожному рядку в CSV-файлі
    for row in reader:
        print(row)
