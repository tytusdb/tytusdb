import Atributo as Atributo
class ListaAtributos:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def agregarAtributo(self,nuevo:Atributo):
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
