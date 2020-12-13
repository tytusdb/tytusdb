from AVL_Delete_201801597 import  AVLTree
from tkinter import * 
from tkinter import Menu 
from tkinter import filedialog 
from tkinter import scrolledtext 
from tkinter import messagebox  
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk

contenidoCSV = ""
class GUI: 
    def __init__(self):
        self.window = tk.Tk()
        self.treeview = ttk.Treeview(self.window)
        self.canva=Canvas()
        self.canva.place(x=2000,y=2000)
        self.window.geometry('1250x650')
        self.window.configure(bg='#000066')

        lbl = Label(self.window, text="TYTUS DB", font="Verdana 20 bold")
        lbl.place(x=5, y=5)

        barraMenu = Menu(self.window)
        self.window.config(menu=barraMenu, width=900, height=700)
        archivoMenu = Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Abrir", command=abrirFile)
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir", command=salir)
            
        barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
        self.window.config(menu=barraMenu)
        
        BDButton = Button(self.window, text="Bases de Datos", width=25,
                  height=5, font="Verdana 14 bold", command=self.database)

        BDButton.place(x=50, y=51)

    def database(self):
        
        treeFill(self.treeview)
        self.treeview.place(x=950, y=50)
        
        img = Image.open('C:/Users/Carlos/Desktop/graphviz210.png')
        # print('GGGG')
        pimg = ImageTk.PhotoImage(img)
        size = img.size
        
        frame=Frame(self.window,width=300,height=300)
        frame.pack(fill=BOTH) #.grid(row=0,column=0)
        frame.place(x=25,y=25)   
        canvaX=Canvas(frame,bg='#FFFFFF',scrollregion=(0,0,size[0],size[1]))
        
        self.canva = canvaX
        hbar=Scrollbar(frame,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command= self.canva.xview)
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command= self.canva.yview)
        

        self.canva.config(width=850,height=450)
        self.canva.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
            
        self.canva.create_image(0,0,anchor='nw',image=pimg)
        self.canva.pack(side=LEFT)    
        self.treeview.bind("<Double-1>", self.OnDoubleClick)
        self.window.mainloop()
    
    def OnDoubleClick(self,event):
       
        item = self.treeview.selection()[0]                
        img = Image.open('C:/Users/Carlos/Desktop/graphviz'+str(self.treeview.item(item,"text"))+'.png')
        pimg = ImageTk.PhotoImage(img)
        size = img.size
        
        frame=Frame(self.window,width=300,height=300)
        frame.pack(fill=BOTH)
        frame.place(x=25,y=25)
        canvaX=Canvas(frame,bg='#FFFFFF',scrollregion=(0,0,size[0],size[1]))
        self.canva=canvaX
        hbar=Scrollbar(frame,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command= self.canva.xview)
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command= self.canva.yview)

        
        self.canva.config(width=850,height=450)
        self.canva.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canva.pack(side=LEFT)       
        self.canva.create_image(0,0,anchor='nw',image=pimg)     
        self.canva.mainloop()

def salir(self):
        value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if value:
            self.window.destroy()

def abrirFile(self):
    global contenidoCSV
    nameFile = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[(
        ("Archivo CSV", ".csv"))])
    if nameFile != '':
        archi1 = open(nameFile, "r")
        contenidoCSV = archi1.read()
        archi1.close()

def treeFill(treeview):
    avl=AVLTree()
    avl.add(1)
    avl.add(210)
    avl.add(13)
    nodos =avl.inorder()
    print(nodos)
    treeview["columns"]=("one")
    treeview.heading("#0", text="Numero",anchor=W)
    
    for nodo in nodos:
        treeview.insert("", tk.END,text=nodo)

x=GUI()
x.window.mainloop()

