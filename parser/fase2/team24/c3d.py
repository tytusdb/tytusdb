from InstruccionesDGA import tabla as ts
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
	
	sql.execute("CREATE DATABASE DBFase2;")
	sql.execute("USE DATABASE DBFase2";)
	n_db = ts.buscarIDTB(NombreDB)
	NuevoSimbolo = TAS.Simbolo(cont,'myFuncion',TAS.TIPO.FUNCTION,n_db)
	ts.agregar(NuevoSimbolo)
	cont+=1
	ts.modificar_valor('texto', 0)
	sql.execute("CREATE TABLE tbProducto(idproducto integer NOT NULL PRIMARY KEY,producto varchar(150) NOT NULL,fechacreacion date NOT NULL,estado integer);")
	sql.execute("CREATE TABLE tbCalificacion(idcalifica integer NOT NULL PRIMARY KEY,item varchar(100) NOT NULL,punteo integer NOT NULL);")
	sql.execute("INSERT INTO tbProducto VALUES(6,'Laptop Lenovo',2021-01-07 00:00:00,'1');")
	t5 = 'texto'
	pila[0] = t5
	myFuncion()
	t6 = pila[10]
	print(t6)
	sql.execute('3D')

	graphTable(ts)
def myFuncion():
	texto = pila[0]
	t0 = 'a'
	pila[0] = t0
	myFuncion()
	t1 = pila[10]
	
	t2 = 'a'
	pila[0] = t2
	myFuncion()
	t3 = pila[10]
	
	t4 = t1 + t3
	texto = t4
	
ejecutar()