import TypeCheck.Constraint as Constraint

class ListaConstraints:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def agregarConstraint(self, nuevo:Constraint):
        if self.primero is None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            nuevo.anterior=self.ultimo
            self.ultimo=nuevo

    def existePropiedad(self,propiedad:int) -> bool:
        actual = self.primero
        while(actual is not None):
            if actual.propiedad == propiedad:
                return True
            actual = actual.siguiente
        return False

    def existeConstraint(self,nombre):
        existe = False
        actual = self.primero
        while actual is not None:
            if actual.nombreConstraint == nombre:
                existe = True
                break
            actual = actual.siguiente
        return existe

    def eliminarConstraint(self,nombre):
            actual = self.primero
            while(actual!=None):
                if actual.nombreConstraint == nombre:
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