from Interprete.simbolo import Simbolo
from Interprete.Valor.Valor import Valor
from StoreManager import jsonMode as dbms
from Interprete.Mode import MODE

class Tabla_de_simbolos(Simbolo):

	def __init__(self):
		super().__init__("", "", "")
		self.Pila_de_tablas = [[]]
		self.Tabla_deSimbolos = []
		self.mode:MODE = MODE.C3D
		self.BD = ""
		self.actual_table = []

	def NuevoAmbito(self):
		nuevoAmito = [Simbolo("VACIO", 2, Valor(2, "VACIO"))]
		self.Pila_de_tablas.append(nuevoAmito)

	def BorrarAmbito(self):
		self.Pila_de_tablas.pop()

	def insertar_variable(self, simbol: Simbolo):
		for item in self.Pila_de_tablas[len(self.Pila_de_tablas) - 1]:
			simbol_: Simbolo = item
			if simbol_.id == simbol.id:
				item = simbol
				print("TS -> se inserto la var: " + simbol.id)
				return
		self.Pila_de_tablas[len(self.Pila_de_tablas) - 1].append(simbol)
		print("TS -> se inserto la var: " + simbol.id)

	def obtener_varibale(self, identificador):
		'''entorno: [] = self.Pila_de_tablas[len(self.Pila_de_tablas) - 1]
        for item_1 in range(len(entorno)):
            simbol:Simbolo = entorno[item_1]
            if simbol.id == identificador:
                return simbol.valor'''
		for item in self.Pila_de_tablas[len(self.Pila_de_tablas) - 1]:
			simbol: Simbolo = item
			if simbol.id == identificador:
				return simbol.valor

	def varibaleExiste(self, identificador):
		for item in self.Pila_de_tablas[len(self.Pila_de_tablas) - 1]:
			simbol: Simbolo = item
			if simbol.id == identificador:
				return True
		return False

	'''
        Manejo de BD
    '''

	def setBD(self, id):

		if self.existTable('global_', 'config') == False:
			dbms.createDatabase('global_')
			dbms.createTable('global_', 'config', 1)
			dbms.insert('global_', 'config', [id])
			dbms.alterAddPK('global_', 'config', [0])
		else:
			config = dbms.extractTable('global_', 'config')
			databaseName = config[0][0]
			result = dbms.update('global_', 'config', {0: id}, [0])

		self.BD = str(id)

	def existTable(self, database: str, table: str) -> bool:
		tables_: list = dbms.showTables(database)
		# La Base de datos existe
		if tables_ != None:
			for table_ in tables_:
				if table_ == table:
					return True
			return False
		else:
			return False

	# ================================================================================================

	def BDisNull(self):
		if self.existTable('global_', 'config') == False:
			return True
		else:
			return False

	def getBD(self):

		if self.existTable('global_', 'config') == False:
			self.BD = ""
		else:
			config = dbms.extractTable('global_', 'config')
			self.BD = config[0][0]

		return str(self.BD)

	def settable(self, table):
		self.actual_table = table

	def gettable(self):
		return self.actual_table
