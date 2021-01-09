from goto import with_goto
import math
from sintactico import *
import reportes.reportesimbolos as rs
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.TablaSimbolos.Arbol import Arbol
from storageManager.jsonMode import *
import sys
global P
global Pila
P = 0
Pila = [None] * 1000
tablaGlobal = Tabla(None)
global sql
global inst
arbol = Arbol(None)
def funcionintermedia():
	global P
	global Pila
	t0 = P+0
	t1 = t0+1
	t2 = Pila[t1]
	print("\n"+'\033[96m'+t2+'\033[0m')
	sql = Pila[t1]
	instrucciones = ejecutar_analisis(sql)
	for instruccion in instrucciones:
		t3 = instruccion.ejecutar(tablaGlobal,arbol)
	t4 = P+0
	t5 = t0+2
	Pila[t5] = t3
	for msj in arbol.consola:
		print(f"{msj}")
	arbol.consola = []
	@with_goto  # Decorador necesario.
	def ValidaRegistros():
	global P
	global Pila
	# Inicia If
	#Obtiene id: tabla
	t0 = P + 1
	t1 = Pila[t0]
	if(t1 == 'tbProducto'):
		goto .l1
	goto .l2
	label .l1
	#Inicia asignación: resultado
	t2 = P + 3
	#Se obtiene el valor
	t3 = 12
	Pila[t2] = t3
	#Fin Asignación
	# Inicia If
	#Obtiene id: cantidad
	t4 = P + 2
	t5 = Pila[t4]
	#Obtiene id: resultado
	t6 = P + 3
	t7 = Pila[t6]
	if(t5 == t7):
		goto .l4
	goto .l5
	label .l4
	#Inicia asignación: retorna
	t8 = P + 4
	#Se obtiene el valor
	t9 = 1
	Pila[t8] = t9
	#Fin Asignación
	goto .l6
	label .l5
	#Inicia asignación: retorna
	t10 = P + 4
	#Se obtiene el valor
	t11 = 0
	Pila[t10] = t11
	#Fin Asignación
	label .l6
	goto .l3
	label .l2
	label .l3
	# Inicia If
	#Obtiene id: tabla
	t12 = P + 1
	t13 = Pila[t12]
	if(t13 == 'tbProductoUp'):
		goto .l7
	goto .l8
	label .l7
	#Inicia asignación: resultado
	t14 = P + 3
	#Se obtiene el valor
	t15 = 12
	Pila[t14] = t15
	#Fin Asignación
	# Inicia If
	#Obtiene id: cantidad
	t16 = P + 2
	t17 = Pila[t16]
	#Obtiene id: resultado
	t18 = P + 3
	t19 = Pila[t18]
	if(t17 == t19):
		goto .l10
	goto .l11
	label .l10
	#Inicia asignación: retorna
	t20 = P + 4
	#Se obtiene el valor
	t21 = 1
	Pila[t20] = t21
	#Fin Asignación
	goto .l12
	label .l11
	#Inicia asignación: retorna
	t22 = P + 4
	#Se obtiene el valor
	t23 = 0
	Pila[t22] = t23
	#Fin Asignación
	label .l12
	goto .l9
	label .l8
	label .l9
	# Inicia If
	#Obtiene id: tabla
	t24 = P + 1
	t25 = Pila[t24]
	if(t25 == 'tbbodega'):
		goto .l13
	goto .l14
	label .l13
	#Inicia asignación: resultado
	t26 = P + 3
	#Se obtiene el valor
	t27 = 12
	Pila[t26] = t27
	#Fin Asignación
	# Inicia If
	#Obtiene id: cantidad
	t28 = P + 2
	t29 = Pila[t28]
	#Obtiene id: resultado
	t30 = P + 3
	t31 = Pila[t30]
	if(t29 == t31):
		goto .l16
	goto .l17
	label .l16
	#Inicia asignación: retorna
	t32 = P + 4
	#Se obtiene el valor
	t33 = 1
	Pila[t32] = t33
	#Fin Asignación
	goto .l18
	label .l17
	#Inicia asignación: retorna
	t34 = P + 4
	#Se obtiene el valor
	t35 = 0
	Pila[t34] = t35
	#Fin Asignación
	label .l18
	goto .l15
	label .l14
	label .l15
	#Se asigna el valor a la posición de return
	#Obtiene id: retorna
	t36 = P + 4
	t37 = Pila[t36]
	t38 = P + 0
	Pila[t38] = t37
	goto .l0
	#Etiqueta de salida función
	label .l0

def main():
	dropAll()
	global P
	global Pila
	#Asignar cadena
	t0 = "create database DBFase2 mode = 1;"
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
	t5 = "use DBFase2;"
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
	t10 = "Create table tbProducto ( idproducto integer not null primary key, producto varchar(150) not null, fechacreacion date not null, estado integer ) ;"
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
	t15 = f"insert into tbProducto values ( 1, 'Laptop Lenovo', now(), 1 );"
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
	t20 = f"insert into tbProducto values ( 2, 'Bateria para Laptop Lenovo T420', now(), 1 );"
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
	t25 = f"insert into tbProducto values ( 3, 'Teclado Inalambrico', now(), 1 );"
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
	t30 = f"insert into tbProducto values ( 4, 'Mouse Inalambrico', now(), 1 );"
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
	t35 = f"insert into tbProducto values ( 5, 'WIFI USB', now(), 1 );"
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
	t40 = f"insert into tbProducto values ( 6, 'Laptop HP', now(), 1 );"
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
	t45 = f"insert into tbProducto values ( 7, 'Teclado Flexible USB', now(), 1 );"
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
	t50 = f"insert into tbProducto values ( 8, 'Laptop Samsung', '2021-01-02', 1 );"
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
	t55 = "Create table tbCalificacion ( idcalifica integer not null primary key, item varchar(100) not null, punteo integer not null ) ;"
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
	t60 = f"SELECT * FROM tbProducto  ;"
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
	#Simulando el paso de parámetros
	t65 = P + 5
	#Asignación de parámetros
	t66 = t65 + 1
	Pila[t66] = 'tbProducto'
	t67 = t65 + 2
	Pila[t67] = 8
	#Cambio de ámbito
	P = P + 5
	#Llamada a la función
	ValidaRegistros()
	#Posición del return en el ámbito de la función
	t68 = t65 + 0
	t69 = Pila[t68]
	P = P - 5
	#Asignar cadena
	t70 = f"insert into tbCalificacion values ( 1, 'Create Table and Insert', "+ str(t69) + "  );"
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
if __name__ == "__main__":
	main()
	rs.crear_tabla(arbol)