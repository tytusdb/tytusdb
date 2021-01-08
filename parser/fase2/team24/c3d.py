from InstruccionesDGA import tabla as ts
from datetime import date
from variables import tabla as ts
from variables import NombreDB
from variables import cont as ncont
import tablaDGA as TAS
import sql as sql
import mathtrig as mt
from reportTable import *

cont = ncont
pila = []
for i in range(100):
    pila.append(i)


def ejecutar():
    global cont

    n_db = ts.buscarIDTB(NombreDB)
    NuevoSimbolo = TAS.Simbolo(
        cont, 'sp_validainsert', TAS.TIPO.FUNCTION, n_db)
    ts.agregar(NuevoSimbolo)
    cont += 1
    sp_validainsert()
    sql.execute('3D')

    graphTable(ts)


def sp_validainsert():
    sql.execute(
        '''insert into tbbodega  values ( 1.0,'BODEGA CENTRAL',1.0 ) ;''')

    sql.execute(
        '''insert into tbbodega (idbodega,bodega) values ( 2.0,'BODEGA ZONA 12' ) ;''')

    sql.execute(
        '''insert into tbbodega (idbodega,bodega,estado) values ( 3.0,'BODEGA ZONA 11',1.0 ) ;''')

    sql.execute(
        '''insert into tbbodega (idbodega,bodega,estado) values ( 4.0,'BODEGA ZONA 1',1.0 ) ;''')

    sql.execute(
        '''insert into tbbodega (idbodega,bodega,estado) values ( 5.0,'BODEGA ZONA 10',1.0 ) ;''')


ejecutar()
