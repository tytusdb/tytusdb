from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
    USE db1;
    SELECT de1.id, caca.name FROM demo1 de1, (SELECT de2.name FROM demo1 de2 WHERE de1.id = de2.id) AS caca;
"""
result = grammar.parse(s)
print(result)
