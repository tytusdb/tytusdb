from goto import with_goto
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.TablaSimbolos.Arbol import Arbol
from storageManager.jsonMode import *
import sintactico

tablaGlobal = Tabla(None)
arbol = Arbol()

def call_funcion_intermedia():
    dropAll()
    input = ""
    for i in stack:
        input += stack[i] + "\n"
    print(input)
    inst = sintactico.ejecutar_analisis(input)
    arbol = Arbol(inst)
    for i in arbol.instrucciones:
        resultado = i.ejecutar(tablaGlobal,arbol)

stack = {}
heap = {}
p = 0
h = 0

@with_goto
def exec():
    global p
    t0 = "CREATE DATABASE IF NOT EXISTS test"
    t1 = t0 + " OWNER = \'root\'" 
    t2 = t1 + " MODE = 1"
    t3 = t2 + ";"
    stack[p] = t3
    p = p + 1
    t4 = "USE test;"
    stack[p] = t4
    p = p + 1
    t5 = "CREATE TABLE tabla (\n"
    t6 = "id integer"
    t7 = t6 + ",\n"
    t8 = t5 + t7
    t9 = "column2 integer"
    t10 = t8 + t9
    t11 = t10 + ");"
    stack[p] = t11
    p = p + 1
    t12 = "CREATE TABLE tbbodega (\n"
    t13 = "id integer"
    t14 = t13 + ",\n"
    t15 = t12 + t14
    t16 = "bodega varchar"
    t17 = t16 + "(120)"
    t18 = t17 + ",\n"
    t19 = t15 + t18
    t20 = "id2 integer"
    t21 = t19 + t20
    t22 = t21 + ");"
    stack[p] = t22
    p = p + 1
    t23 = "CREATE INDEX test2_mm_idx ON tabla(id);"
    stack[p] = t23
    p = p + 1
    t24 = "CREATE INDEX test2_mm_idx ON tabla(id);"
    stack[p] = t24
    p = p + 1
    t25 = "DROP INDEX test2_mm_idx;"
    stack[p] = t25
    p = p + 1

exec()
call_funcion_intermedia()