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

def salir():
    value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if value:
        window.destroy()

def abrirFile():
    global contenidoCSV
    nameFile = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[(
        ("Archivo CSV", ".csv"))])
    if nameFile != '':
        archi1 = open(nameFile, "r")
        contenidoCSV = archi1.read()
        archi1.close()
def treeFill(tree):
    tree["columns"]=("one")
    tree.heading("#0", text="Numero",anchor=W)
    tree.heading("one", text="Nombre",anchor=W)

def database():
    window.destroy()
    db = Tk()

    db.geometry('1375x650')
    db.configure(bg='#000066')    

    barraMenu = Menu(db)
    db.config(menu=barraMenu, width=900, height=700)
    archivoMenu = Menu(barraMenu, tearoff=0)
    archivoMenu.add_command(label="Abrir", command=abrirFile)
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Salir", command=salir)
    barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
    db.config(menu=barraMenu)

    treeview=ttk.Treeview(db)
    treeFill(treeview)
    treeview.place(x=950, y=50)
    create = Button(db, text="Agregar", width=10,
                    height=2, font="Verdana 14 bold")
    create.place(x=50, y=550)

    delete = Button(db, text="Borrar", width=10,
                    height=2, font="Verdana 14 bold")
    delete.place(x=200, y=550)

    update = Button(db, text="Actualizar", width=10,
                    height=2, font="Verdana 14 bold")
    update.place(x=350, y=550)

    read = Button(db, text="Mostrar", width=10,
                  height=2, font="Verdana 14 bold")
    read.place(x=500, y=550)

    # pic = filedialog.askopenfilename()
    # print(pic)
    img = Image.open('C:/Users/Carlos/Desktop/temp.png')
    pimg = ImageTk.PhotoImage(img)
    size = img.size
    
    frame=Frame(db,width=300,height=300)
    frame.pack(fill=BOTH) #.grid(row=0,column=0)
    canvas=Canvas(frame,bg='#FFFFFF',scrollregion=(0,0,size[0],size[1]))
   
    hbar=Scrollbar(frame,orient=HORIZONTAL)
    hbar.pack(side=BOTTOM,fill=X)
    hbar.config(command=canvas.xview)
    vbar=Scrollbar(frame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas.yview)
   
    canvas.config(width=850,height=450)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=LEFT)
    canvas.create_image(0,0,anchor='nw',image=pimg)
    
    frame.place(x=25,y=25)
    db.mainloop()
    window.mainloop()

window = Tk()

window.geometry('1250x650')
window.configure(bg='#000066')

lbl = Label(window, text="TYTUS DB", font="Verdana 20 bold")
lbl.place(x=5, y=5)

barraMenu = Menu(window)
window.config(menu=barraMenu, width=900, height=700)
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Abrir", command=abrirFile)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salir)
barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
window.config(menu=barraMenu)

BDButton = Button(window, text="Bases de Datos", width=25,
                  height=5, font="Verdana 14 bold", command=database)

BDButton.place(x=50, y=51)

# window.state('zoomed')
window.mainloop()
