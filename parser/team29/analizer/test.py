from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
    USE db1;
    --SELECT id as pito, name as alv, 3+3 as "su madre" FROM demo1 WHERE id > 0;
"""


result = grammar.parse(s)
print(result)
