from tkinter import * #importando tkinter

##################################FUNCIONES#################################
def openFile():
    print("hola")

def analisis():
    print("hola")

def errores():
    print("hola")

def tabla():
    print("hola")

def ast():
    print("hola")

def gramatica():
    print("hola")

def guardar():
    print("hola")

def ayuda():
    print("hola")
#root
################################Configuracion#################################
root = Tk()
root.title("TytusDB_Manager")#titulo 
root.resizable(0,0)
root.geometry("1300x700")#ajustar tamaño
root.config(bg="black", cursor="pirate")
###############################Barra menú#####################################
barra = Menu(root)
root.config(menu=barra, width=300, height=300)

archivoMenu = Menu(barra, tearoff=0)
archivoMenu.add_command(label="Abrir", command=openFile)
archivoMenu.add_command(label="Guardar", command=guardar)
barra.add_cascade(label="Archivo", menu=archivoMenu)

herramientaMenu=Menu(barra, tearoff=0)
herramientaMenu.add_command(label="Ejecutar Analisis", command=analisis)
barra.add_cascade(label="Analisis", menu=herramientaMenu)

reporteMenu = Menu(barra, tearoff=0)
reporteMenu.add_command(label="Reporte errores", command=errores)
reporteMenu.add_command(label="Tabla de simbolos", command=tabla)
reporteMenu.add_command(label="Reporte AST", command=ast)
reporteMenu.add_command(label="Reporte Gramatical", command=gramatica)
barra.add_cascade(label="Reportes", menu=reporteMenu)

ayudaMenu=Menu(barra, tearoff=0)
ayudaMenu.add_command(label="Ayuda", command=ayuda)
barra.add_cascade(label="Ayuda", menu=ayudaMenu)
##################################EDITOR DE CODIGO#############################
editor = Text(root, width=122, height=40, bg="white")
editor.place(x=300, y=20)

root.mainloop() #mostrar interfaz