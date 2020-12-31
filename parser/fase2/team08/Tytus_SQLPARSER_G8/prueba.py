from goto import with_goto
import sys
global P
global Pila
P = 0
Pila = [None] * 1000
def funcionintermedia():
	global P
	global Pila
	t0 = P+0
	t1 = t0+1
	t2 = Pila[t1]
	print(t2)
@with_goto  # Decorador necesario.
def main():
	global P
	global Pila
	#Asignar cadena
	t0 = "create or replace if not exists bd1 ;"
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
	t5 = "create or replace if not exists bd1 owner = hola ;"
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
	t10 = "create or replace if not exists bd1 owner = hola mode = 10;"
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
	t15 = "create or replace if not exists bd1 owner = 10 ;"
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
	t20 = "create or replace bd1 ;"
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
	t25 = "create or replace bd1 owner = hola ;"
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
	t30 = "create or replace bd1 owner = hola mode = 10;"
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
	t35 = "create or replace bd1 owner = 10 ;"
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
if __name__ == "__main__":
	main()