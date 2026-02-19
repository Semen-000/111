import tkinter as tk
from tkinter import messagebox
import hashlib
import random
import string
from PIL import Image, ImageTk
import os


class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация и регистрация")

        # Фиксированный размер окна
        self.root.geometry("450x600")
        self.root.resizable(False, False)

        # Центрируем окно
        self.center_window(450, 600)

        # Данные пользователей
        self.users = {}

        # Текущий пользователь
        self.current_user = None

        # Создаем интерфейс
        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        # Основной контейнер с отступами
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=30, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Заголовок
        title_label = tk.Label(main_frame, text="АВТОРИЗАЦИЯ / РЕГИСТРАЦИЯ",
                               font=("Arial", 16, "bold"),
                               bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=(0, 20))

        # Рамка для формы
        form_frame = tk.Frame(main_frame, bg='white', relief=tk.GROOVE, bd=2)
        form_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Внутренние отступы формы
        form_content = tk.Frame(form_frame, bg='white', padx=25, pady=25)
        form_content.pack(fill=tk.BOTH, expand=True)

        # Логин
        tk.Label(form_content, text="Логин:", font=("Arial", 11),
                 bg='white', anchor='w').pack(fill=tk.X, pady=(0, 5))

        self.login_entry = tk.Entry(form_content, font=("Arial", 11),
                                    bg='#f8f9fa', relief=tk.SUNKEN, bd=2)
        self.login_entry.pack(fill=tk.X, pady=(0, 15), ipady=5)
        self.login_entry.focus()

        # Пароль
        tk.Label(form_content, text="Пароль:", font=("Arial", 11),
                 bg='white', anchor='w').pack(fill=tk.X, pady=(0, 5))

        self.password_entry = tk.Entry(form_content, font=("Arial", 11),
                                       show="*", bg='#f8f9fa',
                                       relief=tk.SUNKEN, bd=2)
        self.password_entry.pack(fill=tk.X, pady=(0, 20), ipady=5)

        # Кнопки
        btn_frame = tk.Frame(form_content, bg='white')
        btn_frame.pack(fill=tk.X, pady=10)

        # Первый ряд кнопок
        btn_row1 = tk.Frame(btn_frame, bg='white')
        btn_row1.pack(fill=tk.X, pady=5)

        tk.Button(btn_row1, text="Войти", command=self.login,
                  bg='#3498db', fg='white', font=("Arial", 11, "bold"),
                  width=12, height=1, cursor='hand2', relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_row1, text="Регистрация", command=self.register,
                  bg='#2ecc71', fg='white', font=("Arial", 11, "bold"),
                  width=12, height=1, cursor='hand2', relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=5)

        # Второй ряд кнопок
        btn_row2 = tk.Frame(btn_frame, bg='white')
        btn_row2.pack(fill=tk.X, pady=5)

        tk.Button(btn_row2, text="Сброс", command=self.clear_fields,
                  bg='#e74c3c', fg='white', font=("Arial", 11, "bold"),
                  width=25, height=1, cursor='hand2', relief=tk.RAISED, bd=2).pack()

        # Требования к паролю
        requirements_frame = tk.Frame(form_content, bg='#f8f9fa', relief=tk.SUNKEN, bd=1)
        requirements_frame.pack(fill=tk.X, pady=15)

        tk.Label(requirements_frame, text="Требования к паролю:",
                 font=("Arial", 10, "bold"), bg='#f8f9fa', fg='#2c3e50').pack(anchor='w', padx=10, pady=(10, 5))

        tk.Label(requirements_frame, text="• Минимум 8 символов",
                 font=("Arial", 10), bg='#f8f9fa', fg='#7f8c8d', anchor='w').pack(anchor='w', padx=20)

        tk.Label(requirements_frame, text="• Должен содержать символ ($ # @)",
                 font=("Arial", 10), bg='#f8f9fa', fg='#7f8c8d', anchor='w').pack(anchor='w', padx=20, pady=(0, 10))

        # Статус
        status_frame = tk.Frame(main_frame, relief=tk.SUNKEN, bd=1, bg='white')
        status_frame.pack(fill=tk.X, pady=10)

        self.status_label = tk.Label(status_frame, text="Ожидание ввода...",
                                     font=("Arial", 10), bg='white', fg='#7f8c8d')
        self.status_label.pack(pady=8)

        # Привязываем Enter
        self.root.bind('<Return>', lambda event: self.login())

    def validate_password(self, password):
        """Проверка пароля: минимум 8 символов и содержит спецсимвол ($ # @)"""
        if len(password) < 8:
            return False, "Пароль должен содержать минимум 8 символов"

        # Проверяем наличие спецсимволов $ # @
        special_chars = ['$', '#', '@']
        if not any(char in special_chars for char in password):
            return False, "Пароль должен содержать один из символов: $ # @"

        return True, "Пароль корректен"

    def login(self):
        """Обработка входа"""
        login = self.login_entry.get().strip()
        password = self.password_entry.get()

        if not login or not password:
            messagebox.showerror("Ошибка", "Заполните все поля!")
            self.status_label.config(text="Ошибка: заполните все поля", fg='#e74c3c')
            return

        # Проверяем существование пользователя
        if login in self.users and self.users[login] == password:
            self.current_user = login

            # ОЧИЩАЕМ И ЗАКРЫВАЕМ ФОРМУ АВТОРИЗАЦИИ
            self.clear_fields()
            self.root.withdraw()  # Скрываем главное окно

            # Открываем новое окно с картинкой и поздравлением
            self.show_congratulations(login)

        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")
            self.status_label.config(text="Ошибка входа", fg='#e74c3c')

    def register(self):
        """Обработка регистрации"""
        login = self.login_entry.get().strip()
        password = self.password_entry.get()

        if not login or not password:
            messagebox.showerror("Ошибка", "Заполните все поля!")
            self.status_label.config(text="Ошибка: заполните все поля", fg='#e74c3c')
            return

        if login in self.users:
            messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует!")
            self.status_label.config(text="Логин занят", fg='#e74c3c')
            return

        is_valid, message = self.validate_password(password)
        if not is_valid:
            messagebox.showerror("Ошибка", message)
            self.status_label.config(text=message, fg='#e74c3c')
            return

        self.users[login] = password

        messagebox.showinfo("Успех", "Регистрация прошла успешно!\nТеперь вы можете войти.")
        self.clear_fields()
        self.status_label.config(text="Регистрация успешна", fg='#2ecc71')

    def clear_fields(self):
        """Очистка полей ввода"""
        self.login_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.login_entry.focus()

    def show_congratulations(self, login):
        """Открытие нового окна с картинкой и поздравлением в военном стиле"""
        # Создаем новое окно
        congrats_win = tk.Toplevel()
        congrats_win.title("С 23 Февраля!")
        congrats_win.resizable(False, False)

        # При закрытии окна - закрываем всю программу
        def on_closing():
            congrats_win.destroy()
            self.root.quit()

        congrats_win.protocol("WM_DELETE_WINDOW", on_closing)

        # ВОЕННЫЕ ЦВЕТА (камуфляжная тематика)
        bg_color1 = "#2b4f2b"  # Темно-зеленый (основной)
        bg_color2 = "#3a6b3a"  # Средне-зеленый
        accent_color = "#c0392b"  # Красный (военный)
        gold_color = "#ffd700"  # Золотой
        text_color = "#f0f0f0"  # Светлый текст
        dark_text = "#2c3e50"  # Темный текст для белого фона

        # Основной контейнер с военным градиентом
        main_frame = tk.Frame(congrats_win, bg=bg_color1)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Верхняя полоса (как погон)
        top_bar = tk.Frame(main_frame, bg=accent_color, height=10)
        top_bar.pack(fill=tk.X)

        # Контейнер для контента
        content_frame = tk.Frame(main_frame, bg=bg_color1, padx=30, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Проверяем существование файла картинки
        if os.path.exists("67.png"):
            try:
                # Открываем и загружаем изображение
                image = Image.open("67.png")

                # Получаем размеры картинки
                img_width, img_height = image.size

                # Устанавливаем размер окна
                window_width = max(img_width, 600) + 60
                window_height = img_height + 400

                congrats_win.geometry(f"{window_width}x{window_height}")

                # Центрируем окно
                screen_width = congrats_win.winfo_screenwidth()
                screen_height = congrats_win.winfo_screenheight()
                x = (screen_width - window_width) // 2
                y = (screen_height - window_height) // 2
                congrats_win.geometry(f'{window_width}x{window_height}+{x}+{y}')

                # Рамка для картинки (как в рамке для фото)
                image_frame = tk.Frame(content_frame, bg=gold_color, padx=5, pady=5)
                image_frame.pack(pady=20)

                # Конвертируем для tkinter
                photo = ImageTk.PhotoImage(image)

                # Создаем метку с картинкой
                image_label = tk.Label(image_frame, image=photo, bg=bg_color1)
                image_label.image = photo
                image_label.pack()

            except Exception as e:
                error_label = tk.Label(content_frame, text=f"Ошибка загрузки картинки:\n{e}",
                                       font=("Arial", 12), fg='red', bg=bg_color1)
                error_label.pack(pady=20)
        else:
            # Если файл не найден - показываем красивый текст
            title_frame = tk.Frame(content_frame, bg=bg_color1)
            title_frame.pack(pady=30)

            tk.Label(title_frame, text="ФЕВРАЛЯ",
                     font=("Arial", 36, "bold"), fg=gold_color, bg=bg_color1).pack()

            tk.Label(title_frame, text="С ДНЕМ ЗАЩИТНИКА ОТЕЧЕСТВА!",
                     font=("Arial", 20, "bold"), fg=text_color, bg=bg_color1).pack()

        # Военная лента
        military_tape = tk.Frame(content_frame, bg=accent_color, height=3)
        military_tape.pack(fill=tk.X, padx=50, pady=10)

        # РАМКА С ПОЗДРАВЛЕНИЕМ (в стиле "письмо с фронта")
        congrats_frame = tk.Frame(content_frame, bg='#f5e6d3', relief=tk.RAISED, bd=5, padx=25, pady=20)
        congrats_frame.pack(pady=20, fill=tk.X)

        # Эффект "старой бумаги"
        tk.Frame(congrats_frame, bg=accent_color, height=2).pack(fill=tk.X, pady=(0, 15))

        # Заголовок поздравления
        tk.Label(congrats_frame, text=f"Уважаемый {login}!",
                 font=("Arial", 20, "bold"), fg=accent_color, bg='#f5e6d3').pack(pady=5)

        # Разделитель (золотой)
        tk.Frame(congrats_frame, bg=gold_color, height=2).pack(fill=tk.X, padx=40, pady=10)

        # Текст поздравления (как в письме)
        text_lines = [
            "И подводите к делу защитника Отечества!",
            "",
            "Желаем крепкого здоровья,",
            "мужества, силы духа и уверенности в завтрашнем дне.",
            "",
            "Пусть все начинания будут успешными,",
            "и счастья и благополучия — с наступающим днем!"
        ]

        for line in text_lines:
            if line == "":
                tk.Frame(congrats_frame, bg='#f5e6d3', height=8).pack()
            else:
                label = tk.Label(congrats_frame, text=line,
                                 font=("Arial", 12, "bold" if "!" in line else "normal"),
                                 fg=dark_text, bg='#f5e6d3',
                                 justify=tk.CENTER)
                label.pack(pady=2)

        # Золотая звезда внизу (символ)
        star_frame = tk.Frame(congrats_frame, bg='#f5e6d3')
        star_frame.pack(pady=15)

        tk.Label(star_frame, text="★", font=("Arial", 24), fg=gold_color, bg='#f5e6d3').pack()

        # Нижняя полоса (как погон)
        bottom_bar = tk.Frame(main_frame, bg=accent_color, height=10)
        bottom_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Кнопка закрытия в военном стиле
        close_btn = tk.Button(main_frame, text="ЗАКРЫТЬ", command=on_closing,
                              bg=accent_color, fg='white', font=("Arial", 14, "bold"),
                              width=14, height=1, cursor='hand2', relief=tk.RAISED, bd=5)
        close_btn.place(relx=0.5, rely=0.95, anchor='center')


# Запуск приложения
if __name__ == "__main__":
    # Проверяем наличие Pillow
    try:
        from PIL import Image, ImageTk
    except ImportError:
        print("=" * 50)
        print("УСТАНОВИТЕ БИБЛИОТЕКУ Pillow:")
        print("pip install Pillow")
        print("=" * 50)
        exit()

    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()