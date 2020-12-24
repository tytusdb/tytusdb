
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
import numpy as np
#from pylab import *

class WidthBucket(Instruccion):
    def __init__(self, val1, val2, val3, val4, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3
        self.val4 = val4

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #print("WIDTHBUCKET", self.val1.valor, self.val2.valor, self.val3.valor, self.val4.valor)
        if isinstance(self.val1.valor, int) and isinstance(self.val2.valor, int) and isinstance(self.val3.valor, int) and isinstance(self.val4.valor, int):
            pass
        bin_size = 1
        min_edge = 2 
        max_edge = 3
        N = int((max_edge-min_edge)/bin_size)
        Nplus1 = N + 1
        
        bin_list = np.linspace(min_edge, max_edge, Nplus1,5)
        print(bin_list)
    
        '''
        
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

instruccion = WidthBucket("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''