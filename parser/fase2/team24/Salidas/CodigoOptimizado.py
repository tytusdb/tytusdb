
from datetime import date
from variables import tabla as ts
from variables import NombreDB 
from variables import cont 
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt
from reportTable import *
    
    
pila = []
for i in range(100):
    pila.append(i)
    
def ejecutar():
	global cont
	global ts
	NombreDB = ts.nameDB

	n_db = ts.buscarIDTB(NombreDB)
	NuevoSimbolo = TAS.Simbolo(cont,'myFuncion',TAS.TIPO.FUNCTION,n_db)
	ts.agregar(NuevoSimbolo)
	cont+=1

	texto = pila[0]

t0 = texto
t1 = 2
pila[0] = t1

myFuncion()
t2 = pila[10]

t3 = 2
pila[0] = t3

myFuncion()
t4 = pila[10]

ejecutar()