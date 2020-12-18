from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
SELECT "5.1" < "5";
"""


result = grammar.parse(s)
print(result)
