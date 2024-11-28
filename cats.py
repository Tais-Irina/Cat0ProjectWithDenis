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
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Error {e}.')
        return None

#графический интерфейс для отправки запросов к api
window = Tk()
window.title('Cats')
window.geometry('600x400')
label = Label()
label.pack()

url = 'htts://cataas.com/cat'
img = load_image(url)
if img:
    label.config(image=img)
    label.image = img
    #если картинка присвоена, то сборщик мусора ее не удалит
window.mainloop()