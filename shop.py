import tkinter as tk
from tkinter import messagebox, ttk
import hashlib
import random
import string
from PIL import Image, ImageTk
import os


class ShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Интернет-магазин")

        # Устанавливаем размер окна на весь экран
        self.root.state('zoomed')

        # Данные пользователей
        self.users = {}

        # Текущий пользователь
        self.current_user = None

        # Цветовая схема магазина
        self.bg_color = "#f8f9fa"  # Светлый фон
        self.accent_color = "#2c3e50"  # Темно-синий
        self.gold_color = "#e67e22"  # Оранжевый (акцент)
        self.card_bg = "#ffffff"  # Белый для карточек

        # Загружаем изображения для карточек
        self.load_product_images()

        # Создаем интерфейс
        self.show_auth_form()

    def load_product_images(self):
        """Загрузка или создание изображений для товаров"""
        self.product_images = []

        # Если нет реальных картинок, создаем заглушки
        for i in range(9):
            # Создаем цветной квадрат с номером
            img = tk.PhotoImage(width=150, height=150)
            img.put(self.get_product_color(i), to=(0, 0, 150, 150))
            self.product_images.append(img)

    def get_product_color(self, index):
        """Возвращает цвет для заглушки товара"""
        colors = [
            "#e74c3c", "#3498db", "#2ecc71",
            "#f39c12", "#9b59b6", "#1abc9c",
            "#e67e22", "#34495e", "#d35400"
        ]
        return colors[index % len(colors)]

    def center_window(self, window, width, height):
        """Центрирование окна"""
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f'{width}x{height}+{x}+{y}')

    def show_auth_form(self):
        """Показывает форму авторизации"""
        # Очищаем главное окно
        for widget in self.root.winfo_children():
            widget.destroy()

        # Основной контейнер с фоном
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Центральный контейнер для формы
        center_frame = tk.Frame(main_frame, bg=self.bg_color)
        center_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Логотип
        logo_frame = tk.Frame(center_frame, bg=self.accent_color, width=400, height=80)
        logo_frame.pack_propagate(False)
        logo_frame.pack(pady=(0, 20))

        tk.Label(logo_frame, text="🛍️ SHOP",
                 font=("Arial", 28, "bold"), fg="white", bg=self.accent_color).pack(expand=True)

        # Рамка для формы
        form_frame = tk.Frame(center_frame, bg='white', relief=tk.RAISED, bd=2, padx=30, pady=30)
        form_frame.pack()

        # Заголовок
        tk.Label(form_frame, text="ВХОД / РЕГИСТРАЦИЯ",
                 font=("Arial", 18, "bold"), fg=self.accent_color, bg='white').pack(pady=(0, 20))

        # Поля ввода
        tk.Label(form_frame, text="Логин:", font=("Arial", 12),
                 bg='white', anchor='w').pack(fill=tk.X, pady=(0, 5))

        self.login_entry = tk.Entry(form_frame, font=("Arial", 12),
                                    bg='#f8f9fa', relief=tk.SUNKEN, bd=2, width=30)
        self.login_entry.pack(fill=tk.X, pady=(0, 15), ipady=5)
        self.login_entry.focus()

        tk.Label(form_frame, text="Пароль:", font=("Arial", 12),
                 bg='white', anchor='w').pack(fill=tk.X, pady=(0, 5))

        self.password_entry = tk.Entry(form_frame, font=("Arial", 12),
                                       show="*", bg='#f8f9fa', relief=tk.SUNKEN, bd=2, width=30)
        self.password_entry.pack(fill=tk.X, pady=(0, 20), ipady=5)

        # Кнопки
        btn_frame = tk.Frame(form_frame, bg='white')
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🔑 Войти", command=self.login,
                  bg=self.accent_color, fg='white', font=("Arial", 12, "bold"),
                  width=12, height=1, cursor='hand2', relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="📝 Регистрация", command=self.register,
                  bg=self.gold_color, fg='white', font=("Arial", 12, "bold"),
                  width=12, height=1, cursor='hand2', relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=5)

        # Требования к паролю
        req_frame = tk.Frame(form_frame, bg='#f8f9fa', relief=tk.SUNKEN, bd=1, padx=10, pady=10)
        req_frame.pack(fill=tk.X, pady=15)

        tk.Label(req_frame, text="Требования к паролю:",
                 font=("Arial", 10, "bold"), bg='#f8f9fa', fg=self.accent_color).pack(anchor='w')
        tk.Label(req_frame, text="• Минимум 8 символов",
                 font=("Arial", 10), bg='#f8f9fa', fg='#7f8c8d').pack(anchor='w')
        tk.Label(req_frame, text="• Должен содержать символ ($ # @)",
                 font=("Arial", 10), bg='#f8f9fa', fg='#7f8c8d').pack(anchor='w')

        self.root.bind('<Return>', lambda event: self.login())

    def validate_password(self, password):
        """Проверка пароля"""
        if len(password) < 8:
            return False, "Пароль должен содержать минимум 8 символов"

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
            return

        if login in self.users and self.users[login] == password:
            self.current_user = login
            self.show_shop()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")

    def register(self):
        """Обработка регистрации"""
        login = self.login_entry.get().strip()
        password = self.password_entry.get()

        if not login or not password:
            messagebox.showerror("Ошибка", "Заполните все поля!")
            return

        if login in self.users:
            messagebox.showerror("Ошибка", "Пользователь уже существует!")
            return

        is_valid, message = self.validate_password(password)
        if not is_valid:
            messagebox.showerror("Ошибка", message)
            return

        self.users[login] = password
        messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        self.login_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def show_shop(self):
        """Показывает интернет-магазин с 9 ровными карточками"""
        # Очищаем главное окно
        for widget in self.root.winfo_children():
            widget.destroy()

        # Основной контейнер
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Верхняя панель
        header_frame = tk.Frame(main_frame, bg=self.accent_color, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        # Логотип и приветствие
        tk.Label(header_frame, text=f"🛍️ Добро пожаловать, {self.current_user}!",
                 font=("Arial", 20, "bold"), fg="white", bg=self.accent_color).pack(side=tk.LEFT, padx=30, pady=20)

        # Кнопка выхода
        tk.Button(header_frame, text="🚪 Выход", command=self.show_auth_form,
                  bg=self.gold_color, fg='white', font=("Arial", 12, "bold"),
                  width=10, cursor='hand2', relief=tk.RAISED, bd=2).pack(side=tk.RIGHT, padx=30, pady=20)

        # Заголовок раздела
        tk.Label(main_frame, text="🔥 НАШИ ТОВАРЫ",
                 font=("Arial", 24, "bold"), fg=self.accent_color, bg=self.bg_color).pack(pady=20)

        # Контейнер для карточек
        cards_container = tk.Frame(main_frame, bg=self.bg_color)
        cards_container.pack(expand=True, fill=tk.BOTH, padx=40, pady=20)

        # ПОДРОБНЫЕ ДАННЫЕ ДЛЯ КАРТОЧЕК
        products = [
            {
                "title": "📱 Смартфон Galaxy S23",
                "price": "29 990 ₽",
                "desc": "6.5\" AMOLED, 128GB, 8GB RAM, камера 50МП, процессор Snapdragon 8 Gen 2, батарея 5000mAh",
                "rating": "⭐⭐⭐⭐☆",
                "category": "Электроника",
                "desc_lines": [
                    '6.5" AMOLED, 128GB, 8GB RAM',
                    'камера 50МП, Snapdragon 8 Gen 2',
                    'батарея 5000mAh'
                ]
            },
            {
                "title": "💻 Ноутбук UltraBook Pro",
                "price": "54 990 ₽",
                "desc": "15.6\" IPS, 512GB SSD, 16GB RAM, Intel Core i7, видеокарта NVIDIA GeForce RTX 3050, Windows 11",
                "rating": "⭐⭐⭐⭐⭐",
                "category": "Электроника",
                "desc_lines": [
                    '15.6" IPS, 512GB SSD, 16GB RAM',
                    'Intel Core i7, RTX 3050',
                    'Windows 11'
                ]
            },
            {
                "title": "🎧 Наушники AirSound",
                "price": "4 990 ₽",
                "desc": "Bluetooth 5.3, активное шумоподавление, время работы 30ч, быстрая зарядка, влагозащита IPX4",
                "rating": "⭐⭐⭐⭐☆",
                "category": "Аксессуары",
                "desc_lines": [
                    'Bluetooth 5.3, шумоподавление',
                    'время работы 30ч, быстрая зарядка',
                    'влагозащита IPX4'
                ]
            },
            {
                "title": "📟 Планшет Tab Ultra",
                "price": "24 990 ₽",
                "desc": "10.5\" IPS, 64GB, 6GB RAM, поддержка стилуса, 4 динамика, LTE версия, Android 13",
                "rating": "⭐⭐⭐⭐☆",
                "category": "Электроника",
                "desc_lines": [
                    '10.5" IPS, 64GB, 6GB RAM',
                    'поддержка стилуса, 4 динамика',
                    'LTE версия, Android 13'
                ]
            },
            {
                "title": "⌚ Умные часы Watch 5",
                "price": "12 990 ₽",
                "desc": "GPS, пульсометр, шагомер, измерение давления, сон, 50+ режимов тренировок, водонепроницаемость 5ATM",
                "rating": "⭐⭐⭐⭐⭐",
                "category": "Гаджеты",
                "desc_lines": [
                    'GPS, пульсометр, шагомер',
                    'измерение давления, сон',
                    '50+ режимов, 5ATM'
                ]
            },
            {
                "title": "🔊 Портативная колонка Boom",
                "price": "3 490 ₽",
                "desc": "20W стереозвук, влагозащита IPX7, время работы 15ч, power bank функция, TWS подключение",
                "rating": "⭐⭐⭐☆☆",
                "category": "Аудио",
                "desc_lines": [
                    '20W стереозвук, IPX7',
                    'время работы 15ч',
                    'power bank, TWS'
                ]
            },
            {
                "title": "🖥️ Монитор Curve 27\"",
                "price": "18 990 ₽",
                "desc": "27\" 4K UHD, HDR10, 144Hz, изогнутый экран, 1ms отклик, FreeSync, HDMI/DP, настенный монтаж",
                "rating": "⭐⭐⭐⭐⭐",
                "category": "Комплектующие",
                "desc_lines": [
                    '27" 4K UHD, HDR10, 144Hz',
                    'изогнутый, 1ms, FreeSync',
                    'HDMI/DP, настенный монтаж'
                ]
            },
            {
                "title": "⌨️ Механическая клавиатура",
                "price": "2 990 ₽",
                "desc": "Механические переключатели, RGB подсветка, металлическая основа, съемный кабель, макросы",
                "rating": "⭐⭐⭐⭐☆",
                "category": "Аксессуары",
                "desc_lines": [
                    'Механические переключатели',
                    'RGB подсветка, металлическая',
                    'съемный кабель, макросы'
                ]
            },
            {
                "title": "🖱️ Игровая мышь X7",
                "price": "1 490 ₽",
                "desc": "16000 DPI, беспроводная, 6 программируемых кнопок, RGB подсветка, аккумулятор 500mAh, USB Type-C",
                "rating": "⭐⭐⭐⭐⭐",
                "category": "Аксессуары",
                "desc_lines": [
                    '16000 DPI, беспроводная',
                    '6 программируемых кнопок',
                    'RGB, аккумулятор 500mAh'
                ]
            }
        ]

        # Создаем сетку 3x3 для карточек с фиксированной шириной
        for i in range(3):
            row_frame = tk.Frame(cards_container, bg=self.bg_color)
            row_frame.pack(fill=tk.X, pady=10)

            # Настраиваем равномерное распределение колонок
            for j in range(3):
                row_frame.columnconfigure(j, weight=1, uniform='col')

            for j in range(3):
                idx = i * 3 + j
                if idx < len(products):
                    card = self.create_product_card(row_frame, products[idx], idx)
                    card.grid(row=0, column=j, padx=10, sticky='nsew')

    def create_product_card(self, parent, product, idx):
        """Создание одной карточки товара с идеально ровными размерами"""
        # Рамка карточки с фиксированной минимальной высотой
        card = tk.Frame(parent, bg=self.card_bg, relief=tk.RAISED, bd=2)
        card.grid_propagate(False)  # Запрещаем изменение размера
        card.configure(width=320, height=480)  # Фиксированный размер

        # Внутренний контейнер для отступов
        inner = tk.Frame(card, bg=self.card_bg)
        inner.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

        # Изображение (заглушка) фиксированного размера
        img_frame = tk.Frame(inner, bg=self.get_product_color(idx), width=140, height=140)
        img_frame.pack_propagate(False)
        img_frame.pack(pady=(0, 8))

        # Категория товара
        tk.Label(img_frame, text=f"📦\n{product['category']}",
                 font=("Arial", 10), fg="white", bg=self.get_product_color(idx)).pack(expand=True)

        # Заголовок (название товара)
        tk.Label(inner, text=product["title"],
                 font=("Arial", 12, "bold"), fg=self.accent_color, bg=self.card_bg,
                 wraplength=280).pack(pady=(5, 5))

        # Цена
        tk.Label(inner, text=product["price"],
                 font=("Arial", 16, "bold"), fg=self.gold_color, bg=self.card_bg).pack(pady=(0, 5))

        # Контейнер для описания с фиксированной высотой
        desc_container = tk.Frame(inner, bg=self.card_bg, height=80)
        desc_container.pack_propagate(False)
        desc_container.pack(fill=tk.X, pady=5)

        # Описание товара в три строки
        for line in product["desc_lines"]:
            tk.Label(desc_container, text=line,
                     font=("Arial", 9), fg="#7f8c8d", bg=self.card_bg,
                     wraplength=280).pack()

        # Рейтинг
        tk.Label(inner, text=product["rating"],
                 font=("Arial", 12), fg=self.gold_color, bg=self.card_bg).pack(pady=(5, 8))

        # Кнопка покупки
        tk.Button(inner, text="🛒 В корзину",
                  bg=self.accent_color, fg='white', font=("Arial", 10, "bold"),
                  width=14, cursor='hand2', relief=tk.RAISED, bd=1,
                  command=lambda p=product: self.add_to_cart(p)).pack(pady=5)

        return card

    def add_to_cart(self, product):
        """Добавление товара в корзину с деталями"""
        messagebox.showinfo("Корзина",
                            f"✅ {product['title']} добавлен в корзину!\n\n"
                            f"💰 Цена: {product['price']}\n"
                            f"📝 {product['desc']}\n"
                            f"⭐ Рейтинг: {product['rating']}")


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = ShopApp(root)
    root.mainloop()