import tkinter as tk #подключение библиотеки для создания окна
from tkinter import messagebox #подключение модуль для всплывающего окна


def reverse_text(): #функция переворота текста
    text = entry.get() #получает текст из поля ввода
    reversed_text = text[::-1] #переворачивает текст (срез с конца)

    with open("output.txt", "w", encoding="utf-8") as f: #открывает файл для записи
        f.write(reversed_text) #записывает перевернутый текст в файл

    messagebox.showinfo("Успех", "Текст перевернут и сохранен в output.txt") #сообщение об успехе


def clear_file(): #функция очистки файла
    open("output.txt", "w").close() #открывает и закрывает файл (очищает)
    messagebox.showinfo("Очистка", "Файл очищен") #сообщение об успехе


root = tk.Tk() #создает главное окно
root.title("Перевертыш") #заголовок окна
root.geometry("400x150") #размер окна

label = tk.Label(root, text="Введите текст:") #создает текстовую метку
label.pack(pady=5) #размещает метку с отступом

entry = tk.Entry(root, width=50) #создает поле ввода
entry.pack(pady=5) #размещает поле ввода с отступом

btn_reverse = tk.Button(root, text="Перевернуть", command=reverse_text) #создает кнопку переворота
btn_reverse.pack(side=tk.LEFT, padx=20, pady=10) #размещает кнопку слева

btn_clear = tk.Button(root, text="Очистить файл", command=clear_file) #создает кнопку очистки
btn_clear.pack(side=tk.RIGHT, padx=20, pady=10) #размещает кнопку справа

root.mainloop() #запускает главный цикл приложения