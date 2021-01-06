
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
		instrucciones = g.parse('CREATE DATABASE Prueba1;')
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
		instrucciones = g.parse('USE Prueba1;')
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
		instrucciones = g.parse('CREATE TABLE tbUSUARIO (  id_usuario  INTEGER   );')
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
		instrucciones = g.parse('ALTER TABLE tbUSUARIO ADD CONSTRAINT fk_id_usuario FOREIGN KEY ( id_usuario ) REFERENCES tbESTUDIANTE ( id_usuario );')
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
		instrucciones = g.parse(' CREATE INDEX mytable_cat_1 ON tbUSUARIO  (  id_usuario  )   WHERE       category    =     1        ;')
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
		instrucciones = g.parse(' CREATE INDEX mytable_cat_2 ON tbUSUARIO  (  id_usuario  )   WHERE       category    =     2        ;')
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
		instrucciones = g.parse(' CREATE INDEX mytable_cat_3 ON tbUSUARIO  (  id_usuario  )   WHERE       category    =     3        ;')
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
		instrucciones = g.parse(' DROP INDEX  mytable_cat_1;')
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
		instrucciones = g.parse(' DROP INDEX  mytable_cat_1;')
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
		instrucciones = g.parse(' DROP INDEX  mytable_cat_2 , mytable_cat_3;')
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
		#astGraph = AST()
		#astGraph.generarAST(instrucciones_Global)
		typeC = TipeChecker()
		typeC.crearReporte(tc_global1)
		RTablaS = RTablaDeSimbolos()
		RTablaS.crearReporte(ts_global1,ts_globalIndex1)
		RTablaS.crearReporte1(ts_global1,ts_globalIndex1)
		return ''

