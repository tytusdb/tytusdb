from tkinter import *
from tkinter import ttk
import random
import time

import PLSQL.tsPLSQL as TSPL
import PLSQL.tfPLSQL as TFPL
import PLSQL.gramaticaPLSQL as gPL
import PLSQL.traduccionPLSQL as TRADUC
import PLSQL.report_astPLSQL as AST3D
import PLSQL.report_erroresPLSQL as ERRORES_G
import PLSQL.report_tsPLSQL as RTS_PLSQL
import PLSQL.report_optimizacionPLSQL as ROPTIMIZACION_PLSQL


import sys
from io import StringIO
import contextlib

import  os
import  glob


from os import  path
from os import  remove

instrucciones_Global = []
instrucciones_GlobalPL = []

tc_global1 = []
ts_global1 = []

ts_globalPL = []


erroressss = ERRORES_G.ErrorHTML()

root = Tk() 
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("TytusDB - Query Tools") 
root.state("zoomed")

global selected
selected = False

# ACTIONS
def analizar(txt):
    global instrucciones_GlobalPL
    instruccionesPL = TRADUC.runC3D(txt)
    

    if erroressss.getList() == []:
        instrucciones_GlobalPL = instruccionesPL
        ts_globalPL = TSPL.TablaDeSimbolos()
        codigo3D = ""
        codigo3D = TRADUC.generarC3D(instruccionesPL, ts_globalPL)
        salida3D = open("./salida3D.py", "w")
        salida3D.write(codigo3D)
        salida3D.close()
        salida_table(2,'3D GENERADO CON EXITO')
    else:
        salida_table(2,"PARSER ERROR")
    


def analizar_select(e):
    global selected
    if my_text.selection_get():

        global instrucciones_GlobalPL
        selected = my_text.selection_get()
        instruccionesPL = TRADUC.runC3D(selected)
        

        if erroressss.getList() == []:
            instrucciones_GlobalPL = instruccionesPL
            ts_globalPL = TSPL.TablaDeSimbolos()
            codigo3D = ""
            codigo3D = TRADUC.generarC3D(instruccionesPL, ts_globalPL)
            salida3D = open("./salida3D.py", "w")
            salida3D.write(codigo3D)
            salida3D.close()
            salida_table(2,'3D GENERADO CON EXITO')
        else:
            salida_table(2,"PARSER ERROR")
            

def generarReporteAST():
    global instrucciones_GlobalPL
    AST3DD = AST3D.AST()
    AST3DD.generarAST(instrucciones_GlobalPL) 
    '''global instrucciones_Global
    astGraph = AST()
    astGraph.generarAST(instrucciones_Global)'''

def generarReporteTC():
    print(':v')
    '''global tc_global1
    typeC = TipeChecker()
    typeC.crearReporte(tc_global1)'''

def generarReporteErrores():
    erroressss.crearReporte()

def generarReporteOptimizacion():
    reporteOptimizacion = ROPTIMIZACION_PLSQL.ROptimizacion3D()
    reporteOptimizacion.crearReporte(TRADUC.tablaOptimizacion)

def generarReporteTS():
    reporteTS = RTS_PLSQL.RTablaDeSimbolosF()
    reporteTS.crearReporte(TRADUC.tf)
    '''global ts_global1
    RTablaS = RTablaDeSimbolos()
    RTablaS.crearReporte(ts_global1)'''

def traducir3D():
    f = open("./salida3D.py", "r")
    #f = open("texto3D.py", "r")
    texto3D = f.read()
    my_text2.delete("1.0","end")
    my_text2.insert(1.0,texto3D)

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

def compilar3D():
    try:
        cadena = my_text2.get("1.0",'end-1c')
        with stdoutIO() as s:
            exec(cadena,{})
        salida_table(2,s.getvalue())


    except:
        print("NO SE PUDO :v")
        pass

toolbar_frame = Frame(root)
toolbar_frame.pack(fill = X)

text_frames = Frame(root)
text_frames.pack(pady=5)


entrada_h = int(h * 0.038)
entrada_w = int(w * 0.060)
#VENTANA1
text_frame = Frame(text_frames,width=entrada_w, height=entrada_h)
text_frame.pack( side = LEFT,padx=5)
text_scroll = Scrollbar(text_frame)
text_scroll.pack(side = RIGHT, fill = Y)
hor_scroll = Scrollbar(text_frame, orient = 'horizontal')
hor_scroll.pack(side = BOTTOM, fill = X)
my_text = Text(text_frame, width=entrada_w, height=entrada_h, selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap = "none", xscrollcommand = hor_scroll.set)
my_text.pack()
text_scroll.config(command = my_text.yview)
hor_scroll.config(command = my_text.xview)
#VENTANA 2
text_frame2 = Frame(text_frames,width=entrada_w, height=entrada_h)
text_frame2.pack( side = LEFT ,padx=5)
text_scroll2 = Scrollbar(text_frame2)
text_scroll2.pack(side = RIGHT, fill = Y)
hor_scroll2 = Scrollbar(text_frame2, orient = 'horizontal')
hor_scroll2.pack(side = BOTTOM, fill = X)
my_text2 = Text(text_frame2, width=entrada_w, height=entrada_h, selectforeground="black", undo=True, yscrollcommand=text_scroll2.set, wrap = "none", xscrollcommand = hor_scroll2.set,background="black", foreground="lawn green")
my_text2.pack()
text_scroll2.config(command = my_text2.yview)
hor_scroll2.config(command = my_text2.xview)

#MENU
my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Archivo", menu = file_menu)
file_menu.add_command(label = "Analizar", command = lambda: analizar(my_text.get("1.0",'end-1c')))
file_menu.add_command(label = "Analizar Query" , command = lambda: analizar_select(False))
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

reportes_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Reportes", menu = reportes_menu)
reportes_menu.add_command(label = "Tabla de Simbolos", command = lambda: generarReporteTS())
reportes_menu.add_command(label = "Tabla de Tipos", command = lambda: generarReporteTC())
reportes_menu.add_command(label = "AST", command = lambda: generarReporteAST())
reportes_menu.add_command(label = "Errores", command = lambda: generarReporteErrores())
reportes_menu.add_command(label = "Optimizacion3D", command = lambda: generarReporteOptimizacion())

analizar_button = Button(toolbar_frame)
photoCompila = PhotoImage(file="iconos/all.png")
analizar_button.config(image=photoCompila, width="50", height="50", activebackground="black",command = lambda: analizar(my_text.get("1.0",'end-1c')))
analizar_button.grid(row = 0, column = 0, sticky = W)

analizar_step_step = Button(toolbar_frame)
photoCompila1 = PhotoImage(file="iconos/select.png")
analizar_step_step.config(image=photoCompila1, width="50", height="50", activebackground="black",command = lambda: analizar_select(False))
analizar_step_step.grid(row = 0, column = 1, sticky = W)

translate = Button(toolbar_frame)
photoCompila2 = PhotoImage(file="iconos/translate.png")
translate.config(image=photoCompila2, width="50", height="50", activebackground="black",command=traducir3D)
translate.grid(row = 0, column = 2, sticky = W)

python3d = Button(toolbar_frame)
photoCompila3 = PhotoImage(file="iconos/python.png")
python3d.config(image=photoCompila3, width="50", height="50", activebackground="black",command=compilar3D)
python3d.grid(row = 0, column = 3, sticky = W)

def salida_table(salida,textoSalida):
    if salida == 1:
        global salida_frame
        try:
            global salida_frame
            salida_frame.destroy()
        except:
            pass
        salida_frame = LabelFrame(root, text = "Salida")
        salida_frame.pack(fill = X)

        for widget in salida_frame.winfo_children():
            widget.destroy()

        global random_numero
        random_numero = len(textoSalida)

        prueba_columna = []

        i = 1
        while i <= int(len(textoSalida[0])+1):
            prueba_columna.append(i)
            i += 1

        #print(prueba_columna)
        
        my_tree = ttk.Treeview(salida_frame, columns=prueba_columna)
        my_tree.pack(side=LEFT)
        my_tree.place(x=0,y=0)

        my_tree.column("#"+str(0), stretch=False, width=40)
        my_tree.heading("#"+str(0),text = " ")
        j = 1
        while j <= len(textoSalida[0]):
            my_tree.column("#"+str(j), stretch=False, width=100)
            my_tree.heading("#"+str(j),text = textoSalida[0][j-1])
            j+=1
        

        yscrollbar = ttk.Scrollbar(salida_frame, orient = "vertical", command=my_tree.yview)
        yscrollbar.pack(side = RIGHT, fill = Y)

        xscrollbar = ttk.Scrollbar(salida_frame, orient="horizontal", command = my_tree.xview)
        xscrollbar.pack(side=BOTTOM, fill = X)

        my_tree.configure(yscrollcommand=yscrollbar.set, xscrollcommand = xscrollbar.set)

     
        countt = 1
        while countt < len(textoSalida):
            #print(textoSalida[countt])
            my_tree.insert(parent = '', index = 'end', iid=countt, text = str(countt), values = tuple(textoSalida[countt]))
            countt +=1       

        my_tree.pack(fill = X)

    else:
        try:
            salida_frame.destroy()
        except:
            pass
        salida_frame = LabelFrame(root, text = "Salida")
        salida_frame.pack(fill = X)
        my_text1 = Text(salida_frame)
        my_text1.pack(fill=X)
        my_text1.delete(1.0,"end")
        my_text1.insert(1.0, textoSalida)
        my_text1.config(state=DISABLED)
        
        


root.mainloop() 

print("Eliminar DB")
files = glob.glob('data/json/*')
for ele in files:
    os.remove(ele)