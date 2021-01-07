from InstruccionesDGA import tabla as ts
from datetime import date
from InstruccionesDGA import cont as contador
from InstruccionesDGA import NombreDB
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt


pila = []
for i in range(100):
    pila.append(i)

def ejecutar():
    cont = contador
	
	sql.execute("CREATE DATABASE ayuda;")
	n_db = ts.buscarIDTB(NombreDB)
	NuevoSimbolo = TAS.Simbolo(cont,'CALCULOS',TAS.TIPO.FUNCTION,n_db)
	ts.agregar(NuevoSimbolo)
	cont+=1

	ambitoFuncion =  ts.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'SENO',TAS.TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	ts.agregar(NuevoSimbolo)
	cont+=1

	ambitoFuncion =  ts.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'VALOR',TAS.TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	ts.agregar(NuevoSimbolo)
	cont+=1


	ambitoFuncion =  ts.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'ABSOLUTO',TAS.TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	ts.agregar(NuevoSimbolo)
	cont+=1

	ts.modificar_valor(hora, 999.0)
	ts.modificar_valor(SENO, 999.0)
	ts.modificar_valor(texto, 'fase 2')
	ts.modificar_valor(VALOR, 999.0)
	ts.modificar_valor(VALOR, 6)
	ts.modificar_valor(ABSOLUTO, 1.1752011936438014)
	ts.modificar_valor(ABSOLUTO, 75.0)
	ts.modificar_valor(VALOR, 20.0)
	ts.modificar_valor(VALOR, 10.0)

	print( 'Funcion CALCULOSno existe')
	n_db = ts.buscarIDTB(NombreDB)
	NuevoSimbolo = TAS.Simbolo(cont,'ayuda',TAS.TIPO.FUNCTION,n_db)
	ts.agregar(NuevoSimbolo)
	cont+=1

	ambitoFuncion =  ts.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'SENO',TAS.TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	ts.agregar(NuevoSimbolo)
	cont+=1

	ambitoFuncion =  ts.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'VALOR',TAS.TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	ts.agregar(NuevoSimbolo)
	cont+=1


	ambitoFuncion =  ts.buscarIDF()
	NuevoSimbolo = TAS.Simbolo(cont,'ABSOLUTO',TAS.TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None, None,False,False)
	ts.agregar(NuevoSimbolo)
	cont+=1

	ts.modificar_valor(hora, 999.0)
	ts.modificar_valor(SENO, 999.0)
	ts.modificar_valor(texto, 'fase 2')
	ts.modificar_valor(VALOR, 999.0)
	ts.modificar_valor(VALOR, 6)
	ts.modificar_valor(ABSOLUTO, 1.1752011936438014)
	ts.modificar_valor(ABSOLUTO, 75.0)
	ts.modificar_valor(VALOR, 20.0)
	ts.modificar_valor(VALOR, 10.0)

	n_db = ts.buscarIDTB(NombreDB)
	NuevoSimbolo = TAS.Simbolo(cont,'myFuncion',TAS.TIPO.FUNCTION,n_db)
	ts.agregar(NuevoSimbolo)
	cont+=1

t33 = 'INICIO CALIFICACION FASE 2'
pila[0] = t33
myFuncion()
print(pila[10])
	sql.execute('3D')

def ayuda():
	
	SENO = 0
	VALOR = 0
	
	ABSOLUTO = 0
	nombre = pila[0]
	t17 = 999
	hora = t17
	
	t18 = 999
	SENO = t18
	
	t19 = 'fase 2'
	texto = t19
	
	t20 = 999
	VALOR = t20
	
	t21 = texto
	
	
	VALOR = len(str(t21))
	
	t22 = -1
	
	
	ABSOLUTO = abs(mt.sinh(t22))
	
	t23 = 5
	t24 = 225
	
	t25 = t23 * mt.sqrt(float(t24))
	ABSOLUTO = t25
	
	t26 = VALOR
	
	t27 = 1
	t28 = t26 > t27
	
	if t28:
		t29 = 20
		VALOR = t29
		
	else:
		t30 = 10
		VALOR = t30
		
	
	t31 = VALOR
	
	pila[10] = t31
	
def myFuncion():
	texto = pila[0]
	t32 = texto
	
	pila[10] = t32
	
ejecutar()