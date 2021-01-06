from tkinter import *
from tkinter import ttk
import random
from gramatica import parse
from principal import * 

import ts as TS
from expresiones import *
from instrucciones import *
from report_ast import *
from report_tc import *
from report_ts import *
from report_errores import *

instrucciones_Global = []

tc_global1 = []
ts_global1 = []

erroressss = ErrorHTML()

root = Tk() 
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("TytusDB - Query Tools") 
root.state("zoomed")

global selected
selected = False

# ACTIONS
def analizar(txt):

    global instrucciones_Global,tc_global1,ts_global1,listaErrores
    instrucciones = g.parse(txt)
    if  erroressss.getList()== []:
        instrucciones_Global = instrucciones
        ts_global = TS.TablaDeSimbolos()
        tc_global = TC.TablaDeTipos()
        tc_global1 = tc_global
        ts_global1 = ts_global
        salida = procesar_instrucciones(instrucciones, ts_global,tc_global)

        if type(salida) == list:
            salida_table(1,salida)
        else:
            salida_table(2,salida)
    else:
        salida_table(2,"PARSER ERROR")
    #parse(txt)

def analizar_select(e):
    global selected
    if my_text.selection_get():

        global instrucciones_Global,tc_global1,ts_global1,listaErrores
        selected = my_text.selection_get()
        #print(selected)
        instrucciones = g.parse(selected)
        
        if erroressss.getList() == []:
            instrucciones_Global = instrucciones
            ts_global = TS.TablaDeSimbolos()
            tc_global = TC.TablaDeTipos()
            tc_global1 = tc_global
            ts_global1 = ts_global
            salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
            if type(salida) == list:
                salida_table(1,salida)
            else:
                salida_table(2,salida)
        else:
            salida_table(2,"PARSER ERROR")
            

def generarReporteAST():
    global instrucciones_Global
    astGraph = AST()
    astGraph.generarAST(instrucciones_Global)

def generarReporteTC():
    global tc_global1
    typeC = TipeChecker()
    typeC.crearReporte(tc_global1)

def generarReporteErrores():
    erroressss.crearReporte()

def generarReporteTS():
    global ts_global1
    RTablaS = RTablaDeSimbolos()
    RTablaS.crearReporte(ts_global1)

toolbar_frame = Frame(root)
toolbar_frame.pack(fill = X)

text_frame = Frame(root)
text_frame.pack(pady=5)



# VERTICAL SCROLL BAR
text_scroll = Scrollbar(text_frame)
text_scroll.pack(side = RIGHT, fill = Y)
# HORIZONTAL SCROLL BAR
hor_scroll = Scrollbar(text_frame, orient = 'horizontal')
hor_scroll.pack(side = BOTTOM, fill = X)



my_text_h = int(h * 0.028)
my_text = Text(text_frame, width=w, height=my_text_h, selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap = "none", xscrollcommand = hor_scroll.set)
my_text.pack()

text_scroll.config(command = my_text.yview)
hor_scroll.config(command = my_text.xview)

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

analizar_button = Button(toolbar_frame)
photoCompila = PhotoImage(file="iconos/all.png")
analizar_button.config(image=photoCompila, width="50", height="50", activebackground="black",command = lambda: analizar(my_text.get("1.0",'end-1c')))
analizar_button.grid(row = 0, column = 0, sticky = W)

analizar_step_step = Button(toolbar_frame)
photoCompila1 = PhotoImage(file="iconos/select.png")
analizar_step_step.config(image=photoCompila1, width="50", height="50", activebackground="black",command = lambda: analizar_select(False))
analizar_step_step.grid(row = 0, column = 1, sticky = W)

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