import sqlite3

# Підключення до бази (створить файл university.db у поточній папці)
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Створення таблиць
cursor.executescript("""
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS grades;

CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    faculty TEXT NOT NULL
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT NOT NULL,
    grade INTEGER,
    date TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
""")

# Додавання тестових даних
cursor.executescript("""
INSERT INTO groups (name, faculty) VALUES
('CS-101', 'Computer Science'),
('IT-202', 'Information Technology'),
('DS-303', 'Data Science');

INSERT INTO students (firstname, lastname, group_id) VALUES
('Ivan', 'Petrenko', 1),
('Olena', 'Shevchenko', 1),
('Andriy', 'Koval', 2),
('Maria', 'Tkachenko', 3),
('Petro', 'Ivanov', 2);

INSERT INTO grades (student_id, subject, grade, date) VALUES
(1, 'Math', 90, '2025-10-10'),
(2, 'Programming', 95, '2025-10-09'),
(3, 'Databases', 88, '2025-10-08'),
(4, 'AI', 92, '2025-10-07'),
(5, 'Networking', 85, '2025-10-06');
""")

# Зберігаємо зміни
conn.commit()
conn.close()

print("✅ База даних 'university.db' створена успішно!")
