import gramatica as g
import ts as TS
import tc as TC
from expresiones import *
from instrucciones import *
from graphviz import Digraph
from ast import *
from report_tc import *

from storageManager import jsonMode as j

salida = ""

def procesar_createTable(instr,ts,tc) :
    # print(instr.id)
    if instr.instrucciones != []:
        i = 0
        while i < len(instr.instrucciones):
            print(instr.instrucciones[i])
            i+=1
        for ins in instr.instrucciones:
            if isinstance(ins, Definicion_Columnas): 
                procesar_Definicion(ins,ts,tc,instr.id)
            elif isinstance(ins, LLave_Primaria): 
                procesar_primaria(ins,ts,tc,instr.id)
            elif isinstance(ins, Definicon_Foranea): 
                procesar_Foranea(ins,ts,tc,instr.id)
            elif isinstance(ins, Lista_Parametros): 
                procesar_listaId(ins,ts,tc,instr.id)
            elif isinstance(ins, definicion_constraint): 
                procesar_constraint(ins,ts,tc,instr.id)
            
def procesar_Definicion(instr,ts,tc,tabla) :
    tipo = TC.Tipo(tabla,instr.id,instr.tipo_datos.etiqueta,instr.etiqueta,instr.id_referencia,None)
    tc.agregar(tipo)
    
def procesar_listaId(instr,ts,tc,tabla):
    if instr.identificadores != []:
        for ids in instr.identificadores:
            tipo = TC.Tipo(tabla,ids.id,None,OPCIONESCREATE_TABLE.UNIQUE,None,None)
            tc.actualizarRestriccion(tipo,tabla,ids.id,OPCIONESCREATE_TABLE.UNIQUE)

def procesar_primaria(instr,ts,tc,tabla):
    tipo = TC.Tipo(tabla,instr.id,None,OPCIONESCREATE_TABLE.PRIMARIA,None,None)
    tc.actualizarRestriccion(tipo,tabla,instr.id,OPCIONESCREATE_TABLE.PRIMARIA)

def procesar_Foranea(instr,ts,tc,tabla):
    # print(instr.nombre_tabla,instr.referencia_tabla,instr.campo_referencia)
    tipo = TC.Tipo(tabla,instr.nombre_tabla,None,OPCIONESCREATE_TABLE.PRIMARIA,instr.campo_referencia,instr.referencia_tabla)
    tc.actualizarLlaveForanea(tipo,tabla,instr.nombre_tabla,OPCIONESCREATE_TABLE.FORANEA,instr.referencia_tabla,instr.campo_referencia)
    
def procesar_constraint(instr,ts,tc,tabla):
    if instr.tipo == 'UNIQUE':
        if instr.opciones_constraint != []:
            for ids in instr.opciones_constraint:
                tipo = TC.Tipo(tabla,ids.id,None,OPCIONESCREATE_TABLE.UNIQUE,None,None)
                tc.actualizarRestriccion(tipo,tabla,ids.id,OPCIONESCREATE_TABLE.UNIQUE)
    elif instr.tipo == 'FOREING':
        if instr.opciones_constraint != []:
            for ids in instr.opciones_constraint:
                tipo = TC.Tipo(tabla,instr.columna,None,OPCIONESCREATE_TABLE.FORANEA,ids,instr.referencia)
                tc.actualizarLlaveForanea(tipo,tabla,instr.columna,OPCIONESCREATE_TABLE.FORANEA,instr.referencia,ids)
    elif instr.tipo == 'CHECK':
        if instr.opciones_constraint != []:
            for ids in instr.opciones_constraint:
                if type(ids.exp1) == ExpresionIdentificador:
                    tipo = TC.Tipo(tabla,ids.exp1.id,None,OPCIONES_CONSTRAINT.CHECK,None,None)
                    tc.actualizarRestriccion(tipo,tabla,ids.exp1.id,OPCIONES_CONSTRAINT.CHECK)
                else: 
                    tipo = TC.Tipo(tabla,ids.exp1.id,None,OPCIONES_CONSTRAINT.CHECK,None,None)
                    tc.actualizarRestriccion(tipo,tabla,ids.exp1.id,OPCIONES_CONSTRAINT.CHECK)
    
def procesar_check(instr,ts,tc):
    print('Check')

def procesar_Expresion_Relacional(instr,ts,tc):
    print('Expresion Relacional')

def procesar_Expresion_Binaria(instr,ts,tc):
    print('Expresion Binaria')

def procesar_Expresion_logica(instr,ts,tc):
    print('Expresion Logica')

def resolver_expresion_aritmetica(instr,ts,tc):
    print('Expresion aritmetica')
    
def procesar_Expresion_Numerica(instr,ts,tc):
    print('Entero')

def procesar_createDatabase(instr,ts,tc) :

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

def procesar_instrucciones(instrucciones,ts,tc) :
    global salida
    salida = ""
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        #CREATE DATABASE
        if isinstance(instr,CreateDatabase) : procesar_createDatabase(instr,ts,tc)
        elif isinstance(instr, Create_Table) : procesar_createTable(instr,ts,tc)
        elif isinstance(instr, ExpresionRelacional) : procesar_Expresion_Relacional(instr,ts,tc)
        elif isinstance(instr, ExpresionBinaria) : procesar_Expresion_Binaria(instr,ts,tc)
        elif isinstance(instr, ExpresionLogica) : procesar_Expresion_logica(instr,ts,tc)
        
        else : print('Error: instrucción no válida ' + str(instr))

    return salida

f = open("./entrada.txt", "r")
input = f.read()

instrucciones = g.parse(input)
instrucciones_Global = instrucciones
ts_global = TS.TablaDeSimbolos()
tc_global = TC.TablaDeTipos()
procesar_instrucciones(instrucciones,ts_global,tc_global)

astG = AST()
astG.generarAST(instrucciones)
typeC = TipeChecker()
typeC.crearReporte(tc_global)


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