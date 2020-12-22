from sys import path
from os.path import dirname as dir
from shutil import rmtree

path.append(dir(path[0]))

from analizer import grammar
from analizer.reports import BnfGrammar

dropAll = 0
if dropAll:
    print("Eliminando registros")
    rmtree("data")


s = """ 

USE db1;

insert into tbempleado (idempleado,primernombre,primerapellido,fechadenacimiento,fechacontratacion,idestado) 
values(8,'Maria','Lopez','1990-12-01','2016-09-21',1);


"""
result = grammar.parse(s)
print(result)

BnfGrammar.grammarReport()
