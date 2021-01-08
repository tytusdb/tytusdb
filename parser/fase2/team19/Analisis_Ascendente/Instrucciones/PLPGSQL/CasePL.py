from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes

class CasePL(Instruccion):
    ''' #1 Case search
        #2 Case '''

    def __init__(self, caso, id, cases,elsecaso ,fila, columna):
        self.caso = caso
        self.id = id
        self.cases = cases
        self.elsecaso = elsecaso
        self.fila = fila
        self.columna = columna

    def ejecutar(CasePL , ts, consola, exceptions):

        if CasePL == 1:
            print(CasePL.id)
            print(CasePL.cases)
            print(CasePL.elsecaso)
        elif CasePL == 2:
            print(CasePL.id)
            print(CasePL.cases)
            print(CasePL.elsecaso)

