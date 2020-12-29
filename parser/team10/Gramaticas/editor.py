import os
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import ttk
import parse as lector
import parse2 as imgarbol
from tkinter import messagebox
import webbrowser as wb
import random
from mostrarConsulta import *
import funcionesTS as tabla
import conexionDB as conectar
import ejecucion as ejecutars
import parseGramatical as gramatical
import parserDescendente2 as descendp
from ReporteErrores import  *
from funcionesTS import *
import pruebaNumpy as pn



#variables globales
#Accciones de EDITOR
global resultado
ts2 = tabla.objTabla()
conect = conectar.FuncionesEdd(ts2)
newEJecucion = ejecutars.evaluacion(conect,ts2)
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

def salir():
    root.quit()
    print('salida')
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
    global resultado
    lectura = entrada.lower()
    resultado = lector.parse(lectura)
    imgarbol.parse(lectura)
    consola.config(state=DISABLED)
    messagebox.showinfo('Informacion','Se ha ejecutado el analisis')


def analisisDescendente(entrada):
    lectura = entrada.lower()
    descendp.parse(lectura)
    consola.config(state=DISABLED)
    # paths= str(os.getcwd())
    # nuevapath = paths+'\\graficaArbolDes.png'
    # wb.open_new(nuevapath)
    print('iniciar Analisis Descendente')

def ejecutar(entrada):
    global resultado

    consola.config(state=NORMAL)
    consola.delete('1.0', END)
    consola.config(state=DISABLED)
    
    newEJecucion.iniciar(resultado)
    actualizarAmbitos(newEJecucion.getTablaActual(),newEJecucion.getBaseActual())
    consola.config(state=NORMAL)
    consola.insert('insert',newEJecucion.imprimir)
    consola.config(state=DISABLED)

    consola.config(state=NORMAL)
    consola.insert('insert', mc.listadoResp)
    consola.config(state=DISABLED)
    messagebox.showinfo('Informacion','Se ha ejecutado el analisis')


def graficar():
    #enviar a llamar las funciones para genera la graficar
    print('graficar')
    paths= str(os.getcwd())
    nuevapath = paths+'\\graficaArbol.png'
    wb.open_new(nuevapath)
def generarbnf():
    print('generar bnf')
    paths= str(os.getcwd())
    nuevapath = paths+'\\graficaGramatical.png'
    wb.open_new(nuevapath)

def general_bnf(entrada):
    global resultado
    lectura = entrada.lower()
    resultado = gramatical.parse(lectura)
    consola.config(state=NORMAL)
    consola.insert('insert',' bnf general')
    consola.config(state=DISABLED)
    # paths= str(os.getcwd())
    # nuevapath = paths+'\\graficaGramaticalbnf.png'
    # wb.open_new(nuevapath)
    #messagebox.showinfo('Informacion','Generando Gramatical BNF_General')

def generarReporte():
    paths= str(os.getcwd())
    nuevapath = paths+'\\ts.gv.pdf'
    wb.open_new(nuevapath)
    print('generar Reporte')


def generarReporteLexico():
    ver_lexicos()
    paths= str(os.getcwd())
    nuevapath = paths+'\\lexicos.pdf'
    wb.open_new(nuevapath)
    print('generar Reporte')

def generarReporteSemantico():
    ver_semanticos()
    paths= str(os.getcwd())
    nuevapath = paths+'\\semanticos.pdf'
    wb.open_new(nuevapath)
    print('generar Reporte')
def generarReporteSintactico():
    ver_sintacticos()
    paths= str(os.getcwd())
    nuevapath = paths+'\\sintaticos.pdf'
    wb.open_new(nuevapath)
    print('generar Reporte')
   

def generarTablaSimbolos():
    generarts()
    if len(tsgen) > 0:
        print("Encontrando los valores")
        verts()
    paths= str(os.getcwd())
    nuevapath = paths+'\\ts.gv.pdf'
    wb.open_new(nuevapath)
    print('generar Reporte')


#Construccion de EDitor

root =Tk()
root.title("SQL TYTUSDB")
#variables para tomar informacion de ventana
ancho, alto = root.winfo_screenwidth(), (root.winfo_screenheight()-100)
root.geometry("%dx%d+0+0"%(ancho,alto))

#Parte para separar los botones
frame_herramienta = Frame(root)
frame_herramienta.pack(fill = X )
frame_editor = Frame(root)
frame_editor.pack(pady=5)
frame_consola = Frame(root)
frame_consola.pack(pady=5)


scroll_editor = Scrollbar(frame_editor)
scroll_editor.pack(side = RIGHT, fill=Y)
scroll_editor_horizontal = Scrollbar(frame_editor, orient='horizontal')
scroll_editor_horizontal.pack(side=BOTTOM, fill=X)

editor_h = int(alto*0.025)
consola_h = int(alto*0.02)

scroll_consola = Scrollbar(frame_consola)
scroll_consola.pack(side = RIGHT, fill=Y)
scroll_consola_horizontal = Scrollbar(frame_consola, orient='horizontal')
scroll_consola_horizontal.pack(side=BOTTOM, fill=X)



#CREACION DE MENU   
mnprincipal = Menu(root)
flmenu = Menu(mnprincipal, tearoff=0)
flmenu.add_command(label="Nuevo", command=nuevo)
flmenu.add_command(label="Abrir", command=abrir)
flmenu.add_command(label="Guardar", command=guardar)
flmenu.add_command(label="Guardar como", command=guardar_como)
flmenu.add_separator()
flmenu.add_command(label="Salir",  command= lambda :salir())

mnprincipal.add_cascade(label = "Archivo", menu = flmenu)

menuAnalisis = Menu(mnprincipal, tearoff=0)
menuAnalisis.add_command(label="Analisis Ascendente", command=lambda: analisisAscendente(texto.get("1.0",'end-1c')))
menuAnalisis.add_command(label="Analisis Descendente", command=lambda: analisisDescendente(texto.get("1.0",'end-1c')))
menuAnalisis.add_command(label="Ejecutar Instrucciones", command=lambda:ejecutar(texto.get("1.0",'end-1c')))
menuAnalisis.add_separator()
menuAnalisis.add_command(label="Salir",  command= lambda :salir())

mnprincipal.add_cascade(label = "Analisis", menu = menuAnalisis)


menuReporte = Menu(mnprincipal, tearoff=0)
menuReporte.add_command(label="Generar (BNF) Dinamico", command= lambda :generarbnf())
menuReporte.add_command(label="Generar BNF General", command= lambda :general_bnf(texto.get("1.0",'end-1c')))
menuReporte.add_command(label="AST Descendente", command=  lambda:graficar())
menuReporte.add_command(label="AST ASCENDENTE", command=  lambda:graficar())


menuReporte.add_command(label="Error Lexico", command=lambda:generarReporteLexico())
menuReporte.add_command(label="Error Sintacticos", command=lambda:generarReporteSintactico())
menuReporte.add_command(label="Error Semanticos", command=lambda:generarReporteSemantico())
menuReporte.add_command(label="Ver Tabla de simbolos", command=lambda:generarTablaSimbolos())
menuReporte.add_separator()
menuReporte.add_command(label="Salir", command= lambda :salir())

mnprincipal.add_cascade(label = "Reportes", menu = menuReporte)

#botones
button_exec = Button(frame_herramienta)
icono = PhotoImage(file="Gramaticas/img/play.png")
button_exec.config(image=icono, activebackground="black",width="50", height="50",command=lambda:ejecutar(texto.get("1.0",'end-1c')))
button_exec.grid(row=0, column=0, sticky=W)

button_ascend = Button(frame_herramienta)
icono3 = PhotoImage(file="Gramaticas/img/ascedente.png")
button_ascend.config(image=icono3, activebackground="black",width="50", height="50", command=lambda:  analisisAscendente(texto.get("1.0",'end-1c')))
button_ascend.grid(row=0, column=1, sticky=W)

button_tree = Button(frame_herramienta)
icono2 = PhotoImage(file="Gramaticas/img/tree.png")
button_tree.config(image=icono2, activebackground="black",width="50", height="50", command=  lambda:graficar())
button_tree.grid(row=0, column=2, sticky=W)



button_bnf = Button(frame_herramienta)
icono4 = PhotoImage(file="Gramaticas/img/bnf.png")
button_bnf.config(image=icono4, activebackground="black",width="50", height="50",command= lambda :generarbnf())
button_bnf.grid(row=0, column=3, sticky=W)

button_descend = Button(frame_herramienta)
icono5 = PhotoImage(file="Gramaticas/img/descedente.png")
button_descend.config(image=icono5, activebackground="black",width="50", height="50",command=lambda: analisisDescendente(texto.get("1.0",'end-1c')))
button_descend.grid(row=0, column=4, sticky=W)

button_table = Button(frame_herramienta)
icono6 = PhotoImage(file="Gramaticas/img/table.png")
button_table.config(image=icono6, activebackground="black",width="50", height="50",command=lambda: generarReporte())
button_table.grid(row=0, column=5, sticky=W)




#texto

texto = Text(frame_editor, width=ancho, height=editor_h, undo =True, yscrollcommand=scroll_editor.set, wrap ="none",xscrollcommand=scroll_editor_horizontal.set)
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

scroll_editor.config(command =texto.yview)
scroll_editor_horizontal.config(command=texto.xview)


consola = Text(frame_consola, width=ancho, height=consola_h, undo =True, yscrollcommand=scroll_consola.set, wrap ="none",xscrollcommand=scroll_consola_horizontal.set)
consola.pack()
consola.config(bd=0, padx=6, pady=4, font=("Consolas",12),state=DISABLED)

scroll_consola.config(command =consola.yview)
scroll_consola_horizontal.config(command=consola.xview)





root.config(menu=mnprincipal)

root.mainloop()





