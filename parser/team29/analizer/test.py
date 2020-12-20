from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
    USE db1;
    SELECT de1.*, caca.name FROM demo2 de1, (SELECT de2.name, de2.hint FROM demo2 de2 WHERE de1.id = de2.id) AS caca;
    SELECT d.*, 3 FROM demo1 d WHERE d.id > 1;
    --SELECT * FROM demo3 WHERE id > 1;
    DELETE FROM demo1 as d WHERE d.id > 10;
    --DELETE FROM demo3 as d WHERE d.id > 1;
    --DELETE FROM demo4 as d WHERE d.id > 2;
"""


result = grammar.parse(s)
print(result)
