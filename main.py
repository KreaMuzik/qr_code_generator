from tkinter import *
from tkinter import ttk
import pyqrcode


class CreateQRCode():
    def __init__(self, user_url_name, user_url):
        self.user_url_name = user_url_name
        self.user_url = user_url

        url = pyqrcode.create(user_url)
        url.png(user_url_name + '.png', scale = 8)


class MainWindow():
    def __init__(self):
        window = Tk()

        window.title('QR Code Generator')
        window.geometry('800x800')

        window.mainloop()


CreateQRCode(input('QR Code Name: '), input('URL: '))
