from abc import ABC, abstractmethod
#from graphviz import Digraph


class Instruccion(ABC):
        
    @abstractmethod
    def ejecutar(self, tabla, arbol):
        #print('Ejecutando...?')
        if  self.strGram:
            arbol.lRepDin.append(self.strGram)
        pass
    
    def __init__(self, tipo, linea, columna, strGram):
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.nodoPadre = None
        self.nodosLista = []
        self.strGram = strGram

    #@abstractmethod
    #def nodoGraphviz(self, nodoPadre, nodosLista):
    #    self.nodoPadre = nodoPadre
    #    self.nodosLista = nodosLista

        
'''   
class Prueba(Instruccion):

    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))


p = Prueba("imprime",None,1,2)
p.ejecutar(None,None)
'''