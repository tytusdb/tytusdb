class Nodo:
	def __init__(self, valor):
		self.valor = valor
		self.izq = self.der = None
		self.padre = None
		self.altura = 0

class ArbolAVL:
	def __init__(self):
		self.raiz=None
		
	def agregar(self,valor):
		if self.raiz==None:
			self.raiz=Nodo(valor)
		else:
			self._agregar(valor, self.raiz)

	def _agregar(self,valor,tmp):
		if valor<tmp.valor:
			if tmp.izq==None:
				tmp.izq=Nodo(valor)
				tmp.izq.padre=tmp
				self.confirmaAgre(tmp.izq)
			else:
				self._agregar(valor,tmp.izq)
		else:
			if tmp.der==None:
				tmp.der=Nodo(valor)
				tmp.der.padre=tmp
				self.confirmaAgre(tmp.der)
			else:
				self._agregar(valor,tmp.der)

	def preorden(self):
		self._preorden(self.raiz)
		print()

	def _preorden(self, tmp):
		if tmp:
			print(tmp.valor,end = ' ')
			self._preorden(tmp.izq)
			self._preorden(tmp.der)
	
	def enorden(self):
		self._enorden(self.raiz)
		print()

	def _enorden(self, tmp):
		if tmp:
			self._preorden(tmp.izq)
			print(tmp.valor,end = ' ')
			self._preorden(tmp.der)

	def postorden(self):
		self._preorden(self.raiz)
		print()

	def _postorden(self, tmp):
		if tmp:
			self._preorden(tmp.izq)
			self._preorden(tmp.der)
			print(tmp.valor,end = ' ')
	
	def altura(self):
		if self.raiz!=None:
			return self._altura(self.raiz,0)
		else:
			return 0

	def _altura(self,tmp, altPrevia):
		if tmp==None: return altPrevia
		alturaIzq=self._altura(tmp.izq,altPrevia+1)
		alturaDer=self._altura(tmp.der,altPrevia+1)
		return max(alturaIzq, alturaDer)

	def buscar(self,valor):
		if self.raiz!=None:
			return self._buscar(valor,self.raiz)
		else:
			return None

	def _buscar(self,valor,tmp):
		if valor==tmp.valor:
			return tmp
		elif valor<tmp.valor and tmp.izq!=None:
			return self._buscar(valor,tmp.izq)
		elif valor>tmp.valor and tmp.der!=None:
			return self._buscar(valor,tmp.der)

	def eliminar(self,valor):
		return self._eliminar(self.buscar(valor))

	def _eliminar(self,tmp):


		if tmp==None or self.buscar(tmp.valor)==None:
			print("No se encuentra el valor")
			return None 

		def minimValor(tmp):
			actual=tmp
			while actual.izq!=None:
				actual=actual.izq
			return actual

		def numHijos(tmp):
			numHijos=0
			if tmp.izq!=None: 
				numHijos+=1
			if tmp.der!=None:
				numHijos+=1
			return numHijos

		nodoPadre=tmp.padre

		nodoHijo=numHijos(tmp)

		if nodoHijo==0:

			if nodoPadre!=None:
				if nodoPadre.izq==tmp:
					nodoPadre.izq=None
				else:
					nodoPadre.der=None
			else:
				self.raiz=None

		if nodoHijo==1:

			if tmp.izq!=None:
				hijo=tmp.izq
			else:
				hijo=tmp.der

			if nodoPadre!=None:
				if nodoPadre.izq==tmp:
					nodoPadre.izq=hijo
				else:
					nodoPadre.der=hijo
			else:
				self.raiz=hijo

			# correct the padre pointer in node
			hijo.padre=nodoPadre

		if nodoHijo==2:

			siguiente=minimValor(tmp.der)

			tmp.valor=siguiente.valor

			self._eliminar(siguiente)

			return

		if nodoPadre!=None:
			nodoPadre.altura=1+max(self.altura(nodoPadre.izq),self.altura(nodoPadre.der))
			self.validaEliminacion(nodoPadre)

	def confirmaAgre(self,tmp,ajuste=[]):
		if tmp.padre==None: return
		ajuste=[tmp]+ajuste

		alturaIzq =self.altura(tmp.padre.izq)
		alturaDer=self.altura(tmp.padre.der)

		if abs(alturaIzq-alturaDer)>1:
			ajuste=[tmp.padre]+ajuste
			self.balanceo(ajuste[0],ajuste[1],ajuste[2])
			return

		nuevaAltura=1+tmp.altura 
		if nuevaAltura>tmp.padre.altura:
			tmp.padre.altura=nuevaAltura

		self.confirmaAgre(tmp.padre,ajuste)

	def validaEliminacion(self,tmp):
		if tmp==None: return

		if abs(self.altura(tmp.izq)-self.altura(tmp.der))>1:
			y=self.hijoMayor(tmp)
			x=self.hijoMayor(y)
			self.balanceo(tmp,y,x)

		self.validaEliminacion(tmp.padre)

	def balanceo(self,z,y,x):
		if y==z.izq and x==y.izq:
			self.rotDer(z)
		elif y==z.izq and x==y.der:
			self.rotIzq(y)
			self.rotDer(z)
		elif y==z.der and x==y.der:
			self.rotIzq(z)
		elif y==z.der and x==y.izq:
			self.rotDer(y)
			self.rotIzq(z)

	def rotDer(self,z):
		sub_raiz=z.padre 
		y=z.izq
		t3=y.der
		y.der=z
		z.padre=y
		z.izq=t3
		if t3!=None: t3.padre=z
		y.padre=sub_raiz
		if y.padre==None:
				self.raiz=y
		else:
			if y.padre.izq==z:
				y.padre.izq=y
			else:
				y.padre.der=y		
		z.altura=1+max(self.altura(z.izq),
			self.altura(z.der))
		y.altura=1+max(self.altura(y.izq),
			self.altura(y.der))

	def rotIzq(self,z):
		sub_raiz=z.padre 
		y=z.der
		t2=y.izq
		y.izq=z
		z.padre=y
		z.der=t2
		if t2!=None: t2.padre=z
		y.padre=sub_raiz
		if y.padre==None: 
			self.raiz=y
		else:
			if y.padre.izq==z:
				y.padre.izq=y
			else:
				y.padre.der=y
		z.altura=1+max(self.altura(z.izq),
			self.altura(z.der))
		y.altura=1+max(self.altura(y.izq),
			self.altura(y.der))

	def altura(self,tmp):
		if tmp==None: 
			return 0
		return tmp.altura

	def hijoMayor(self,tmp):
		izq=self.altura(tmp.izq)
		der=self.altura(tmp.der)
		return tmp.izq if izq>=der else tmp.der


t = ArbolAVL()
t.agregar(1)
t.agregar(23)
t.agregar(45)
t.agregar(86)
t.agregar(89)
t.agregar(5)

t.preorden()
t.enorden()

t.eliminar(23)

t.preorden()
t.enorden()