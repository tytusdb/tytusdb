from InterpreteF2.Primitivos.TIPO import TIPO

'''
    SUMA
        0  1  2  3
    ---------------
    0 | 0  1  2  %  
    1 | 1  1  2  %  
    2 | 2  2  2  2 
    3 | %  %  2  2  
'''

class COMPROBADOR_deTipos:

    def __init__(self, izq, der, tipoOpera):
        self.izq:int = izq
        self.der:int = der
        self.tipoOperacion = tipoOpera
        self.Matrix_SUMA = [ [ 0, 1, 2,-1], [ 1, 1, 1,-1], [ 2, 2, 2, 2], [-1,-1, 2, 2] ];

    def getTipoResultante(self):
        if self.tipoOperacion == "+":
            return self.Matrix_SUMA[self.izq][self.der]
        # if self.tipoOperacion == "-":
            # return self.Matrix_RESTA[self.izq, self.der]


