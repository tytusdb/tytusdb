from tkinter import ttk 
from tkinter import scrolledtext 
import tkinter as tk 
from tkinter import *

class base:
    #esto es un constructor
    def __init__(self, window):
        self.wind = window #guarda la ventana que tiene como parametro  
        self.wind.title('TytusDB')

        #creando el contenedor de barra de herramientas superior
        #columnspam para un espaciado dentro de las columnass
        #padding espacio entre cada elemento

        #self.toolbar = Frame(root,bg="gray",height=40)
        #self.toolbar.pack(side=TOP, fill=X)


        Bases = LabelFrame(self.wind, text= 'BASES DE DATOS EXISTENTES', background='white')
        Bases.grid(row=0, column=0, columnspan=3, pady=20)

        text_area = scrolledtext.ScrolledText(self.wind, wrap = tk.WORD, width = 40, height = 10,  
                                      font = ("Times New Roman", 
                                              15)) 
  
        text_area.grid(row= 0, column = 20, pady = 40, padx = 10) 
        text_area.focus() 

        #self.datos = Entry(Entrada)
        #self.datos.grid(row=1, column=1)

        

        #haciendo un texto

        Label(Bases, text='BASES DE DATOS 1', background='white').grid(row=1, column=0)
        Label(Bases, text='BASES DE DATOS 2', background='white').grid(row=2, column=0)
        Label(Bases, text='BASES DE DATOS 3', background='white').grid(row=3, column=0)
        Label(Bases, text='BASES DE DATOS 3.1', background='white').grid(row=4, column=1)
        Label(Bases, text='BASES DE DATOS 3.2', background='white').grid(row=5, column=1)
        Label(Bases, text='BASES DE DATOS 4', background='white').grid(row=6, column=0)


        #self.name = Entry(frame_prueba)
        #self.name.grid(row=1, column=1)
        menubar =Menu(self.wind)
        self.wind.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command= self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Object")
        menubar.add_cascade(label="Tools")
        menubar.add_cascade(label="Help")

    def onExit(self):

        self.quit()

if __name__ == '__main__':
        window = Tk()
        window.geometry("850x450+100+100")
        window.configure(background='white')
        application = base(window)
        
        window.mainloop()