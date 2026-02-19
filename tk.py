import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# Функция для центрации окна на экране
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

# ЗАДАЧА 1: Кнопки по диагонали
def task1():
    win = tk.Toplevel()
    win.title("Задача 1: Кнопки по диагонали")
    center_window(win, 400, 400)

    def show_position(position):
        messagebox.showinfo("Позиция", f"Кнопка находится: {position}")

    # Создаем кнопки по диагонали с разными side и anchor
    btn_nw = tk.Button(win, text="NW", bg="lightblue",
                       command=lambda: show_position("в верхнем левом углу"))
    btn_nw.pack(anchor='nw', padx=10, pady=10)

    btn_n = tk.Button(win, text="N", bg="lightgreen",
                      command=lambda: show_position("вверху по центру"))
    btn_n.pack(anchor='n', pady=10)

    btn_ne = tk.Button(win, text="NE", bg="lightcoral",
                       command=lambda: show_position("в верхнем правом углу"))
    btn_ne.pack(anchor='ne', padx=10, pady=10)

    # Для создания диагонали добавим пустой фрейм как распорку
    spacer = tk.Frame(win, height=50)
    spacer.pack()

    btn_center = tk.Button(win, text="CENTER", bg="lightyellow",
                           command=lambda: show_position("по центру"))
    btn_center.pack(anchor='center', pady=10)

    spacer2 = tk.Frame(win, height=50)
    spacer2.pack()

    btn_sw = tk.Button(win, text="SW", bg="lightpink",
                       command=lambda: show_position("в нижнем левом углу"))
    btn_sw.pack(anchor='sw', padx=10, pady=10)

    btn_s = tk.Button(win, text="S", bg="lightgrey",
                      command=lambda: show_position("внизу по центру"))
    btn_s.pack(anchor='s', pady=10)

    btn_se = tk.Button(win, text="SE", bg="lightsalmon",
                       command=lambda: show_position("в нижнем правом углу"))
    btn_se.pack(anchor='se', padx=10, pady=10)

# ЗАДАЧА 2: Форма авторизации
def task2():
    win = tk.Toplevel()
    win.title("Задача 2: Авторизация")
    center_window(win, 300, 150)

    tk.Label(win, text="Логин:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
    login_entry = tk.Entry(win)
    login_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(win, text="Пароль:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
    pass_entry = tk.Entry(win, show="*")
    pass_entry.grid(row=1, column=1, padx=5, pady=5)

    def submit():
        login = login_entry.get()
        password = pass_entry.get()
        if login and password:
            messagebox.showinfo("Успех", f"Добро пожаловать, {login}!")
        else:
            messagebox.showerror("Ошибка", "Заполните все поля!")

    def clear():
        login_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END)

    def close():
        win.destroy()

    tk.Button(win, text="Войти", command=submit).grid(row=2, column=0, pady=10)
    tk.Button(win, text="Очистить", command=clear).grid(row=2, column=1, pady=10)
    tk.Button(win, text="Закрыть", command=close).grid(row=2, column=2, pady=10)

# ЗАДАЧА 3: Хеш пароля и запись в CSV
def task3():
    win = tk.Toplevel()
    win.title("Задача 3: Хеш пароля в CSV")
    center_window(win, 400, 200)

    tk.Label(win, text="Введите пароль:").pack(pady=5)
    entry = tk.Entry(win, show="*")
    entry.pack(pady=5)

    result_label = tk.Label(win, text="Хеш: ")
    result_label.pack(pady=5)

    def calculate_hash():
        password = entry.get()
        if not password:
            messagebox.showwarning("Предупреждение", "Введите пароль!")
            return
        total = sum(ord(char) for char in password)
        result_label.config(text=f"Хеш: {total}")
        return total

    def save_to_csv():
        password = entry.get()
        if not password:
            messagebox.showwarning("Предупреждение", "Введите пароль для сохранения!")
            return
        total = sum(ord(char) for char in password)
        file_exists = os.path.isfile('passwords.csv')
        with open('passwords.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Пароль', 'Хеш'])
            writer.writerow([password, total])
        messagebox.showinfo("Сохранено", f"Пароль и хеш {total} сохранены в passwords.csv")

    def clear_csv():
        if os.path.exists('passwords.csv'):
            os.remove('passwords.csv')
            messagebox.showinfo("Очищено", "Файл passwords.csv удален.")
        else:
            messagebox.showinfo("Очищено", "Файл не существовал.")

    tk.Button(win, text="Хеш", command=calculate_hash).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(win, text="Сохранить в CSV", command=save_to_csv).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(win, text="Очистить CSV", command=clear_csv).pack(side=tk.LEFT, padx=10, pady=10)

# ЗАДАЧА 4: Вход / Очистка / Закрытие
def task4():
    win = tk.Toplevel()
    win.title("Задача 4: Вход в систему")
    center_window(win, 300, 200)

    tk.Label(win, text="Username:").pack(pady=5)
    user_entry = tk.Entry(win)
    user_entry.pack(pady=5)

    tk.Label(win, text="Password:").pack(pady=5)
    pass_entry = tk.Entry(win, show="*")
    pass_entry.pack(pady=5)

    status_label = tk.Label(win, text="", fg="green")
    status_label.pack(pady=5)

    def submit():
        if user_entry.get() and pass_entry.get():
            status_label.config(text="Выполнен вход")
        else:
            messagebox.showerror("Ошибка", "Заполните оба поля!")

    def clear():
        user_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END)
        status_label.config(text="")

    def close():
        win.destroy()

    tk.Button(win, text="Submit", command=submit).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(win, text="Clear", command=clear).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(win, text="Close", command=close).pack(side=tk.LEFT, padx=10, pady=10)

# ЗАДАЧА 5: Поиск чисел в строке
def task5():
    win = tk.Toplevel()
    win.title("Задача 5: Поиск чисел")
    center_window(win, 350, 150)

    tk.Label(win, text="Введите данные через запятую:").pack(pady=5)
    entry = tk.Entry(win, width=40)
    entry.pack(pady=5)

    result_label = tk.Label(win, text="")
    result_label.pack(pady=5)

    def check_numbers():
        data = entry.get()
        if not data:
            messagebox.showwarning("Предупреждение", "Поле пустое!")
            return
        items = [item.strip() for item in data.split(',')]
        count = 0
        for item in items:
            if item.isdigit():
                count += 1
        result_label.config(text=f"Найдено чисел: {count}")

    tk.Button(win, text="Проверить", command=check_numbers).pack(pady=10)

# ЗАДАЧА 6: Запись в текстовый файл
def task6():
    win = tk.Toplevel()
    win.title("Задача 6: Запись в файл")
    center_window(win, 300, 250)

    fields = ["Имя", "Фамилия", "Класс", "Группа"]
    entries = {}

    for i, field in enumerate(fields):
        tk.Label(win, text=field + ":").grid(row=i, column=0, padx=5, pady=5, sticky='e')
        entry = tk.Entry(win)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries[field] = entry

    def save_to_file():
        data = []
        for field in fields:
            value = entries[field].get().strip()
            if not value:
                messagebox.showerror("Ошибка", f"Поле '{field}' не заполнено!")
                return
            data.append(value)

        with open("student_data.txt", "a", encoding="utf-8") as f:
            f.write(", ".join(data) + "\n")

        messagebox.showinfo("Успех", "Данные сохранены в student_data.txt")
        for entry in entries.values():
            entry.delete(0, tk.END)

    tk.Button(win, text="Сохранить в файл", command=save_to_file).grid(row=len(fields), column=0, columnspan=2, pady=10)

# ГЛАВНОЕ ОКНО (МЕНЮ ВЫБОРА ЗАДАЧ)
def main():
    root = tk.Tk()
    root.title("Сборник задач по Tkinter")
    center_window(root, 400, 400)

    tk.Label(root, text="Выберите задачу для запуска:", font=("Arial", 14)).pack(pady=20)

    tasks = [
        ("Задача 1: Кнопки по диагонали", task1),
        ("Задача 2: Форма авторизации", task2),
        ("Задача 3: Хеш пароля и CSV", task3),
        ("Задача 4: Вход / Очистка / Закрытие", task4),
        ("Задача 5: Поиск чисел в строке", task5),
        ("Задача 6: Запись в текстовый файл", task6),
    ]

    for text, command in tasks:
        tk.Button(root, text=text, command=command, width=30).pack(pady=5)

    tk.Button(root, text="Выход", command=root.quit, bg="red", fg="white").pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()