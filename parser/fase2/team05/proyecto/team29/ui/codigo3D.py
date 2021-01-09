from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
from team29.ui.Pantalla_TS import *
from team29.ui.Pantalla_AST import *
from team29.ui.Pantalla_Error import *
import tkinter.messagebox
import math
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
	t0 = "create or replace database DBFase2;"
	lista = [t0 ] 
	funcionIntermedia() 
	t1 = "use DBFase2;"
	lista = [t1 ] 
	funcionIntermedia() 
	t2 = "create table tbProducto ( idproducto integer  not null  primary key ,producto  varchar(150)  not null ,fechacreacion date  not null ,estado integer );"
	lista = [t2 ] 
	funcionIntermedia() 
	t3 = "create table tbCalificacion ( idcalifica integer  not null  primary key ,item  varchar(100)  not null ,punteo integer  not null  );"
	lista = [t3 ] 
	funcionIntermedia() 
	t4 = "insert into tbProducto values (    1,'Laptop Lenovo',now(),1);"
	lista = [t4 ] 
	funcionIntermedia() 
	t5 = "insert into tbProducto values (    2,'Bateria para Laptop Lenovo T420',now(),1);"
	lista = [t5 ] 
	funcionIntermedia() 
	t6 = "insert into tbProducto values (    3,'Teclado Inalambrico',now(),1);"
	lista = [t6 ] 
	funcionIntermedia() 
	t7 = "insert into tbProducto values (    4,'Mouse Inalambrico',now(),1);"
	lista = [t7 ] 
	funcionIntermedia() 
	t8 = "insert into tbProducto values (    5,'WIFI USB',now(),1);"
	lista = [t8 ] 
	funcionIntermedia() 
	t9 = "insert into tbProducto values (    6,'Laptop HP',now(),1);"
	lista = [t9 ] 
	funcionIntermedia() 
	t10 = "insert into tbProducto values (    7,'Teclado Flexible USB',now(),1);"
	lista = [t10 ] 
	funcionIntermedia() 
	t11 = "insert into tbProducto values (    8,'Laptop Samsung','2021-01-02',1);"
	lista = [t11 ] 
	funcionIntermedia() 
	t15 = "update tbProducto set estado = 2 where estado = 1;"
	lista = [t15 ] 
	funcionIntermedia() 
	t18 = "create table tbbodega ( idbodega integer  not null  primary key ,bodega  varchar(100)  not null ,estado integer );"
	lista = [t18 ] 
	funcionIntermedia() 
	C3D_sp_validainsert()
	t24=0
	t25=simulador_pila[t24]
	C3D_sp_validaupdate()
	t27=0
	t28=simulador_pila[t27]
	t29 = "delete from tbbodega where idbodega = 4;"
	lista = [t29 ] 
	funcionIntermedia() 
	t30 = "select * from tbbodega;"
	lista = [t30 ] 
	funcionIntermedia() 

@with_goto
def C3D_myFuncion():
	global lista
	t31=0
	texto=simulador_pila[t31]
	t31=t31 + 1
	t32=texto
	t33=0
	simulador_pila[t33]=t32
@with_goto
def C3D_ValidaRegistros():
	global lista
	t34=0
	tabla=simulador_pila[t34]
	t34=t34 + 1
	cantidad=simulador_pila[t34]
	t34=t34 + 1
	t35=tabla
	if t35=="tbProducto": goto .L0
	goto .L1
	label .L0
	t36=True
	goto .L2
	label .L1
	t36=False
	label .L2
	if t36 == True: goto .L3
	goto .L4
	label .L3
	t12 = "SELECT COUNT(*) from tbProducto;"
	lista=[t12 ]
	t37=funcionIntermedia()
	resultado=t37
	t38=cantidad
	t39=resultado
	if t38==t39: goto .L5
	goto .L6
	label .L5
	t40=True
	goto .L7
	label .L6
	t40=False
	label .L7
	if t40 == True: goto .L8
	goto .L9
	label .L8
	retorna=1
	goto .L10
	label .L9
	retorna=0
	label .L10
	label .L4
	t41=tabla
	if t41=="tbProductoUp": goto .L11
	goto .L12
	label .L11
	t42=True
	goto .L13
	label .L12
	t42=False
	label .L13
	if t42 == True: goto .L14
	goto .L15
	label .L14
	t13 = "SELECT COUNT(*) from tbProducto where estado = 2;"
	lista=[t13 ]
	t43=funcionIntermedia()
	resultado=t43
	t44=cantidad
	t45=resultado
	if t44==t45: goto .L16
	goto .L17
	label .L16
	t46=True
	goto .L18
	label .L17
	t46=False
	label .L18
	if t46 == True: goto .L19
	goto .L20
	label .L19
	retorna=1
	goto .L21
	label .L20
	retorna=0
	label .L21
	label .L15
	t47=tabla
	if t47=="tbbodega": goto .L22
	goto .L23
	label .L22
	t48=True
	goto .L24
	label .L23
	t48=False
	label .L24
	if t48 == True: goto .L25
	goto .L26
	label .L25
	t14 = "SELECT COUNT(*) from tbbodega;"
	lista=[t14 ]
	t49=funcionIntermedia()
	resultado=t49
	t50=cantidad
	t51=resultado
	if t50==t51: goto .L27
	goto .L28
	label .L27
	t52=True
	goto .L29
	label .L28
	t52=False
	label .L29
	if t52 == True: goto .L30
	goto .L31
	label .L30
	retorna=1
	goto .L32
	label .L31
	retorna=0
	label .L32
	label .L26
	t53=retorna
	t54=0
	simulador_pila[t54]=t53
@with_goto
def C3D_CALCULOS():
	global lista
	t16 = "SELECT extract (HOUR from timestamp '2001-02-16 20:38:40' ) ;"
	lista=[t16 ]
	t55=funcionIntermedia()
	hora=t55
	t17 = "SELECT SIN(1);"
	lista=[t17 ]
	t56=funcionIntermedia()
	SENO=t56
	t57=VALOR
	if t57>1: goto .L33
	goto .L34
	label .L33
	t58=True
	goto .L35
	label .L34
	t58=False
	label .L35
	if t58 == True: goto .L36
	goto .L37
	label .L36
	VALOR=20
	goto .L38
	label .L37
	VALOR=10
	label .L38
	t59=VALOR
	t60=0
	simulador_pila[t60]=t59
@with_goto
def C3D_sp_validainsert():
	global lista
	t19 = "insert into tbbodega values (   1,'BODEGA CENTRAL',1);"
	lista=[t19 ]
	t61=funcionIntermedia()
	t20 = "insert into tbbodega (  idbodega,bodega) values ( 2,'BODEGA ZONA 12');"
	lista=[t20 ]
	t62=funcionIntermedia()
	t21 = "insert into tbbodega (   idbodega,bodega,estado) values (  3,'BODEGA ZONA 11',1);"
	lista=[t21 ]
	t63=funcionIntermedia()
	t22 = "insert into tbbodega (   idbodega,bodega,estado) values (  4,'BODEGA ZONA 1',1);"
	lista=[t22 ]
	t64=funcionIntermedia()
	t23 = "insert into tbbodega (   idbodega,bodega,estado) values (  5,'BODEGA ZONA 10',1);"
	lista=[t23 ]
	t65=funcionIntermedia()
@with_goto
def C3D_sp_validaupdate():
	global lista
	t26 = "update tbbodega set bodega = 'bodega zona 9' where idbodega = 4;"
	lista=[t26 ]
	t66=funcionIntermedia()


if __name__ == "__main__": 
	 main()
