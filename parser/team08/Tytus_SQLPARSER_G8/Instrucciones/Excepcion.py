class Excepcion():
    'Esta clase se utiliza para guardar errores de tipo léxico, sintáctico y semántico.'

    def __init__(self, id, tipo, valor, linea, columna):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna