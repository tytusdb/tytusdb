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
def ValidaRegistros(): 
	global P

	global Pila

	t0 = P+0
	#Comienza instruccion de expresion
	#Asignar variable
	t1 =  9
	#se coloca el dato en la posicion de la pila
	t2 = 0
	#Asignacion de parametros a la posicion de parametro
	Pila[t2] = t1
	#Comienza instruccion de expresion
	#Asignar variable
	t3 =  49
	#se coloca el dato en la posicion de la pila
	t4 = 0
	#Asignacion de parametros a la posicion de parametro
	Pila[t4] = t3
	#Asignar cadena
	t5 = " Create table mr(id integer  primary key, precio integer );"
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
	t10 = "select * from tabli;"
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
	#Comienza instruccion de expresion
	t15 = P+0
	Pila[t15] = t1
def main():
	global P
	global Pila
	#Llamada de funcion
	P = P+2
	ValidaRegistros()
	P = P-2
	#Salida de funcion
	#obtener resultado
	t16 = P+2
	t17 = Pila[t16]
	print(t17) 
if __name__ == "__main__":
	main()
