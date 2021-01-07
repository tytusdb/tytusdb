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
	n_db = tabla.buscarIDTB(NombreDB)
	NuevoSimbolo = Simbolo(cont,'CALCULOS',TIPO.FUNCTION,n_db)
	cont+=1

	ambitoFuncion =  tabla.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'SENO',TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	tabla.agregar(NuevoSimbolo)
	cont+=1

	ambitoFuncion =  tabla.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'VALOR',TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	tabla.agregar(NuevoSimbolo)
	cont+=1


	ambitoFuncion =  tabla.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'ABSOLUTO',TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	tabla.agregar(NuevoSimbolo)
	cont+=1

	tabla.modificar_valor(hora, 999.0)
	tabla.modificar_valor(SENO, 999.0)
	tabla.modificar_valor(texto, 'fase 2')
	tabla.modificar_valor(VALOR, 999.0)
	tabla.modificar_valor(VALOR, 6)
	tabla.modificar_valor(ABSOLUTO, 1.1752011936438014)
	tabla.modificar_valor(ABSOLUTO, 75.0)
	tabla.modificar_valor(VALOR, 20.0)
	tabla.modificar_valor(VALOR, 10.0)

def CALCULOS():
	
	SENO = 0
	VALOR = 0
	
	ABSOLUTO = 0
	nombre = pila[0]
	t1 = 999
	hora = t1
	
	t2 = 999
	SENO = t2
	
	t3 = 'fase 2'
	texto = t3
	
	t4 = 999
	VALOR = t4
	
	t5 = texto
	
	
	VALOR = len(str(t5))
	
	t6 = -1
	
	
	ABSOLUTO = abs(mt.sinh(t6))
	
	t7 = 5
	t8 = 225
	
	t9 = t7 * mt.sqrt(float(t8))
	ABSOLUTO = t9
	
	t10 = VALOR
	
	t11 = 1
	t12 = t10 > t11
	
	if t12:
		t13 = 20
		VALOR = t13
		
	else:
		t14 = 10
		VALOR = t14
		
	
	t15 = VALOR
	
	pila[10] = t15
	
ejecutar()