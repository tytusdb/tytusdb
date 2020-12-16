#from Arquitectura árbol import preorden
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
    file = filedialog.askopenfilename(filetypes =[('Archivo HTML', '*.html'),('Archivo CSS', '*.css'),('Archivo ASM', '*.asm')])
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

def Anal(): #analiza
    print("Datos del grupo")
        
        
    


def guardarU():
    print("guardar")


    

def Guardarcomo():
    print("guardar como")


def Funciona1():
    print("funcion1")

    


##Configuracion de la parte visual
raiz.title("Base de datos con AVL")
raiz.geometry("1150x600")
raiz.config(bg="black")

#titulo
Titulo = Label(raiz, text="BASE DE DATOS GRUPO 6", font=("Impact",30))
Titulo.place(x=400,y=25)

##Botones para las funciones
boton1 = Button(raiz, text="FUNCION 1", activebackground="#F50743",command=Funciona1)
boton1.place(x=600,y=100)
boton2 = Button(raiz, text="FUNCION 2", activebackground="#F50743",command=Funciona1)
boton2.place(x=700,y=100)
boton3 = Button(raiz, text="FUNCION 3", activebackground="#F50743",command=Funciona1)
boton3.place(x=800,y=100)
boton4 = Button(raiz, text="FUNCION 4", activebackground="#F50743",command=Funciona1)
boton4.place(x=900,y=100)
boton5 = Button(raiz, text="FUNCION 5", activebackground="#F50743",command=Funciona1)
boton5.place(x=1000,y=100)
boton6 = Button(raiz, text="FUNCION 6", activebackground="#F50743",command=Funciona1)
boton6.place(x=600,y=150)
boton7 = Button(raiz, text="FUNCION 7", activebackground="#F50743",command=Funciona1)
boton7.place(x=700,y=150)
boton8 = Button(raiz, text="FUNCION 8", activebackground="#F50743",command=Funciona1)
boton8.place(x=800,y=150)
boton9 = Button(raiz, text="FUNCION 9", activebackground="#F50743",command=Funciona1)
boton9.place(x=900,y=150)
boton10 = Button(raiz, text="FUNCION 10", activebackground="#F50743",command=Funciona1)
boton10.place(x=1000,y=150)
boton11 = Button(raiz, text="FUNCION 11", activebackground="#F50743",command=Funciona1)
boton11.place(x=600,y=200)
boton12 = Button(raiz, text="FUNCION 12", activebackground="#F50743",command=Funciona1)
boton12.place(x=700,y=200)
boton13 = Button(raiz, text="FUNCION 13", activebackground="#F50743",command=Funciona1)
boton13.place(x=800,y=200)
boton14 = Button(raiz, text="FUNCION 14", activebackground="#F50743",command=Funciona1)
boton14.place(x=900,y=200)
boton15 = Button(raiz, text="FUNCION 15", activebackground="#F50743",command=Funciona1)
boton15.place(x=1000,y=200)
boton16 = Button(raiz, text="FUNCION 16", activebackground="#F50743",command=Funciona1)
boton16.place(x=600,y=250)
boton17 = Button(raiz, text="FUNCION 17", activebackground="#F50743",command=Funciona1)
boton17.place(x=700,y=250)
boton18 = Button(raiz, text="FUNCION 18", activebackground="#F50743",command=Funciona1)
boton18.place(x=800,y=250)
boton19 = Button(raiz, text="FUNCION 19", activebackground="#F50743",command=Funciona1)
boton19.place(x=900,y=250)
boton20 = Button(raiz, text="FUNCION 20", activebackground="#F50743",command=Funciona1)
boton20.place(x=1000,y=250)

BotonEjecutar = Button(raiz, text="Ejecutar Base de datos", activebackground="#F50743",command=Funciona1)
BotonEjecutar.place(x=600,y=500)

BotonVer = Button(raiz, text="Ver Base de datos", activebackground="#F50743",command=Funciona1)
BotonVer.place(x=750,y=500)


#Menu de acciones
menubar.add_command(label = "Nuevo", command = nuevoA)
menubar.add_command(label = "Abrir", command = Abrir)
menubar.add_command(label = "Guardar", command=guardarU)
menubar.add_command(label = "Guardar Como", command=Guardarcomo)
menubar.add_command(label = "Saber mas", command=Anal)
menubar.add_command(label = "Salir", command = raiz.quit)

#bucle de la aplicacion
raiz.mainloop()




