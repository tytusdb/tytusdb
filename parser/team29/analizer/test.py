from sys import path
from os.path import dirname as dir
from shutil import rmtree

path.append(dir(path[0]))

from analizer import grammar
from analizer.reports import BnfGrammar

dropAll = 0
if dropAll:
    print("Eliminando registros")
    rmtree("data")


s = """ 
USE test;
select E.*,
  estado,
  I.identificacion,
  tipoidentificacion
from tbempleado E,
  tbestado ES,
  tbempleadoidentificacion I,
  tbidentificaciontipo IT
where ES.idestado = E.idestado
  and I.idempleado = E.idempleado
  and IT.ididentificaciontipo = I.ididentificaciontipo;
"""
result = grammar.parse(s)
print(result)
#grammar.InitTree()
# BnfGrammar.grammarReport()
