from InstruccionesDGA import tabla 
from datetime import date
from InstruccionesDGA import cont 
from InstruccionesDGA import NombreDB
from tablaDGA import *
from sql import * 
import mathtrig as mt
#Funcion sql.execute

pila = []
for i in range(100):
    pila.append(i)

def ejecutar(): 
	n_db = tabla.id_db(NombreDB)
	NuevoSimbolo = Simbolo(cont,myFuncion,TIPO.FUNCTION,n_db)
	cont+=1

	tabla.modificar_valor(res, t15)
	tabla.modificar_valor(color, t16)
	tabla.modificar_valor(identificador, today.strftime("%Y-%m-%d %H:%M:%S"))
	tabla.modificar_valor(res, t25)

	n_db = tabla.id_db(NombreDB)
	NuevoSimbolo = Simbolo(cont,segunda,TIPO.FUNCTION,n_db)
	cont+=1

	tabla.modificar_valor(res, t42)
	tabla.modificar_valor(color, t43)
	tabla.modificar_valor(identificador, today.strftime("%Y-%m-%d %H:%M:%S"))
	tabla.modificar_valor(res, t52)

def myFuncion():
	
	texto = pila[0]
	identificador = pila[1]
	t9 = identificador
	
	t10 = 0
	t11 = t9 < t10
	
	t12 = color
	
	t13 = 'negative'
	t14 = t12 == t13
	
	if t11:
		t15 = 0
		res = t15
		
	elif t14 :
		t16 = 'positive'
		color = t16
		
	else:
		
		today = date.today()
		identificador = today.strftime("%Y-%m-%d %H:%M:%S")
		
	
	t17 = 9
	t18 = 8
	t19 = t17 + t18
	t20 = 7
	t21 = t19 - t20
	t22 = 6
	t23 = t21 * t22
	t24 = 5
	t25 = t23 / t24
	
	res = t25
	
	t26 = texto
	
	pila[10] = t26
	
def segunda():
	
	texto = pila[0]
	identificador = pila[1]
	t36 = identificador
	
	t37 = 0
	t38 = t36 < t37
	
	t39 = color
	
	t40 = 'negative'
	t41 = t39 == t40
	
	if t38:
		t42 = 0
		res = t42
		
	elif t41 :
		t43 = 'positive'
		color = t43
		
	else:
		
		today = date.today()
		identificador = today.strftime("%Y-%m-%d %H:%M:%S")
		
	
	t44 = 9
	t45 = 8
	t46 = t44 + t45
	t47 = 7
	t48 = t46 - t47
	t49 = 6
	t50 = t48 * t49
	t51 = 5
	t52 = t50 / t51
	
	res = t52
	
	t53 = texto
	
	pila[10] = t53
	
ejecutar() 