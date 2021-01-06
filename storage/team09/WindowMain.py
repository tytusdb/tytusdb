import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import  Windows3

class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Principal Tytus")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        label1 = Label(text="¡ Welcome To TitusDB!")
        label1.config(font=("Verdana", 50))
        label1.grid(row=1, column=3)
        label2 = Label(text="¡ Select your option : ")
        label2.config(font=("Verdana", 28))
        label2.grid(row=3, column=3)
        label3 = Label(text="\n\n1.option 1\n2.option 2\n3.option 3\n4. ISAM \n5.option 5")
        label3.config(font=("Verdana", 23))
        label3.grid(row=5, column=3)   
        label4 = Label(text="\n\nInsert Number")
        label4.config(font=("Verdana", 15))
        label4.grid(row=7, column=3)
        self.entry = Entry()
        self.entry.grid(row=10, column=3)
        button = Button(text='Accept', padx=15, pady=6, bg='grey', fg='white', command=self.SegundaVentana)
        button.grid(row=12, column=3)


        



    def SegundaVentana(self):
        print(self.entry.get())
        self.destroy()
        Windows3.Ventana(self.parent)
        
   
        

if __name__ == "__main__":
    root = tk.Tk()
    
    MainWindow(root)
    
    root.mainloop()
