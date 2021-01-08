from sys import path
from os.path import dirname as dir
import os
path.append(dir(path[0]))
from tkinter import ttk
import tkinter as tk
from tkinter import *

from optimization.genOptimized import optimizeCode

class PantallaOpt:
    def __init__(self):
        self.lexicalErrors = list()
        self.syntacticErrors = list()
        self.semanticErrors = list()
        self.postgreSQL = list()
        self.ts = list()
        self.inicializarScreen()

    def inicializarScreen(self):
        # inicializacion de la pantalla
        self.window = Tk()
        self.window.geometry("700x300")
        self.window.resizable(0, 0)
        self.window.title("Optimize Tool")
        self.window.config(bg="black")
        self.frame_entrada = Frame(
            self.window, height=300, width=520, bd=10, bg="black"
        )
        self.txt_scroll = Scrollbar(self.frame_entrada)
        self.txt_scroll.pack(side=RIGHT, fill=Y)
        self.txt_entrada = tk.Text(
            self.frame_entrada, yscrollcommand=self.txt_scroll.set, height=15, width=80
        )
        self.txt_entrada.pack(side=TOP)
        self.txt_scroll.config(command=self.txt_entrada.yview)
        self.frame_entrada.pack()
        # Definicion del menu de items
        navMenu = Menu(self.window)
        navMenu.add_command(label="OPTIMIZAR",
                    command=self.optimizar)
        self.window.config(menu=navMenu)
        self.window.mainloop()

    def optimizar(self):
        entrada = self.txt_entrada.get("1.0",END)
        optimizeCode(entrada)

def main():  # Funcion main
    queryTool = PantallaOpt()
    os.system('cd codigoOptimizado.py')
    os.system('cd reporteOptimizado.html')
    return 0

if __name__ == "__main__":
    main()