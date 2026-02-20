import tkinter as tk  # Импорт библиотеки для графического интерфейса

def start_machine():  # Функция запуска станка
    label.config(text="СТАНОК ЗАПУЩЕН", fg="green")  # Меняем текст на зеленый
    btn_start.config(bg="green", fg="white", relief=tk.SUNKEN)  # Кнопка запуска становится зеленой
    btn_pause.config(bg="gray", fg="black", relief=tk.RAISED)  # Кнопка паузы становится серой
    btn_stop.config(bg="gray", fg="black", relief=tk.RAISED)  # Кнопка выключения становится серой

def pause_machine():  # Функция паузы станка
    label.config(text="СТАНОК ПРИГОТОВЛЕН", fg="orange")  # Меняем текст на оранжевый
    btn_pause.config(bg="orange", fg="white", relief=tk.SUNKEN)  # Кнопка паузы становится оранжевой
    btn_start.config(bg="gray", fg="black", relief=tk.RAISED)  # Кнопка запуска становится серой
    btn_stop.config(bg="gray", fg="black", relief=tk.RAISED)  # Кнопка выключения становится серой

def stop_machine():  # Функция выключения станка
    label.config(text="СТАНОК ВЫКЛЮЧЕН", fg="red")  # Меняем текст на красный
    btn_stop.config(bg="red", fg="white", relief=tk.SUNKEN)  # Кнопка выключения становится красной
    btn_start.config(bg="gray", fg="black", relief=tk.RAISED)  # Кнопка запуска становится серой
    btn_pause.config(bg="gray", fg="black", relief=tk.RAISED)  # Кнопка паузы становится серой

root = tk.Tk()  # Создаем главное окно
root.title("Управление станком")  # Заголовок окна
root.geometry("500x250")  # Размер окна
root.resizable(False, False)  # Запрещаем изменение размера окна

# Верхняя метка "Label" как на рисунке
top_label = tk.Label(root, text="Label", font=("Arial", 12, "bold"))  # Создаем верхнюю метку
top_label.pack(pady=5)  # Размещаем метку

label = tk.Label(root, text="СТАНОК ВЫКЛЮЧЕН", font=("Arial", 18, "bold"), fg="red")  # Создаем основную метку
label.pack(pady=20)  # Размещаем метку

frame = tk.Frame(root)  # Создаем фрейм для кнопок
frame.pack(pady=20)  # Размещаем фрейм

# Создаем кнопки с рамками и фиксированным размером
btn_start = tk.Button(frame, text="СТАНОК ЗАПУСК", bg="gray", fg="black",
                      font=("Arial", 10), width=15, height=2,
                      relief=tk.RAISED, bd=3, command=start_machine)  # Кнопка запуска
btn_start.pack(side=tk.LEFT, padx=10)  # Размещаем слева

btn_pause = tk.Button(frame, text="СТАНОК ПАУЗА", bg="gray", fg="black",
                      font=("Arial", 10), width=15, height=2,
                      relief=tk.RAISED, bd=3, command=pause_machine)  # Кнопка паузы
btn_pause.pack(side=tk.LEFT, padx=10)  # Размещаем слева

btn_stop = tk.Button(frame, text="СТАНОК ВЫКЛЮЧЕН", bg="gray", fg="black",
                     font=("Arial", 10), width=15, height=2,
                     relief=tk.RAISED, bd=3, command=stop_machine)  # Кнопка выключения
btn_stop.pack(side=tk.LEFT, padx=10)  # Размещаем слева

root.mainloop()  # Запускаем главный цикл приложения