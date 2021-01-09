from Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class Alias(Instruccion):
    def __init__(self,idnuevo,dolarnumero,idviejo,fila,columna):
        self.idnuevo = idnuevo
        self.dolarnumero = dolarnumero
        self.idviejo = idviejo
        self.fila = fila
        self.columna = columna

