from tkinter import *
from tkinter import ttk 

root = Tk()
root.title('Menu de dropdowns!')
root.geometry("700x400+1000+500") 
root.configure(background='dark turquoise') 

BasesdeDatos = ["Bd1","Bd2","Bd3","Bd4","Bd5","Bd6","Bd7"]
Tablas = ["Tabla1","Tabla2","Tabla3","Tabla4","Tabla5","Tabla6","Tabla7"]
Tuplas = ["Tupla1","Tupla2","Tupla3","Tupla4","Tupla5","Tupla6","Tupla7"]

def comboclick(event): 
    if myCombo.get() == 'Bd2':  ###  
        myCombo2.pack(side='left',padx=0,pady=0) 
    else:
        pass

def comboclick2(event):
    if myCombo2.get() == 'Tabla2':  
        
        myCombo3.pack(side='left',padx=30,pady=0)
    else:
        pass

def comboclick3(event):
    pass 

    
def borarOmostrar():
    if myCombo2.place_info() != {}:
        myCombo2.place_forget()
    else:
        myCombo2.place(x=253, y=189)



clicked = StringVar()
clicked.set(BasesdeDatos[0])


myCombo = ttk.Combobox(root,value=BasesdeDatos)
myCombo.current(0) 
myCombo.bind("<<ComboboxSelected>>",comboclick) 
myCombo.pack(side='left',padx=30,pady=0) 

myCombo2 = ttk.Combobox(root,value=Tablas)
myCombo2.current(0) 
myCombo2.bind("<<ComboboxSelected>>",comboclick2) 

myCombo3 = ttk.Combobox(root,value=Tuplas)
myCombo3.current(0) 
myCombo3.bind("<<ComboboxSelected>>",comboclick3) 


myButton = Button(root, text="Mostrar Tablas de:", command=borarOmostrar)
myButton.pack() 
myButton.place(x=45, y=150)

myButton2 = Button(root, text="Mostrar Tuplas de:", command=borarOmostrar)
myButton2.pack() 
myButton2.place(x=220, y=150)

myButton3 = Button(root, text="Mostrar Bases de Datos", command=borarOmostrar)
myButton3.pack() 
myButton3.place(x=170, y=90)

textlabel = ttk.Entry(root)
textlabel.place(x=550, y=190)


root.mainloop() 
