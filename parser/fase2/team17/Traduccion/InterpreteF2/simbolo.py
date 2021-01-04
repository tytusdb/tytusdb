from InterpreteF2.Valor.Valor import Valor

class Simbolo():

    def __init__(self, id, tipo, valor):
        self.id = id
        self.tipo = tipo
        self.valor:Valor = valor
        self.temporal = ""

    def setTemp(self, tmp):
        self.temporal = str(tmp)

    def getTemp(self):
        return str(self.temporal)
