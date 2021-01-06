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
    t0 = "CREATE DATABASE DBFase2"
    t1 = t0 + " MODE = 1"
    t2 = t1 + ";"
    stack[p] = t2
    p = p + 1
    t3 = "USE DBFase2;"
    stack[p] = t3
    p = p + 1
    t4 = "CREATE TABLE tbCalificacion (\n"
    t5 = "idcalifica integer"
    t6 = t5 + " not null"
    t7 = t6 + " primary key"
    t8 = t7 + ",\n"
    t9 = t4 + t8
    t10 = "item varchar"
    t11 = t10 + "(100)"
    t12 = t11 + " not null"
    t13 = t12 + ",\n"
    t14 = t9 + t13
    t15 = "punteo integer"
    t16 = t15 + " not null"
    t17 = t14 + t16
    t18 = t17 + ");"
    stack[p] = t18
    p = p + 1