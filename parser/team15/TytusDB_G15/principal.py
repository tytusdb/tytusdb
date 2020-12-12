import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *
from graphviz import Digraph
#from ast import *

from storageManager import jsonMode as j

salida = ""

def procesar_createTable(instr,ts) :
    # print('Crear Tabla Normal')
    simbolo = TS.Simbolo(instr.nombre_tabla, TS.TIPO_DATO.CREATE_TABLE, 0)
    ts.agregar(simbolo)
    if instr.intrucc != []:
        procesar_instrucciones(instr.intrucc,ts)

def procesar_createTable_Herencia(instr,ts) :
    # print('Crear Tabla con herencia')
    simbolo = TS.Simbolo(instr.nombre_tabla, TS.TIPO_DATO.CREATE_TABLE, 0)
    ts.agregar(simbolo)
    if instr.intrucc != []:
        procesar_instrucciones(instr.intrucc,ts)

def procesar_Definicion(instr,ts) :
    # print('Definicion')
    simbolo = TS.Simbolo(instr.id.id, TS.TIPO_DATO.CREATE_TABLE, 0)
    ts.agregar(simbolo)

def procesar_createDatabase(instr,ts) :

    result = j.createDatabase(str(instr.nombre.id))
    
    if result == 0:
        global salida
        salida = "\nCREATE DATABASE"
        print("CREATE DATABASE")
    elif result == 1 :
        salida = "\nERROR:  internal_error \nSQL state: XX000 "
        print("ERROR:  internal_error \nSQL state: XX000 ")
    elif result == 2 :
        salida = "\nERROR:  database \"" + str(instr.nombre.id) +"\" already exists \nSQL state: 42P04 "
        print("ERROR:  database \"" + str(instr.nombre.id) +"\" already exists \nSQL state: 42P04 ")

def procesar_instrucciones(instrucciones,ts) :
    global salida
    salida = ""
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        #CREATE DATABASE
        if isinstance(instr,CreateDatabase) : procesar_createDatabase(instr,ts)
        else : print('Error: instrucción no válida ' + str(instr))

    return salida


#f = open("./entrada.txt", "r")
#input = f.read()
#instrucciones = g.parse(input)
#instrucciones_Global = instrucciones
#ts_global = TS.TablaDeSimbolos()
#procesar_instrucciones(instrucciones,ts_global)

#astG = AST()
#astG.generarAST(instrucciones)



def ts_graph(ts_global):
    dot3 = Digraph('TS', node_attr={'shape': 'plaintext','color': 'lightblue2'})
    cadena = "<\n"
    cadena = cadena + "<table border='1' cellborder='1'>\n"
    cadena = cadena + "<tr><td colspan='3'>Tabla de Simbolos</td></tr>"
    cadena = cadena + "<tr><td port='port_one'>Id</td><td port='port_two'>Tipo</td><td port='port_three'>Valor</td></tr>"
    for key in ts_global.simbolos:
        cadena2 = "<tr><td port='port_one'>" + str(ts_global.simbolos[key].id) + "</td><td port='port_two'>" + str(ts_global.simbolos[key].tipo) + "</td><td port='port_three'>" + str(ts_global.simbolos[key].valor) + "</td></tr>\n"
        cadena = cadena + cadena2
    cadena = cadena + "</table>"
    cadena = cadena + '>'
    dot3.node('tab', label=cadena)
    dot3.view('Reportes/TS', cleanup=True)


#ts_graph(ts_global)