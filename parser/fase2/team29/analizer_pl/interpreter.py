from re import S
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

import analizer_pl.grammar as grammar
from analizer_pl.abstract import global_env
from analizer_pl.reports import BnfGrammar
from analizer_pl.C3D.operations import block


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
    #grammar.InitTree()
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
CREATE function foo(i integer) RETURNS integer AS $$
declare 
	j integer := -i + md5(3+3-md5(4),4);
	k integer;
BEGIN
	case 
        when i > -10 then
            k = i;
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
    drop function foo;
	k = foo(5);
    k = foo(10);
    k = foo(15);
END;
$$ LANGUAGE plpgsql;

drop procedure p1;
"""

sql = """
CREATE DATABASE DBFase2;
USE DBFase2;
CREATE FUNCTION myFuncion(texto text) RETURNS text AS $$ BEGIN RETURN texto;
END;
$$ LANGUAGE plpgsql;
CREATE TABLE tbProducto (
  idproducto integer not null primary key,
  producto varchar(150) not null,
  fechacreacion date not null,
  estado integer
);
CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);
CREATE TABLE tbCalificacion (
  idcalifica integer not null primary key,
  item varchar(100) not null,
  punteo integer not null
);
CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);
execute myFuncion("Francisco");
"""

traducir(s)