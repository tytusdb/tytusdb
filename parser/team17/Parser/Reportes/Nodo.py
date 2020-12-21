
class Nodo:

	def __init__(self,valor,tipo):
			self.id =0
			self.valor=str(valor)
			self.tipo=str(tipo)
			self.hijos=[]

	def getValor(self):
		return self.valor

	def getTipo(self):
		return self.tipo

	def add(self, hijo):
		self.hijos.append(hijo)