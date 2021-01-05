from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

import analizer_pl.grammar as grammar2

s = """ 

--insert into tb values(1,2);

CREATE FUNCTION myFuncion(texto text, puta integer) RETURNS text AS $$
declare 
	texto2 integer := 2;
BEGIN
	case when 1<2 then texto:= '4'; else texto := 'd'; end case;
	--insert into tb values(1,2);
	texto := 'jaja';
	puta := 23;
	RETURN (5+2>8*1 and  1+3*3 != 4) is not TRUE;
END;
$$ LANGUAGE plpgsql;

"""
result = grammar2.parse(s)

print(result)
for r in result:
    x = r.execute(None).value
    print(x)
