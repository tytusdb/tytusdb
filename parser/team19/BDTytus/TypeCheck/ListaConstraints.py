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