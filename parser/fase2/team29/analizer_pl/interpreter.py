from re import S
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

import analizer_pl.grammar as grammar2
from analizer_pl.abstract import global_env


def traducir(input):
    result = grammar2.parse(input)
    env = global_env.GlobalEnvironment()
    c3d = "from analizer import interpreter as fase1\ndbtemp = None\n"
    c3d += "stack = []\n"
    c3d += "\n"
    for r in result:
        if r:
            c3d += r.execute(env).value
        else:
            c3d += "Instruccion SQL \n"
    print(c3d)
    # grammar2.InitTree()
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
USE test;
DROP DATABASE tbroles;
DROP DATABASE  IF EXISTS  califica2;
DROP TABLE IF EXISTS tbcalifica2;
drop table tbempleadoidentificacion;
DROP TABLE tbroles;
SHOW DATABASES; 
TRUNCATE TABLE tbroles;
TRUNCATE tbrol;
"""

sql = """
CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);
CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);
CREATE INDEX ON tbbodega ((lower(bodega)));
"""

traducir(s)