import tkinter as tk #подключение библиотеки для создания окна
from datetime import datetime #импортирует datetime для работы с временем

def determine_time_of_day(): #функция определения времени суток
    time_str = entry.get() #получает текст из поля ввода
    try: #блок try — для обработки возможных ошибок
        time_obj = datetime.strptime(time_str, "%H:%M") #преобразует строку в время
        hour = time_obj.hour #получает час из времени

        if 6 <= hour < 12: #если час от 6 до 12
            result = "Утро" #результат - Утро
        elif 12 <= hour < 18: #если час от 12 до 18
            result = "День" #результат - День
        elif 18 <= hour < 24: #если час от 18 до 24
            result = "Вечер" #результат - Вечер
        else: #если час от 0 до 6
            result = "Ночь" #результат - Ночь

        label_result.config(text=result) #выводит результат
    except: #если произошла ошибка
        label_result.config(text="Ошибка! Введите HH:MM") #сообщение об ошибке

root = tk.Tk() #создаёт корневое окно
root.title("Определение времени суток") #заголовок окна
root.geometry("300x150") #размер окна

label_prompt = tk.Label(root, text="Введите время (HH:MM):") #текст-подсказка
label_prompt.pack(pady=5) #размещает с отступом

entry = tk.Entry(root, width=15) #поле для ввода времени
entry.pack(pady=5) #размещает с отступом

button = tk.Button(root, text="Определить", command=determine_time_of_day) #кнопка
button.pack(pady=5) #размещает кнопку

label_result = tk.Label(root, text="", font=("Arial", 14)) #метка для результата
label_result.pack(pady=10) #размещает с отступом

root.mainloop() #запускает главный цикл программы