from enum import Enum

class TIPO(Enum) :
    DATABASE = 1
    TABLE = 2
    COLUMN = 3
    SMALLINT = 4
    INTEGER = 5
    BIGINT = 6
    DECIMAL = 7
    NUMERIC = 8
    REAL = 9
    DOUBLE_PRECISION = 10
    CHARACTER_VARYING = 11
    VARCHAR = 12
    CHARACTER = 13
    CHAR = 14
    TEXT = 15
    TIMESTAMP = 16
    DATE = 17
    TIME = 18
    INTERVAL = 19
    BOOLEAN = 20

class Simbolo() :
    
    def __init__(self, id, tipo, valor,ambito,contador=0,indice=0,pk=False,fk=False) :
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.ambito =  ambito
        self.contador = contador
        self.indice = indice
        self.pk = pk
        self.fk = fk

class Tabla() :
    
    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos

    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        if not id in self.simbolos :
            print('(obtener)Error: variable ', id, ' no definida.')

        return self.simbolos[id]

    def BuscarNombre(self, valor) :
        for simbolo in self.simbolos:
            if self.simbolos[simbolo].valor == valor:
                return self.simbolos[simbolo]
        if not valor in self.simbolos :
            print('(BuscarNombre)Error: variable ', valor, ' no definida.')

    def BuscarAmbito(self, ambito) :
        for simbolo in self.simbolos:
            if self.simbolos[simbolo].ambito == ambito:
                return self.simbolos[simbolo]
        if not ambito in self.simbolos :
            print('(BuscarAmbito)Error: variable ', ambito, ' no definida.')

    def actualizar(self, simbolo) :
        if not simbolo.id in self.simbolos :
            print('(actualizar)Error: variable ', simbolo.id, ' no definida.')
        else :
            self.simbolos[simbolo.id] = simbolo