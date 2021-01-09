from abc import ABC, abstractmethod
import sys
sys.path.append("..")

class InstruccionC3D(ABC):
        
    @abstractmethod
    def ejecutar(self, tabla, arbol):
        print('Ejecutando...')
        pass
    
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna
        self.tabulacion = "\t"

'''
class Prueba(InstruccionC3D):

    def __init__(self, valor, tipo, linea, columna):
        InstruccionC3D.__init__(self,tipo,linea,columna)
        self.valor = valor
        print("ENTRO A PRUEBA")
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))


p = Prueba("imprime",None,1,2)
p.ejecutar(None,None)
'''


