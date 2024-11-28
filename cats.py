from tkinter import *
from PIL import Image, ImageTk # библиотеки для загрузки изображения
import requests

from io import BytesIO#ввод вывод информации в двоичном виде
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
        print(f'Error {e}.')
        return None


def update_img():
    url = 'https://cataas.com/cat'
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img
        # если картинка присвоена, то сборщик мусора ее не удалит
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img
        # если картинка присвоена, то сборщик мусора ее не удалит

def exit():
    window.destroy()
#графический интерфейс для отправки запросов к api
window = Tk()
window.title('Cats')
window.geometry('600x520')

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)#чтобы меню не отклеивалось
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=update_img)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)
label = Label()
label.pack()

# update_button = Button(text = 'Обновить', command = update_img)
# update_button.pack()

update_img()

window.mainloop()