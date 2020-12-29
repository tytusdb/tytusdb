from sys import path
from os.path import dirname as dir
from shutil import rmtree

path.append(dir(path[0]))

from analizer import grammar
from analizer.reports import BnfGrammar
from analizer.interpreter import symbolReport

dropAll = 0
if dropAll:
    print("Eliminando registros")
    rmtree("data")


s = """ 
--SELECT * FROM tab where 5 IN (select * from tab2);
--SELECT factorial(17) AS factorial, 
--EXP(2.0) as Exponencial,
--LN(5.0) "Logaritmo Natural",
--PI(),
--POWER(5,2);
--create table tblibrosalario
--( idempleado integer not null,
  --aniocalculo integer not null CONSTRAINT aniosalario CHECK (aniocalculo > 0),
  --mescalculo  integer not null CONSTRAINT mescalculo CHECK (mescalculo > 0 ),
  --salariobase  money not null,
  --comision decimal(1,1),
  --primary key(idempleado)
 --);
--SELECT * from tab1 where exists (select * from tab2 where 1 < 2);
--ALTER TABLE tab1  ADD foreign key(a,b) references tab2(b,c);
--ALTER TABLE tab1  ADD COLUMN col1 NUMERIC(1,2);
--UPDATE tbempleadopuesto SET idpuesto = 2 where idempleado = 2;
--select primernombre,segundonombre,primerapellido,fechaventa, sum(s)
--from tbventa V,tbempleado E
--where V.idempleado = E.idempleado
--group by primernombre,segundonombre,primerapellido,fechaventa
--having x = 2 limit all offset 2;
--USE test;
--select E.*,
--  estado,
--  I.identificacion,
--  tipoidentificacion
--from tbempleado E,
--  tbestado ES,
--  tbempleadoidentificacion I,
--  tbidentificaciontipo IT
--where ES.idestado = E.idestado
  --and I.idempleado = E.idempleado
  --and IT.ididentificaciontipo = I.ididentificaciontipo;
--SELECT distinct caca.primernombre FROM tbempleado de1, (SELECT de2.primernombre FROM tbempleado de2 WHERE de1.idempleado = de2.idempleado) AS caca;

"""
result = grammar.parse(s)
print(result)

# print(symbolReport())
# grammar.InitTree()
# BnfGrammar.grammarReport()
