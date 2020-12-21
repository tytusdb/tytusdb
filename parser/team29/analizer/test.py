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
USE db1;
/*
CREATE TABLE demo7 (
  id INTEGER,
  name VARCHAR(20),
  username VARCHAR(20)
);
*/
--SELECT de1.id, caca.name FROM demo5 de1, (SELECT de2.name FROM demo5 de2 WHERE de1.id = de2.id) AS caca;
--SELECT d.* FROM demo5 d WHERE d.id > 1;
"""
result = grammar.parse(s)
print(result)
