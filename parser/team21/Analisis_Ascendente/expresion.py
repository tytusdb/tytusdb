class Exp:
    'clase abstracta'

class Expresion(Exp):
    def __init__(self, iz, dr, operador):
        self.iz = iz
        self.dr = dr
        self.operador = operador

class Unario(Exp):
    def __init__(self, operador, op):
        self.operador = operador
        self.op = op

class Primitivo(Exp):
    def __init__(self, valor = 0):
        self.valor = valor

class Id(Exp):
    def __init__(self, id):
        self.id = id