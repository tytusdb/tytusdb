from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import ttk

import random




#Accciones de EDITOR
def nuevo():
    global ruta
    ruta=""
    texto.delete(1.0,"end")
def abrir():
    global ruta
    ruta = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(("Ficheros de texto", "*.sql"),),
        title="Abrir un fichero de texto")
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")

def guardar():
    if ruta !="":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
    else:
        guardar_como()
def guardar_como():
    global ruta
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".sql")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
    else:
        ruta = ""


def analisisAscendente(entrada):
    print('iniciar analisis Ascedente')

def analisisDescendente(entrada):
    print('iniciar Analisis Descendente')

def ejecutar(entrada):
    print('iniciar ejecucion')
    print(entrada);

def graficar():
    #enviar a llamar las funciones para genera la graficar
    print('graficar')
def generarbnf():
    print('generar bnf')

def generarReporte():
    print('generar Reporte')



#Construccion de EDitor

root =Tk()
root.title("SQL TYTUSDB")
#variables para tomar informacion de ventana
ancho, alto = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(ancho,alto))

#CREACION DE MENU   
mnprincipal = Menu(root)
flmenu = Menu(mnprincipal, tearoff=0)
flmenu.add_command(label="Nuevo", command=nuevo)
flmenu.add_command(label="Abrir", command=abrir)
flmenu.add_command(label="Guardar", command=guardar)
flmenu.add_command(label="Guardar como", command=guardar_como)
flmenu.add_separator()
flmenu.add_command(label="Salir", command=root.quit)

mnprincipal.add_cascade(label = "Analisis", menu = flmenu)

menuAnalisis = Menu(mnprincipal, tearoff=0)
menuAnalisis.add_command(label="Analisis Ascendente", command=lambda: analisisAscendente(texto.get("1.0",'end-1c')))
menuAnalisis.add_command(label="Analisis Descendente", command=lambda: analisisAscendente(texto.get("1.0",'end-1c')))
menuAnalisis.add_command(label="Ejecutar Instrucciones", command=lambda:ejecutar(texto.get("1.0",'end-1c')))
menuAnalisis.add_separator()
menuAnalisis.add_command(label="Salir", command=root.quit)

mnprincipal.add_cascade(label = "Analisis", menu = menuAnalisis)


menuReporte = Menu(mnprincipal, tearoff=0)
menuReporte.add_command(label="Generar AST(BNF)", command= lambda :generarbnf())
menuReporte.add_command(label="Generar Grafica", command=  lambda:graficar())
menuReporte.add_command(label="Generar Reporte(Tabla Errores)", command=lambda:generarReporte())
menuReporte.add_separator()
menuReporte.add_command(label="Salir", command=root.quit)

mnprincipal.add_cascade(label = "Reportes", menu = menuReporte)







#texto

texto = Text(root)
texto.pack(fill="both",expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))



root.config(menu=mnprincipal)

root.mainloop()





