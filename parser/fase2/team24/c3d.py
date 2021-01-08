
from datetime import date
from variables import tabla as ts
from variables import NombreDB 
from variables import cont as ncont
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt
from reportTable import *

cont = ncont
pila = []
for i in range(100):
    pila.append(i)

def ejecutar():
    global cont
	
	sql.execute("CREATE DATABASE local;")
	n_db = ts.buscarIDTB(NombreDB)
	NuevoSimbolo = TAS.Simbolo(cont,'ValidaRegistros',TAS.TIPO.FUNCTION,n_db)
	ts.agregar(NuevoSimbolo)
	cont+=1
	ambitoFuncion =  ts.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'resultado',TAS.TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	ts.agregar(NuevoSimbolo)
	cont+=1

	ambitoFuncion =  ts.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'retorna',TAS.TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	ts.agregar(NuevoSimbolo)
	cont+=1

	ts.modificar_valor('resultado', 7777.0)
	ts.modificar_valor('retorna', 1.0)
	ts.modificar_valor('retorna', 0.0)
	ts.modificar_valor('resultado', 8888.0)
	ts.modificar_valor('retorna', 1.0)
	ts.modificar_valor('retorna', 0.0)
	ts.modificar_valor('resultado', 9999.0)
	ts.modificar_valor('retorna', 1.0)
	ts.modificar_valor('retorna', 0.0)

	sql.execute('3D')

	graphTable(ts)
def ValidaRegistros():
	resultado = 0
	retorna = 0
	tabla = pila[0]
	cantidad = pila[1]
	t0 = tabla
	
	t1 = 'tbProducto'
	t2 = t0 == t1
	
	if t2:
		t3 = 7777
		resultado = t3
		
		t4 = cantidad
		
		t5 = resultado
		
		t6 = t4 == t5
		
		if t6:
			t7 = 1
			retorna = t7
			
		else:
			t8 = 0
			retorna = t8
			
		
	
	t9 = tabla
	
	t10 = 'tbProductoUp'
	t11 = t9 == t10
	
	if t11:
		t12 = 8888
		resultado = t12
		
		t13 = cantidad
		
		t14 = resultado
		
		t15 = t13 == t14
		
		if t15:
			t16 = 1
			retorna = t16
			
		else:
			t17 = 0
			retorna = t17
			
		
	
	t18 = tabla
	
	t19 = 'tbbodega'
	t20 = t18 == t19
	
	if t20:
		t21 = 9999
		resultado = t21
		
		t22 = cantidad
		
		t23 = resultado
		
		t24 = t22 == t23
		
		if t24:
			t25 = 1
			retorna = t25
			
		else:
			t26 = 0
			retorna = t26
			
		
	
	t27 = retorna
	
	pila[10] = t27
	
ejecutar()