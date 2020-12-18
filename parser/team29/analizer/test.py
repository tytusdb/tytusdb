from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
--DROP DATABASE test;
--SELECT cos(cos(10));
--SELECT  sqrt(5*(4+1)+cos(10)) > 0 AND 4+5*8 < 1;
--SELECT extract(hour from timestamp '2002-09-17 19:27:45');

"""

result = grammar.parse(s)
print(result)
