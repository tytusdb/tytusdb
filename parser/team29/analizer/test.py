from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
DROP DATABASE test;
"""

result = grammar.parse(s)
print(result)
