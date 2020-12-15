from Interpreter import lex
from Interpreter import ascparse

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, filedialog, Button, Menu
from tkinter.ttk import *

expresiones = "./Scripts/Consultas.sql"

data = open(expresiones).read()
script = ascparse.parse(data)
print(script)

# INTERFACE
win = tk.Tk()
win.title("Query Tool")
win.geometry("790x530")

style = ttk.Style()
style.configure('TButton', font=('calibri', 10, 'bold'), borderwidth='4')


def openFile():
    try:
        text = filedialog.askopenfilename(
            initialdir="C:/", title="Open Text File", filetypes=(("Text Files", "*.*"), ))
        text = open(text, 'r')
        stuff = text.read()

        entrada.insert(1.0, stuff)
        text.close()
    except IOError:
        print("Could not read file")


def saveFile():
    try:
        text = filedialog.askopenfilename(
            initialdir="C:/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
        text = open(text, 'w')
        text.write(entrada.get(1.0, tk.END))
    except IOError:
        print("Could not Write file")


def clear():
    entrada.delete(1.0, tk.END)
    salida.delete(1.0, tk.END)


def Ejecutar():
    texto = entrada.get('1.0', tk.END)


def TreeAST():
    print("TreeAST")


def TablaSimbolos():
    print("Tabla")


def ErrorLexico():
    print("Errores")


menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=clear)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)
menubar.add_cascade(label="File", menu=filemenu, font=("Times New Roman", 15))
helpmenu = Menu(menubar, tearoff=0)
win.config(menu=menubar)

open_button = Button(win, text="EJECUTAR", command=Ejecutar)
open_button.place(x=20, y=25)

ejecutar = Button(win, text="TREE AST", command=TreeAST)
ejecutar.place(x=110, y=25)

arbol = Button(win, text="TABLA DE SIMBOLOS", command=TablaSimbolos)
arbol.place(x=200, y=25)

ERR_lex = Button(win, text="ERRORES", command=ErrorLexico)
ERR_lex.place(x=325, y=25)


label1 = Label(win, text='Entrada:', font=("Times New Roman", 15))
label1.place(x=20, y=50)

entrada = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=85, height=9,
                                    font=("Times New Roman", 12))
entrada.grid(column=0, pady=74, padx=20)
entrada.focus()

label2 = Label(win, text='Salida:', font=("Times New Roman", 15))
label2.place(x=20, y=290)

salida = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=85, height=10,
                                   font=("Times New Roman", 12))

salida.grid(column=0, pady=0, padx=20)
salida.focus()

win.mainloop()
