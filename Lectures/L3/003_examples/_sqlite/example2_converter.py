import json
import sqlite3


# пишемо свій адаптер, який перетворює словник на текст формату JSON
def adapt_json(data):
    return json.dumps(data)


# пишемо свій конвертер, який перетворює текст формату JSON на словник
# дія зворотна адаптеру
def convert_json(raw):
    return json.loads(raw)


# conn = sqlite3.connect(":memory:")
# cur = conn.cursor()
#
# cur.execute('CREATE TABLE test(p json)')
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'ppp': 10},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'ppp': 11},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 3, 'ppp': 12},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 4, 'ppp': 13},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 5, 'ppp': 14},))
# cur.execute('SELECT * FROM test')
# row = cur.fetchone()
#
# conn.close()


# реєструємо адаптер та конвертер.
# визначаємо поведінки для конвертації у двох напрямках
# 1. з мови Python до бази даних
# 2. з бази даних SQLite в типи даних Python (у нашому випадку dict)
sqlite3.register_adapter(dict, adapt_json)
sqlite3.register_converter('json', convert_json)

# визначаємо базу даних в оперативній пам'яті
conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()

# створюємо таблицю з нашим типом даних та пробуємо вставити dict
cur.execute('CREATE TABLE test(p json)')
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'ppp': 10},))
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'ppp': 11},))

# беремо перший запис і перевіряємо роботу нашого адаптера та конвертера
cur.execute('SELECT * FROM test')
record = cur.fetchone()
print(type(record[0]))
