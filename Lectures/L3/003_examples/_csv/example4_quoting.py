import csv

# екранування усіх комірок файлу
quoting = csv.QUOTE_ALL

with open('data/output.csv', 'w') as f:
    # використовуємо DictWriter для зручнішої роботи з даними він дозволяє працювати з рядками як зі словником,
    # звертаючись до значень за ключами (назвою колонок)
    writer = csv.DictWriter(
        f,
        fieldnames=['first_name', 'last_name', 'age'],
        quoting=quoting
    )
    # запис ключів:
    writer.writeheader()
    # запис також проводиться з використанням словників як рядки з даними,
    # що більш інтуїтивно, ніж просто плоский список
    writer.writerow({
        'first_name': 'Ivan',
        'last_name': 'Petrov @ ll, Test',
        'age': 20
    })
    writer.writerow({
        'first_name': 'Dmitry',
        'last_name': 'Sidorov',
        'age': 30
    })
    writer.writerow({
        'first_name': 'Alexey',
        'last_name': 'Ivanov',
        'age': 30
    })
