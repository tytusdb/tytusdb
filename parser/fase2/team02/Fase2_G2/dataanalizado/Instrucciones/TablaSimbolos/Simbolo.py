class Simbolo():
    'Esta clase se utiliza para crear un símbolo de base para una declaración de variable.'

    def __init__(self, id, tipo, valor, linea, columna):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna