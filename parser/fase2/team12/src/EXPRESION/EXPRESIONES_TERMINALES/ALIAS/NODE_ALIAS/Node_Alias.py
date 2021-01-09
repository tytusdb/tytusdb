import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion

class Alias_Expresion(Expresion):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Type_Expresion(Data_Type.non)
        self.alias = '?column?'

    def execute(self, enviroment):

        exp = self.hijos[0]
        id = self.hijos[1]

        expValue = exp.execute(enviroment)

        if exp.tipo.data_type == Data_Type.error :

            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = expValue
            return self.valorExpresion
        
        else :

            self.alias = id.valor
            self.tipo = exp.tipo
            self.valorExpresion = expValue
            return self.valorExpresion

    def compile(self, enviroment):
        print("")
    
    def getText(self):
        expresionAlias = self.hijos[0]
        nombreAlias = self.hijos[1]

        if nombreAlias.nombreNodo == 'Identificador':
            stringAlias = expresionAlias.getText() + ' as ' + nombreAlias.valor
            return stringAlias
        else:
            stringAlias = expresionAlias.getText() + ' as \'' + nombreAlias.valor + '\''
            return stringAlias    