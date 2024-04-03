import pyqrcode
import png
from tkinter import *

'''
    Эта функция отвечает за получение введённых данных, их преобразование
    в изображение QR-кода и сохранение этого изображения в формате PNG.
'''
def get_code():
    # Получаем данные из текстового поля
    data_var = data.get()
    qr = pyqrcode.create(str(data_var))
    qr.png('code.png', scale=6)

# Создаём окно Tk размером 400x200
base = Tk()
base.geometry("400x200")
base.title("Генератор QR-кодов")

# Переменная для хранения текста QR-кода
data = StringVar()

# Поле для ввода текста
dataEntry = Entry(textvariable=data, width="30")
dataEntry.place(x=80,y=50)
button = Button(base, text="Создать код", command=get_code, width="30", height="2", bg="grey")
button.place(x=80, y=100)
base.mainloop()
