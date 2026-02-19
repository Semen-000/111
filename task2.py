import tkinter as tk #подключение библиотеки для создания окна
from tkinter import messagebox #подключение модуль для всплывающего окна

def calculate(): # функция для расчётов квадрата
    try: #блок try — для обработки возможных ошибок
        a = float(entry_a.get()) #значение из поля entry_a и преобразуем в float
        b = float(entry_b.get()) #значение из поля entry_b и преобразуем в float
        sum_sq = (a + b) ** 2 #рассчитывает квадрат суммы по формуле (a + b)²
        diff_sq = (a - b) ** 2 #рассчитывает квадрат разности по формуле (a - b)²
        result_text.delete(1.0, tk.END) #очищает текстовую область
        result_text.insert(tk.END, f"Квадрат суммы: {sum_sq}\nКвадрат разности: {diff_sq}") #вставляет результаты в текстовую область
    except ValueError: #если пользователь ввёл не число — перехватываем ошибку ValueError
        messagebox.showerror("Ошибка", "Введите числа!") #показывает всплывающее окно с ошибкой

def save_result(): #определяет функцию save_result для сохранения результатов в файл
    try: #начинает блок try — для обработки возможных ошибок
        with open("result.txt", "w") as f: #открывает файл result.txt в режиме записи ('w')
            f.write(result_text.get(1.0, tk.END)) #записывает содержимое текстовой области в файл
        messagebox.showinfo("Успех", "Результат сохранён в result.txt") #показывает сообщение об успешном сохранении
    except Exception as e: #если произошла другая ошибка — перехватываем её
        messagebox.showerror("Ошибка", str(e)) #показывает всплывающее окно с текстом ошибки

def clear_file(): #определяет функцию clear_file для очистки файла
    try: #начинает блок try — для обработки возможных ошибок
        with open("result.txt", "w") as f: #открывает файл result.txt в режиме записи ('w')
            f.write("") #очищает файл, записывая в него пустую строку
        messagebox.showinfo("Успех", "Файл очищен") #показывает сообщение об успешной очистке
    except Exception as e: #если произошла ошибка — перехватываем её
        messagebox.showerror("Ошибка", str(e)) #показывает всплывающее окно с текстом ошибки

root = tk.Tk() #создаёт основное окно приложения
root.title("Расчёт квадратов") #устанавливает заголовок окна

tk.Label(root, text="a:").grid(row=0, column=0) #создаёт метку "a:" и размещаем в ячейке (0, 0)
entry_a = tk.Entry(root) #создаёт поле ввода для переменной a
entry_a.grid(row=0, column=1) #размещает поле entry_a в ячейке (0, 1)

tk.Label(root, text="b:").grid(row=1, column=0) #создаёт метку "b:" и размещаем в ячейке (1, 0)
entry_b = tk.Entry(root) #создаёт поле ввода для переменной b
entry_b.grid(row=1, column=1) #размещает поле entry_b в ячейке (1, 1)

tk.Button(root, text="Рассчитать", command=calculate).grid(row=2, column=0, columnspan=2) #создаёт кнопку "Рассчитать" и привязываем к функции calculate, размещаем на 2 строке, на 2 столбца

result_text = tk.Text(root, height=3, width=30) #создаёт текстовую область для вывода результатов (высота — 3 строки, ширина — 30 символов)
result_text.grid(row=3, column=0, columnspan=2) #размещает текстовую область на 3 строке, на 2 столбца

tk.Button(root, text="Сохранить", command=save_result).grid(row=4, column=0) #создаёт кнопку "Сохранить" и привязываем к функции save_result, размещаем в ячейке (4, 0)
tk.Button(root, text="Очистить файл", command=clear_file).grid(row=4, column=1) #создаёт кнопку "Очистить файл" и привязываем к функции clear_file, размещаем в ячейке (4, 1)

root.mainloop() #запускает главный цикл окна — приложение начинает работу
