import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/execution/querie')
sys.path.append('../tytus/storage')
from querie import * 
from environment import *
from table import *
from column import *
from typ import *
from storageManager import jsonMode as admin

class Least(Querie):

    def __init__(self,listaDatos, row,column):
        Querie.__init__(self, row, column)
        self.listaDatos = listaDatos

    def execute(self, environment,tableName):
        if isinstance(self.listaDatos,list):       
            if len(listaDatos) == 0:
                return {'value':'null', 'typ':Type.NULL}
            else:
                tipo = None
                for value in self.listaDatos:
                    valor = value.execute(environment)
                    if tipo == None:
                        tipo = valor['typ']
                    else:
                        if tipo != valor['typ']:
                            return {'Error': 'La lista de datos difiere en los tipos', 'Fila':self.row, 'Columna': self.column }    
                menor = None
                for value in self.listaDatos:
                    valor = value.execute(environment)
                    if menor == None:
                        menor = valor['value']
                    else:
                        if menor > valor['value']:
                            menor= valor['value']
            return{'value':menor,'typ':tipo}          
        else:
            return {'Error': 'El parametro debe de ser una lista', 'Fila':self.row, 'Columna': self.column}