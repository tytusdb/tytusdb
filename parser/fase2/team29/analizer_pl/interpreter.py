from re import S
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

import analizer_pl.grammar as grammar2
from analizer_pl.abstract import global_env


def traducir(input):
    result = grammar2.parse(input)
    env = global_env.GlobalEnvironment()
    c3d = "from analizer import interpreter as fase1\n"
    c3d += "from goto import with_goto\n"
    c3d += 'dbtemp = ""\n'
    c3d += "stack = []\n"
    c3d += "\n"
    for r in result:
        if r:
            c3d += r.execute(env).value
        else:
            c3d += "Instruccion SQL \n"
    f = open("test-output/c3d.py", "w+")
    f.write(c3d)
    f.close()
    # grammar2.InitTree()
    reporteFunciones(env)


def reporteFunciones(env):
    rep = [["Id", "Tipo de Retorno", "No. de Parametros"], []]
    for (f, x) in env.functions.items():
        r = []
        r.append(x.id)
        if x.returnType:
            r.append(x.returnType.name)
        else:
            r.append("NULL")
        r.append(x.params)
        rep[1].append(r)
    print(rep)


s = """ 
CREATE function foo(i integer) RETURNS integer AS $$
declare 
	j integer := i + 1;
	k integer;
BEGIN
	case 
        when i > 10 then
            k = 0;
            RETURN j * k + 1;
        when i < 10 then
            k = 1;
            RETURN j * k + 2;
        else 
            k = 2;
            RETURN j * k + 3;
    end case;
END;
$$ LANGUAGE plpgsql;

CREATE procedure p1() AS $$
declare 
	k integer;
BEGIN
	k = foo(5);
    k = foo(10);
    k = foo(15);
END;
$$ LANGUAGE plpgsql;
"""

sql = """
CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);
CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);
CREATE INDEX ON tbbodega ((lower(bodega)));
"""

traducir(s)