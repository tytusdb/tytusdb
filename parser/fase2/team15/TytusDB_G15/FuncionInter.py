
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

