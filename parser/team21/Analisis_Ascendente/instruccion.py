class Instruccion:
    'clase abstracta'

#CREATE TABLE
class CreateTable(Instruccion):
    def __init__(self, id, campos):
        self.id = id
        self.campos = campos

class Campo(Instruccion):
    '''#1 ID tipo
       #2 CONSTRAINT
       #3 FOREIGN
       #4 PRIMARY'''
    def __init__(self, caso, id, tipo, acompaniamiento, idFk, tablaR, idR):
        self.caso = caso
        self.id = id
        self.tipo = tipo
        self.acompaniamiento = acompaniamiento
        self.idFk = idFk
        self.tablaR = tablaR
        self.idR = idR

class Acompaniamiento(Instruccion):
    def __init__(self, tipo, valorDefault):
        self.tipo = tipo
        self.valorDefault = valorDefault

#TIPOS DE DATO
class Tipo(Instruccion):
    def __init__(self, tipo, longitud):
        self.tipo = tipo
        self.longitud = longitud


