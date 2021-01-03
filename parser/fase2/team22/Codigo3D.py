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
    t4 = "CREATE DATABASE IF NOT EXISTS califica"
    t5 = t4 + " OWNER = \'root\'" 
    t6 = t5 + " MODE = 2"
    t7 = t6 + ";"
    stack[p] = t7
    p = p + 1
    t8 = "SHOW DATABASES"
    t9 = t8 + ";"
    stack[p] = t9
    p = p + 1
    t10 = "USE test;"
    stack[p] = t10
    p = p + 1
    t11 = "CREATE TABLE tbcalifica (\n"
    t12 = "iditem integer"
    t13 = t12 + " not null"
    t14 = t13 + " primary key"
    t15 = t14 + ",\n"
    t16 = t11 + t15
    t17 = "item varchar"
    t18 = t17 + "(150)"
    t19 = t18 + " not null"
    t20 = t19 + ",\n"
    t21 = t16 + t20
    t22 = "puntos decimal"
    t23 = t22 + "(8,2)"
    t24 = t23 + " not null"
    t25 = t21 + t24
    t26 = t25 + ");"
    stack[p] = t26
    p = p + 1
    t27 = "CREATE TABLE tbusuario (\n"
    t28 = "idusuario integer"
    t29 = t28 + " not null"
    t30 = t29 + " primary key"
    t31 = t30 + ",\n"
    t32 = t27 + t31
    t33 = "nombre varchar"
    t34 = t33 + "(50)"
    t35 = t34 + ",\n"
    t36 = t32 + t35
    t37 = "apellido varchar"
    t38 = t37 + "(50)"
    t39 = t38 + ",\n"
    t40 = t36 + t39
    t41 = "usuario varchar"
    t42 = t41 + "(15)"
    t43 = t42 + " unique"
    t44 = t43 + " not null"
    t45 = t44 + ",\n"
    t46 = t40 + t45
    t47 = "password varchar"
    t48 = t47 + "(15)"
    t49 = t48 + " not null"
    t50 = t49 + ",\n"
    t51 = t46 + t50
    t52 = "fechacreacion date"
    t53 = t51 + t52
    t54 = t53 + ");"
    stack[p] = t54
    p = p + 1
    t55 = "CREATE TABLE tbroles (\n"
    t56 = "idrol integer"
    t57 = t56 + " not null"
    t58 = t57 + " primary key"
    t59 = t58 + ",\n"
    t60 = t55 + t59
    t61 = "rol varchar"
    t62 = t61 + "(15)"
    t63 = t60 + t62
    t64 = t63 + ");"
    stack[p] = t64
    p = p + 1
    t65 = "DROP TABLE tbroles;"
    stack[p] = t65
    p = p + 1
    t66 = "CREATE TABLE tbrol (\n"
    t67 = "idrol integer"
    t68 = t67 + " not null"
    t69 = t68 + " primary key"
    t70 = t69 + ",\n"
    t71 = t66 + t70
    t72 = "rol varchar"
    t73 = t72 + "(15)"
    t74 = t71 + t73
    t75 = t74 + ");"
    stack[p] = t75
    p = p + 1
    t76 = "CREATE TABLE cities (\n"
    t77 = "name text"
    t78 = t77 + ",\n"
    t79 = t76 + t78
    t80 = "population decimal"
    t81 = t80 + ",\n"
    t82 = t79 + t81
    t83 = "elevation integer"
    t84 = t82 + t83
    t85 = t84 + ");"
    stack[p] = t85
    p = p + 1
    t86 = "CREATE TABLE capitals (\n"
    t87 = "state char"
    t88 = t87 + "(2)"
    t89 = t86 + t88
    t90 = t89 + "\n) INHERITS (cities"
    t91 = t90 + ");"
    stack[p] = t91
    p = p + 1

exec()
ejecutar3D()