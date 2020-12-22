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
SELECT Set_byte(d.name, 0, 97) FROM demo5 d WHERE d.id > 1;
--SELECT md5(name) FROM demo5 WHERE id < 4;
--SELECT Trim("both", "er", "eeeeeerancisco al chileeeeeee");
--SELECT Set_byte("Name", 0, 97);
SELECT convert_int('5');
"""
result = grammar.parse(s)
print(result)

BnfGrammar.grammarReport()
