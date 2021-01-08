from tkinter import * #importando tkinter
import tkinter as TK
import gramatica as g

import gramaticaF2 as g2

import Utils.TablaSimbolos as table
import Utils.Lista as l
import Librerias.storageManager.jsonMode as storage
from tkinter.filedialog import askopenfilename as files
import os
import webbrowser
from Utils.fila import fila
from Error import *
import Instrucciones.DML.select as select
import json
import reporte as reporte
import optimizar as opt
#from select import *

##########################################################################

storage.dropAll()
datos = l.Lista({}, '')

##################################FUNCIONES#################################
def openFile():
    route = files(
        filetypes=[("TXT Files", "*.txt")]
    )
    if not route:
        salida.insert("end", "\nERROR AL ABRIR AL ARCHIVO")
        return
    editor.delete("1.0", TK.END)
    with open(route, "r") as input_file:
        text = input_file.read()
        editor.insert(TK.END, text)
    root.title(f"TYTUSDB_Parser - {route}")



def analisis():
    global datos

    salida.delete("1.0", "end")
    texto = editor.get("1.0", "end")

    #g2.tempos.restartTemp() #reinicia el contador de temporales.
    prueba = g2.parse(texto)
    try:
        escribirEnSalidaFinal(prueba['printList'])
    except:
        ''
    #print(prueba['text'])
    try:
        exepy = '''
#imports
import sys
sys.path.append('../G26/Librerias/goto')

from goto import *
import gramatica as g
import Utils.Lista as l
import Librerias.storageManager.jsonMode as storage
import Instrucciones.DML.select as select
from Error import *
import reporte as reporte

#storage.dropAll()

heap = []
semerrors = []
erroresS = list()

datos = l.Lista({}, '')
l.readData(datos)
'''
        exepy += '''
#funcion intermedia
def mediador(value):
    global heap
    global semerrors
    global reporte
   # Analisis sintactico
    instrucciones = g.parse(heap.pop())
    erroresS = (g.getMistakes())

    for instr in instrucciones['ast'] :
        if instr == None:
            erroresS = g.getMistakes()
            return 0
        try:
            val = instr.execute(datos)
        except:
            val = (instr.execute(datos, {}))

        if isinstance(val, Error):
            'error semantico'
            print(val)
            semerrors.append(val)
        elif isinstance(instr, select.Select) :

            if value == 0:
                try:
                    print(val)
                    if len(val.keys()) > 1 :
                        print('El numero de columnas retornadas es mayor a 1')
                        return 0
                    for key in val:
                        if len(val[key]['columnas']) > 1 :
                            print('El numero de filas retornadas es mayor a 1')
                        else :
                            return val[key]['columnas'][0][0]
                        break
                except:
                    return 0
            else:
                print(instr.ImprimirTabla(val))
        else :
            try:
                return val.val
            except:
                print(val)

    l.writeData(datos)
'''

        exepy += '''
#funciones de plg-sql


'''
        l.readData(datos)
        optt = ""
        for val in datos.tablaSimbolos.keys():
            if val == 'funciones_':
                for func in datos.tablaSimbolos[val]:
                    try:
                        f = open("./Funciones/" + func['name'] + ".py", "r")
                        pruebaaa = f.read()
                        optt = opt.optimizar(pruebaaa)
                        exepy += optt
                        f.close()
                    except:
                        exepy += '#Se cambio el nombre del archivo que guarda la funcion. Funcion no encontrada'
        exepy += '''
#main
@with_goto
def main():
    global heap
'''

        exepy += str(prueba['text'])
        exepy += '''
    reporte.Rerrores(erroresS, semerrors, "Reporte_Errores_Semanticos.html")

#Ejecucion del main
if __name__ == "__main__":
    main()
'''

        f = open("./c3d.py", "w")
        f.write(exepy)
        f.close()


        l.readData(datos)
        if 'funciones_' in datos.tablaSimbolos:
            for funciones in datos.tablaSimbolos['funciones_']:
                #print(funciones)
                if funciones['drop'] == 0:
                    try:
                        os.remove('../G26/Funciones/' + funciones['name'] +'.py')
                    except:
                        ''



        try:
           reporte.hacerReporteGramatica(prueba['reporte'])
           errores = g2.getMistakes()
           recorrerErrores(errores)
           reporte.Rerrores(errores, [], "Reporte_Errores_Sintactico_Lexicos.html")
           reporte.reporteTabla(datos)
        except:
           ''

        escribirEnSalidaFinal('Se ha generado el codigo en 3 direcciones.')
        #aqui se puede poner o llamar a las fucniones para imprimir en la consola de salida
        reptOpti = prueba['opt']
        fro = open("./Reportes/ReporteOptimizacion.txt", "w")
        fro.write(reptOpti)
        fro.close()
    except:
        print("No se ha podido generar el codigo ya que existen errores sintacticos")
        escribirEnSalidaFinal("No se ha podido generar el codigo ya que existen errores sintacticos")

try:
    l.readData(datos)
    reporte.reporteTabla(datos)
except:
    ''

def tabla():
    ruta = ".\\Reportes\\Reporte_TablaSimbolos.html"
    webbrowser.open(ruta)

def ast():
    g2.grafo.showtree()

def gramatica():
    os.system("notepad   ./Reportes/GramaticaAutomatica.md")

def guardar():
    print("hola")

def ayuda():
    print("hola")

def mistakes():
    ruta = ".\\Reportes\\Reporte_Errores.html"
    webbrowser.open(ruta)

def recorrerErrores(errores):
    salidaE = ""
    for error in errores:
        salidaE += error.toString() + "\n"
    salida.insert("1.0", salidaE)




def escribirEnSalidaInicio(texto): #borra lo que hay y escribe al inicio
    salida.insert("1.0", texto)

def escribirEnSalidaFinal(texto): # no borra y escribe al final de lo que ya estaACTIVE
    text = texto + "\n"
    salida.insert("end", text)
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
reporteMenu.add_command(label="Reporte errores", command=mistakes)
reporteMenu.add_command(label="Tabla de simbolos", command=tabla)
reporteMenu.add_command(label="Reporte AST", command=ast)
reporteMenu.add_command(label="Reporte Gramatical", command=gramatica)
barra.add_cascade(label="Reportes", menu=reporteMenu)

ayudaMenu=Menu(barra, tearoff=0)
ayudaMenu.add_command(label="Ayuda", command=ayuda)
barra.add_cascade(label="Ayuda", menu=ayudaMenu)
##################################EDITOR DE CODIGO#############################
nombreL=Label( root, text="EDITOR", fg="BLUE", font=("Arial", 12))
nombreL.place(x=300, y=10)
editor = Text(root, width=122, height=18, bg="white")
editor.place(x=300, y=45)

nombreL=Label( root, text="SALIDA", fg="BLUE", font=("Arial", 12))
nombreL.place(x=300, y=350)
salida = Text(root, width=122, height=18, bg="skyblue")
salida.place(x=300, y=380)


root.mainloop() #mostrar interfaz
