from goto import with_goto
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.TablaSimbolos.Arbol import Arbol
from storageManager.jsonMode import *
import sintactico

tablaGlobal = Tabla(None)
arbol = Arbol()

def ejecutar3D():
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
    t5 = "CREATE TABLE tbcalifica (\n"
    t6 = "iditem integer"
    t7 = t6 + " not null"
    t8 = t7 + " primary key"
    t9 = t8 + ",\n"
    t10 = t5 + t9
    t11 = "item varchar"
    t12 = t11 + "(150)"
    t13 = t12 + " not null"
    t14 = t13 + ",\n"
    t15 = t10 + t14
    t16 = "puntos decimal"
    t17 = t16 + "(8,2)"
    t18 = t17 + " not null"
    t19 = t15 + t18
    t20 = t19 + ");"
    stack[p] = t20
    p = p + 1= t41
    p = p + 1

exec()
ejecutar3D()