from tkinter import *
import pyqrcode


class CreateQRCode():
    def __init__(self, user_url_name, user_url):
        self.user_url_name = user_url_name
        self.user_url = user_url

        # creates qr code destination
        url = pyqrcode.create(user_url)
        # creates the qr code image and name
        url.png(user_url_name + '.png', scale = 8)


class MainWindow():
    def __init__(self):
        # initializing the main window
        window = Tk()
        window.title('QR Code Generator')
        window.geometry('800x800')
        window.configure(bg = 'white')

        qr_code_name_label = Label(window, bg = 'white', text='QR Code Name')
        qr_code_name_label.grid(row = 1, column = 2)

        qr_code_url_label = Label(window, bg = 'white', text = 'URL')
        qr_code_url_label.grid(row = 2, column = 2)

        qr_code_name_entry = Entry(window, bg = 'white')
        qr_code_name_entry.grid(row = 2, column = 3)

        window.mainloop()

#MainWindow()
CreateQRCode(input('QR Code Name: '), input('URL: '))
