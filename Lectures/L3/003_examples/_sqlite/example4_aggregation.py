import sqlite3


class RowSet:
    """
    Клас для реалізації функціоналу власної агрегаційної функції.

    Приклад:
        id, first_name, last_name
        1, f1, l1
        2, f2, l2
        3, f3, l3
        4, f4, l4
        5, f5, l5

    Запит:
        SELECT row_set(first_name) AS result FROM users;

    Результат:
        f1;f2;f3;f4;f5
    """

    def __init__(self):
        # ініціалізуємо контейнер
        self.rows = set()

    def step(self, value):
        # додаємо елемент до контейнера
        self.rows.add(value)

    def finalize(self):
        # завершення агрегації
        return ';'.join(self.rows)


conn = sqlite3.connect(':memory:')
# реєструємо наш клас для роботи з нашою агрегаційною функцією
conn.create_aggregate('row_set', 1, RowSet)

cur = conn.cursor()
cur.execute('CREATE TABLE users(first_name)')
cur.execute(
    """INSERT INTO users(first_name)
       VALUES ("Dmitry"),
              ("Eugene"),
              ("Viktor"),
              ("Nikita"),
              ("Eugene")
     """
)

# пробуємо запуск агрегації по полю first_name - результат буде конкатенація всіх first_name до таблиці
cur.execute('SELECT row_set(first_name) AS result FROM users')
results = cur.fetchall()
print(dict())
