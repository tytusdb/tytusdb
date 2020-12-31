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


select iditem,  from tbcalifica order by tbcalifica.puntos desc nulls first, tbcalifica.item  nulls last;

"""

result = grammar.parse(s)

x = [r.execute(None) for r in result]
print(x)
# print(symbolReport())
# grammar.InitTree()
# BnfGrammar.grammarReport()
