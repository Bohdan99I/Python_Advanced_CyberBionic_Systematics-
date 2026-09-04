import sqlite3


# функція конвертації значення
def upper_word(raw):
    return raw.upper()


conn = sqlite3.connect(':memory:')
# реєструємо нашу функцію, щоб використовувати її в SQL запиті
conn.create_function('upper1', 1, upper_word)
cur = conn.cursor()

cur.execute('CREATE TABLE users(first_name char(20))')
cur.execute(
    'INSERT INTO users(first_name) VALUES ("Eugene"),("Dmitry"),("Viktor")'
)
# тестуємо нашу функцію
cur.execute('SELECT upper1(first_name) FROM users')
row = cur.fetchone()
print(row)
