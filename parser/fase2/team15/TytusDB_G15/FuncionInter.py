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


	def procesar_funcionCreateDatabase0(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionUseDatabase1(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionCreateTable2(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionCreateIndex3(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse(' CREATE  UNIQUE  INDEX idx_producto ON tbProducto   (  idproducto       );')
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionCreateTable4(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionCreateIndex5(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse(' CREATE  UNIQUE  INDEX idx_califica ON tbCalificacion   (  idcalifica       );')
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionInsert6(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionInsert7(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionInsert8(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionInsert9(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionInsert10(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionInsert11(self):
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
			print(salida)
		else:
			print('Parser Error')


	def procesar_funcionSelect12(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss,ts_globalIndex1
		instrucciones = g.parse('  select    *   from  tbCalificacion   ;')
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
			print(salida)
		else:
			print('Parser Error')


	def Reportes(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,ts_globalIndex1
		astGraph = AST()
		astGraph.generarAST(instrucciones_Global)
		typeC = TipeChecker()
		typeC.crearReporte(tc_global1)
		RTablaS = RTablaDeSimbolos()
		RTablaS.crearReporte(ts_global1,ts_globalIndex1)
		RTablaS.crearReporte1(ts_global1,ts_globalIndex1)