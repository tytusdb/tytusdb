import Atributo as Atributo
class ListaAtributos:
    def __init__(self):
        self.columnNumber = 0
        self.primero=None
        self.ultimo=None

    def agregarAtributo(self,nuevo:Atributo):
        self.columnNumber = self.columnNumber + 1
        nuevo.columnNumber = self.columnNumber
        if self.primero is None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            nuevo.anterior=self.ultimo
            self.ultimo=nuevo

    def existeAtributo(self,columna:str):
        existe = False
        actual = self.primero
        while(actual!=None):
            if actual.nombre == columna:
                existe = True
                break
            actual = actual.siguiente
        return existe

    def obtenerTipoAtributo(self,columna:str):
        actual = self.primero
        while(actual!=None):
            if actual.nombre == columna:
                return actual.tipo
            actual = actual.siguiente
        return None

    def alterAddPK(self,columns:list):
        #0:Encontro todas las columnas, 5:columnas fuera de limites
        for columna in columns:
            encontrado = False
            actual = self.primero
            while(actual!=None):
                if(actual.nombre==columna):
                    actual.isPrimary = True
                    encontrado = True
                    break
                actual = actual.siguiente
            if encontrado == False:
                return 5
        return 0

    def alterDropPK(self):
        actual = self.primero
        while(actual!=None):
            actual.isPrimary = False
            actual = actual.siguiente

    def eliminiarNAtributo(self,niteracion:int):
        contador = 1
        actual = self.primero
        atras = None
        while(contador<=niteracion and actual!=None):
            if contador == niteracion:
                if actual == self.primero:
                    self.primero = self.primero.siguiente
                    self.primero.anterior = None
                else:
                    atras.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
            contador += 1
            atras = actual
            actual = actual.siguiente
