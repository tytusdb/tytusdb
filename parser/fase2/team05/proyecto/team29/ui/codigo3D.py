from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
from team29.ui.Pantalla_TS import *
from team29.ui.Pantalla_AST import *
from team29.ui.Pantalla_Error import *
import tkinter.messagebox
from team29.analizer import interpreter
from goto import with_goto

# VARIABLES GLOBALES
window = Tk()
tabControl = ttk.Notebook(window, width=700, height=300)
text_Consola = None
lexicalErrors = list()
syntacticErrors = list()
semanticErrors = list()
postgreSQL = list()
ts = list()
lista = []
simulador_pila = [None]*100

def main():
    global window, tabControl, text_Consola, lexicalErrors, syntacticErrors, semanticErrors, postgreSQL, ts
    # inicializacion de la pantalla
    window.geometry("700x320")
    window.resizable(0, 0)
    window.title("Query Tool")

    # Definicion del menu de items
    navMenu = Menu(window)
    navMenu.add_command(label="Tabla de Simbolos", command=open_ST)
    navMenu.add_command(label="AST", command=open_AST)
    navMenu.add_command(label="Reporte de errores", command=open_Reporte)
    window.config(menu=navMenu)

    # Creacion del notebook
    tabControl = ttk.Notebook(window, width=700, height=300)
    console_frame = Frame(tabControl, height=20, width=150, bg="#d3d3d3")
    text_Consola = tk.Text(console_frame, height=20, width=150)
    text_Consola.pack(fill=BOTH)
    console_frame.pack(fill=BOTH)
    tabControl.add(console_frame, text="Consola")
    tabControl.pack()
    main3d()
    window.mainloop()


def open_ST():
    global window, ts
    windowTableS = Pantalla_TS(window, ts)


def open_AST():
    global window
    windowTableS = Pantalla_AST(window)


def open_Reporte():
    global window, lexicalErrors, syntacticErrors, semanticErrors
    windowTableS = Pantalla_Error(
        window, lexicalErrors, syntacticErrors, semanticErrors
    )


def fill_table(columns, rows, table):  # funcion que muestra la salida de la/s consulta/s
    table["columns"] = columns
    """
    Definicion de columnas y encabezado
    """
    table.column("#0", width=25, minwidth=50)
    i = 0
    ancho = int(600 / len(columns))
    if ancho < 100:
        ancho = 100
    while i < len(columns):
        table.column(str(i), width=ancho, minwidth=50, anchor=CENTER)
        i += 1
    table.heading("#0", text="#", anchor=CENTER)
    i = 0
    while i < len(columns):
        table.heading(str(i), text=str(columns[i]), anchor=CENTER)
        i += 1
    """
    Insercion de filas
    """
    i = 0
    for row in rows:
        i += 1
        table.insert(parent="", index="end", iid=i, text=i, values=(row))


def show_result(consults):
    global tabControl, text_Consola
    if consults is not None:
        i = 0
        for consult in consults:
            i += 1
            if consult is not None:
                frame = Frame(tabControl, height=300, width=450, bg="#d3d3d3")
                # Creacion del scrollbar
                table_scroll = Scrollbar(frame, orient="vertical")
                table_scrollX = Scrollbar(frame, orient="horizontal")
                table = ttk.Treeview(
                    frame,
                    yscrollcommand=table_scroll.set,
                    xscrollcommand=table_scrollX.set,
                    height=12,
                )
                table_scroll.config(command=table.yview)
                table_scrollX.config(command=table.xview)
                fill_table(consult[0], consult[1], table)
                table_scroll.pack(side=RIGHT, fill=Y)
                table_scrollX.pack(side=BOTTOM, fill=X)
                table.pack(side=LEFT, fill=BOTH)
                frame.pack(fill=BOTH)
                tabControl.add(frame, text="Consulta " + str(i))
            else:
                text_Consola.insert(
                    INSERT, "Error: Consulta sin resultado" + "\n"
                )
    tabControl.pack()


def refresh():
    global tabControl, text_Consola, lexicalErrors, syntacticErrors, semanticErrors, postgreSQL, ts
    tabls = tabControl.tabs()
    i = 1
    while i < len(tabls):
        tabControl.forget(tabls[i])
        i += 1
    text_Consola.delete("1.0", "end")
    semanticErrors.clear()
    syntacticErrors.clear()
    lexicalErrors.clear()
    postgreSQL.clear()
    ts.clear()


def analize(entrada):
    global tabControl, text_Consola, lexicalErrors, syntacticErrors, semanticErrors, postgreSQL, ts
    entrada = str(entrada)
    result = interpreter.execution(entrada)
    lexicalErrors = result["lexical"]
    syntacticErrors = result["syntax"]
    semanticErrors = result["semantic"]
    postgreSQL = result["postgres"]
    ts = result["symbols"]
    if (
            len(lexicalErrors)
            + len(syntacticErrors)
            + len(semanticErrors)
            + len(postgreSQL)
            > 0
    ):
        tkinter.messagebox.showerror(
            title="Error", message="La consulta contiene errores"
        )
        if len(postgreSQL) > 0:
            i = 0
            text_Consola.insert(INSERT, "-----------ERRORS----------" + "\n")
            while i < len(postgreSQL):
                text_Consola.insert(INSERT, postgreSQL[i] + "\n")
                i += 1
    querys = result["querys"]
    show_result(querys)
    messages = result["messages"]
    if len(messages) > 0:
        i = 0
        text_Consola.insert(INSERT, "-----------MESSAGES----------" + "\n")
        while i < len(messages):
            text_Consola.insert(INSERT, str(messages[i]) + "\n")
            i += 1
    text_Consola.insert(INSERT, "\n")
    tabControl.pack()
    retorno = querys
    for ret in retorno:
        for i in range(0, len(ret)):
            if i == len(ret) - 1:
                return len(ret[i])

def funcionIntermedia(): 
	global lista
	entrada = lista.pop()
	return analize(entrada)


@with_goto
def main3d(): 
	global lista
	T1 = a
	a = T1
	t50=False
	label .L1

@with_goto
def C3D_myFuncion():
	global lista
	t45=0
	texto=simulador_pila[t45]
	t45=t45 + 1
	t46=texto
	t47=0
	simulador_pila[t47]=t46
@with_goto
def C3D_ValidaRegistros():
	global lista
	goto .L1
	t50=True
	t50=False
	label .L1

@with_goto
def C3D_CALCULOS():
	global lista
	t30 = "SELECT extract (HOUR from timestamp '2001-02-16 20:38:40' ) ;"
	lista=[t30 ]
	t69=funcionIntermedia()
	hora=t69
	t31 = "SELECT SIN(1);"
	lista=[t31 ]
	t70=funcionIntermedia()
	SENO=t70
	t71=VALOR
	if t71>1: goto .L33
	goto .L34
	label .L33
	t72=True
	goto .L35
	label .L34
	t72=False
	label .L35
	if t72 == True: goto .L36
	goto .L37
	label .L36
	VALOR=20
	goto .L38
	label .L37
	VALOR=10
	label .L38
	t73=VALOR
	t74=0
	simulador_pila[t74]=t73
@with_goto
def C3D_sp_validainsert():
	global lista
	t33 = "insert into tbbodega values (   1,'BODEGA CENTRAL',1);"
	lista=[t33 ]
	t75=funcionIntermedia()
	t34 = "insert into tbbodega (  idbodega,bodega) values ( 2,'BODEGA ZONA 12');"
	lista=[t34 ]
	t76=funcionIntermedia()
	t35 = "insert into tbbodega (   idbodega,bodega,estado) values (  3,'BODEGA ZONA 11',1);"
	lista=[t35 ]
	t77=funcionIntermedia()
	t36 = "insert into tbbodega (   idbodega,bodega,estado) values (  4,'BODEGA ZONA 1',1);"
	lista=[t36 ]
	t78=funcionIntermedia()
	t37 = "insert into tbbodega (   idbodega,bodega,estado) values (  5,'BODEGA ZONA 10',1);"
	lista=[t37 ]
	t79=funcionIntermedia()
@with_goto
def C3D_sp_validaupdate():
	global lista
	t40 = "update tbbodega set bodega = 'bodega zona 9' where idbodega = 4;"
	lista=[t40 ]
	t80=funcionIntermedia()


if __name__ == "__main__": 
	 main()
