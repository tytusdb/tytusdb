
from re import S
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
from analizer_pl.C3D.operations import block
from analizer_pl.reports import BnfGrammar
from analizer_pl.abstract import global_env
import analizer_pl.grammar as grammar

def traducir(input):
    result = grammar.parse(input)
    lexerErrors = grammar.returnLexicalErrors()
    syntaxErrors = grammar.returnSyntacticErrors()
    env = global_env.GlobalEnvironment()
    c3d = "from sys import path\n"
    c3d += "from os.path import dirname as dir\n"
    c3d += "path.append(dir(path[0]))\n"
    c3d += "from analizer import interpreter as fase1\n"
    c3d += "from goto import with_goto\n"
    c3d += 'dbtemp = ""\n'
    c3d += "stack = []\n"
    c3d += "\n"
    optimizacion = c3d
    if len(lexerErrors) + len(syntaxErrors) == 0 and result:
        for r in result:
            if r:
                c3d += r.execute(env).value
            else:
                c3d += "Instruccion SQL \n"
    f = open("test-output/c3d.py", "w+")
    f.write(c3d)
    f.close()
    optimizacion += grammar.optimizer_.optimize()
    f = open("test-output/c3dopt.py", "w+")
    f.write(optimizacion)
    f.close()
    semanticErrors = []
    functions = functionsReport(env)
    symbols = symbolReport()
    obj = {
        "lexical": lexerErrors,
        "syntax": syntaxErrors,
        "semantic": semanticErrors,
        "symbols": symbols,
        "functions": functions,
    }
    # grammar.InitTree()
    BnfGrammar.grammarReport()
    return obj


def symbolReport():
    environments = block.environments
    report = []
    for env in environments:
        envName = env[0]
        env = env[1]
        vars = env.variables
        enc = [["ID", "Tipo", "Fila", "Columna", "Declarada en"]]
        filas = []
        for (key, symbol) in vars.items():
            r = [
                symbol.value,
                symbol.type.name if symbol.type else "UNKNOWN",
                symbol.row,
                symbol.column,
                envName,
            ]
            filas.append(r)
        enc.append(filas)
        report.append(enc)
    environments = list()
    return report


def functionsReport(env):
    rep = [["Tipo", "ID", "Tipo de Retorno", "No. de Parametros"], []]
    for (f, x) in env.functions.items():
        r = []
        r.append(x.type)
        r.append(x.id)
        if x.returnType:
            r.append(x.returnType.name)
        else:
            r.append("NULL")
        r.append(x.params)
        rep[1].append(r)
    return rep


s = """ 

CREATE FUNCTION myFuncion(texto text, b boolean) RETURNS text AS $$
BEGIN
INSERT INTO tbProducto values(1,'Laptop Lenovo',md5(foo(texto)),1);
SELECT 3-5>4 and -3=texto as sho, texto between symmetric 2 and 3 as alv;
b = texto between symmetric 2 and 3;
	RETURN texto;
END;
$$ LANGUAGE plpgsql;

select * from tbCalificacion;
select *
from tbventa where ventaregistrada = false;
select *
from tbempleadopuesto
group by departamento;
select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;



select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido,fechaventa
limit 1;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido
UNION
select DISTINCT * 
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by 1,2,3
order by 1;
"""
s2 = """

CREATE FUNCTION foo(texto text, b boolean) RETURNS text AS $$
BEGIN
return texto;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION myFuncion(texto text, b boolean) RETURNS text AS $$
BEGIN
INSERT INTO tbProducto values(1,'Laptop Lenovo',md5(texto),1);
SELECT 3-5>4 and -3=texto as sho, texto between symmetric 2 and 3 as alv;

select * from tbCalificacion;
select * from tbventa where ventaregistrada = false;
select * from tbempleadopuesto group by departamento;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;


select v.id+foo(texto, 3)
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido,fechaventa
limit 1;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido
UNION
select DISTINCT * 
from tbventa V,tbempleado E
where V.idempleado = texto
group by 1,2,3
order by 1;

b = texto between symmetric 2 and 3;
	RETURN texto;
END;
$$ LANGUAGE plpgsql;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;

"""

traducir(s2)
