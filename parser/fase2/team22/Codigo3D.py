from goto import with_goto
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Sql_insert import insertTable
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

def call_insert_table():
    arbolAux = arbol
    arbolAux.bdUsar = heap[p-3]
    tabla = insertTable.insertTable(heap[p-2], None, heap[p-1], heap[p], '', 0, 0)
    tabla.ejecutar(tablaGlobal, arbolAux)

stack = {}
heap = {}
p = 0
h = 0

@with_goto
def exec():
    global p
    t0 = "CREATE INDEX test2_mm_idx ON tabla(id);"
    stack[p] = t0
    p = p + 1

exec()
call_funcion_intermedia()