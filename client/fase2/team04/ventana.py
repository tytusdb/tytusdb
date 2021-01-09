import tkinter as tk
from tkinter import Menu, Tk, Text, WORD, DISABLED, NORMAL, RAISED,Frame, FLAT, Button, Scrollbar, Canvas, END, Entry, Label
from tkinter import messagebox as MessageBox
from tkinter import ttk,filedialog, INSERT, PhotoImage
import os
import pathlib
from campo import Campo, MyDialog
from arbol import Arbol
import http.client
import json

formularios=[]
textos=[]
control=0
notebook= None
consola = None
bases = None
raiz = None
tools = None
loginOn = False
jsonTree = None
jsonDB = None
myQuery = ""
_words=None
#Variables para simular credenciales
ActiveUsername = ""
ActivePassword = ""

#Metodo GET para probar peticiones al servidor
def myGET():
    myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)

    headers = {
        "Content-type": "application/json"
    }

    myConnection.request("GET", "/getUsers", "", headers)
    response = myConnection.getresponse()
    global consola
    print("GET: Status: {} and reason: {}".format(response.status, response.reason))
    if response.status == 200:       
        data = response.read()   
        consola.config(state=NORMAL)
        consola.insert(INSERT,"\n" + data.decode("utf-8"))
        consola.config(state=DISABLED)
    else:
        consola.config(state=NORMAL)
        consola.insert(INSERT,"\nHa ocurrido un error.")
        consola.config(state=DISABLED)
    myConnection.close()

#Metodo GET para leer json con bases de datos existentes
def getDatabases():

    global jsonTree
    global jsonDB

    myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)

    headers = {
        "Content-type": "application/json"
    }

    myConnection.request("GET", "/getDatabases", "", headers)
    response = myConnection.getresponse()
    print("GET: Status: {} and reason: {}".format(response.status, response.reason))
    if response.status == 200:       
        data = response.read()
        resData = json.loads(data.decode("utf-8"))
        #Variable global jsonTree tiene el contenido (string) del json en tabla.txt
        jsonTree = resData["jsonText"]
        #Variable global jsonDB tiene el contenido (string) del json databases
        jsonDB = resData["databases"]   
    myConnection.close()

#Metodo POST para crear usuarios
def crearUsuario():
    global raiz
    d = MyDialog(raiz)
    if d.accept is True:
        newUsername = d.result[0]
        newPassword = d.result[1]

        if not "".__eq__(newUsername) and not "".__eq__(newPassword):
            #Data en formato json
            jsonData = { "username": newUsername, "password": newPassword }
            myJson = json.dumps(jsonData)

            myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)

            headers = {
                "Content-type": "application/json"
            }

            myConnection.request("POST", "/createUser", myJson, headers)
            response = myConnection.getresponse()
            print("POST: Status: {} and reason: {}".format(response.status, response.reason))
            if response.status == 200:       
                data = response.read()
                result = data.decode("utf-8")
                consola.config(state=NORMAL)
                if result == "false":
                    consola.insert(INSERT,"\nUsuario creado correctamente.")
                else:
                    consola.insert(INSERT,"\nUsuario ya existe actualmente, intente con otro username.")
                consola.config(state=DISABLED)
            else:
                consola.config(state=NORMAL)
                consola.insert(INSERT,"\nHa ocurrido un error.")
                consola.config(state=DISABLED)
            myConnection.close()
        else:
            MessageBox.showerror("Error", "Es necesario llenar ambos campos!")

#Metodo POST para enviar un query!
def enviarQuery():

    global myQuery
    global notebook
    global textos
    global jsonTree
    global jsonDB
    global bases

    idx = 0
    if notebook.select():
        idx = notebook.index('current')

    myQuery = textos[idx].text.get(1.0, END)
    myQuery = myQuery[:-1]

    jsonData = { "text": myQuery }
    myJson = json.dumps(jsonData)

    myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)

    headers = {
        "Content-type": "application/json"
    }

    myConnection.request("POST", "/runQuery", myJson, headers)
    response = myConnection.getresponse()
    print("POST: Status: {} and reason: {}".format(response.status, response.reason))
    if response.status == 200:       
        data = response.read()
        resData = json.loads(data.decode("utf-8"))
        result = resData["consola"]
        jsonTree = resData["jsonText"]
        jsonDB = resData["databases"]
        consola.config(state=NORMAL)
        consola.insert(INSERT,"\n{}".format(result))
        consola.config(state=DISABLED)
        bases.entregado(jsonDB)

    else:
        consola.config(state=NORMAL)
        consola.insert(INSERT,"\nHa ocurrido un error.")
        consola.config(state=DISABLED)
    myConnection.close()

def changeToLogout():
    global tools
    global loginOn
    loginOn = True
    tools.entryconfig(5, label="LOGOUT")

def changeToLogin():
    global tools
    global loginOn
    loginOn = False
    tools.entryconfig(5, label="LOGIN")

def LimpiarConsola():
    global consola
    consola.config(state=NORMAL)
    consola.delete("1.0", tk.END)
    consola.insert(1.0,"Consola de Salida:")
    consola.config(state=DISABLED)

def LogIn():
    ###ventana para el log
    global raiz
    global loginOn
    global ActiveUsername
    global bases
    global jsonDB
    if loginOn is False:
        d = MyDialog(raiz)
        if d.accept is True:
            myUsername = d.result[0]
            myPassword = d.result[1]
            
            if not "".__eq__(myUsername) and not "".__eq__(myPassword):
                myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)

                headers = {
                    "Content-type": "application/json"
                }

                #Data en formato json
                jsonData = { "username": myUsername, "password": myPassword }
                myJson = json.dumps(jsonData)

                myConnection.request("POST", "/checkLogin", myJson, headers)
                response = myConnection.getresponse()
                global consola
                print("POST: Status: {} and reason: {}".format(response.status, response.reason))
                if response.status == 200:       
                    data = response.read()
                    result = data.decode("utf-8")
                    consola.config(state=NORMAL)
                    if result == "true":
                        ActiveUsername = myUsername
                        consola.insert(INSERT,"\nUsuario " + ActiveUsername + " loggeado correctamente.")
                        changeToLogout()
                        getDatabases()
                        bases.entregado(jsonDB)
                    else:
                        consola.insert(INSERT,"\nDatos invalidos o usuario inexistente.")
                    consola.config(state=DISABLED)
                else:
                    consola.config(state=NORMAL)
                    consola.insert(INSERT,"\nHa ocurrido un error.")
                    consola.config(state=DISABLED)
                myConnection.close()
            else:
                MessageBox.showerror("Error", "Es necesario llenar ambos campos!")
    else:
        changeToLogin()
        consola.config(state=NORMAL)
        consola.insert(INSERT,"\nUsuario " + ActiveUsername + " ha cerrado sesión exitosamente.")
        consola.config(state=DISABLED)

def CrearMenu(masterRoot):
    global tools
    ########### menu ############
    #Se crea la barra
    barraDeMenu=Menu(masterRoot, tearoff=0,relief=FLAT, font=("Verdana", 12),activebackground='gray59')
    barraDeMenu.config(bg='gray21',fg='white')
    #Se crean los menus que se deseen
    archivo=Menu(barraDeMenu, tearoff=0,bg='gray21',fg='white',activebackground='gray59')
    #Crear las opciones de la opción del menú
    #Se elimino el comando de crear Ventana por problemas con las imagenes

    archivo.add_command(label="Nueva ventana")
    archivo.add_command(label="Abrir query",command=abrir)
    archivo.add_command(label="Abrir un modelo")
    archivo.add_separator()
    archivo.add_command(label="Nueva Query",command=lambda: añadir('Nuevo'))
    archivo.add_command(label="Guardar como...",command=guardarComo)
    archivo.add_command(label="Guardar",command=guardarArchivo)
    archivo.add_command(label="Cerrar pestaña actual",command=cerrarPestaña)
    archivo.add_separator()
    archivo.add_command(label="Salir",command=cerrarVentana)

    #creando el Editar
    editar=Menu(barraDeMenu,tearoff=0,bg='gray21',fg='white',activebackground='gray59')
    #agregando su lista
    editar.add_command(label="Cortar")
    editar.add_command(label="Pegar")
    editar.add_command(label="Copiar")
    editar.add_separator()
    editar.add_command(label="Seleccionar todo")
    editar.add_command(label="Formato")
    editar.add_command(label="Preferencias")

    #se agrega Tools
    tools=Menu(barraDeMenu, tearoff=0,bg='gray21',fg='white',activebackground='gray59')
    #se agrega su lista
    tools.add_command(label="Configuración")
    tools.add_command(label="Utilidades")
    tools.add_command(label="Limpiar consola", command = LimpiarConsola)
    #Temporary tools to test client-server connection
    tools.add_command(label="GET USERS", command = myGET)
    tools.add_command(label="CREATE USER", command = crearUsuario)
    #Log In sera parte de la barra de herramientas
    tools.add_command(label="LOGIN", command = LogIn)
    tools.add_command(label="Actualizar", command = actualizar)

    #se agrega ayuda
    ayuda=Menu(barraDeMenu, tearoff=0,bg='gray21',fg='white',activebackground='gray59')
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

def actualizar():
    global bases
    getDatabases()
    bases.entregado(jsonDB)

def abrir():
    global archivo
    global notebook
    global control
    archivo = filedialog.askopenfilename(title = "Abrir Archivo")
    if archivo != '':
        name = os.path.basename(archivo)
        añadir(name)
        pathlib.Path(archivo).suffix
        entrada = open(archivo, encoding="utf-8")
        content = entrada.read()
        textos[control-1].text.insert(tk.INSERT, content)
        entrada.close()
        notebook.select(control-1)

def guardarArchivo():
    global archivo
    idx = 0
    if notebook.select():
        idx = notebook.index('current')
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w", encoding="utf-8")
        guardarc.write(textos[idx].text.get(1.0, END))
        guardarc.close()

def guardarComo():
    global archivo
    global notebook
    idx = 0
    if notebook.select():
        idx = notebook.index('current')
    guardar = filedialog.asksaveasfilename(title = "Guardar Archivo")
    if guardar != '':
        fguardar = open(guardar, "w+", encoding="utf-8")
        fguardar.write(textos[idx].text.get(1.0, END))
        fguardar.close()
        archivo = guardar

def CrearVentana():
    global raiz
    raiz = Tk()
    #Configuracion de ventana
    raiz.title("TytuSQL") #Cambiar el nombre de la ventana
    #raiz.iconbitmap('resources/icon.ico')
    raiz.configure(bg='gray21')
    raiz.rowconfigure(0, minsize=800, weight=1)
    raiz.columnconfigure(1, minsize=800, weight=1)
    raiz.config(menu=CrearMenu(raiz), background='silver')
    #Frame del Arbol
    FrameIzquiero = Frame(raiz, relief=RAISED, bd=2, bg='gray21')
    FrameIzquiero.pack(side="left", fill="both")
    #Se llama a la clase Arbol
    global bases
    bases = Arbol(FrameIzquiero)
    #Boton para realizar consulta
    Button(raiz, text="Enviar Consulta",bg='gray',fg='white',activebackground='slate gray', command = enviarQuery).pack(side="top",fill="both")
    #Consola de Salida
    global consola
    consola = Text(raiz,bg='gray7',fg='white',selectbackground="gray21")
    #inactiveselectbackground="green"
    consola.pack(side="bottom",fill="both")
    consola.insert(1.0,"Consola de Salida:")
    consola.config(wrap=WORD)
    consola.config(state=DISABLED)
    ###### CREAMOS EL PANEL PARA LAS PESTAÑAS ########
    global notebook
    global control
    global textos
    global _words
    style = ttk.Style()
    style.theme_use("classic")
    style.configure("TNotebook.Tab", background="gray21", font="helvetica 14",foreground='white')
    style.map("TNotebook.Tab", background = [("selected", "slate gray")])
    notebook=ttk.Notebook(raiz)
    notebook.pack(side="right", fill="both", expand=True)
    añadir('Nuevo')
    
    b=notebook.select()
    a=notebook.index(b)
    textos[a].text.bind("<KeyRelease>",Spellcheck)
    textos[a].text.bind("<Key>", Spellcheck)
    # initialize the spell checking dictionary. YMMV.
    _words=open("clave").read().split("\n")
    raiz.mainloop()



def añadir(titulo):
    global consola
    global control
    global notebook
    global textos
    if control > 0:
        consola.config(state=NORMAL)
        consola.insert(INSERT,"\nSe creo una nueva Pestaña")
        consola.config(state=DISABLED)
    formularios.append(Frame(notebook,bg="white"))
    contador=control
    notebook.add(formularios[contador], text=titulo)
    valor=Campo(formularios[contador])
    valor.pack(side="left", fill="both",expand=True)
    vsb=Scrollbar(formularios[contador],orient="vertical",command=valor.text.yview)
    valor.text.configure(yscrollcommand=vsb.set,bg='gray49',fg='white',font="helvetica 12")
    vsb.pack(side="right",fill="y")
    textos.append(valor)
    contador=control+1
    control=contador
    b=notebook.select()
    a=notebook.index(b)
    textos[control-1].text.bind("<KeyRelease>", Spellcheck)
    textos[control-1].text.bind("<Key>", Spellcheck)
    

def Spellcheck(self):
    global notebook
    global control
    global textos
    global _words
    b=notebook.select()
    a=notebook.index(b)
    
    index = textos[a].text.search(r'\s', "insert", backwards=True, regexp=True)
    if index == "":
        index ="1.0"
    else:
        index = textos[a].text.index("%s+1c" % index)
    word =  textos[a].text.get(index, "insert")
    # print(word)
    if word in _words:
        textos[a].text.tag_add("reserve", index, "%s+%dc" % (index, len(word)))
    else:
        textos[a].text.tag_remove("reserve", index, "%s+%dc" % (index, len(word)))  

def cerrarPestaña():
    global notebook
    global control
    b=notebook.select()
    a=notebook.index(b)
    notebook.forget(a)

def cerrarVentana():
    global raiz
    raiz.destroy()

def main():
    CrearVentana()
if __name__ == "__main__":
    main()