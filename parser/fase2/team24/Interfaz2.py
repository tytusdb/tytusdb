#IMPORTS
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import grammar2 as g
from variables import tabla as ts
from reportAST import *
from reportError import *
from reportBNF import *
from reportTable import *
import prettytable as pt
import os
from reportBNF import *
import webbrowser as wb
import OptimizarMirilla as optm
import OptimizarObjetos as optobj
# Esta es la lista de objetos
from procedural import objopt



def analiz(input):
    raiz = g.parse(input)
    results = []
    executeGraphTree(raiz)
    for val in raiz:
        res = val.ejecutar()
        if isinstance(res,CError):
            results.append("Error "+ res.tipo+". Descripcion: " +res.descripcion)
        else:
            results.append( res)
    graphTable(ts)
    report_errors()
    report_BNF()
    return results

def traducir(input):
    global STACK_INSTRUCCIONES
    STACK_INSTRUCCIONES = str(input).split(';')
    raiz = g.parse(input)
    results = []
    for val in raiz:
        res = val.traducir()
        if isinstance(res, CError):
            print('')
        else:
            results.append(res)
    return results
root = Tk()
cont = 1

"""PROPIEDADES DE LA VENTANA"""
root.geometry("1100x650")
root.title("[OLC2]Fase 1")
root.configure(bg='grey')

"""FUNCIONES MENU"""
ruta = ""
nombrearchivo = ""
def Salir():
    root.quit()
def AcercaDe():
    messagebox.showinfo("Acerca de [OLC2]Fase 1", "Organización de Lenguajes y Compiladores 2")
def Abrir():
    global ruta
    global nombrearchivo
    ruta = filedialog.askopenfilename(title="Seleccionar Archivo", filetypes=(("Todos los archivos","*.*"),("Archivos txt","*.txt")))
    nombrearchivo=os.path.basename(ruta)
    try:
        archivo = open(ruta,"r")
        texto.delete('1.0',END)
        contenido = archivo.read()
        texto.insert(END,contenido)
        archivo.close()
    except:
        print("ERROR")
def Guardar():
    global ruta
    cont = texto.get("1.0",END)
    try:
        archivo = open(ruta,"w")
        archivo.write(cont)
        archivo.close()
    except:
        print("Error al guardar archivo")
def GuardarComo():
    global ruta
    ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Todos los archivos","*.*"),("Archivos txt","*.txt")))
    cont = texto.get("1.0",END)
    try:
        archivo = open(ruta,"w")
        archivo.write(cont)
        archivo.close()
    except:
        print("Error al guardar como archivo")
    return
def LimpiarTexto():
    texto.delete('1.0',END)
def LimpiarConsola():
    consola.delete('1.0',END)
    global cont
    cont = 1

def Analizar():
    results = analiz(texto.get("1.0", "end-1c"))
    global cont
    for res in results:
        consola.insert(str(float(cont)), res)
        if isinstance(res,pt.PrettyTable):
            cont += (res.get_string().count('\n')+2)
        else:
            cont += (res.count('\n')+2)
        consola.insert(str(float(cont)), '\n')

def Analizar2(texto: str):
    results = traducir(texto)
    global cont
    for res in results:
        #consola.insert(str(float(cont)), res)
        #print(str(float(cont)), res)
        if isinstance(res,pt.PrettyTable):
            cont += (res.get_string().count('\n')+2)
        else:
            cont += (res.count('\n')+2)
        #consola.insert(str(float(cont)), '\n')
        consola.insert(str(float(cont)), res)
        print(str(float(cont)), res)


# def para escribir el archivo de 3d y mostrarlo en la interfaz
def escribir3D(entrada):
    global objopt
    a = open("c3d.py", "w")
    a.write('''
from datetime import date
from variables import tabla as ts
from variables import NombreDB 
from variables import cont 
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt
from reportTable import *
    
    
pila = []
for i in range(100):
    pila.append(i)
    
def ejecutar():
\tglobal cont
\tglobal ts
\tNombreDB = ts.nameDB
\n''')

    input = entrada
    raiz = g.parse(input)
    results = []
    res =''
    #executeGraphTree(raiz)
    for val in raiz:
        res += val.traducir()
        #pass
    a.write(res)

    a.write('\tgraphTable(ts)\n')
    for fa in g.funciones:
        a.write(fa)

    a.write('''ejecutar()''')
    a.close()
    f = open('c3d.py', 'r')
    file_contents = f.read()
    consola.insert(str(float(0)), file_contents)
    #PARA OPTIMIZACION
    optm.Optimizador(objopt).ejecutar()

def Traducir():
    escribir3D(texto.get("1.0", "end-1c"))
def AbrirAST():
    wb.open_new(r'tree.gv.pdf')
def AbrirBNF():
    wb.open_new(r'reporteBNF.gv.pdf')
def AbrirErrores():
    wb.open_new(r'reporteErrores.gv.pdf')
def AbrirTablaSimbolos():
    wb.open_new(r'reporteTabla.gv.pdf')


"""CREACION DE COMPONENTES GRAFICOS"""
BarraMenu=Menu(root)

root.config(menu=BarraMenu)
MenuArchivo= Menu(BarraMenu, tearoff=0)
MenuArchivo.add_command(label="Arbrir",command=Abrir)
MenuArchivo.add_command(label="Guardar",command=Guardar)
MenuArchivo.add_command(label="Guardar Como...",command=GuardarComo)
MenuArchivo.add_separator()
MenuArchivo.add_command(label="Salir", command=Salir)
BarraMenu.add_cascade(label="Archivo", menu=MenuArchivo)

MenuEditar= Menu(BarraMenu, tearoff=0)
MenuEditar.add_command(label="Limpiar Consola",command=LimpiarConsola)
MenuEditar.add_command(label="Limpiar Texto",command=LimpiarTexto)
BarraMenu.add_cascade(label="Editar", menu=MenuEditar)

MenuAnalizador= Menu(BarraMenu, tearoff=0)
MenuAnalizador.add_command(label="Ejecutar Analisis",command=Analizar)
MenuAnalizador.add_command(label="Traducir a 3D",command=Traducir)
BarraMenu.add_cascade(label="Analizar", menu=MenuAnalizador)

MenuReportes= Menu(BarraMenu, tearoff=0)
BarraMenu.add_cascade(label="Reportes", menu=MenuReportes)
MenuReportes.add_command(label="AST", command=AbrirAST)
MenuReportes.add_command(label="BNF", command=AbrirBNF)
MenuReportes.add_command(label="Errores", command=AbrirErrores)
MenuReportes.add_command(label="Tabla Simbolos",command=AbrirTablaSimbolos)

MenuAyuda= Menu(BarraMenu, tearoff=0)
MenuAyuda.add_command(label="Acerca de...",command=AcercaDe)
BarraMenu.add_cascade(label="Ayuda", menu=MenuAyuda)

lblanalizador = Label(root,text="Area del Analizador",bg='grey')
texto = scrolledtext.ScrolledText(root, height=35, width=80,borderwidth=1,wrap="none")
textHsb = Scrollbar(root, orient="horizontal", command=texto.xview)
texto.configure(xscrollcommand=textHsb.set)

lblconsola = Label(root,text="Area de la consola",bg='grey')
consola = scrolledtext.ScrolledText(root, height=35, width=50,bg="black",fg="#bbd500",borderwidth=1,wrap="none")
consolaHsb = Scrollbar(root, orient="horizontal", command=consola.xview)
consola.configure(xscrollcommand=consolaHsb.set)

"""COLOCACION DE COMPONENTES"""
lblanalizador.grid(row=1,column=0)
lblconsola.grid(row=1,column=1)
texto.grid(row=2,column=0)
textHsb.grid(row=3, column=0, sticky="ew")
consola.grid(row=2,column=1)
consolaHsb.grid(row=3, column=1, sticky="ew")

"""INICIA EJECUCION DE LA VENTANA"""
root.mainloop()