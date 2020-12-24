from sys import path
from os.path import dirname as dir
from shutil import rmtree

path.append(dir(path[0]))

from analizer import grammar
from analizer.reports import BnfGrammar
from analizer.interpreter import symbolReport

dropAll = 0
if dropAll:
    print("Eliminando registros")
    rmtree("data")


s = """ 
USE test;

SELECT distinct caca.primernombre FROM tbempleado de1, (SELECT de2.primernombre FROM tbempleado de2 WHERE de1.idempleado = de2.idempleado) AS caca;


"""
result = grammar.parse(s)
print(result)

#print(symbolReport())
#grammar.InitTree()
BnfGrammar.grammarReport()
