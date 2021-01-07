from enum import Enum


class TIPO_DATO(Enum):
    VARIABLE = 1
    ARREGLO = 2
    ENTERO = 3
    FLOTANTE = 4
    CHARACTER = 5
    STRING = 6
    ETIQUETA = 7
    BOOLEAN = 8


class Simbolo():
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor, temporal):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.temporal = temporal


class TablaDeSimbolos():
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            print('Error: variable ', id, ' no definida.')
            return None
        return self.simbolos[id]

    def actualizar(self, simbolo):
        if not simbolo.id in self.simbolos:
            print('Error: variable ', simbolo.id, ' no definida.')
        else:
            self.simbolos[simbolo.id] = simbolo

    def eliminar(self, id):
        if id in self.simbolos:
            del self.simbolos[id]
            