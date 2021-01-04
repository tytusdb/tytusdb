from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

import analizer.grammarFP as grammar2

s = """ 
CREATE DATABASE DBFase2;

USE DBFase2;

CREATE FUNCTION myFuncion(texto text) RETURNS text AS $$
BEGIN
	
	RETURN texto between 2 and 19;
	RETURN texto not between 2 and 19;
	RETURN texto between SYMMETRIC 2 and 19;
	RETURN (5+2>8*1 and  1+3*3 != 4) is not TRUE;
END;
$$ LANGUAGE plpgsql;

"""
result = grammar2.parse(s)
print(result)
"""
for r in result:
	if r :
		for t in r:
			t = t.execute(0)
			print(t.temp,t.value)"""
