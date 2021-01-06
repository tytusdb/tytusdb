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
    t66 = "CREATE DATABASE IF NOT EXISTS test"
    t67 = t66 + " OWNER = \'root\'" 
    t68 = t67 + " MODE = 1"
    t69 = t68 + ";"
    stack[p] = t69
    p = p + 1
    t70 = "USE test;"
    stack[p] = t70
    p = p + 1
    t71 = "CREATE TABLE tabla (\n"
    t72 = "id integer"
    t73 = t72 + ",\n"
    t74 = t71 + t73
    t75 = "column2 integer"
    t76 = t75 + ",\n"
    t77 = t74 + t76
    t78 = "column3 integer"
    t79 = t78 + ",\n"
    t80 = t77 + t79
    t81 = "column4 integer"
    t82 = t80 + t81
    t83 = t82 + ");"
    stack[p] = t83
    p = p + 1
    t84 = "CREATE TABLE tbbodega (\n"
    t85 = "id integer"
    t86 = t85 + ",\n"
    t87 = t84 + t86
    t88 = "bodega varchar"
    t89 = t88 + "(120)"
    t90 = t89 + ",\n"
    t91 = t87 + t90
    t92 = "id2 integer"
    t93 = t91 + t92
    t94 = t93 + ");"
    stack[p] = t94
    p = p + 1
    t95 = "CREATE INDEX test2_mm_idx ON tabla(id);"
    stack[p] = t95
    p = p + 1
    t96 = "CREATE INDEX test2_mm_idx ON tabla(id);"
    stack[p] = t96
    p = p + 1
    t97 = "DROP INDEX ;"
    stack[p] = t97
    p = p + 1
    t98 = "DROP INDEX ;"
    stack[p] = t98
    p = p + 1

exec()
call_funcion_intermedia()