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
	NuevoSimbolo = Simbolo(cont,'CALCULOS',TIPO.FUNCTION,n_db)
	cont+=1

	ambitoFuncion =  buscarIDF(cont)
	NuevoSimbolo = TAS.Simbolo(cont,'SENO',TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	tabla.agregar(NuevoSimbolo)
	cont+=1

	ambitoFuncion =  buscarIDF(cont)
	NuevoSimbolo = TAS.Simbolo(cont,'VALOR',TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	tabla.agregar(NuevoSimbolo)
	cont+=1


	ambitoFuncion =  buscarIDF(cont)
	NuevoSimbolo = TAS.Simbolo(cont,'ABSOLUTO',TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	tabla.agregar(NuevoSimbolo)
	cont+=1

	tabla.modificar_valor(hora, t0)
	tabla.modificar_valor(SENO, t1)
	tabla.modificar_valor(texto, t2)
	tabla.modificar_valor(VALOR, t3)
	tabla.modificar_valor(VALOR, len(str(t4)))
	tabla.modificar_valor(ABSOLUTO, abs(mt.sinh(t5)))
	tabla.modificar_valor(ABSOLUTO, t8)
	tabla.modificar_valor(VALOR, t12)
	tabla.modificar_valor(VALOR, t13)

	n_db = tabla.id_db(NombreDB)
	NuevoSimbolo = Simbolo(cont,'ayuda',TIPO.FUNCTION,n_db)
	cont+=1


def CALCULOS():
	
	SENO = 0
	VALOR = 0
	
	ABSOLUTO = 0
	nombre = pila[0]
	t0 = 999
	hora = t0
	
	t1 = 999
	SENO = t1
	
	t2 = 'fase 2'
	texto = t2
	
	t3 = 999
	VALOR = t3
	
	t4 = texto
	
	
	VALOR = len(str(t4))
	
	t5 = -1
	
	
	ABSOLUTO = abs(mt.sinh(t5))
	
	t6 = 5
	t7 = 225
	
	t8 = t6 * mt.sqrt(float(t7))
	ABSOLUTO = t8
	
	t9 = VALOR
	
	t10 = 1
	t11 = t9 > t10
	
	if t11:
		t12 = 20
		VALOR = t12
		
	else:
		t13 = 10
		VALOR = t13
		
	
	t14 = VALOR
	
	pila[10] = t14
	
def ayuda():
	
	aas = pila[0]
	t15 = aas
	
	pila[10] = t15
	NuevoSimbolo = Simbolo(cont,sp_validainsert,TIPO.FUNCTION,n_db)
	cont+=1
 insert into tbbodega  values ( 1 BODEGA CENTRAL 1 ) ; insert into tbbodega idbodega bodega values ( 2 BODEGA ZONA 12 ) ; insert into tbbodega ( idbodega, bodega) estado values ( 3 BODEGA ZONA 11 1 ) ; insert into tbbodega ( idbodega, bodega) estado values ( 4 BODEGA ZONA 1 1 ) ; insert into tbbodega ( idbodega, bodega) estado values ( 5 BODEGA ZONA 10 1 ) ;def sp_validainsert():
	
	
	
	
	
ejecutar() 