class errorSemantico() :
	'Esta clase representa un símbolo dentro de nuestra tabla de símbolos'

	def __init__(self, id, tipo) :
		self.id = id
		self.tipo = tipo


class ListaErroresSemanticos() :
	'Esta clase representa la tabla de símbolos'

	def __init__(self, simbolos = {}) :
		self.simbolos = simbolos

	def agregar(self, simbolo):
		self.simbolos[simbolo.id] = simbolo