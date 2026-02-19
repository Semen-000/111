import sqlite3
from tabulate import tabulate

# Подключение к базе данных
conn = sqlite3.connect('.venv/example.db')
cursor = conn.cursor()

# Создание таблицы Students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        grade INTEGER,
        city TEXT
    )
''')

# Очищаем таблицу перед добавлением
cursor.execute('DELETE FROM Students')

# Добавление 10 строк
students = [
    ('Иван', 18, 5, 'Москва'),
    ('Ольга', 19, 4, 'Казань'),
    ('Сергей', 20, 5, 'Самара'),
    ('Мария', 18, 3, 'Омск'),
    ('Анна', 21, 4, 'Тула'),
    ('Павел', 22, 5, 'Пермь'),
    ('Юлия', 20, 3, 'Томск'),
    ('Андрей', 19, 4, 'Сочи'),
    ('Виктор', 18, 5, 'Уфа'),
    ('Светлана', 21, 4, 'Воронеж')
]

cursor.executemany('INSERT INTO Students (name, age, grade, city) VALUES (?, ?, ?, ?)', students)
conn.commit()

def print_pretty(title, data, headers):
    print(f"\n{title}")
    print(tabulate(data, headers=headers, tablefmt="grid", numalign="center", stralign="center"))


# Все студенты
cursor.execute('SELECT * FROM Students')
all_students = cursor.fetchall()
print_pretty("ПОЛНЫЙ СПИСОК СТУДЕНТОВ", all_students, ["ID", "Имя", "Возраст", "Оценка", "Город"])

# Оценка 5
cursor.execute('SELECT name, age, grade, city FROM Students WHERE grade = 5')
grade_5 = cursor.fetchall()
print_pretty("СТУДЕНТЫ С ОЦЕНКОЙ 5", grade_5, ["Имя", "Возраст", "Оценка", "Город"])

# Оценка 4
cursor.execute('SELECT name, age, grade, city FROM Students WHERE grade = 4')
grade_4 = cursor.fetchall()
print_pretty("СТУДЕНТЫ С ОЦЕНКОЙ 4", grade_4, ["Имя", "Возраст", "Оценка", "Город"])

# Оценка 3
cursor.execute('SELECT name, age, grade, city FROM Students WHERE grade = 3')
grade_3 = cursor.fetchall()
print_pretty("СТУДЕНТЫ С ОЦЕНКОЙ 3", grade_3, ["Имя", "Возраст", "Оценка", "Город"])

# Поиск студента из Москвы
cursor.execute('SELECT * FROM Students WHERE city = "Москва"')
moscow_students = cursor.fetchall()

if moscow_students:
    print("\n" + "=" * 60)
    print_pretty("СТУДЕНТ ИЗ МОСКВЫ", moscow_students, ["ID", "Имя", "Возраст", "Оценка", "Город"])

conn.close()