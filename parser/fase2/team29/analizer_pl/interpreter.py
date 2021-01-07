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
    grammar.InitTree()
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
	j integer := -i + 5;
	k integer:= date_part('seconds', INTERVAL '4 hours 3 minutes 15 seconds');
    texto text := "3+3"||md5("Francisco");
BEGIN
	case 
        when i > -10 then
            RETURN k;
        when i < 10 then
            RETURN texto;
        else 
            RETURN k;
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

--drop procedure p1;
execute foo(5);
execute foo(20);
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

s2 = """
--Manipulacion de datos
CREATE DATABASE IF NOT EXISTS test OWNER = 'root' MODE = 1;
CREATE DATABASE IF NOT EXISTS califica OWNER = 'root' MODE = 2;
SHOW DATABASES;
USE test;
create table tbcalifica (
  iditem integer not null primary key,
  item varchar(150) not null,
  puntos decimal(8, 2) not null
);
CREATE TABLE tbusuario (
  idusuario integer NOT NULL primary key,
  nombre varchar(50),
  apellido varchar(50),
  usuario varchar(15) UNIQUE NOT NULL,
  password varchar(15) NOT NULL,
  fechacreacion date
);
CREATE TABLE tbroles (
  idrol integer NOT NULL primary key,
  rol varchar(15)
);
DROP TABLE tbroles;
CREATE TABLE tbrol (
  idrol integer NOT NULL primary key,
  rol varchar(15)
);
"""

traducir(sql)