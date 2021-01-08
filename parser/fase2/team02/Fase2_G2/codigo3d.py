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

	t45 = P+0
	t46 = Pila[t45]
	t45 = t45+1
	t47 = Pila[t45]
	#Asignar cadena
	t48 = " delete from tbProducto   where  producto = 'WIFI USB';"
	#Entrar al ambito
	t49 = P+2
	#parametro 1
	t50 = t49+1
	#Asignacion de parametros
	Pila[t50] = t48
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t51 = P+2
	t52 = Pila[t51]
	#Salida de funcion
	P = P-2
def ValidaRegistros2(): 
	global P

	global Pila

	t53 = P+0
	t54 = Pila[t53]
	t53 = t53+1
	t55 = Pila[t53]
	#Asignar cadena
	t56 = " update  tbProducto set estado= 4  where  idproducto = 4;"
	#Entrar al ambito
	t57 = P+2
	#parametro 1
	t58 = t57+1
	#Asignacion de parametros
	Pila[t58] = t56
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t59 = P+2
	t60 = Pila[t59]
	#Salida de funcion
	P = P-2
	#Asignar cadena
	t61 = "select * from tbProducto ;"
	#Entrar al ambito
	t62 = P+2
	#parametro 1
	t63 = t62+1
	#Asignacion de parametros
	Pila[t63] = t61
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t64 = P+2
	t65 = Pila[t64]
	#Salida de funcion
	P = P-2
def main():
	global P
	global Pila
	#Asignar cadena
	t0 = " Create table tbProducto(idproducto integer  not null primary key, producto varchar (150) not null, fechacreacion date  not null, estado integer );"
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
	t5 = " insert into tbProducto values( 1, 'Laptop Lenovo', '2021-01-07 17:08:08', 1) ;" 
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
	t10 = " insert into tbProducto values( 2, 'Bateria para Laptop Lenovo T420', '2021-01-07 17:08:08', 1) ;" 
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
	t15 = " insert into tbProducto values( 3, 'Teclado Inalambrico', '2021-01-07 17:08:08', 1) ;" 
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
	t20 = " insert into tbProducto values( 4, 'Mouse Inalambrico', '2021-01-07 17:08:08', 1) ;" 
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
	t25 = " insert into tbProducto values( 5, 'WIFI USB', '2021-01-07 17:08:08', 1) ;" 
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
	t30 = " insert into tbProducto values( 6, 'Laptop HP', '2021-01-07 17:08:08', 1) ;" 
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
	t35 = " insert into tbProducto values( 7, 'Teclado Flexible USB', '2021-01-07 17:08:08', 1) ;" 
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
	t40 = " insert into tbProducto values( 8, 'Laptop Samsung', '2021-01-02', 1) ;" 
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
	t66 = P+1
	t67 = 'tbProducto'
	#Asignacion de parametro a pila
	t66 = t66+1
	Pila[t66] = t67
	t68 = 3
	#Asignacion de parametro a pila
	t66 = t66+1
	Pila[t66] = t68
	#Llamada de funcion
	P = P+2
	ValidaRegistros()
	P = P-2
	#Salida de funcion
	#obtener resultado
	t69 = P+2
	t70 = Pila[t69]
	print(t70) 
	#Entrar al ambito
	t71 = P+2
	#parametro 1
	t72 = t71+1
	#Asignacion de parametros
	Pila[t72] ="print('"+str(t70)+"');"
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t73 = P+2
	t74 = Pila[t73]
	#Salida de funcion
	P = P-2
	t75 = P+1
	t76 = 'tbProducto'
	#Asignacion de parametro a pila
	t75 = t75+1
	Pila[t75] = t76
	t77 = 3
	#Asignacion de parametro a pila
	t75 = t75+1
	Pila[t75] = t77
	#Llamada de funcion
	P = P+2
	ValidaRegistros2()
	P = P-2
	#Salida de funcion
	#obtener resultado
	t78 = P+2
	t79 = Pila[t78]
	print(t79) 
	#Entrar al ambito
	t80 = P+2
	#parametro 1
	t81 = t80+1
	#Asignacion de parametros
	Pila[t81] ="print('"+str(t79)+"');"
	#Llamada de funcion
	P = P+2
	funcionintermedia()
	#obtener resultado
	t82 = P+2
	t83 = Pila[t82]
	#Salida de funcion
	P = P-2
if __name__ == "__main__":
	start()
	main()
