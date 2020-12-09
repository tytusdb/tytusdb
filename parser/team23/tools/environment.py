from tools.simbolo import *
from error.errores import *

class environment:
    def __init__(self, anterior = None):
        self.variables = dict()
        self.funciones = dict()
        self.prev = anterior

    def save_var(self, id_, valor, tipo, linea, columna):
        env = self

        while env != None:
            if id_ in env.variables:
                errores.append(nodo_error(linea, columna, id_, 'Variable ' + id_ + ' ya declarada.'))
                return
            env = env.prev

        self.variables.setdefault(id_, symbol(valor, tipo, id_))

    def save_function(self, id_, function, linea, columna):
        env = self

        while env != None:
            if id_ in env.funciones:
                errores.append(nodo_error(linea, columna, id_, 'Función ' + id_ + ' ya declarada.'))
                return
            env = env.prev

        self.variables.setdefault(id_, function)

    def get_var(self, id_):
        env = self

        while env != None:
            if id_ in env.variables:
                return env.variables.get(id_)
            env = env.prev

        return None

    def get_function(self, id_):
        env = self

        while env != None:
            if id_ in env.funciones:
                return env.funciones.get(id_)
            env = env.prev

        return None