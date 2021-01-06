from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class While(Instruccion):
    def __init__(self, opNot, E, instrucciones, fila, columna):
        self.opNot = opNot
        self.E = E
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna