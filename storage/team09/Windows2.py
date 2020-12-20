import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox  # message box
import WindowMain
import Windows3

class Ventana2(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
     
     #label3.place(x=0,y=0,relwidth=1.0,relheight=1.0)
        label1=Label(self, text="LOADING DATA BASE")
        label1.config(font=("Verdana",50))
        label1.grid(row=1, column=3)
        label2=Label(self, text=" serch your data base  ")
        label2.config(font=("Verdana",15))
        label2.grid(row=7, column=3)
        
        
        button1 = Button(self, text= 'Atras', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana1)
        button1.grid(row=15, column=0)
        button5 = Button(self, text= 'Serch', padx= 15, pady=6, bg= 'grey',fg='white',command=self.Open_Archive)
        button5.grid(row=15, column=3)
      
        # Expandir verticalmente la fila 0.

        self.parent.withdraw()

       
    def ventana1(self):
        self.parent.deiconify()
        self.destroy()

    def Ventana3(self):
        self.destroy()
        Windows3.Ventana(self.parent)
    
    def close(self):
        self.parent.destroy()

    def imagen(self):
        image= tk.PhotoImage(file="imagen.png")
        image=image.subsample(3,3)
        Label7=tk.Label(image=image)
        Label7.pack()

    def Open_Archive(self):
        archive = filedialog.askopenfilename(initialdir="/home/msaban/descargas",
                                             title="seleccione Archivo", filetypes=(("jpeg files", "*jpg"),
                                                                                    ("all files", "*.*")))
        print(archive)
        messagebox.showinfo("Loading data", "DATA SAVED IN TYTUS")
        self.Ventana3()