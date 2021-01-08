from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.TablaSimbolosPL.TipoPL import TipoPL, Tipo_DatoPL

from enum import Enum

class Direction_Enum(Enum):
    ABSOLUTE=0
    RELATIVE= 1
    FORWARD= 2
    BACKWARD= 3
    NEXT = 4
    LAST = 5
    PRIOR= 6
    FIRST= 7

class Directions(InstruccionPL):
    def __init__(self, valor,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self, valor,linea,columna, strGram)
        self.valor = valor
        self.tipo = tipo
    def ejecutar(self):
        print('ejecutar')
    def traducir(self):
        print('Traducciendo')