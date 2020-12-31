from abc import ABC, abstractmethod
import sys
sys.path.append("..")

class Instruccion(ABC):
        
    @abstractmethod
    def ejecutar(self, tabla, arbol):
        print('Ejecutando...')
        pass
    
    def __init__(self, tipo, linea, columna):
        self.tipo = tipo
        self.linea = linea
        self.columna = columna


'''   
class Prueba(Instruccion):

    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))


p = Prueba("imprime",None,1,2)
p.ejecutar(None,None)
'''