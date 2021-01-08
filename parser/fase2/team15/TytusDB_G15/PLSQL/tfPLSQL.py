from enum import Enum


class TIPO_DATO(Enum):
    VARIABLE = 1
    ARREGLO = 2
    ENTERO = 3
    FLOTANTE = 4
    CHARACTER = 5
    STRING = 6
    ETIQUETA = 7


class Funcion():
    'Esta clase representa una funcion dentro de nuestra tabla de funciones'

    def __init__(self, id, tipo, parametros, temporales, instrucciones):
        self.id = id
        self.tipo = tipo
        self.parametros = parametros
        self.temporales = temporales
        self.instrucciones = instrucciones


class TablaDeFunciones():
    'Esta clase representa la tabla de Funciones'

    def __init__(self, funciones=None):
        if funciones is None:
            funciones = {}
        self.funciones = funciones

    def agregar(self, funcion):
        self.funciones[funcion.id] = funcion

    def obtener(self, id):
        if not id in self.funciones:
            print('Error: funcion ', id, ' no definida.')
            return None
        return self.funciones[id]

    def actualizar(self, funcion):
        if not funcion.id in self.funciones:
            print('Error: funcion ', funcion.id, ' no definida.')
        else:
            self.funciones[funcion.id] = funcion

    def eliminar(self, id):
        if id in self.funciones:
            del self.funciones[id]
