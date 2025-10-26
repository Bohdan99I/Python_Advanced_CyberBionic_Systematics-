import sqlite3

# Підключення до бази даних
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

print("=== 📚 Список студентів ===")
cursor.execute("""
SELECT s.id, s.firstname, s.lastname, g.name AS group_name, g.faculty
FROM students s
LEFT JOIN groups g ON s.group_id = g.id
""")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | {row[1]} {row[2]} | Група: {row[3]} | Факультет: {row[4]}")

print("\n=== 🧮 Оцінки студентів ===")
cursor.execute("""
SELECT s.firstname || ' ' || s.lastname AS student_name, subject, grade, date
FROM grades gr
JOIN students s ON gr.student_id = s.id
ORDER BY s.id
""")
for row in cursor.fetchall():
    print(f"Студент: {row[0]} | Предмет: {row[1]} | Оцінка: {row[2]} | Дата: {row[3]}")

conn.close()
