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
CREATE INDEX orderindex ON orders (x,t);
"""
result = grammar.parse(s)
print(result)
# print(result[0].execute(None))
# print(grammar.returnPostgreSQLErrors())
