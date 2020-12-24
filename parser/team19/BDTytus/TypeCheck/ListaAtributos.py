import TypeCheck.Atributo as Atributo
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

    def getNumeroColumna(self,nombreColumna:str):
        numero = 1
        actual = self.primero
        while actual is not None:
            if actual.nombre == nombreColumna:
                return numero
            numero += 1
            actual = actual.siguiente
        return 0

    def eliminarAtributo(self,nombreAtributo:str):
            actual = self.primero
            while(actual!=None):
                if actual.nombre == nombreAtributo:
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