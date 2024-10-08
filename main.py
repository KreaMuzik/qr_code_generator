"""Imports"""
from tkinter import *
from tkinter import ttk
import segno


def create_qr_code(name, url):
    '''
    Creates QR code from user's input variables
    '''
    qrcode = segno.make(url)
    qrcode.save(name+'.png')

def btn_click():
    '''
    On button click, get Entry variables as Strings
    '''
    name = qr_name.get()
    url = qr_url.get()
    create_qr_code(name, url)

# Creates main window
root = Tk()

ttk.Label(root, text='Name').grid(column=0, row=0, padx=5, pady=5)
ttk.Label(root, text='URL').grid(column=0, row=1, padx=5, pady=5)

qr_name = ttk.Entry(root)
qr_name.grid(column=1, row=0, padx=5, pady=5)

qr_url = ttk.Entry(root)
qr_url.grid(column=1, row=1, padx=5, pady=5)

btn = ttk.Button(root, text='Create QR Code', command=btn_click)
btn.grid(column=0, row=2, columnspan=2, padx=5, pady=5)

root.mainloop()
