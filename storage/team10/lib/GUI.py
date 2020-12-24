from tkinter import *
from tkinter import ttk ##Para combobox
import HashMode as tytus
import DataBase as database
Tablas2=[]
Tuplas2=[]

##Clase Objetos########################################################################################################


#########################################################################################################################    

def gui2():
    BasesdeDatos = [] ##Esto agrega las bases de datos de tytus
    for l in tytus.databases:
        BasesdeDatos.append(l.name) 

    root = Tk()
    root.title('Consultas')
    root.geometry("700x400+1000+500") ##TAMAÑO DE LA VENTANA
    root.configure(background='#3b5971') 

    def comboclick(event): ##Segundo DropdownList
        AuxTablas=[] 
        try:
            for i in tytus.showTables(myCombo.get()): ##metodo para imprimir tablas segun la base de datos mandando lo que hay en el drop1
                AuxTablas.append(i)
        except :
            print("No hay tablas ingresadas")

        myCombo2['values'] = AuxTablas
        myCombo2.pack(side='left',padx=0,pady=0) ##Para que imprima este dropdown
        myCombo2.set('')
        #myCombo3.set('')
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
        return AuxTuplas    
    
        #myCombo3['values'] = AuxTuplas
    
        #myCombo3.pack(side='left',padx=30,pady=0) ##Para que imprima este dropdown
    
        #myCombo3.set('')
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


#DropDown de BD
    myCombo = ttk.Combobox(root,value=BasesdeDatos)
    myCombo.current(0) 
    myCombo.bind("<<ComboboxSelected>>",comboclick) ##Comboclick es una funcion que esta arriba
    myCombo.pack(side='left',padx=30,pady=0) ##Para que salga

#Dropdown de las tablas
    myCombo2 = ttk.Combobox(root,value=Tablas2)
    myCombo2.bind("<<ComboboxSelected>>",comboclick2) ##Comboclick es una funcion que esta arriba  

#Tercer Combobox
    #myCombo3 = ttk.Combobox(root,value=Tuplas)
    #myCombo3.bind("<<ComboboxSelected>>",comboclick3) ##Comboclick es una funcion que esta arriba


##Boton1
    myButton = Button(root, text="Mostrar Tablas de:", command=lambda : tytus.graphTBL(myCombo.get()))
    myButton.pack() 
    myButton.place(x=45, y=150)

##Boton2
    myButton2 = Button(root, text="Mostrar Tabla Hash", command=lambda : tytus.graphTable(myCombo.get(),myCombo2.get()))
    myButton2.pack() 
    myButton2.place(x=400, y=150)

##Boton3
    myButton3 = Button(root, text="Mostrar Bases de Datos", command=lambda : tytus.graphDB())
    myButton3.pack() 
    myButton3.place(x=285, y=90)

##Boton4
    myButton4 = Button(root, text="Atras", command=borarOmostrar)
    myButton4.pack() 
    myButton4.place(x=30, y=360)

##txtLabel1
#textlabel = ttk.Entry(root)
#textlabel.place(x=550, y=190)


######Tabla:




    root.mainloop() 


##Clase Objetos####################

