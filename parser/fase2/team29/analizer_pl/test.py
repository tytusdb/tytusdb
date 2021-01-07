from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

import analizer_pl.grammar as grammar2

s = """ 

--insert into tb values(1,2);
CREATE procedure myFuncion(texto text, puta integer) as $$
declare 
	texto2 integer := 2;
BEGIN
	if 5 > 6 then
		texto2 = 3;
	elsif 9 * 5 != 8 then
		texto2 = 5;
		if 9 + 5 > 5 then
			texto2 = 55;
		end if;
		texto2 = 6;
	else
		texto2 = 9;
	end if;
	RETURN (5+2>8*1 and  1+3*3 != 4) is not TRUE;
END;
$$ LANGUAGE plpgsql;

"""
result = grammar2.parse(s)

print(result)
for r in result:
    x = r.execute(None).value
    print(x)
