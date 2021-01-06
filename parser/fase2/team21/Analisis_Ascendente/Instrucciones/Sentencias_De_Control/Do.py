from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class Do(Instruccion):
    def __init__(self, caso, E, declareInst, beginInst, linea, columna):
        self.caso = caso
        self.E = E
        self.declareInst = declareInst
        self.beginInst = beginInst
        self.linea = linea
        self.columna = columna