from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class Loop(Instruccion):
    def __init__(self, instrucciones, linea, columna):
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna