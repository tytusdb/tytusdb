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
def main():
	global P
	global Pila
	#Asignar Cadena
	t0="show databases; "
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
if __name__ == "__main__":
	main()
