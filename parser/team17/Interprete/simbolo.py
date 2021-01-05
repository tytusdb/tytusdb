from Interprete.Valor.Valor import Valor

class Simbolo():

    def __init__(self, id, tipo, valor):
        self.id = id
        self.tipo = tipo
        self.valor:Valor = valor