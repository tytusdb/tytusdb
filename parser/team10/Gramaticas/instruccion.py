from enum import Enum
from  datetime import datetime

class valido(Enum):
	invalido = 0
	valido = 1




class Sentencia:
	'''Clase abtracta para realizar las diferentes operaciones'''

class insDML(Sentencia):
	def __init__(self, instru):
		self.instru = instru

class insDDL(Sentencia):
	def __init__(self, instru):
		self.instru = instru

class instruccionL(Sentencia):
	def __init__(self, instru):
		self.instru = instru

class Create(Sentencia):
	def __init__(self, instru):
		self.instru = instru

class Replace(Sentencia):
	def __init__(self, instru):
		self.instru = instru

class CreateType(Sentencia):
	def __init__(self, valor, listInser):
		self.valor = valor
		self.listInser = listInser

class CreateDatabase(Sentencia):
	def __init__(self, ifNot):
		self.ifNot =ifNot
		
class CreateTable(Sentencia):
	def __init__(self, ifNot, colTabla, finTabla):
		self.ifNot = ifNot
		self.colTabla= colTabla
		self.finTabla= finTabla

class inherencia(Sentencia):
	def __init__(self, ids):
		self.ids = ids

class modoExist(Sentencia):
	def __init__(self, existe, identificador, valor):
		self.existe = existe
		self.identificador = identificador
		self.valor = valor 

class modo(Sentencia):
	def __init__(self, existe, identificador, valor):
		self.existe = existe
		self.identificador = identificador
		self.valor = valor 

class propCol(Sentencia):
	def __init__(self, identificador, tipo, propiedades):
		self.identificador = identificador
		self.tipo = tipo
		self.propiedades = propiedades

class tiposD(Sentencia):
	def __init__(self, tipo, num):
		self.tipo = tipo
		self.num = num

class alter(Sentencia):
     def __init__(self, alterObjeto):
        self.alterObjeto = alterObjeto


class tabla(Sentencia):
    def __init__(self, identificador, alterno):
        self.identificador = identificador
        self.alterno = alterno


class dataBase(Sentencia):
    def __init__(self, identificador, usuario, identificador2):
        self.identificador = identificador
        self.usuario = usuario
        self.identificador2 = identificador2

class conAdd(Sentencia):
    def __init__(self, tipo):
        self.tipo = tipo



class columnas(Sentencia):
    def __init__(self, identificador, tipo):
        self.identificador = identificador
        self.tipo = tipo

class checks(Sentencia):
    def __init__(self, valor):
        self.valor = valor


class primaryKey(Sentencia):
	def __init__(self, propiedades):
		self.propiedades = propiedades

class propiedad(Sentencia):
	def __init__(self, var, var2):
		self.var = var	
		self.var2 = var2

class foreingKey(Sentencia):
    def __init__(self, identificador, identificador2):
        self.identificador = identificador
        self.identificador2 = identificador2


class conDrop(Sentencia):
    def __init__(self, tipo, identificador):
        self.tipo = tipo
        self.identificador = identificador

class conRename(Sentencia):
    def __init__(self, identificador, identificador2):
        self.identificador = identificador
        self.identificador2 = identificador2


class ConAlter(Sentencia): 
    def __init__(self,identificador, setNull):
        self.identificador = identificador
        self.setNull = setNull
      
  #Sentencia DROP    
class Drop(Sentencia): 
    def __init__(self,  objeto, if_exist):
        self.objeto = objeto
        self.if_exist = if_exist
     
class IfExist(Sentencia): 
	def __init__(self, existe, identificador):
		self.existe = existe
		self.identificador = identificador

class IfExist2(Sentencia): 
	def __init__(self, existe, identificador, _owner, valor):
		self. existe =  existe
		self.identificador = identificador
		self._owner = _owner
		self.valor = valor
	

	



class Objeto(Sentencia): 
    def __init__(self, var):
        self.var = var
      
 #TRUNCATE

class Truncate(Sentencia): 
	def __init__(self, identificador):          
		self.identificador = identificador
      
#-------------DML -------------------
#INSERT
class INSERTAR(Sentencia): 
    def __init__(self,  identificador, insertCont): 
        self.identificador = identificador
        self.insertCont = insertCont
     
class InsertarCont(Sentencia): 
	def __init__(self, values, listaInsertar):
		self.values = values
		self.listaInsertar = listaInsertar

class InsertarCont2(Sentencia): 
	def __init__(self, lista_campos, values, listaInsertar):
		self.lista_campos = lista_campos
		self.values = values
		self.listaInsertar = listaInsertar
     
   
# def actualizar(Sentencia):
# 	def __init__(self, identificador, identificador2, operacion, condicion):
# 		self.identificador = identificador
# 		self.identificador2 = identificador2
# 		self.operacion = operacion
# 		self.condicion = condicion

class Actualizar(Sentencia): 
	def __init__(self, ids, id2, opera, cond):
		self.ids =  ids
		self.id2 = id2
		self.opera = opera
		self.cond = cond
	



#Delete


#select
class Select(Sentencia): 
    def __init__(self, _select, opciones_fecha):
        self._select =  _select
        self.opciones_fecha = opciones_fecha


class Borrar(Sentencia):
	def __init__(self, cont, cond):
		self.cont = cont
		self.cond = cond

class BorrarCont(Sentencia):
	def __init__(self, only, ids, por):
		self.only = only
		self.ids = ids
		self.por = por

class seleccionF(Sentencia):
	def __init__(self, fechas):
		self.fechas = fechas

class seleccionCont(Sentencia):
	def __init__(self, cont):
		self.cont = cont	

class seleccion(Sentencia):
	def __init__(self, cont, listFrom, cond):
		self.cont = cont
		self.listFrom = listFrom
		self.cond = cond



class ordenar(Sentencia):
	def __init__(self, ids, opOrden, fin):
		self.ids = ids
		self.opOrden = opOrden
		self.fin = fin

class limts(Sentencia):
	def __init__(self, op1, fin):
		self.op1 = op1
		self.fin = fin


class offsets(Sentencia):
	def __init__(self, op1, fin):
		self.op1 =op1
		self.fin =fin


class OpcionOrder(Sentencia): 
    def __init__(self,_asc):
	    self._asc = _asc

class whereAgrupado(Sentencia):
	def __init__(self, op1, ids , fin):
		self.op1 = op1
		self.ids = ids
		self.fin = fin


class WhereSimple(Sentencia):
	def __init__(self,op1, fin):
		self.op1 = op1
		self.fin = fin

class Groups(Sentencia):
	def __init__(self, list1, havings, fin ):
		self.list1 = list1
		self.havings = havings
		self.fin =fin

class WheresExist(Sentencia):
	def __init__(self, op1, fin):
		self.op1 =op1
		self.fin = fin
     
class wheres(Sentencia):
	def __init__(self, op1, ins, op2, fin):
		self.op1 = op1
		self.ins = ins
		self.op2 = op2
		self.fin = fin

class CondicionCount9(Sentencia): 
    def __init__(self,fin_select):
	    self.fin_select = fin_select
       
class uniones(Sentencia):
	def __init__(self, sents):
		self.sents =sents

class interseccion(Sentencia):
	def __init__(self, sents):
		self.sents = sents

class excepto(Sentencia):
	def __init__(self, sents):
		self.sents = sents

class como(Sentencia):
	def __init__(self, id1, id2):
		self.id1 =id1
		self.id2 = id2

class TipoJoin(Sentencia): 
    def __init__(self, tipo):
    	self.tipo = tipo

     
class HacerJoinOn(Sentencia):
    def __init__(self, identificador, tipo_join,  identificador2, operacion_logica):
        self.identificador = identificador
        self.tipo_join = tipo_join
        self.identificador2 = identificador2
        self.operacion_logica = operacion_logica
     
class HacerJoin(Sentencia): 
    def __init__(self,identificador, tipo_join, identificador2):
	    self.identificador = identificador
	    self.tipo_join = tipo_join
	    self.identificador2 = identificador2


class ast(Sentencia): 
    def __init__(self,por):
	    self.por = por
     
class Distinct(Sentencia): 
    def __init__(self, lista_id):
	     
	    self.lista_id = lista_id


class SenCase(Sentencia): 
    def __init__(self, _case, case_when):
	    self. _case =  _case
	    self.case_when = case_when

class CaseWhen(Sentencia): 
    def __init__(self, operacion_logica, operacion_aritmetica, case_when):
	    self.operacion_logica = operacion_logica
	    self.operacion_aritmetica = operacion_aritmetica
	    self.case_when = case_when
     
class endWhen(Sentencia): 
    def __init__(self, valor):
	    self.valor = valor


class ListaId(Sentencia): 
    def __init__(self,lista_id, coma, operacion_aritmetica):
	    self.lista_id = lista_id
	    self.coma = coma
	    self.operacion_aritmetica = operacion_aritmetica

class ListaId2(Sentencia): 
    def __init__(self,lista_id, identificador, identificador2):
	    self.lista_id = lista_id
	    self.identificador = identificador
	    self.identificador2 = identificador2
 
     
class ListaSubString(Sentencia): 
    def __init__(self,_substring, valor, valor2, valor3):
	    self._substring = _substring
	    self.valor = valor
	    self.valor2 = valor2
	    self.valor3 = valor3
     

class OpcionesFecha2(Sentencia): 
	def __init__(self,_now):
	    self._now = _now
	def getValor(self):
		return datetime.now()

class OpcionesFecha3(Sentencia): 
	def __init__(self,date_part,  valor, interval, valor2):
	    self.date_part = date_part
	    self.valor = valor
	    self.interval = interval
	    self.valor2 = valor2

	def getValor(self):
		if self.date_part == 'extract':	
			compuesta = self.valor2.cadC.replace('\'', '')
			fecha = datetime.strptime(compuesta, '%Y-%m-%d %H:%M:%S')
			tipo = self.valor.tipo
			if(tipo =='year'):
				return fecha.year
			elif tipo =='month':
				return fecha.month
			elif tipo =='day':
				return fecha.day
			elif tipo == 'hour':
			    return fecha.hour
			elif tipo == 'minute':
			    return fecha.minute
			elif tipo == 'second':
			    return fecha.second
			else:
				return -1
		elif self.date_part == 'date_part':
			print(self.valor.cadC)
			if self.valor.cadC == '\''+'hour'+'\'':
				if self.valor2.cadC.find('minutes')>-1 and  self.valor2.cadC.find('seconds')>-1 :
					compuesta = self.valor2.cadC.replace('\'', '')
					tiempo = datetime.strptime(compuesta, '%H hours %M minutes %S seconds')	
					return tiempo.hour
				elif self.valor2.cadC.find('minutes')>-1 :
					compuesta = self.valor2.cadC.replace('\'', '')
					tiempo = datetime.strptime(compuesta, '%H hours %M minutes')
					return tiempo.hour
				else :
					compuesta = self.valor2.cadC.replace('\'', '')
					tiempo = datetime.strptime(compuesta, '%H hours')
					return tiempo.hour
			elif  self.valor.cadC == '\''+'minutes'+'\'':
				if self.valor2.cadC.find('minutes')>-1 and  self.valor2.cadC.find('seconds')>-1 :
					compuesta = self.valor2.cadC.replace('\'', '')
					tiempo = datetime.strptime(compuesta, '%H hours %M minutes %S seconds')	
					return tiempo.minute
				elif self.valor2.cadC.find('minutes')>-1 :
					compuesta = self.valor2.cadC.replace('\'', '')
					tiempo = datetime.strptime(compuesta, '%H hours %M minutes')
					return tiempo.minute
				else :
					compuesta = self.valor2.cadC.replace('\'', '')
					tiempo = datetime.strptime(compuesta, '%H hours')
					return tiempo.minute
			elif self.valor.cadC == '\''+'seconds'+'\'':
				if self.valor2.cadC.find('minutes')>-1 and  self.valor2.cadC.find('seconds')>-1 :
					compuesta = self.valor2.cadC.replace('\'', '')
					tiempo = datetime.strptime(compuesta, '%H hours %M minutes %S seconds')	
					return tiempo.minute
				elif self.valor2.cadC.find('minutes')>-1 :
					compuesta = self.valor2.cadC.replace('\'', '')
					tiempo = datetime.strptime(compuesta, '%H hours %M minutes')
					return tiempo.minute
				else :
					compuesta = self.valor2.cadC.replace('\'', '')
					tiempo = datetime.strptime(compuesta, '%H hours')
					return tiempo.minute
	
    			
class Opcionesfecha4(Sentencia): 
	def __init__( self, current_date, valor):
		self.current_date = current_date
		self.valor = valor

	def getValor(self):
		if self.valor == valido.invalido:
			if self.current_date== 'current_time':
				return datetime.now().strftime("%H:%M:%S")
			elif self.current_date == 'current_date':
				return datetime.today().strftime("%Y-%m-%d")
		else:
			fecha = 0
			if len(self.valor.cadC)<14 :
				compuesta = self.valor.cadC.replace('\'', '')
				fecha = datetime.strptime(compuesta, '%Y-%m-%d')
			else: 
				compuesta = self.valor.cadC.replace('\'', '')
				fecha = datetime.strptime(compuesta, '%Y-%m-%d %H:%M:%S')
			return fecha	

class Condicion(Sentencia):
     def __init__(self, isIn, oper1, oper2, existe, Id):
        self.isIn = isIn
        self.op1 = oper1
        self.op2 = oper2
        self.existe = existe
        self.Id = Id


class SentenciaShow(Sentencia): 
    def __init__(self,show_cont):
	    self.show_cont = show_cont
     

class InsLike(Sentencia): 
    def __init__(self, identificador):
	    self.identificador = identificador
     
class Empty(Sentencia): 
    def __init__(self,_empty):
	    self._empty = _empty