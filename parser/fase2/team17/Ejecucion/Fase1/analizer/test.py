from sys import path
from os.path import dirname as dir
from shutil import rmtree

path.append(dir(path[0]))

from analizer import grammar

dropAll = 0
if dropAll:
    print("Eliminando registros")
    rmtree("data")


s = """ 
USE test;
(SELECT "puta") union (SELECT "hola");
"""
result = grammar.parse(s)
print(result)
# print(result[0].execute(None))
# print(result[1].execute(None))
# print(grammar.returnPostgreSQLErrors())
