
from gramatica import parse
from principal import * 
import ts as TS
from expresiones import *
from instrucciones import *
from report_ast import *
from report_tc import *
from report_ts import *
from report_errores import *


class Intermedio():
	instrucciones_Global = []
	tc_global1 = []
	ts_global1 = []

	def __init__(self):
		''' Funcion Intermedia '''


	def procesar_funcion0(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse('CREATE DATABASE prueba1;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion1(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse('USE prueba1;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion2(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse('CREATE TABLE usuario (  id_usuario  INTEGER  , nombre  VARCHAR ( 50 )  , apellido  VARCHAR ( 50 )   );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion3(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse('CREATE TABLE usuario1 (  id_usuario  INTEGER  , nombre  VARCHAR ( 50 )  , apellido  VARCHAR ( 50 )   );')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion4(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX test1_id_index ON tbUSUARIO  (  id_usuario  ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion5(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX name ON tbUSUARIO  USING HASH ( id_usuario ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion6(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX test2_mm_idx ON tbUSUARIO  (  id_usuario,id_usuario  ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion7(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX test2_info_nulls_low ON tbUSUARIO  (  id_usuario NULLS  FIRST   ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion8(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX test3_desc_index ON tbUSUARIO  (  id_usuario  DESC  NULLS  LAST   ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion9(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE UNIQUE INDEX name ON tbUSUARIO  (  id_usuario,id_usuario,id_usuario  ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion10(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX test1_lower_col1_idx ON tbUSUARIO  (  lower ( id_usuario )  ) ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion11(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX access_log_client_ip_ix ON tbUSUARIO  (  id_usuario  )   WHERE   NOT     (     id_usuario   >   inet    AND     id_usuario   <   inet      )       ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion12(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX mytable_cat_1 ON tbUSUARIO  (  id_usuario  )   WHERE       category    =     1        ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion13(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX mytable_cat_2 ON tbUSUARIO  (  id_usuario  )   WHERE       category    =     2        ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion14(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse(' CREATE INDEX mytable_cat_3 ON tbUSUARIO  (  id_usuario  )   WHERE       category    =     3        ;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def Reportes(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores
		#astGraph = AST()
		#astGraph.generarAST(instrucciones_Global)
		typeC = TipeChecker()
		typeC.crearReporte(tc_global1)
		RTablaS = RTablaDeSimbolos()
		RTablaS.crearReporte(ts_global1)
		return ''

