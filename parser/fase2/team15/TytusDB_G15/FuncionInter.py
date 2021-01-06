
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
		instrucciones = g.parse('CREATE TABLE usuario (  id_usuario  INTEGER  , nombre  VARCHAR ( 50 )  , apellido  VARCHAR ( 50 )  , fecha  VARCHAR ( 50 )   );')
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
		instrucciones = g.parse('INSERT INTO usuario VALUES (     1    , SUBSTR ( \'julio\' ,    0    ,    2    ) , SUBSTRING ( \'cotzo\' ,    0    ,    2    ) , NOW ( )  );')
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
		instrucciones = g.parse('INSERT INTO usuario ( id_usuario,nombre,apellido ) VALUES (     2    , MD5 ( \'julio1\' ) , TRIM ( \'             cotzo2\' )  );')
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
		instrucciones = g.parse('INSERT INTO usuario ( id_usuario,nombre,apellido ) VALUES (     3    , MD5 ( \'julio2\' ) ,   \'             cotzo2\'    );')
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

