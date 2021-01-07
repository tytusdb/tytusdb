class Exp:
    'clase abstracta'


#EXPRESION


class Unario(Exp):
    def __init__(self, operador, op,fila,columna):
        self.operador = operador
        self.op = op
        self.fila = fila
        self.columna = columna


class Primitivo(Exp):
    def __init__(self, valor,fila,columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna


class Id(Exp):
    def __init__(self, id,fila,columna):
        self.id = id
        self.fila = fila
        self.columna = columna

class Funcion(Exp):
    def __init__(self,id,expresiones,fila,columna):
        self.id = id
        self.listaexpresiones = expresiones
        self.fila = fila
        self.columna = columna
