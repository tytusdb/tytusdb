from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
    USE db1;
    SELECT d.id FROM demo1 d;
"""


result = grammar.parse(s)
print(result)
