from tkinter import Tk, Canvas
from settings import *


window = Tk()  # Создаём окно.
window.title("Карандаши")  # Заголовок окна
global canvas  # Глобальная переменая, видна во всех функциях
canvas = Canvas(window, width=canvas_width, height=canvas_height)  # Canvas - "холст" для рисования.

global x


def draw_pencil(color, length, is_sharp):  # Функция для рисования однаго карандаша
    global x
    x1 = x
    y1 = pencil_padding
    x2 = x1 + pencil_width
    y2 = y1 + pencil_cm * length
    y2 -= pencil_width
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    x3 = x1 + pencil_width / 4
    x4 = x2 - pencil_width / 4
    canvas.create_rectangle(x3, y1, x4, y2, fill=color)
    y3 = y2 + pencil_width
    canvas.create_polygon(x1, y2, x3, y3, x4, y3, x2, y2, fill="white", outline="black")
    x5 = x1 + pencil_width / 2
    y4 = y3 + pencil_width * 0.75
    y5 = y3 + pencil_width * 0.5
    y6 = y3 + pencil_width * 0.8
    canvas.create_polygon(x3, y3, x5, y4, x4, y3, fill=color, outline=color)
    if not is_sharp:
        canvas.create_rectangle(x3, y5, x4, y6, fill="white", outline="white")
    x = x + pencil_width + pencil_gap


pencil_box = [
    ("red", 9, False),
    ("red", 5, True),
    ("red", 90, False),  # Слишком длинный.
    ("red", 2, True),  # Слишком короткий.
    ("pink", 6, False),
    ("black", 19, True),
    ("red", 13, False),
    ("blue", 20, True),
]


print(f"Всего карандашей: {len(pencil_box)}.")
pencil_box = [pencil for pencil in pencil_box if pencil[1] >= 5 and pencil[1] <= 20]  # Фильтрация карандашей по длине.
print(f"Правильных карандашей: {len(pencil_box)}.")
x = canvas_width / 2 - len(pencil_box) * (pencil_width + pencil_gap) / 2 - pencil_gap


for pencil in pencil_box:
    # draw_pencil(pencil[0], pencil[1], pencil[2])  # Рисуем карандаш, берем данные из кортежа
    color, length, is_sharp = pencil  # Разбор кортежа
    draw_pencil(color, length, is_sharp)
    print(pencil)
# draw_pencil("red", 10, True) # Вызов функции
# x=x+50
# draw_pencil("blue", 10, True) # Вызов функции
# x=x+50
# draw_pencil("pink", 10, True) # Вызов функции
canvas.pack()  # Размищения канвы в нутри окна
window.mainloop()  # Показать окно на экране


