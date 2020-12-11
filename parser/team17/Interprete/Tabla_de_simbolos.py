from Interprete.simbolo import Simbolo

class Tabla_de_simbolos(Simbolo) :

    def __init__(self) :
        self.Pila_de_tablas  = list( dict() )
        self.Tabla_deSimbolos = dict()

    def NuevoAmbito(self):
        nuevoAmito = dict();
        self.Pila_de_tablas.append(nuevoAmito)

    def BorrarAmbito(self):
        self.Pila_de_tablas.pop()
