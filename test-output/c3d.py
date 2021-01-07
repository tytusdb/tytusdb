from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from analizer import interpreter as fase1
from goto import with_goto
dbtemp = ""
stack = []

fase1.execution("CREATE  DATABASE  dbfase2  ;")
dbtemp = "USE dbfase2;"

@with_goto
def myfuncion():
	texto = stack.pop()
	stack.append(texto)
	goto .endLabel
	stack.append(None)
	label .endLabel

fase1.execution(dbtemp + " CREATE TABLE  tbproducto (idproducto INTEGER NOT NULL PRIMARY KEY, producto VARCHAR(150) NOT NULL, fechacreacion DATE NOT NULL, estado INTEGER  );")
fase1.execution(dbtemp + " CREATE UNIQUE INDEX idx_producto ON tbproducto (idproducto);")
fase1.execution(dbtemp + " CREATE TABLE  tbcalificacion (idcalifica INTEGER NOT NULL PRIMARY KEY, item VARCHAR(100) NOT NULL, punteo INTEGER NOT NULL );")
fase1.execution(dbtemp + " CREATE UNIQUE INDEX idx_califica ON tbcalificacion (idcalifica);")

stack.append("Francisco")
myfuncion()
t0 = stack.pop()

