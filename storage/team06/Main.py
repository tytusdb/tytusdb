from ArbolAVL import *
from tkinter import *
from tkinter import filedialog

raiz=Tk()
menubar = Menu(raiz)

cadena = "vacio"
nombreArchivo = ""
ficheroactual=""

teeexto=""

#se asigna el menu completo
raiz.config(menu = menubar)

yscroll = Scrollbar(raiz)
yscroll.pack(side=RIGHT, fill=Y)

#cajas de texto
caja1=Text(raiz,width=65,height=30)
caja1.place(x=60,y=100)

caja2=Text(raiz,width=30,height=10)
caja2.place(x=600,y=300)


#Metodos para la interfaz
def Abrir(): #abrir archivo
    caja1.delete(1.0,END)
    global ficheroactual
    file = filedialog.askopenfilename(filetypes =[('Archivo HTML', '*.html'),('Archivo CSV', '*.csV')])
    fichero = open(file)
    ficheroactual=file
    global cadena
    global teeexto
    global nombreArchivo
    nombreArchivo = file.split("/")[-1]

    muchoTexto = fichero.read()
    cadena=muchoTexto
    teeexto=muchoTexto
    caja1.delete(1.0,END)
    caja1.insert("insert",muchoTexto)
    fichero.close()
    
    

def nuevoA(): #Nuevo archivo
    caja1.delete(1.0,END)

def Datos(): #analiza
    #prueba para mostrar el arbol 
    mWindow= Toplevel()
    mWindow.geometry('300x200')
    mWindow.title('Miembros del grupo')
    mWindow.config(bg="black")
    Dato1 = Label(mWindow, text="GRUPO #6", font=("Impact",10))
    Dato1.place(x=10,y=10)
    Dato2 = Label(mWindow, text="Alex", font=("Impact",10))
    Dato2.place(x=10,y=50)
    Dato3 = Label(mWindow, text="Sohany", font=("Impact",10))
    Dato3.place(x=10,y=90)
    Dato4 = Label(mWindow, text="Jorge", font=("Impact",10))
    Dato4.place(x=10,y=130)
    Dato5 = Label(mWindow, text="Diego", font=("Impact",10))
    Dato5.place(x=10,y=130)
    print("Datos del grupo")
        
        
    


def guardarU():
    global nombreArchivo
    global ficheroactual
    global teeexto
    textt=caja1.get(1.0,END)
    abrirHtml = open(ficheroactual,"w")
    abrirHtml.write(textt)
    abrirHtml.close()
    print("guardar")


    

def Guardarcomo():
    global teeexto
    global ficheroactual
    textt=caja1.get(1.0,END)
    guardar = filedialog.asksaveasfile(title="Guardar Archivo",initialdir="C:",filetypes = (("Archivo de HTML","*.html*"),("Archivo de CSV","*.csV*")))
    yguardar = open(guardar,"w+",encoding="UTF-8")
    yguardar.write(textt)
    yguardar.close()
    teeexto = guardar
    print("guardar como")


def CreateDB():
    print("funcion1")

def CreateTable():
    print("crear tabla")



def AlterDataBase():
    print("crear base")


def ShowDataBase():
    print("mostrar data")
    #prueba para mostrar el arbol 
    VBase= Toplevel()
    VBase.geometry('600x600')
    VBase.config(bg="black")
    VBase.title('Arbol')
    #se agrega la imagen
    imagenL=PhotoImage(file="grafo.png")
    grafico=Label(VBase,image=imagenL)
    grafico.place(x=0,y=0)
    VBase.wait_window()

def DropDatabase():
    print("dropear base")

def AlterTable():
    print("alter table")

def showTables():
    print("show tables")

def extractTable():
    print("extract")

def extractRangeTable():
    print("extract")

def alterAddPK():
    print("alterAdd")


def alterDropPK():
    print("droppk")

def alterAddFK():
    print("AlterAddFK")

def alterAddIndex():
    print("alterAddIndex")    


def alterTable():
    print("alterTable")


def alterAddColumn():
    print("alterAddColumn")


def alterDropColumn():
    print("alterDropColumn")


def dropTable():
    print("dropTable")


def insert():
    print("insert")

def loadCSV():
    print("loadCSV")


def extractRow():
    print("extractRow")


def update():
    print("update")


def EjecutarBD():
    print("ejecutando Base de datos")


def VBD():
    print("ver base de datos")
    


##Configuracion de la parte visual
raiz.title("Base de datos con AVL")
raiz.geometry("1150x600")
raiz.config(bg="black")


#titulo
Titulo = Label(raiz, text="BASE DE DATOS GRUPO 6", font=("Impact",30))
Titulo.place(x=400,y=25)

##Botones para las funciones
boton1 = Button(raiz, text="createDatabase", activebackground="#F50743",command=CreateDB)
boton1.place(x=600,y=100)
boton1.config(width=13, height=1)
boton2 = Button(raiz, text="showDatabases", activebackground="#F50743",command=ShowDataBase)
boton2.place(x=700,y=100)
boton2.config(width=13, height=1)
boton3 = Button(raiz, text="alterDatabase", activebackground="#F50743",command=AlterDataBase)
boton3.place(x=800,y=100)
boton3.config(width=13, height=1)
boton4 = Button(raiz, text="dropDatabase", activebackground="#F50743",command=DropDatabase)
boton4.place(x=900,y=100)
boton4.config(width=13, height=1)
boton5 = Button(raiz, text="createTable", activebackground="#F50743",command=CreateTable)
boton5.place(x=1000,y=100)
boton5.config(width=13, height=1)
boton6 = Button(raiz, text="showTables", activebackground="#F50743",command=showTables)
boton6.place(x=600,y=150)
boton6.config(width=13, height=1)
boton7 = Button(raiz, text="extractTable", activebackground="#F50743",command=extractTable)
boton7.place(x=700,y=150)
boton7.config(width=13, height=1)
boton8 = Button(raiz, text="update", activebackground="#F50743",command=update)
boton8.place(x=800,y=150)
boton8.config(width=13, height=1)
boton9 = Button(raiz, text="alterAddPK", activebackground="#F50743",command=alterAddPK)
boton9.place(x=900,y=150)
boton9.config(width=13, height=1)
boton10 = Button(raiz, text="alterDropPK", activebackground="#F50743",command=alterDropPK)
boton10.place(x=1000,y=150)
boton10.config(width=13, height=1)
boton11 = Button(raiz, text="alterAddFK", activebackground="#F50743",command=alterAddFK)
boton11.place(x=600,y=200)
boton11.config(width=13, height=1)
boton12 = Button(raiz, text="alterAddIndex", activebackground="#F50743",command=alterAddIndex)
boton12.place(x=700,y=200)
boton12.config(width=13, height=1)
boton13 = Button(raiz, text="alterTable", activebackground="#F50743",command=alterTable)
boton13.place(x=800,y=200)
boton13.config(width=13, height=1)
boton14 = Button(raiz, text="alterAddColumn", activebackground="#F50743",command=alterAddColumn)
boton14.place(x=900,y=200)
boton14.config(width=13, height=1)
boton15 = Button(raiz, text="alterDropColumn", activebackground="#F50743",command=alterDropColumn)
boton15.place(x=1000,y=200)
boton15.config(width=13, height=1)
boton16 = Button(raiz, text="dropTable", activebackground="#F50743",command=dropTable)
boton16.place(x=600,y=250)
boton16.config(width=13, height=1)
boton17 = Button(raiz, text="insert", activebackground="#F50743",command=insert)
boton17.place(x=700,y=250)
boton17.config(width=13, height=1)
boton18 = Button(raiz, text="loadCSV", activebackground="#F50743",command=loadCSV)
boton18.place(x=800,y=250)
boton18.config(width=13, height=1)
boton19 = Button(raiz, text="extractRow", activebackground="#F50743",command=extractRow)
boton19.place(x=900,y=250)
boton19.config(width=13, height=1)
boton20 = Button(raiz, text="extractRangeTable", activebackground="#F50743",command=extractRangeTable)
boton20.place(x=1000,y=250)
boton20.config(width=13, height=1)

BotonEjecutar = Button(raiz, text="Ejecutar Base de datos", activebackground="#F50743",command=EjecutarBD)
BotonEjecutar.place(x=600,y=500)

BotonVer = Button(raiz, text="Ver Base de datos", activebackground="#F50743",command=VBD)
BotonVer.place(x=750,y=500)


#Menu de acciones
menubar.add_command(label = "Nuevo", command = nuevoA)
menubar.add_command(label = "Abrir", command = Abrir)
menubar.add_command(label = "Guardar", command=guardarU)
menubar.add_command(label = "Guardar Como", command=Guardarcomo)
menubar.add_command(label = "Saber mas", command=Datos)
menubar.add_command(label = "Salir", command = raiz.quit)

#bucle de la aplicacion
raiz.mainloop()




