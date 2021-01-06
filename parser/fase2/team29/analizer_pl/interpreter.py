from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

import analizer_pl.grammar as grammar2
from analizer_pl.abstract import global_env


def traducir(input):
    result = grammar2.parse(input)
    env = global_env.GlobalEnvironment()
    c3d = "from analizer import interpreter\ndbtemp = None\n"
    c3d += "stack = []\n"
    c3d += "\n"
    for r in result:
        if r:
            c3d += r.execute(env).value
        else:
            c3d += "Instruccion SQL \n"
    print(c3d)
    reporteFunciones(env)


def reporteFunciones(env):
    rep = [["Id", "Tipo de Retorno", "No. de Parametros"], []]
    for (f, x) in env.functions.items():
        r = []
        r.append(x.id)
        r.append(x.returnType.name)
        r.append(x.params)
        rep[1].append(r)
    print(rep)


s = """ 
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
    RETURN (5+2>81 and  1+33 != 4) is not TRUE;
END;
$$ LANGUAGE plpgsql;

CREATE function alv(texto text) RETURNS text AS $$
declare 
    texto2 integer := 2;
    puta text;
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
    RETURN (5+2>81 and  1+33 != 4) is not TRUE;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION sales_tax(nombre integer) RETURNS integer AS $$
DECLARE
    x integer := 12;
    msg integer := 0;
BEGIN
CASE
    WHEN x BETWEEN 0 AND 10 THEN
        msg := 'value is between zero and ten';
    WHEN x BETWEEN 11 AND 20 THEN
        msg := 'value is between eleven and twenty';
END CASE;
END;
$$ LANGUAGE plpgsql;
"""

traducir(s)
result = grammar2.parse(s)
print(result)