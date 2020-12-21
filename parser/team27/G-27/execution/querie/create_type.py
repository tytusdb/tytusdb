import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/execution/querie')
sys.path.append('../tytus/storage')
from querie import * 
from environment import *
from table import *
from column import *
from storageManager import jsonMode as admin
from typ import *

class Create_Type(Querie):
    """
    name: nombre del nuevo tipo de dato
    array: arreglo que contiene objetos Literal
    """
    def __init__(self, name, array, row, column):
        Querie.__init__(self, row, column)
        self.name = name
        self.array = array

    def execute(self, environment):
        values = []

        for value in self.array:
            valor = value.execute(environment)
            print(valor['typ'])
            if valor['typ'] != Type.STRING:
                return {'Error': 'El tipo de dato no es una cadena', 'Fila' : self.row, 'Columna' : self.column}

            values.append(valor['value'])
            print(valor['value'])
        
        for i in range(len(values)):
            if i+1 < len(values):
                for j in range(i+1, len(values)):
                    print(values[i])
                    print(values[j])
                    if values[i] == values[j]:
                        return {'Error': 'El valor del enum ya fue ingresado anteriormente' , 'Fila':self.row, 'Columna': self.column}
