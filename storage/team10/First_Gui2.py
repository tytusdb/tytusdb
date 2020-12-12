from tkinter import *
from tkinter import ttk 
BasesdeDatos = ["Bd1","Bd2","Bd3","Bd4","Bd5","Bd6","Bd7","Bd1","Bd2","Bd3","Bd4","Bd5","Bd6","Bd7"]
Tablas = ["Tabla1","Tabla2","Tabla3","Tabla4","Tabla5","Tabla6","Tabla7"]
Tuplas = ["Tupla1","Tupla2","Tupla3","Tupla4","Tupla5","Tupla6","Tupla7"]
Tablas2=[]
Tuplas2=[]

class Tabla:
    def __init__(self, clave, nombre,bd):
        self.Id = clave
        self.Nombre = nombre
        self.Bd = bd

Tabla1 = Tabla('0', 'Tomates','Bd1')   
Tablas2.append(Tabla1)   
Tabla2 = Tabla('1', 'Tomates','Bd2') 
Tablas2.append(Tabla2)   
Tabla3 = Tabla('2', 'Tomates2','Bd1')    
Tablas2.append(Tabla3)   
Tabla4 = Tabla('3', 'Tomates2','Bd2')    
Tablas2.append(Tabla4)   
Tabla5 = Tabla('4', 'Tomates3','Bd1')  
Tablas2.append(Tabla5)          
Tabla6 = Tabla('5', 'Tomates','Bd3')   
Tablas2.append(Tabla6)    
Tabla7 = Tabla('6', 'Tomates','Bd4')   
Tablas2.append(Tabla7)    
Tabla8 = Tabla('7', 'Tomates4','Bd1')    
Tablas2.append(Tabla8)   
Tabla9 = Tabla('8', 'Tomates2','Bd4')    
Tablas2.append(Tabla9)   
Tabla10 = Tabla('9', 'Tomates2','Bd3')   
Tablas2.append(Tabla10)  

for i in Tablas2:
    print(i.Nombre)

class Tupla:
    def __init__(self, clave, nombre,tabla):
        self.Id = clave
        self.Nombre = nombre
        self.Tabla = tabla    

Tupla1 = Tupla('0', 'Ricos','0')   
Tuplas2.append(Tupla1)   
Tupla2 = Tupla('1', 'Tupla Tabla2','1') 
Tuplas2.append(Tupla2)   
Tupla3 = Tupla('2', 'Tupla Tabla3','2')    
Tuplas2.append(Tupla3)   
Tupla4 = Tupla('3', 'Ricos','0')    
Tuplas2.append(Tupla4)   
Tupla5 = Tupla('4', 'Tupla Tabla4','3')  
Tuplas2.append(Tupla5)          
Tupla6 = Tupla('5', 'Tupla Tabla4','3')   
Tuplas2.append(Tupla6)    
Tupla7 = Tupla('6', 'Tupla Tabla1','2')   
Tuplas2.append(Tupla7)    
Tupla8 = Tupla('7', 'Tupla Tabla2','1')    
Tuplas2.append(Tupla8)   
Tupla9 = Tupla('8', 'Tomates','0')    
Tuplas2.append(Tupla9)   
Tupla10 = Tupla('9', 'Tupla Tabla6','5') 
Tuplas2.append(Tupla10) 

root = Tk()
root.title('Consultas')
root.geometry("700x400+1000+500") 
root.configure(background='dark turquoise') 

def comboclick(event): 
    AuxTablas=[]
    
    for i in Tablas2:
        if(i.Bd==myCombo.get()):
            AuxTablas.append(i.Nombre)
            aa=i.Id
    
    myCombo2['values'] = AuxTablas
    
    myCombo2.pack(side='left',padx=0,pady=0) 
    
    myCombo2.set('')
    myCombo3.set('')
    print(myCombo.get())
    AuxTablas=[]
    
def comboclick2(event):
    AuxTuplas=[]
    
    for i in Tablas2:  
        if(i.Nombre==myCombo2.get() and i.Bd==myCombo.get()):          
            for i2 in Tuplas2:
                print("")
                print(i.Id)
                print(i2.Tabla)
                if(i2.Tabla==i.Id):   
                    print("Aqeui es")              
                    AuxTuplas.append(i2.Nombre)

    myCombo3['values'] = AuxTuplas
    
    myCombo3.pack(side='left',padx=30,pady=0) ##Para que imprima este dropdown
    
    myCombo3.set('')
    print(myCombo.get())
    AuxTuplas=[]

def comboclick3(event):
    root2 = Tk()
    root2.title('Tupla')
    root2.geometry("420x230+1150+600") ##TAMAÑO DE LA VENTANA
    root2.configure(background='dark turquoise')

    tabla = ttk.Treeview(root2,columns=2)##El marco sera mi misma ventana
    tabla.place(x=10, y=0)##Trabajammos por filas
    tabla.heading("#0",text="ID",anchor=CENTER) ##ANCHOR ES PARA CENTRAR
    tabla.heading("#1",text="Nombre",anchor=CENTER)

    
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
myCombo2 = ttk.Combobox(root,value=Tablas2)
myCombo2.bind("<<ComboboxSelected>>",comboclick2) 
myCombo3 = ttk.Combobox(root,value=Tuplas)
myCombo3.bind("<<ComboboxSelected>>",comboclick3) 
myButton = Button(root, text="Mostrar Tablas de:", command=borarOmostrar)
myButton.pack() 
myButton.place(x=45, y=150)
myButton2 = Button(root, text="Mostrar Tuplas de:", command=borarOmostrar)
myButton2.pack() 
myButton2.place(x=220, y=150)
myButton3 = Button(root, text="Mostrar Bases de Datos", command=borarOmostrar)
myButton3.pack() 
myButton3.place(x=285, y=90)
myButton4 = Button(root, text="Atras", command=borarOmostrar)
myButton4.pack() 
myButton4.place(x=30, y=360)

root.mainloop() 





