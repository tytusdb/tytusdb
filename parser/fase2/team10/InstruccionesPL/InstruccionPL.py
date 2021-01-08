from abc import ABC, abstractmethod

class InstruccionPL():
        
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