from abc import ABCMeta, abstractmethod
class Nodo(metaclass=ABCMeta):

    # Constructor
    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        self.nombreNodo = nombreNodo
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.hijos = []

    # Metodos get y set
    def get_nombreNodo(self):
        return self.nombreNodo
    
    def set_nombreNodo(self, nombreNodo):
        self.nombreNodo = nombreNodo

    def get_fila(self):
        return self.fila

    def set_fila(self, fila):
        self.fila = fila

    def get_columna(self):
        return self.columna

    def set_columna(self, columna):
        self.columna = columna
    
    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_hijos(self):
        return self.hijos

    def set_hijos(self, hijos):
        self.hijos = hijos

    # Metodo abstracto execute
    @abstractmethod
    def execute(self, enviroment):
        pass

    @abstractmethod
    def compile(self, enviroment):
        pass

    @abstractmethod
    def getText(self):
        pass