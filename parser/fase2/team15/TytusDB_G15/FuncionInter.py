
from gramatica import parse
from principal import * 
import ts as TS
import ts_index as TSINDEX
from expresiones import *
from instrucciones import *
from report_ast import *
from report_tc import *
from report_ts import *
from report_errores import *


class Intermedio():
	instrucciones_Global = []
	tc_global1 = []
	ts_globalIndex1 = []
	ts_global1 = []

	def __init__(self):
		''' Funcion Intermedia '''


	def procesar_funcion0(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('CREATE DATABASE DBFase2;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion1(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('USE DBFase2;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion2(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('CREATE TABLE tbProducto (  idproducto  integer    not null    primary key   , producto  varchar ( 150 )    not null   , fechacreacion  date    not null   , estado  integer   );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion3(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse(' CREATE UNIQUE INDEX idx_producto ON tbProducto  (  idproducto  ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion4(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('CREATE TABLE tbCalificacion (  idcalifica  integer    not null    primary key   , item  varchar ( 100 )    not null   , punteo  integer    not null    );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion5(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse(' CREATE UNIQUE INDEX idx_califica ON tbCalificacion  (  idcalifica  ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion6(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('INSERT INTO tbProducto values (     1    ,   \'Laptop Lenovo\'   , now ( ) ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion7(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('INSERT INTO tbProducto values (     2    ,   \'Bateria para Laptop Lenovo T420\'   , now ( ) ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion8(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('INSERT INTO tbProducto values (     3    ,   \'Teclado Inalambrico\'   , now ( ) ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion9(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('INSERT INTO tbProducto values (     4    ,   \'Mouse Inalambrico\'   , now ( ) ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion10(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('INSERT INTO tbProducto values (     5    ,   \'WIFI USB\'   , now ( ) ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion11(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('INSERT INTO tbProducto values (     6    ,   \'Laptop HP\'   , now ( ) ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion12(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('INSERT INTO tbProducto values (     7    ,   \'Teclado Flexible USB\'   , now ( ) ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion13(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('INSERT INTO tbProducto values (     8    ,   \'Laptop Samsung\'   ,   \'2021-01-02\'   ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion14(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbCalificacion values (     1    ,   \'Create Table and Insert\'   ,    2     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion15(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse(' update tbProducto set  estado =     2       where       estado    =     1        ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion16(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbCalificacion values (     2    ,   \'Update\'   ,    2     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion17(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbCalificacion values (     3    ,   \' Valida Funciones\'   ,    2     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion18(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('create table tbbodega (  idbodega  integer    not null    primary key   , bodega  varchar ( 100 )    not null   , estado  integer   );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion19(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse(' CREATE INDEX tbbodegaIndex ON tbbodega  (  lower ( bodega )  ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion20(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbCalificacion values (     4    ,   \'Valida Store Procedure\'   ,    5     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion21(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse(' delete from tbbodega  where       idbodega    =     4        ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion22(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbCalificacion values (     5    ,   \'Valida Delete\'   ,    2     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion23(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('  select    *   from  tbbodega   ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion24(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbbodega values (     1    ,   \'BODEGA CENTRAL\'   ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion25(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbbodega ( idbodega,bodega ) values (     2    ,   \'BODEGA ZONA 12\'    );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion26(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbbodega ( idbodega,bodega,estado ) values (     3    ,   \'BODEGA ZONA 11\'   ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion27(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbbodega ( idbodega,bodega,estado ) values (     4    ,   \'BODEGA ZONA 1\'   ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion28(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('insert into tbbodega ( idbodega,bodega,estado ) values (     5    ,   \'BODEGA ZONA 10\'   ,    1     );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion29(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse(' update tbbodega set  bodega =    \'bodega zona 9\'      where       idbodega    =     4        ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion30(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('  select    *   from  tbbodega   ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			ts_globalIndex = TSINDEX.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			ts_globalIndex1 = ts_globalIndex
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global,ts_globalIndex)
			return salida
		else:
			return 'Parser Error'


	def Reportes(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,ts_globalIndex1
		astGraph = AST()
		astGraph.generarAST(instrucciones_Global)
		typeC = TipeChecker()
		typeC.crearReporte(tc_global1)
		RTablaS = RTablaDeSimbolos()
		RTablaS.crearReporte(ts_global1,ts_globalIndex1)
		RTablaS.crearReporte1(ts_global1,ts_globalIndex1)
		return ''

