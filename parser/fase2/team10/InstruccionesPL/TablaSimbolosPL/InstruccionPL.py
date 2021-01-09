from abc import ABC, abstractmethod
#from graphviz import Digraph


class InstruccionPL(ABC):
        
    
    @abstractmethod
    def ejecutar(self, tabla, arbol):
        #print('Ejecutando...?')
        print('ejectuar')


    @abstractmethod
    def traducir(self, tabla, arbol):
        print('Ejecutando...?')
   



    def __init__(self, tipo, linea, columna, strGram):
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.nodoPadre = None
        self.nodosLista = []
        self.strGram = strGram