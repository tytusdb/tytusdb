import tkinter as tk
from tkinter import Toplevel, Button, Tk, Menu, Frame, messagebox, ttk, END, Scrollbar, CENTER, LEFT, Label, Image
from PIL import Image, ImageTk
import avlMode as Crud
import pathlib

def CargarDatos():
        Crud.leerBD()
        Crud.leerREG()
        url=str(pathlib.Path().absolute())
        iconBD = tk.PhotoImage(file=url +"\\Imagenes\\imagenesBaseDatos\\database.png")
        iconTBL = tk.PhotoImage(file=url +"\\Imagenes\\imagenesBaseDatos\\table.png")
        iconREG = tk.PhotoImage(file=url +"\\Imagenes\\imagenesBaseDatos\\file.png")
        Crud.graficaBD()
        listaDB = Crud.showDatabases()
        for db in listaDB:
            itemDB = treeview.insert("", tk.END, text=db, image=iconBD)
            Crud.graficaTBL(db)
            listaTBL = Crud.showTables(db)
            for tbl in listaTBL:
                treeview.insert(itemDB, tk.END, text=tbl, image=iconTBL, tags=(db,"mytag"))
                Crud.graficaREG(db, tbl)

def GraficaBasesDatos():
    url=str(pathlib.Path().absolute())
    img  = Image.open(url +"\\imagenes\\graficaArboles\\BBDD.png") 
    photo = ImageTk.PhotoImage(img)
    lab = Label(image=photo).place(x=310,y=10)
    update_idletasks()

def item_selected(event):
        selected = event.widget.selection()
        for idx in selected:
            nombreTabla = treeview.item(idx)['text']
            nombreBaseDatos = treeview.item(idx)['tags'][0]
        registros = Crud.extractTable(nombreBaseDatos, nombreTabla)
        for i in treeRegs.get_children():
            treeRegs.delete(i)
        if registros:
            columnas = len(registros[0])
            t = []
            for c in range (0, columnas):
                t.append("Col_"+str(c))
            treeRegs["columns"] = t
        treeRegs.column("#0", width=0, minwidth=0, stretch=tk.NO)
        for i in treeRegs["columns"]:
            treeRegs.column(i, width=200, stretch=tk.NO)
            treeRegs.heading(i, text=i.title(), anchor = tk.W)
        mColor = 'par'
        for reg in registros:
            treeRegs.insert("", tk.END, values=reg, tags=(mColor,))
            if mColor == 'par': mColor = 'impar'
            else: mColor = 'par'
        url=str(pathlib.Path().absolute())
        img  = Image.open(url +"\\imagenes\\graficaArboles\\"+ nombreTabla + ".png") 
        photo = ImageTk.PhotoImage(img)
        lab = Label(image=photo).place(x=310,y=10)
        update_idletasks()

def About():
    messagebox.showinfo(message=" TytusDB \n Universidad de San Carlos de Guatemala \n Facultad de Ingenieria \n Ingenieria en Ciencias y Sistemas \n \n Estructuras de Datos \n Diciembre 2020 \n Catedratico M.SC. Luis Fernando Espino Barrios \n Auxiliar Carlos Andree Avalos Soto \n \n Estudiantes: \n Edwin Mauricio Mazariegos \n Edgar Enrique Patzan Yoc \n Gabriel Orlando Ajsivinac Xicay \n Walter Manolo Martinez Mateo \n Karen Elisa Lopez Pinto", title="About...")

miAplicacion = Tk()
miAplicacion.minsize(1200, 700)
miAplicacion.maxsize(1200, 700)
menubar = Menu(miAplicacion)
help = Menu(menubar, tearoff=0)
help.add_command(label="About", command = About)
help.add_separator()
help.add_command(label="Grafica Bases de Datos", command = GraficaBasesDatos)
help.add_separator()
help.add_command(label="Exit", command = miAplicacion.quit)
menubar.add_cascade(label="Help", menu=help)
miAplicacion.config(menu=menubar)

treeview = ttk.Treeview(selectmode=tk.BROWSE)
treeview.place(x=10,y=10)
treeview.heading("#0",text="TytusDB - Modo AVL")
treeview.tag_bind("mytag", "<<TreeviewSelect>>", item_selected)

treeRegs = ttk.Treeview(selectmode=tk.BROWSE)
treeRegs.place(x=10,y=410)
treeRegs.tag_configure('par',background='white',foreground='black')
treeRegs.tag_configure('impar',background='black',foreground='white')

img  = Image.open("imgTytus.png") 
photo = ImageTk.PhotoImage(img)
lab = Label(image=photo).place(x=310,y=10)

CargarDatos()

miAplicacion.mainloop()
