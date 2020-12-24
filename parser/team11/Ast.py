from prettytable import PrettyTable
from datetime import date
from datetime import datetime
import math
import random


class Nodo:
    '''Clase que define la estructura de los nodos del AST.'''
    
    def __init__(self, etiqueta, valor, hijos = [], linea = -1, columna = -1, gramatica = ''):
        self.etiqueta = etiqueta
        self.valor = valor
        self.hijos = hijos
        self.linea = linea
        self.columna = columna
        self.gramatica = gramatica

    def toString(self):
        cadena = self.etiqueta + ',' + self.valor + ' L: ' + str(self.linea) + ' C: ' + str(self.columna)+'\n'
        for n in self.hijos:
            cadena = cadena + ' --- ' + n.toString()
        return cadena

#---------------------------------------------------------------------------------------------------------------
