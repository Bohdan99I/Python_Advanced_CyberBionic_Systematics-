import csv

# створюємо екземпляр класу Sniffer для подальшого використання при
# # сканування структур файлів
sniffer = csv.Sniffer()
dialect = None

# спроба прочитати файл без вказівки конкретного діалекту, але файл містить
# нестандартні правила, що призведе до некоректності читання.
# Деякі стовпці зовсім будуть об'єднані і дані будуть прочитані неправильно.
with open('data/undefined_dialect.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# спроба відкрити файл та просканувати його вміст на визначення діалекту
# за допомогою Sniffer.
with open('data/undefined_dialect.csv', 'r') as f:
    content = f.read()
    # можна віддавати шматок файлу, не обов'язково весь, все залежить від розміру файлу та порції даних,
    # за якою sniffer зможе визначити діалект.
    dialect = sniffer.sniff(content)

# виводимо отриманий результат, щоб переконатися, що роздільники та екранування коректно обчислені
print(dialect.delimiter, dialect.doublequote, dialect.quoting)

# успішне читання файлу CSV за допомогою обчисленого діалекту.
with open('data/undefined_dialect.csv', 'r') as f:
    reader = csv.reader(f, dialect=dialect)
    for row in reader:
        print(row)
