
class Nodo:

	def __init__(self,valor:str,tipo:str):
			self.id =0
			self.valor=valor
			self.tipo=tipo
			self.hijos=[]

	def getValor(self):
		return self.valor

	def getTipo(self):
		return self.tipo

	def add(self, hijo):
		self.hijos.append(hijo)