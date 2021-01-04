from goto import with_goto
from sintactico import *
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.TablaSimbolos.Arbol import Arbol
import sys
global P
global Pila
P = 0
Pila = [None] * 1000
tablaGlobal = Tabla(None)
global sql
global inst
global arbol
def funcionintermedia():
	global P
	global Pila
	t0 = P+0
	t1 = t0+1
	t2 = Pila[t1]
	print(t2)
	sql = Pila[t1]
	inst = ejecutar_analisis(sql)
	arbol = Arbol(inst)
	for instruccion in arbol.instrucciones:
		instruccion.ejecutar(tablaGlobal,arbol)
	for msj in arbol.consola:
		print(f"{msj}")
@with_goto  # Decorador necesario.
def main():
	global P
	global Pila
<<<<<<< HEAD
	goto .l0
	label .l0
	goto .l1
	goto .l2
	#Inicio print
	label .l1
	t0 = 1
	goto .l3
	label .l2
	t0 = 0
	goto .l3
	label .l3
	if(t0 == 1):
		goto .l4
	goto .l5
	#True
	label .l4
	print(True)
	goto .l6
	#False
	label .l5
	print(False)
	label .l6
	#Fin print
=======
	#Asignar cadena
	t0 = "create database if not exists test owner = 'root' mode = 1;"
	#Entrar al ambito
	t1 = P+2
	#parametro 1
	t2 = t1+1
	#Asignacion de parametros
	Pila[t2] = t0
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t3 = P+2
	t4 = Pila[t3]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t5 = "create database if not exists califica owner = 'root' mode = 2;"
	#Entrar al ambito
	t6 = P+2
	#parametro 1
	t7 = t6+1
	#Asignacion de parametros
	Pila[t7] = t5
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t8 = P+2
	t9 = Pila[t8]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t10 = "create database if not exists califica2 owner = 'root' mode = 3;"
	#Entrar al ambito
	t11 = P+2
	#parametro 1
	t12 = t11+1
	#Asignacion de parametros
	Pila[t12] = t10
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t13 = P+2
	t14 = Pila[t13]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t15 = "use test;"
	#Entrar al ambito
	t16 = P+2
	#parametro 1
	t17 = t16+1
	#Asignacion de parametros
	Pila[t17] = t15
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t18 = P+2
	t19 = Pila[t18]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t20 = "SELECT 'VALIDA CREATE DATABASE' ;"
	#Entrar al ambito
	t21 = P+2
	#parametro 1
	t22 = t21+1
	#Asignacion de parametros
	Pila[t22] = t20
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t23 = P+2
	t24 = Pila[t23]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t25 = "Create table tbcalifica ( iditem integer not null primary key, item varchar(150) not null, puntos decimal(8,2) not null);"
	#Entrar al ambito
	t26 = P+2
	#parametro 1
	t27 = t26+1
	#Asignacion de parametros
	Pila[t27] = t25
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t28 = P+2
	t29 = Pila[t28]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t30 = "Create table tbusuario ( idusuario integer not null primary key, nombre varchar(50), apellido varchar(50), usuario varchar(15) unique not null, password varchar(15) not null, fechacreacion date);"
	#Entrar al ambito
	t31 = P+2
	#parametro 1
	t32 = t31+1
	#Asignacion de parametros
	Pila[t32] = t30
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t33 = P+2
	t34 = Pila[t33]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t35 = "Create table tbroles ( idrol integer not null primary key, rol varchar(15));"
	#Entrar al ambito
	t36 = P+2
	#parametro 1
	t37 = t36+1
	#Asignacion de parametros
	Pila[t37] = t35
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t38 = P+2
	t39 = Pila[t38]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t40 = "SELECT 'VALIDA TIPO DE DATOS' ;"
	#Entrar al ambito
	t41 = P+2
	#parametro 1
	t42 = t41+1
	#Asignacion de parametros
	Pila[t42] = t40
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t43 = P+2
	t44 = Pila[t43]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t45 = "SELECT EXTRACT (YEAR FROM TIMESTAMP '2001-02-16 20:38:40') ;"
	#Entrar al ambito
	t46 = P+2
	#parametro 1
	t47 = t46+1
	#Asignacion de parametros
	Pila[t47] = t45
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t48 = P+2
	t49 = Pila[t48]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t50 = "SELECT date_part('hour', INTERVAL '4 hours 3 minutes') ;"
	#Entrar al ambito
	t51 = P+2
	#parametro 1
	t52 = t51+1
	#Asignacion de parametros
	Pila[t52] = t50
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t53 = P+2
	t54 = Pila[t53]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t55 = "SELECT now() ;"
	#Entrar al ambito
	t56 = P+2
	#parametro 1
	t57 = t56+1
	#Asignacion de parametros
	Pila[t57] = t55
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t58 = P+2
	t59 = Pila[t58]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t60 = "SELECT EXTRACT (HOUR FROM TIMESTAMP '2001-02-16 20:38:40') ;"
	#Entrar al ambito
	t61 = P+2
	#parametro 1
	t62 = t61+1
	#Asignacion de parametros
	Pila[t62] = t60
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t63 = P+2
	t64 = Pila[t63]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t65 = "SELECT EXTRACT (MINUTE FROM TIMESTAMP '2001-02-16 20:38:40') ;"
	#Entrar al ambito
	t66 = P+2
	#parametro 1
	t67 = t66+1
	#Asignacion de parametros
	Pila[t67] = t65
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t68 = P+2
	t69 = Pila[t68]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t70 = "SELECT EXTRACT (SECOND FROM TIMESTAMP '2001-02-16 20:38:40') ;"
	#Entrar al ambito
	t71 = P+2
	#parametro 1
	t72 = t71+1
	#Asignacion de parametros
	Pila[t72] = t70
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t73 = P+2
	t74 = Pila[t73]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t75 = "SELECT EXTRACT (YEAR FROM TIMESTAMP '2001-02-16 20:38:40') ;"
	#Entrar al ambito
	t76 = P+2
	#parametro 1
	t77 = t76+1
	#Asignacion de parametros
	Pila[t77] = t75
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t78 = P+2
	t79 = Pila[t78]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t80 = "SELECT EXTRACT (MONTH FROM TIMESTAMP '2001-02-16 20:38:40') ;"
	#Entrar al ambito
	t81 = P+2
	#parametro 1
	t82 = t81+1
	#Asignacion de parametros
	Pila[t82] = t80
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t83 = P+2
	t84 = Pila[t83]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t85 = "SELECT EXTRACT (DAY FROM TIMESTAMP '2001-02-16 20:38:40') ;"
	#Entrar al ambito
	t86 = P+2
	#parametro 1
	t87 = t86+1
	#Asignacion de parametros
	Pila[t87] = t85
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t88 = P+2
	t89 = Pila[t88]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t90 = "SELECT date_part('minutes', INTERVAL '4 hours 3 minutes') ;"
	#Entrar al ambito
	t91 = P+2
	#parametro 1
	t92 = t91+1
	#Asignacion de parametros
	Pila[t92] = t90
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t93 = P+2
	t94 = Pila[t93]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t95 = "SELECT date_part('seconds', INTERVAL '4 hours 3 minutes 15 seconds') ;"
	#Entrar al ambito
	t96 = P+2
	#parametro 1
	t97 = t96+1
	#Asignacion de parametros
	Pila[t97] = t95
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t98 = P+2
	t99 = Pila[t98]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t100 = "SELECT CURRENT_DATE ;"
	#Entrar al ambito
	t101 = P+2
	#parametro 1
	t102 = t101+1
	#Asignacion de parametros
	Pila[t102] = t100
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t103 = P+2
	t104 = Pila[t103]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t105 = "SELECT CURRENT_TIME ;"
	#Entrar al ambito
	t106 = P+2
	#parametro 1
	t107 = t106+1
	#Asignacion de parametros
	Pila[t107] = t105
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t108 = P+2
	t109 = Pila[t108]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t110 = "SELECT TIMESTAMP 'now' ;"
	#Entrar al ambito
	t111 = P+2
	#parametro 1
	t112 = t111+1
	#Asignacion de parametros
	Pila[t112] = t110
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t113 = P+2
	t114 = Pila[t113]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t115 = "SELECT 'VALIDA Funciones Date-Extract' ;"
	#Entrar al ambito
	t116 = P+2
	#parametro 1
	t117 = t116+1
	#Asignacion de parametros
	Pila[t117] = t115
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t118 = P+2
	t119 = Pila[t118]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t120 = "create type area as enum (  'CONTABILIDAD', 'ADMINISTRACION', 'VENTAS', 'TECNOLOGIA', 'FABRICA');"
	#Entrar al ambito
	t121 = P+2
	#parametro 1
	t122 = t121+1
	#Asignacion de parametros
	Pila[t122] = t120
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t123 = P+2
	t124 = Pila[t123]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t125 = "SELECT 'VALIDA TYPE' ;"
	#Entrar al ambito
	t126 = P+2
	#parametro 1
	t127 = t126+1
	#Asignacion de parametros
	Pila[t127] = t125
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t128 = P+2
	t129 = Pila[t128]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t130 = "show databases;"
	#Entrar al ambito
	t131 = P+2
	#parametro 1
	t132 = t131+1
	#Asignacion de parametros
	Pila[t132] = t130
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t133 = P+2
	t134 = Pila[t133]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t135 = "SELECT 'VALIDA SHOW DATBASE' ;"
	#Entrar al ambito
	t136 = P+2
	#parametro 1
	t137 = t136+1
	#Asignacion de parametros
	Pila[t137] = t135
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t138 = P+2
	t139 = Pila[t138]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t140 = "drop database if exists califica2;"
	#Entrar al ambito
	t141 = P+2
	#parametro 1
	t142 = t141+1
	#Asignacion de parametros
	Pila[t142] = t140
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t143 = P+2
	t144 = Pila[t143]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t145 = "SELECT 'VALIDA DROP DATABASE' ;"
	#Entrar al ambito
	t146 = P+2
	#parametro 1
	t147 = t146+1
	#Asignacion de parametros
	Pila[t147] = t145
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t148 = P+2
	t149 = Pila[t148]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t150 = "drop table tbroles;"
	#Entrar al ambito
	t151 = P+2
	#parametro 1
	t152 = t151+1
	#Asignacion de parametros
	Pila[t152] = t150
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t153 = P+2
	t154 = Pila[t153]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t155 = "SELECT 'VALIDA DROP TABLES' ;"
	#Entrar al ambito
	t156 = P+2
	#parametro 1
	t157 = t156+1
	#Asignacion de parametros
	Pila[t157] = t155
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t158 = P+2
	t159 = Pila[t158]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t160 = "Create table tbrol ( idrol integer not null primary key, rol varchar(15));"
	#Entrar al ambito
	t161 = P+2
	#parametro 1
	t162 = t161+1
	#Asignacion de parametros
	Pila[t162] = t160
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t163 = P+2
	t164 = Pila[t163]
	#Salida de funcion
	P = P-2
>>>>>>> 48cd4d37c23a2e7ba9edcfefe53ef801055b5866
if __name__ == "__main__":
	main()