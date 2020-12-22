import TypeCheck.Atributo as Atributo
class ListaAtributos:
    def __init__(self):
        self.columnNumber = 0
        self.primero=None
        self.ultimo=None

    def agregarAtributo(self,nuevo:Atributo):
        self.columnNumber = self.numero + 1
        nuevo.numero = self.columnNumber
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

    def obtenerAtributo(self,columna:str):
        actual = self.primero
        while (actual != None):
            if actual.nombre == columna:
                break
            actual = actual.siguiente
        return actual

    def obtenerTipoAtributo(self,columna:str):
        actual = self.primero
        while(actual!=None):
            if actual.nombre == columna:
                return actual.tipo
            actual = actual.siguiente
        return None

    def eliminiarNAtributo(self,number:int):
        actual = self.primero
        atras = None
        while(actual!=None):
            if actual.numero == number:
                if actual == self.primero:
                    self.primero = self.primero.siguiente
                    self.primero.anterior = None
                else:
                    atras.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                break
            atras = actual
            actual = actual.siguiente

    def eliminarAtributo(self,nombreAtributo:str):
            actual = self.primero
            while(actual!=None):
                if actual.nombreBase == nombreAtributo:
                    if self.primero == self.ultimo:
                        self.primero = self.ultimo = None
                    elif actual == self.primero:
                        self.primero = self.primero.siguiente
                        self.primero.anterior = None
                    elif actual == self.ultimo:
                        self.ultimo = self.ultimo.anterior
                        self.ultimo.siguiente = None
                    else:
                        actual.siguiente.anterior = actual.anterior
                        actual.anterior.siguiente = actual.siguiente
                    return 0
                actual = actual.siguiente
            return 1