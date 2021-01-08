from tkinter import *
from tkinter import ttk 
import Tytus as tytus

def gui2():

    root = Tk()
    root.title('Tytus')
    root.geometry("700x250+1000+500") ##TAMAÑO DE LA VENTANA
    root.configure(background='#3b5971') 


##Boton1
    #myButton = Button(root, text="Mostrar Tablas de:", command=lambda : tytus.graphTBL(myCombo.get()))
    myButton = Button(root, text="Cargar Persistencia:", command=lambda : tytus.chargePersistence())
    myButton.pack() 
    myButton.place(x=500, y=150)

##Boton2
    #myButton2 = Button(root, text="Mostrar Tabla Hash", command=lambda : tytus.graphTable(myCombo.get(),myCombo2.get()))
    myButton2 = Button(root, text="Generar Grafos de dependencias")
    myButton2.pack() 
    myButton2.place(x=245, y=150)

##Boton3
    #myButton3 = Button(root, text="Mostrar Bases de Datos", command=lambda : tytus.graphDB())
    myButton3 = Button(root, text="Generar Grafos de blockchain", command=lambda : tytus.generateGraphBlockChain(textlabel.get(), textlabel2.get()))
    myButton3.pack() 
    myButton3.place(x=250, y=90)

##Boton4
    """myButton4 = Button(root, text="Atras", command=borarOmostrar)
    myButton4.pack() 
    myButton4.place(x=30, y=360)"""


##txtLabel1

    t1 = Label(root, text = "Base de datos", font = ("Arial"))
    t1.place(x = 60, y = 40)
    textlabel = ttk.Entry(root)
    textlabel.place(x=50, y=75)

##txtLabel2
    t2 = Label(root, text = "Tabla", font = ("Arial"))
    t2.place(x = 90, y = 115)
    textlabel2 = ttk.Entry(root)
    textlabel2.place(x=50, y=150)    

    root.mainloop() 

gui2()
