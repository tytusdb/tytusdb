from Interprete.Insert.InsertReturn import InsertReturn
from Interprete.Insert.HeadTYpes import HEAD
from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from StoreManager import jsonMode as j

#############################
# Patrón intérprete: INSERT #
#############################

# UPDATE: modificar atributos de una tabla


class Insert(NodoArbol):

	#'SLV', 'El Salvado', 'Central America', 21041
	# insert : into countries values('COL','Colombia','Sur America',0256);
	#        | INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER

	def __init__(self,tableName,listColumn,listValues,line,column):
		super().__init__(line, column)
		self.tableName:str   = tableName
		self.listColumn:list = listColumn
		self.listValues:list = listValues


	# insert into countries values('COL','Colombia','Sur America',0256);
	def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):

		#DatabaseName: world
		#tableName:countries

		#todo:obtener base de datos por el momento ira quemada
		databaseName = 'world'

		#todo:2.verificar los tipos en la columna

		if self.exist(databaseName,self.tableName)== True:
			table:list = j.extractTable(databaseName,self.tableName)

			if self.checkLen(table[0])==True and \
			   self.TypesCompare(table[0],entorno,arbol)==True:

				values:list = self.getValues(entorno,arbol)

				j.insert(databaseName, self.tableName,values)
				print(self.tableName, ' Registro Ingresado con exito')


	def getValues(self,entorno,arbol) -> list:
		result:list = []

		for v in self.listValues:
			value = v.execute(entorno, arbol).data
			result.append(value)
		return result


	def checkLen(self,columns:list) -> bool:
		lengthColumn = len(columns)
		lengthValues = len(self.listValues)

		if lengthValues > lengthColumn:
			print('Hay Mas valores de los permitidos')
			return False
		elif lengthValues < lengthColumn:
			print('Faltan valores en la columna')
			return  False
		#si no es mayor ni tampoco menor entonces es igual
		else:
			return  True

	#todo: Mejorar metodo separar en varios metodos
	def TypesCompare(self,headColumns,entorno,arbol) -> bool:
		result:bool = True
		for i in range(len(headColumns)):
			col = headColumns[i]
			v 	=  self.listValues[i]

			headColumn_:list= col.split(',')
			value:Valor = v.execute(entorno,arbol)

			typeColumn:int = int(headColumn_[HEAD.typeColumn.value])
			typeValue:int = value.tipo.value


			if typeColumn != typeValue:
				print('el valor no es un tipo aceptado por la columna x')
				result = False

		return  result

	def exist(self,database:str,table:str) -> bool:
		tables_: list = j.showTables(database)
		#La Base de datos existe
		if tables_!=None:
			for table_ in tables_:
				if table_ == table:
					return True
			print('La tabla no existe en ' + database)
			return False
		else:
			print('La base de datos no existe')
			return False


#list b1, b2
#create table b1
#
#use b1
#create table tas
#
#create b2
#
#use b2
#
#create table tas
#
#
#insert tas