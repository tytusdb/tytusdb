from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import tytus.parser.fase2.team21.Analisis_Ascendente.ascendente as tr
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

class AlterIndex(Instruccion):
    def __init__(self,id,tipo,fila,columna):
        self.tipo = tipo
        self.id = id
        self.fila = fila
        self.columna = columna
