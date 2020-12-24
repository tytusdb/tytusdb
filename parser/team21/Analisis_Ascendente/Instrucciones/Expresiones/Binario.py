from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class Binario(Instruccion):

    '''#1 LENGTH
       #2 SHA256
       #3 ENCODE
       #4 DECODE
       #5 SUBSTRING | SUBSTR
       #6 TRIM
       #7 GET_BYTE
       #8 SET_BYTE
       #9 CONVERT
       #10 GREATEST
       #11 LEAST '''

    def __init__(self, caso, valor1, valor2, valor3,fila,columna):
        self.caso = caso
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3
        self.fila = fila
        self.columna = columna

