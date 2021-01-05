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
CREATE FUNCTION myFuncion(texto text) RETURNS text AS $$
BEGIN
	RETURN texto;
END;
$$ LANGUAGE plpgsql;

CREATE INDEX ON tbbodega ((lower(bodega)));

create procedure sp_validainsert()
language plpgsql
as $$
DECLARE resultado INTEGER; 
		retorna   INTEGER;
begin
	resultado = 5;
end; $$
								 
EXECUTE sp_validainsert();
																			  

create procedure sp_validaupdate()
language plpgsql
as $$
begin
	update tbbodega set bodega = 'bodega zona 9' where idbodega = 4; 
end; $$

EXECUTE sp_validaupdate();

"""

# traducir(s)
result = grammar2.parse(s)
print(result)