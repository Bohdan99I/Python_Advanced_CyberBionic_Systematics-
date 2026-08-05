import csv


class CustomDialect(csv.Dialect):
    """
    Створення власне діалекту, який дозволяє нам описати правила для читання та запису файлу.
    Зручний механізм, якщо ви використовуєте власні правила обробки CSV, які можна згрупувати у діалект.
    """
    quoting = csv.QUOTE_ALL
    # заповнення порожнечі
    quotechar = "*"
    # знаки перерахування
    delimiter = "!"
    lineterminator = '\n'


# реєстрація діалекту, щоб він був доступний під час створення reader/writer.
csv.register_dialect('tester', CustomDialect)

with open('data/output.csv', 'w') as f:
    # два варіанти передачі діалекту
    # 1. передача класу діалекту
    # writer = csv.writer(f, dialect=CustomDialect)
    # 2. передача імені діалекту, який заздалегідь зареєстрували з цим же ім'ям.
    writer = csv.writer(f, dialect='tester')
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
