from goto import with_goto
import sys
global Apuntador
global PILAOHEAP
Apuntador = 0
PILAOHEAP = [None] * 1000

def funcionintermedia():
	#recibir una cadena "use bd1" o "create databases1" o "insert ..."
	global Apuntador
	global PILAOHEAP
	t10 = Apuntador+0 # el 0 es la posicion del return
	t11 = t10+1  #el 1 es la posicion de parametro
	t12 = PILAOHEAP[t11]
	t13 = t10+2 #el 2 es la posicion de parametro
	t14 = PILAOHEAP[t13]
	print(t12)
	print(t14)
	#funciones(param1, param2, p...)
    #cadena = "use bd1" o "create databases1" o "insert ..."
	res = "esta es una respuesta desde la funcion intermediaria"
	PILAOHEAP[t10] = res


@with_goto  # Decorador necesario.
def main():
	global Apuntador
	global PILAOHEAP
	#Asignar cadena
	t0 = "use bd1;"
	t1 = "aqui iria un insert;"
	#Entrar al ambito
	t2 = Apuntador+2 #el tamaño de la función 0 return 1 parametro1 2 parametro2
	#parametro 1
	t3 = t2+1  #el 1 es la posicion de parametro
	#Asignacion de parametros
	PILAOHEAP[t3] = t0
	#parametro 2
	t4 = t2+2  #el 2 es la posicion de parametro
	#Asignacion de parametros
	PILAOHEAP[t4] = t1
	#Llamada de funcion
	Apuntador = Apuntador+2
	funcionintermedia()
	#obtener resultado
	t5 = Apuntador+0 # el 0 es la posicion del return
	t6 = PILAOHEAP[t5]
	#Salida de funcion
	Apuntador = Apuntador-2
	print(t6)


if __name__ == "__main__":
	main()