import tkinter as tk
from tkinter import Menu, Tk, Text, DISABLED, RAISED,Frame, FLAT, Button, Scrollbar, Canvas, END
from tkinter import messagebox as MessageBox
from tkinter import ttk,filedialog, INSERT
import os
import pathlib
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
    archivo.add_command(label="Abrir query",command=abrir)
    archivo.add_command(label="Abrir un modelo")
    archivo.add_separator()
    archivo.add_command(label="Nueva Query",command=lambda: añadir('Nuevo'))
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

def abrir():
    global archivo
    global notebook
    global control
    archivo = filedialog.askopenfilename(title = "Abrir Archivo")
    if archivo != '':
        name = os.path.basename(archivo)
        añadir(name)
        lenguaje = pathlib.Path(archivo).suffix
        entrada = open(archivo, encoding="utf-8")
        content = entrada.read()
        textos[control-1].text.insert(tk.INSERT, content)
        entrada.close()
        notebook.select(control-1)


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
    consola =  Text(raiz)
    consola.pack(side="bottom",fill="both")
    consola.insert(1.0,"Consola de Salida")
    consola.config(state=DISABLED)
    ###### CREAMOS EL PANEL PARA LAS PESTAÑAS ########
    global notebook
    global control
    notebook=ttk.Notebook(raiz)
    notebook.pack(side="right", fill="both", expand=True)
    añadir('Nuevo')
    raiz.mainloop()

def añadir(titulo):
    global control
    global notebook
    formularios.append(Frame(notebook,bg="white"))
    contador=control
    notebook.add(formularios[contador], text=titulo)
    valor=Campo(formularios[contador])
    valor.pack(side="left", fill="both",expand=True)
    vsb=Scrollbar(formularios[contador],orient="vertical",command=valor.text.yview)
    valor.text.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right",fill="y")
    textos.append(valor)
    contador=control+1
    control=contador


def main():
    CrearVentana()
if __name__ == "__main__":
    main()
