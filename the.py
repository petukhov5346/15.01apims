from tkinter import *
from tkinter import filedialog, messagebox, PhotoImage, ttk
from PIL import Image, ImageTk

# Создаем главное окно
root = Tk()
root.title("Умный дом")  # Заголовок окна

# Размер окна
window_width = 800
window_height = 700

# Получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Вычисляем координаты для центра
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Устанавливаем размер и позицию окна
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Загрузка изображений
img_la = PhotoImage(file="LA.PNG")
img_l = PhotoImage(file="L.PNG")
img_h = PhotoImage(file="H.PNG")
img_w = PhotoImage(file="W.PNG")


# Задаем иконку (убедитесь, что файл icon.ico есть в той же папке)
try:
    root.iconbitmap('icon.ico')
except:
    pass  # Если файла иконки нет, проигнорируем

devices_info = {
    "Эл.замок": {
        "характеристики": "Беспроводной электронный замок с функцией голосового управления.",
        "функции": "Открытие и закрытие по приложению, автоматическое закрывание.",
        "изображение": "lock.png"
    },
    "Умная лампочка": {
        "характеристики": "RGB-лампочка с регулировкой яркости и цвета.",
        "функции": "Управление через Wi-Fi, настройка сцен, таймер.",
        "изображение": "lamp.png"
    },
    "Система отопления": {
        "характеристики": "RGB-лампочка с регулировкой яркости и цвета.",
        "функции": "Управление через Wi-Fi, настройка по комнате.",
        "изображение": "heating.png"
    },
    "Автоматический полив растений": {
        "характеристики": "RGB-лампочка с регулировкой яркости и цвета.",
        "функции": "Управление через Приложение, настройка потока, таймер.",
        "изображение": "watering.png"
    }

}

# Основное меню
mainmenu = Menu(root)
root.config(menu=mainmenu)

def открыть_инструкцию():
    # Создаем новое окно
    инструкция_окно = Toplevel(root)
    инструкция_окно.title("Инструкция для пользователя")
    инструкция_окно.geometry("500x400")
    # Текст инструкции
    инструкции_text = (
        "Инструкция для пользователя:\n\n"
        "Эл.замок: Беспроводной электронный замок с функцией голосового управления.\n"
        " - Управление по приложению.\n"
        " - Автоматическое закрывание.\n\n"
        "Умная лампочка: RGB-лампочка с регулировкой яркости и цвета.\n"
        " - Управление через Wi-Fi.\n"
        " - Настройка сцен, таймеров.\n\n"
        "Система отопления: Регулируемая система отопления по комнатам.\n"
        " - Управление через приложение.\n"
        " - Настройка температуры.\n\n"
        "Автоматический полив растений: система автоматического полива.\n"
        " - Управление через приложение.\n"
        " - Настройка потока воды и таймеров."
    )
    # Создаем текстовый виджет для отображения инструкции
    text_widget = Text(инструкция_окно, wrap='word')
    text_widget.insert('1.0', инструкции_text)
    text_widget.config(state='disabled')  # Только чтение
    text_widget.pack(expand=True, fill='both', padx=10, pady=10)

# Функции для пунктов меню
def open_file():
    filename = filedialog.askopenfilename(title="Открыть файл", filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if filename:
        messagebox.showinfo("Открытие файла", f"Вы выбрали файл:\n{filename}")

def save_file():
    filename = filedialog.asksaveasfilename(title="Сохранить файл", defaultextension=".txt", filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if filename:
        messagebox.showinfo("Сохранение файла", f"Файл сохранен:\n{filename}")

def exit_app():
    root.destroy()

# Создаем меню "Файл"
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...", command=open_file)
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=exit_app)

# Создаем меню "Справка"
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")
helpmenu.add_command(label="Инструкция", command=открыть_инструкцию)

# Добавляем меню в главное меню
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

def открыть_подменю_устройства(устройство):
    # Создаем новое окно
    окно_устройства = Toplevel(root)
    окно_устройства.title(устройство)
    окно_устройства.geometry("400x300")

    # Функции для перехода к разделам
    def открыть_изображение():
        messagebox.showinfo(f"{устройство} - Изображение", f"Здесь можно сделать окно для {устройство} - Изображение")

    def открыть_характеристики():
        messagebox.showinfo(f"{устройство} - Характеристики", f"Здесь могут быть характеристики {устройство}")

    def открыть_функции():
        messagebox.showinfo(f"{устройство} - Функции", f"Здесь описание функций {устройство}")

    # Добавляем кнопки или меню для перехода к разделам
    Label(окно_устройства, text=f"{устройство}").pack(pady=10)
    Button(окно_устройства, text="Изображение", command=открыть_изображение).pack(pady=5)
    Button(окно_устройства, text="Характеристики", command=открыть_характеристики).pack(pady=5)
    Button(окно_устройства, text="Функции", command=открыть_функции).pack(pady=5)

# Создаем меню "Устройства"
device_menu = Menu(mainmenu, tearoff=0)

# Функции для каждого устройства
def открыть_эл_замок():
    открыть_подменю_устройства("Эл.замок")

def открыть_умная_лампочка():
    открыть_подменю_устройства("Умная лампочка")

def открыть_система_отопления():
    открыть_подменю_устройства("Система отопления")

def открыть_автоматический_полив():
    открыть_подменю_устройства("Автоматический полив растений")

# Добавляем устройства в меню
device_menu.add_command(label="Эл.замок", command=открыть_эл_замок)
device_menu.add_command(label="Умная лампочка", command=открыть_умная_лампочка)
device_menu.add_command(label="Система отопления", command=открыть_система_отопления)
device_menu.add_command(label="Автоматический полив растений", command=открыть_автоматический_полив)

# Добавляем меню "Устройства" к главному меню
mainmenu.add_cascade(label="Устройства", menu=device_menu)

# Можно добавить простую иконку на главное окно (если есть, заменить 'icon.ico')
try:
    root.iconbitmap('icon.ico')
except:
    pass


def открыть_подменю_устройства(устройство):
    info = devices_info.get(устройство)
    if info:
        # Создаем новое окно
        окно_устройства = Toplevel(root)
        окно_устройства.title(устройство)
        окно_устройства.geometry("500x600")  # увеличьте размер для изображений и текста

        # Название устройства
        Label(окно_устройства, text=устройство, font=("Arial", 16, "bold")).pack(pady=10)

        # Попытка загрузить изображение
        try:
            from PIL import Image, ImageTk
            img = Image.open(info["изображение"])
            img = img.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            img_label = Label(окно_устройства, image=photo)
            img_label.image = photo  # сохранить ссылку
            img_label.pack(pady=10)
        except:
            # если PIL не установлена или изображение не найдено
            Label(окно_устройства, text="Изображение недоступно").pack(pady=10)

        # Отображение характеристик
        Label(окно_устройства, text="Характеристики:", font=("Arial", 14, "underline")).pack(pady=5)
        text_char = Text(окно_устройства, height=4, width=50, wrap='word')
        text_char.insert('1.0', info["характеристики"])
        text_char.config(state='disabled')
        text_char.pack(pady=5)

        # Отображение функций
        Label(окно_устройства, text="Функции:", font=("Arial", 14, "underline")).pack(pady=5)
        text_funcs = Text(окно_устройства, height=4, width=50, wrap='word')
        text_funcs.insert('1.0', info["функции"])
        text_funcs.config(state='disabled')
        text_funcs.pack(pady=5)

# Создаем главный интерфейс (например, для управления "Умным домом")

button_frame = Frame(root)
button_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)

# Функция для подсказки (tooltip)
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event):
        if self.tipwindow or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = Label(tw, text=self.text, background="#ffffe0", relief='solid', borderwidth=1, font=("tahoma", "8", "normal"))
        label.pack()

    def hide_tip(self, event):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()



# Создаем кнопки справа
buttons_info = [
    ("Лампа", img_l, "Управление освещением"),
    ("Замок", img_la, "Управление замком"),
    ("Отопление", img_h, "Настройка системы отопления"),
    ("Полив", img_w, "Управление автоматическим поливом")
]

for (text, img, tooltip_text) in buttons_info:
    btn = Button(button_frame, image=img, command=lambda t=text: открыть_подменю_устройства(t))
    btn.pack(pady=5, fill=X)
    ToolTip(btn, tooltip_text)
# Запуск цикла обработки событий
root.mainloop()