import os
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import ttk
from tkinter import messagebox
import webbrowser as wb
import random
import math

#importaciones
import PLSQLParser as planalizador
from InstruccionesPL.TablaSimbolosPL import ArbolPL as arbolplObjeto
from InstruccionesPL.TablaSimbolosPL import TablaPL as tablaplObjeto
from reportes.reportetabla import *
from Documentacion import PLSQLParser_AST as imgast
from Documentacion import PLSQLParser_Gramatical as imggram
from Documentacion import PLSQLParser_GramaticalDinamico as imggramdinamico
from reportes.ErroresReporte import ErroresReporte
global arbolPL 
arbolPL = None

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


def ejecutar(entrada):

    global arbolPL
    instrucciones = planalizador.getParser(entrada)
    arbolPL = arbolplObjeto.ArbolPL(instrucciones)
    tablasimpl = tablaplObjeto.TablaPL(None)
    if len(planalizador.lista_lexicos)>0:
        messagebox.showerror('Tabla de Errores','La Entrada Contiene Errores!')
        ErroresReporte.generar_reporte_lexicos(planalizador.lista_lexicos)

    for i in arbolPL.getInstrucciones():
        result = i.ejecutar(tablasimpl, arbolPL)
    mensaje = ''
    for m in arbolPL.consola:
            mensaje += m + '\n'
    consola.config(state=NORMAL)
    consola.insert('insert',mensaje)
    consola.config(state=DISABLED)

    messagebox.showinfo('Informacion','Se ha ejecutado el analisis')

def mostrarTabla():
    global arbolPL
    crear_tabla(arbolPL)
def imgAst(entrada):
    imgast.parse(entrada)
    print('graficar')
    paths= str(os.getcwd())
    nuevapath = paths+'\\graficaArbol.png'
    wb.open_new(nuevapath)

def imgGramatical(entrada):
    imggram.parse(entrada)
    print('graficar')
    paths= str(os.getcwd())
    nuevapath = paths+'\\graficaGramatical.png'
    wb.open_new(nuevapath)

def imgGramaticalDinamico(entrada):
    imggramdinamico.parse(entrada)
    print('graficar')
    paths= str(os.getcwd())
    nuevapath = paths+'\\graficaGramaticalbnf.png'
    wb.open_new(nuevapath)

def verTablaError():
    if len(planalizador.lista_lexicos)==0:
        messagebox.showinfo('Tabla de Erores','La Entrada no Contiene Errores!')
    else:
        ErroresReporte.generar_reporte_lexicos(planalizador.lista_lexicos)

def modificar():
    print('modificar')

#construccion de Editor

root = Tk()
root.title("SQL TYTUSDB")

#toma la informacion de la ventana
ancho, alto = root.winfo_screenwidth(), (root.winfo_screenheight()-100)
ancho = math.trunc((ancho/5)*3)
alto = math.trunc((alto/5)*4)
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

#creacion de MENU
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
menuAnalisis.add_command(label="Analisis Ascendente", command=lambda: ejecutar(texto.get("1.0",'end-1c')))
menuAnalisis.add_command(label="Analisis Descendente", command=lambda: ejecutar(texto.get("1.0",'end-1c')))
menuAnalisis.add_command(label="Ejecutar Instrucciones", command=lambda:ejecutar(texto.get("1.0",'end-1c')))
menuAnalisis.add_separator()
menuAnalisis.add_command(label="Salir",  command= lambda :salir())


mnprincipal.add_cascade(label = "Analisis", menu = menuAnalisis)


menuReporte = Menu(mnprincipal, tearoff=0)
menuReporte.add_command(label="Generar (BNF) Dinamico", command=lambda:imgGramaticalDinamico(texto.get("1.0",'end-1c')))
menuReporte.add_command(label="Generar BNF General", command=lambda:imgGramatical(texto.get("1.0",'end-1c')))
menuReporte.add_command(label="AST ASCENDENTE",command=lambda:imgAst(texto.get("1.0",'end-1c')))


menuReporte.add_command(label="Ver tabla de Errores", command=lambda:verTablaError())
menuReporte.add_command(label="Ver Tabla de simbolos", command=lambda:mostrarTabla())
menuReporte.add_separator()
menuReporte.add_command(label="Salir", command= lambda :salir())

mnprincipal.add_cascade(label = "Reportes", menu = menuReporte)

#botones
button_exec = Button(frame_herramienta)
icono = PhotoImage(file="img/play.png")
button_exec.config(image=icono, activebackground="black",width="50", height="50",command=lambda:ejecutar(texto.get("1.0",'end-1c')))
button_exec.grid(row=0, column=0, sticky=W)

button_ascend = Button(frame_herramienta)
icono3 = PhotoImage(file="img/ascedente.png")
button_ascend.config(image=icono3, activebackground="black",width="50", height="50", command=lambda:  ejecutar(texto.get("1.0",'end-1c')))
button_ascend.grid(row=0, column=1, sticky=W)

button_tree = Button(frame_herramienta)
icono2 = PhotoImage(file="img/tree.png")
button_tree.config(image=icono2, activebackground="black",width="50", height="50", command=lambda:imgAst(texto.get("1.0",'end-1c')))
button_tree.grid(row=0, column=2, sticky=W)



button_bnf = Button(frame_herramienta)
icono4 = PhotoImage(file="img/bnf.png")
button_bnf.config(image=icono4, activebackground="black",width="50", height="50",command=lambda:imgGramaticalDinamico(texto.get("1.0",'end-1c')))
button_bnf.grid(row=0, column=3, sticky=W)

button_traducir = Button(frame_herramienta)
icono5 = PhotoImage(file="img/traducir.png")
button_traducir.config(image=icono5, activebackground="black",width="50", height="50",command=lambda: ejecutar(texto.get("1.0",'end-1c')))
button_traducir.grid(row=0, column=4, sticky=W)

button_optimizar = Button(frame_herramienta)
icono7 = PhotoImage(file="img/optimizar.png")
button_optimizar.config(image=icono7, activebackground="black",width="50", height="50",command=lambda: ejecutar(texto.get("1.0",'end-1c')))
button_optimizar.grid(row=0, column=5, sticky=W)

button_table = Button(frame_herramienta)
icono6 = PhotoImage(file="img/table.png")
button_table.config(image=icono6, activebackground="black",width="50", height="50",command=lambda: mostrarTabla())
button_table.grid(row=0, column=6, sticky=W)




#texto

texto = Text(frame_editor, width=ancho, height=editor_h, undo =True, yscrollcommand=scroll_editor.set, wrap ="none",xscrollcommand=scroll_editor_horizontal.set)
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

scroll_editor.config(command =texto.yview)
scroll_editor_horizontal.config(command=texto.xview)


consola = Text(frame_consola, width=ancho, height=consola_h, undo =True, yscrollcommand=scroll_consola.set, wrap ="none",xscrollcommand=scroll_consola_horizontal.set)
consola.pack()
consola.config(bd=0, padx=6, pady=4, font=("Consolas",12),state=DISABLED,background="#070707",foreground="#FEFDFD")

scroll_consola.config(command =consola.yview)
scroll_consola_horizontal.config(command=consola.xview)





root.config(menu=mnprincipal)

root.mainloop()



