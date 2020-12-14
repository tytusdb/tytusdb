import os
from tkinter import *


class mainwindow:
    def __init__(self, app):
        app.title("TytusDB - Compiladores 2")
        app.geometry("1100x560")

        self.app = app

        self.upper_frame = Frame(app,  bg='grey')
        self.upper_frame.pack(fill=BOTH)
        self.middle_frame = Frame(app,  bg='grey')
        self.middle_frame.pack(fill=BOTH)
        self.buttom_frame = Frame(app,  bg='grey')
        self.buttom_frame.pack(fill=BOTH)


if __name__ == "__main__":
    app = Tk()
    Interfaz = mainwindow(app)
    app.mainloop()
