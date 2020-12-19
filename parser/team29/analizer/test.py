from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
    USE db1;
    
    SELECT 3+3;
    SELECT users.id+300 as shute FROM users WHERE users.id < 6;
"""


result = grammar.parse(s)
print(result)


