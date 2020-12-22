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

select  caca.name, count(mierda.name) from mierda, (select name from mierda where id<5) as caca group by 2;

"""
result = grammar.parse(s)
print(result)

BnfGrammar.grammarReport()
