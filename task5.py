import tkinter as tk #подключение библиотеки для создания окна
from tkinter import messagebox #подключение модуль для всплывающего окна

def save_to_file(): #функция сохранения в файл
    planets = entry.get().split(',') #получает текст из поля и разбиваем по запятой
    planets = [p.strip() for p in planets if p.strip()] #убирает пробелы и пустые значения

    if len(planets) != 8: #если не 8 планет
        messagebox.showerror("Ошибка", "Введите ровно 8 планет через запятую") #показывает ошибку
        return #выходит из функции

    earth_like = planets[:4] #первые 4 - землеподобные
    gas_giants = planets[4:] #остальные 4 - газовые гиганты

    with open("planets.txt", "w", encoding="utf-8") as f: #открывает файл для записи
        f.write("Планеты-Землеподобные\tГазовые гиганты\n") #записывает заголовки столбцов
        for i in range(4): #цикл на 4 строки
            e = earth_like[i] if i < len(earth_like) else "" #берет планету из первой группы
            g = gas_giants[i] if i < len(gas_giants) else "" #берет планету из второй группы
            f.write(f"{e}\t{g}\n") #записывает строку в файл

    messagebox.showinfo("Успех", "Данные сохранены в planets.txt") #сообщение об успехе

def clear_file(): #функция очистки файла
    open("planets.txt", "w").close() #открывает и закрывает файл (очищает)
    messagebox.showinfo("Очистка", "Файл очищен") #сообщение об успехе

root = tk.Tk() #создает главное окно
root.title("Планеты") #заголовок окна
root.geometry("400x150") #размер окна

label = tk.Label(root, text="Введите 8 планет через запятую:") #создает текстовую метку
label.pack(pady=5) #размещает метку с отступом

entry = tk.Entry(root, width=50) #создает поле ввода
entry.pack(pady=5) #размещает поле ввода с отступом

btn_save = tk.Button(root, text="Сохранить в файл", command=save_to_file) #создает кнопку сохранения
btn_save.pack(side=tk.LEFT, padx=20, pady=10) #размещает кнопку слева

btn_clear = tk.Button(root, text="Очистить файл", command=clear_file) #создает кнопку очистки
btn_clear.pack(side=tk.RIGHT, padx=20, pady=10) #размещает кнопку справа

root.mainloop() #запускает главный цикл приложения