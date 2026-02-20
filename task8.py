import tkinter as tk #подключение библиотеки для создания окна
from tkinter import messagebox #подключение модуль для всплывающего окна


def save_data(): #функция сохранения данных
    fio = entry_fio.get() #получает ФИО из поля ввода
    faculty = entry_faculty.get() #получает факультет из поля ввода

    if not fio or not faculty: #если поля пустые
        messagebox.showerror("Ошибка", "Заполните все поля") #показывает ошибку
        return #выходит из функции

    with open("students.txt", "a", encoding="utf-8") as f: #открывает файл для добавления
        f.write(f"ФИО: {fio}, Факультет: {faculty}\n") #записывает данные в файл

    entry_fio.delete(0, tk.END) #очищает поле ФИО
    entry_faculty.delete(0, tk.END) #очищает поле факультета
    messagebox.showinfo("Успех", "Данные сохранены") #сообщение об успехе

def clear_file(): #функция очистки файла
    open("students.txt", "w").close() #открывает и закрывает файл (очищает)
    messagebox.showinfo("Очистка", "Файл очищен") #сообщение об успехе

root = tk.Tk() #создает главное окно
root.title("Студенты") #заголовок окна
root.geometry("400x200") #размер окна

tk.Label(root, text="ФИО студента:").pack(pady=5) #метка для ФИО
entry_fio = tk.Entry(root, width=40) #поле ввода для ФИО
entry_fio.pack(pady=5) #размещает поле

tk.Label(root, text="Факультет:").pack(pady=5) #метка для факультета
entry_faculty = tk.Entry(root, width=40) #поле ввода для факультета
entry_faculty.pack(pady=5) #размещает поле

frame = tk.Frame(root) #фрейм для кнопок
frame.pack(pady=10) #размещает фрейм

btn_save = tk.Button(frame, text="Сохранить", command=save_data, width=10) #кнопка сохранения
btn_save.pack(side=tk.LEFT, padx=10) #размещает слева

btn_clear = tk.Button(frame, text="Очистить файл", command=clear_file, width=10) #кнопка очистки
btn_clear.pack(side=tk.LEFT, padx=10) #размещает слева

root.mainloop() #запускает главный цикл приложения