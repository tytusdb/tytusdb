import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\C3D\\')
sys.path.append(c3d_dir)

group_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DML\\Groups')
sys.path.append(group_path)

ent_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\ENTORNO\\')
sys.path.append(ent_dir)

from Nodo import Nodo
from Union import Union
from UnionAll import UnionAll
from Intersect import Intersect
from Except import Except
from Tipo_Expresion import Type_Expresion
from Tipo import Data_Type

class Sentencia_Return(Nodo):

    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
        self.valorReturn = None
        self.tipoReturn = Type_Expresion(Data_Type.non)
    
    def execute(self, enviroment):
        print('Ejecutando return')
        expReturn = self.hijos[0]
        self.valorReturn = expReturn.execute(enviroment)
        self.tipoReturn = expReturn.tipo
        print('Valor Return: ', self.valorReturn)
        print('Valor Return: ', self.tipoReturn.data_type)
        return self
    
    def compile(self, enviroment):
        pass

    def getText(self):
        expReturn = self.hijos[0]
        stringExp = str(expReturn.getText())
        return 'RETURN ' + stringExp + '\n'
