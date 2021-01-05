from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

import analizer_pl.grammar as grammar2

s = """ 

--insert into tb values(1,2);
CREATE procedure myFuncion(texto text, puta integer) RETURNS text AS $$
declare 
	texto2 integer := 2;
BEGIN
	case when 1=2 then
	texto2 := 25; 
		case when texto is true then
			puta = 'cisco';
		else
			puta = 'alv';
		end case;
	else 
	texto := 'd'; 
	puta := 'i'; 
	end case;
	RETURN (5+2>8*1 and  1+3*3 != 4) is not TRUE;
END;
$$ LANGUAGE plpgsql;

"""
result = grammar2.parse(s)

print(result)
for r in result:
    x = r.execute(None).value
    print(x)
