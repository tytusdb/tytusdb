import tkinter as tk
from tkinter import Menu, Tk, Text, DISABLED, RAISED,Frame, FLAT, Button, Scrollbar, Canvas, END
from tkinter import messagebox as MessageBox
from tkinter import ttk

from campo import Campo
from arbol import Arbol

import http.client
formularios=[]
textos=[]
control=0
notebook= None
#Metodo GET para probar peticiones al servidor
def myGET():
    myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)

    headers = {
        "Content-type": "text/plain"
    }

    myConnection.request("GET", "/data/database.tytus", "", headers)
    response = myConnection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))
    myData = response.read()
    print(myData.decode("utf-8") )
    myConnection.close()

#Metodo POST para probar peticiones al servidor
def myPOST():
    myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)

    headers = {
        "Content-type": "text/plain"
    }

    postData = "Test http.server from http.client :D"

    myConnection.request("POST", "/", postData, headers)
    response = myConnection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))
    myData = response.read()
    print(myData.decode("utf-8") )
    myConnection.close()   


def CrearMenu(masterRoot):

    ########### menu ############
    #Se crea la barra
    barraDeMenu=Menu(masterRoot, tearoff=0,relief=FLAT, font=("Verdana", 12),activebackground='red')
    #Se crean los menus que se deseen
    archivo=Menu(barraDeMenu, tearoff=0)
    #Crear las opciones de la opción del menú
    #Se elimino el comando de crear Ventana por problemas con las imagenes

    archivo.add_command(label="Nueva ventana")
    archivo.add_command(label="Abrir un documento",command=abrirDoc)
    archivo.add_command(label="Abrir un modelo")
    archivo.add_separator()
    archivo.add_command(label="Nueva Query",command=añadir)
    archivo.add_command(label="Guardar como...")
    archivo.add_command(label="Guardar")
    archivo.add_separator()
    archivo.add_command(label="Salir")

    #creando el Editar
    editar=Menu(barraDeMenu, tearoff=0)
    #agregando su lista
    editar.add_command(label="Cortar")
    editar.add_command(label="Pegar")
    editar.add_command(label="Copiar")
    editar.add_separator()
    editar.add_command(label="Seleccionar todo")
    editar.add_command(label="Formato")
    editar.add_command(label="Preferencias")

    #se agrega Tools
    tools=Menu(barraDeMenu, tearoff=0)
    #se agrega su lista
    tools.add_command(label="Configuración")
    tools.add_command(label="Utilidades")
    #Temporary tools to test client-server connection
    tools.add_command(label="SELECT (GET)", command = myGET)
    tools.add_command(label="CREATE (POST)", command = myPOST)
    

    #se agrega ayuda
    ayuda=Menu(barraDeMenu, tearoff=0)
    #lista de ayuda
    ayuda.add_command(label="Documentación de TytuSQL")
    ayuda.add_command(label="Acerca de TytuSQL")

    #Se agrgan los menús a la barra
    barraDeMenu.add_cascade(label="Archivo",menu=archivo)
    barraDeMenu.add_cascade(label="Editar",menu=editar)
    barraDeMenu.add_cascade(label="Herramientas",menu=tools)
    barraDeMenu.add_cascade(label="Ayuda",menu=ayuda)
    #Se indica que la barra de menú debe estar en la ventana
    return barraDeMenu

def abrirDoc():
    MessageBox.showinfo(title="Aviso",message="Hizo clic en abrir documento")

def CrearVentana():
    raiz = Tk()
    #Configuracion de ventana
    raiz.title("TytuSQL") #Cambiar el nombre de la ventana
    #raiz.iconbitmap('resources/icon.ico')
    raiz.rowconfigure(0, minsize=800, weight=1)
    raiz.columnconfigure(1, minsize=800, weight=1)
    raiz.config(menu=CrearMenu(raiz), background='silver')

    #Frame del Arbol
    FrameIzquiero = Frame(raiz, relief=RAISED, bd=2)
    FrameIzquiero.pack(side="left", fill="both")
    #Se llama a la clase Arbol
    Arbol(FrameIzquiero)

    #Boton para realizar consulta
    Button(raiz, text="Enviar Consulta").pack(side="top",fill="both")

    #Consola de Salida
    consola = Text(raiz)
    consola.pack(side="bottom",fill="both")
    consola.insert(1.0,"Consola de Salida")
    consola.config(state=DISABLED)

    ###### CREAMOS EL PANEL PARA LAS PESTAÑAS ########
    global notebook
    notebook=ttk.Notebook(raiz)
    notebook.pack(side="right", fill="both", expand=True)
    añadir()
    raiz.mainloop()

def añadir():
    global control
    global notebook
    titulo="Nuevo_" + str(control)
    formularios.append(Frame(notebook,bg="white"))
    contador=control
    notebook.add(formularios[contador], text=titulo)
    textos.append(Campo(formularios[contador]).pack(side="right", fill="both", expand=True))
    contador=control+1
    control=contador
  #  b= notebook.select() 
  #  a=notebook.index(b)
  #  print(a)

def main():
    CrearVentana()
if __name__ == "__main__":
    main()
