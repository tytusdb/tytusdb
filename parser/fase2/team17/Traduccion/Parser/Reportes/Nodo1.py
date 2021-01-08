class Nodo:

	def __init__(self,valor=''):
			self.id =0
			self.valor=str(valor)
			self.hijos=[]

	def getValor(self):
		return self.valor

	def setValor(self,valor):
		self.valor = valor



	def add(self, hijo):
		self.hijos.append(hijo)