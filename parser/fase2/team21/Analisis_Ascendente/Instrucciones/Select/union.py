#from Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
class Union(Instruccion):
    def __init__(self, tipo, all, q1, q2):
        self.tipo = tipo
        self.all = all
        self.q1 = q1 
        self.q2 = q2 