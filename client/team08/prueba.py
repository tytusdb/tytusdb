from tkinter import ttk 
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as tkscrolled
# pip install pillow
from PIL import ImageTk, Image
class base:
    #esto es un constructor
    def __init__(self, window):
        self.wind = window #guarda la ventana que tiene como parametro  
        self.wind.title('TytusDB')
        load = Image.open("icondb.jpg")
        self.wind.iconphoto(False, ImageTk.PhotoImage(load))
        #creando el contenedor de barra de herramientas superior
        #columnspam para un espaciado dentro de las columnass
        #padding espacio entre cada elemento

        #self.toolbar = Frame(root,bg="gray",height=40)
        #self.toolbar.pack(side=TOP, fill=X)
        Bases = LabelFrame(self.wind, text= 'BASES DE DATOS EXISTENTES', background="white")
        Bases.grid(row=1, column=0, columnspan=3, pady=20)

        Entrada = LabelFrame(self.wind, text='TYTUSDB')
        Entrada.grid(row=0, column=5, columnspan=3, pady=20)
        Label(Entrada, text=' ').grid(row=2, column=0)

        Label(Bases, text='BASES DE DATOS 1').grid(row=1, column=0)
        Label(Bases, text='BASES DE DATOS 2').grid(row=2, column=0)
        Label(Bases, text='BASES DE DATOS 3').grid(row=3, column=0)
        Label(Bases, text='BASES DE DATOS 3.1').grid(row=4, column=1)
        Label(Bases, text='BASES DE DATOS 3.2').grid(row=5, column=1)
        Label(Bases, text='BASES DE DATOS 4').grid(row=6, column=0)

        #self.name = Entry(frame_prueba)
        #self.name.grid(row=1, column=1)
        menubar =Menu(self.wind,  background="gray")

        self.wind.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command= self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Object")
        menubar.add_cascade(label="Tools")
        menubar.add_cascade(label="Help")


        #------IMAGE-------

        
        render = ImageTk.PhotoImage(load)
        img = Label(self.wind, image=render)
        img.image = render
        img.place(x=0, y=0)
        #------TEXTAREA SALIDA------
       # Vertical (y) Scroll Bar
        scroll = Scrollbar(self.wind)
        scroll.pack(side=RIGHT, fill=Y)

    def onExit(self):

        self.quit()

if __name__ == '__main__':
        window = Tk()
        window.geometry("850x450+100+100")

        window.configure(background='white')
        application = base(window)
        window.mainloop()
