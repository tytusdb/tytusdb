import sys
global P
global Pila
P = 0
Pila = [None] * 1000

def start():
	f = open ("dataanalizado/traducido0.txt", "w")
	f.write("")
	f.close()
def agregar(texto):
	try:
		f = open ("dataanalizado/traducido0.txt", "a")
		f.write(str(texto))
		f.close()
	except Exception as e:
		print(e)

def funcionintermedia():
	global P
	global Pila
	t0 = P+0
	t1 = t0+1
	t2 = Pila[t1]
	print(t2)
	agregar(t2)
def ValidaRegistros(): 
	global P

	global Pila

	t0 = P+0
	t1 = Pila[t0]
	t0 = t0+1
	t2 = Pila[t0]
	#Comienza instruccion de expresion
	#Asignar variable
	t3 =  1002
	#se coloca el dato en la posicion de la pila
	t4 = 0
	#Asignacion de parametros a la posicion de parametro
	Pila[t4] = t3
	#Comienza instruccion de expresion
	#Comienza instruccion de expresion
	#Asignar variable
	t5 =  1007
	#se coloca el dato en la posicion de la pila
	t6 = 0
	#Asignacion de parametros a la posicion de parametro
	Pila[t6] = t5
	#Comienza instruccion de Return
	t7 =  1007
	t8 = P+0
	Pila[t8] = t7
def main():
	global P
	global Pila
	#Asignar cadena
	t9 = " Create table tbCalificacion(idcalifica integer  not null primary key, item varchar (100) not null, punteo integer  not null);"
	#Entrar al ambito
	t10 = P+2
	#parametro 1
	t11 = t10+1
	#Asignacion de parametros
	Pila[t11] = t9
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t12 = P+2
	t13 = Pila[t12]
	#Salida de funcion
	P = P-2
	t14 = P+1
	t15 = 'house'
	#Asignacion de parametro a pila
	t14 = t14+1
	Pila[t14] = t15
	t16 = 9
	#Asignacion de parametro a pila
	t14 = t14+1
	Pila[t14] = t16
	#Llamada de funcion
	P = P+2
	ValidaRegistros()
	P = P-2
	#Salida de funcion
	#obtener resultado
	t17 = P+2
	t18 = Pila[t17]
	print(t18) 
	#Entrar al ambito
	t19 = P+2
	#parametro 1
	t20 = t19+1
	#Asignacion de parametros
	Pila[t20] ="print('"+str(t18)+"');"
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t21 = P+2
	t22 = Pila[t21]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t23 = " insert into tbCalificacion values( 'Update', "+str(t18)+") ;" 
	#Entrar al ambito
	t24 = P+2
	#parametro 1
	t25 = t24+1
	#Asignacion de parametros
	Pila[t25] = t23
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t26 = P+2
	t27 = Pila[t26]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t28 = "select * from tbCalificacion ;"
	#Entrar al ambito
	t29 = P+2
	#parametro 1
	t30 = t29+1
	#Asignacion de parametros
	Pila[t30] = t28
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t31 = P+2
	t32 = Pila[t31]
	#Salida de funcion
	P = P-2
if __name__ == "__main__":
	start()
	main()
