from tkinter import ttk
import tkinter as tk
from tkinter import *


class Pantalla_AST:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry("1024x1024")
        self.top.resizable(0, 0)
        self.top.title("AST")
        label = Label(self.top, text="AST")
        label.config(font=("Verdana", 20, "bold"))
        label.pack(anchor=W)
        self.pw = PanedWindow(self.top, orient="vertical")
        imagen = PhotoImage(file="./test-output/round-table.gv.png")
        Label(self.pw, image=imagen, bd=0).pack()
        self.pw.pack()
        btn = Button(self.top, text="Regresar", command=self.close)
        btn.pack(side=TOP, anchor=E, padx=25, pady=20)
        self.top.mainloop()

    def close(self):
        self.top.destroy()