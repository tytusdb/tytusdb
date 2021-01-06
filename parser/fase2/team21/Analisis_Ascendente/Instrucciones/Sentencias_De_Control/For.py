from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class For(Instruccion):
    def __init__(self, caso, E1, reverse, E2, E3, E4, instrucciones, inst, fila, columna):
        self.caso = caso
        self.E1 = E1
        self.reverse = reverse
        self.E2 = E2
        self.E3 = E3
        self.E4 = E4
        self.instrucciones = instrucciones
        self.inst = inst
        self.fila = fila
        self.columna = columna