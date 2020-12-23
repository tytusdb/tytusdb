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
--SELECT hint, count(*) FROM demo5 WHERE id <5 GROUP BY 1;
--SELECT caca.i FROM (SELECT 3+3 as d, 8-8 i) AS caca;
--SELECT 3+3 as d, 8-8 i;
--SELECT name, hint FROM demo5 d5, demo1 as d1 WHERE d5.id = d1.id;
--SELECT d.name, d.hint FROM demo1 d;
--SELECT a.name as feca, md5(a.hint) as put FROM demo1 a;
--SELECT a.id as feca, a.hint as puta FROM demo5 a WHERE a.id < 5 and a.hint = 'Su puta madre';
--(SELECT d.name, d.hint FROM demo1 d) UNION (SELECT f.name, f.hint FROM demo5 f);

--(SELECT name FROM demo1 WHERE id < 7) EXCEPT (SELECT name FROM demo1 WHERE id > 7);

--SELECT 3+3 as d, 8-8 i;
SELECT caca.d, name FROM demo5, (SELECT 3+3 as d, 8-8 i) AS caca;
"""
result = grammar.parse(s)
print(result)

# BnfGrammar.grammarReport()
