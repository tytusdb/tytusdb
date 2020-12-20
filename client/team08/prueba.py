from tkinter import ttk 
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import tkinter.scrolledtext as tkscrolled
# pip install pillow
from PIL import ImageTk, Image
class base:
    #esto es un constructor
    def __init__(self, window):
        self.wind = window #guarda la ventana que tiene como parametro  
        self.wind.title('TytusDB')
        load = Image.open("icondb.png")
        self.wind.iconphoto(False, ImageTk.PhotoImage(load))
        #creando el contenedor de barra de herramientas superior
        #columnspam para un espaciado dentro de las columnass
        #padding espacio entre cada elemento

        #self.toolbar = Frame(root,bg="gray",height=40)
        #self.toolbar.pack(side=TOP, fill=X)
        Bases = LabelFrame(self.wind, text= 'BASES DE DATOS EXISTENTES', background="white")
        Bases.grid(row=0, column=0, columnspan=3, pady=95)
        
        text_area = scrolledtext.ScrolledText(self.wind, wrap = tk.WORD, width = 50, height = 7,  
                                      font = ("Times New Roman", 
                                              15)) 
  
        text_area.place(x=290, y=40)
        text_area.focus() 
        load1 = Image.open("tytus.gif")
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self.wind, image=render1)
        img1.image = render1
        img1.place(x=290, y=215)
        tk.Label(self.wind,  
         text = "Salida",  
         font = ("Arial", 20),  
         background = '#B5F5E0',  
         foreground = "black").place(x=370, y=215)
        text_area1 = scrolledtext.ScrolledText(self.wind, wrap = tk.WORD, width = 50, height = 7,  
                                      font = ("Times New Roman", 
                                              15)) 
  
        text_area1.place(x=290, y=250) 
        
        text_area1.focus() 

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
        
    def onExit(self):

        self.quit()

if __name__ == '__main__':
        window = Tk()
        window.geometry("850x450+100+100")

        window.configure(background='white')
        application = base(window)
        window.mainloop()
