from tkinter import *
from PIL import Image, ImageTk # библиотеки для загрузки изображения
import requests
from tkinter import messagebox as mb
from tkinter import ttk#набор улучшенных виджетов
from io import BytesIO#ввод вывод информации в двоичном виде

Allowed_tags = ['white', 'black', 'funny', 'happy', 'sleep', 'jump', 'fight', 'cute', 'bengal', 'siamese']

def load_image(url):
    try:
        response = requests.get(url)
        # если возникнет ошибка при отправке запроса то проверим это
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        #способ по которому будет конвертироваться изображение
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        mb.showinfo("Предупреждение","Такого тега нет, введите другой тег")
        return None


def open_new_window():
    tag_cat = tag_combobox.get()
    url = f'https://cataas.com/cat/{tag_cat}' if tag_cat else 'https://cataas.com/cat'
    img = load_image(url)
    if img:
        new_window = Toplevel(window)
        new_window.title("Картинка с котиком")
        new_window.geometry('600x480')
        l = Label(new_window)
        l.pack()
        l.config(image=img)
        l.image = img
        # если картинка присвоена, то сборщик мусора ее не удалит

def exit():
    window.destroy()


#графический интерфейс для отправки запросов к api
window = Tk()
window.title('Cats')
window.geometry('500x80')

#tag_entry = Entry()
#tag_entry.pack()

tag_label = Label(text='Выбери тег')
tag_label.pack()


tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack()
button = Button(text = 'Загрузить по тегу котика', command = open_new_window)
button.pack()

window.mainloop()


'''
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)#чтобы меню не отклеивалось
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=update_img)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)
'''



