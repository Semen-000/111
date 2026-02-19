import tkinter as tk #подключение библиотеки для создания окна
from tkinter import messagebox #подключение модуль для всплывающего окна

prices = [] #создание списка
def add_price(): #функция для добавления цены
    try: #блок try — для обработки возможных ошибок
        prices.append(float(entry.get())) #берёт текст превращает в число и добавляет в список
        entry.delete(0, tk.END) #очищает после добавления
        messagebox.showinfo("Успех", "Товар добавлен!") #сообщение об успехе
    except: #если произошла ошибка
        messagebox.showerror("Ошибка", "Введите корректную цену") #сообщение об ошибке

def show_total(): #функция для подсчёта суммы
    total = sum(prices) #сумма всех цен
    label_total.config(text=f"Итого:{total:.2f}") #обновляет текст после новой суммы

def save_to_file(): #функция для сохранения файлов
    with open("purchase.txt","w") as f: #открывает файл в режиме записи и закрывает(очищает)
        f.write(str(sum(prices))) #записывает в файл общую сумму
        messagebox.showinfo("Сохранено","Результат записан в purchase.txt") #сообщение о сохранении

def clear_file(): #функция очистки файла
    open("purchase.txt", "w").close() #открывает файл в режиме записи и закрывает(очищает)
    messagebox.showinfo("Очищено", "Файл очищен") #сообщение очистки файла

root = tk.Tk() #главное окно
root.title("Калькулятор покупок") #название окна

entry = tk.Entry(root) #поле ввода чисел
entry.pack(pady=5) #размещение окна с отступом

tk.Button(root,text="+",command=add_price).pack() #кнопка +
tk.Button(root,text="Итого",command=show_total).pack() #кнопка итого
tk.Button(root,text="Сохранить",command=save_to_file).pack() #кнопка сохранить
tk.Button(root,text="Очистить",command=clear_file).pack() #кнопка очистить

label_total=tk.Label(root,text="Итого:0.0") #текстовая метка для вывода суммы
label_total.pack(pady=5) #размещение метки с отступом

root.mainloop() #запуск цикла окна