import arbol.AST as a
import gramatica2 as g
from tkinter import *
from reportes import *
from Entorno.Entorno import Entorno
from subprocess import check_call
from Entorno.Entorno import Entorno


ventana= Tk()
ventana.geometry("1000x900")
ventana.resizable(False,False)
ventana.config(background = "gray25")


def reporte_lex_sin():
    if len(reporteerrores) != 0:
        contenido = "Digraph  reporte{label=\"REPORTE ERRORES LEXICOS Y SINTACTICOS\"\n"
        contenido += "node [shape=record,style=rounded,color=\"#4b8dc5\"];\n"
        contenido += "arset [label=<\n<TABLE border= \"2\"  cellspacing= \"-1\" color=\"#4b8dc5\">\n"
        contenido += "<TR>\n<TD bgcolor=\"#1ED0EC\">Tipo</TD>\n<TD bgcolor=\"#1ED0EC\">Linea</TD>\n"
        contenido += "<TD bgcolor=\"#1ED0EC\">Columna</TD>\n<TD bgcolor=\"#1ED0EC\">Descripcion</TD>\n</TR>\n"

        for error in reporteerrores:
            contenido += '<TR> <TD>' + error.tipo + '</TD><TD>' + error.linea +'</TD> <TD>' + error.columna +'</TD><TD>' + error.descripcion +'</TD></TR>'
        
        contenido += '</TABLE>\n>, ];}'
    
        with open('reporteerrores.dot','w',encoding='utf8') as reporte:
             reporte.write(contenido)
      

def mostrarimagenre():
    check_call(['dot','-Tpng','reporteerrores.dot','-o','imagenerrores.png'])

def send_data():
    print("Analizando Entrada:")
    print("==============================================")
    #reporteerrores = []
    contenido = Tentrada.get(1.0, 'end')
    Tsalida.delete("1.0", "end")
    Tsalida.configure(state='normal')
    Tsalida.insert(INSERT, "Salida de consultas")
    Tsalida.configure(state='disabled')
   
    #print(contenido)
    Principal = Entorno()

    instrucciones = g.parse(contenido)
    for instr in instrucciones:
        if instr != None:
            instr.ejecutar(Principal)

    reporte_lex_sin()

def arbol_ast():
    contenido = Tentrada.get(1.0, 'end')
    a.generarArbol(contenido)



entrada = StringVar()
Tentrada = Text(ventana)
Tentrada.config(width=120, height=35)
Tentrada.config(background="gray18")
Tentrada.config(foreground="white")
Tentrada.config(insertbackground="white")
Tentrada.place(x = 10, y = 10)

Tsalida = Text(ventana)
Tsalida.config(width=120, height=19)
Tsalida.config(background="gray10")
Tsalida.config(foreground="white")
Tsalida.config(insertbackground="white")
Tsalida.place(x = 10, y = 580)
Tsalida.configure(state='disabled')
menu_bar = Menu(ventana)

ventana.config(menu=menu_bar)
# Menu Ejecutar
ej_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Ejecutar",menu=ej_menu)
ej_menu.add_command(label="Analizar Entrada", command=send_data)

# Menu Reportes

reps_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Reportes",menu=reps_menu)
reps_menu.add_command(label="Errores Lexicos y SIntacticos", command=mostrarimagenre)
reps_menu.add_command(label="Tabla de Simbolos", command=send_data)
reps_menu.add_command(label="AST", command=arbol_ast)
reps_menu.add_command(label="Gramatica", command=send_data)



ventana.mainloop()



