import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

nodo_select = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\DML\\Select\\')
sys.path.append(nodo_select)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion
from Select import Info_Tabla
from Select import Info_Column

class Sentencia_Case(Expresion):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Type_Expresion(Data_Type.non)
    
    def execute(self, environment):
        
        if len(self.hijos) == 2 :

            #print("Case 2")
            listaCase = self.hijos[0]
            sentenciaElse = self.hijos[1]

            for case in listaCase.hijos:
                
                condicional = case.hijos[0]
                exp = case.hijos[1]

                valorCondicional = condicional.execute(environment)

                if condicional.tipo.data_type == Data_Type.boolean :

                    if valorCondicional == True :

                        valorExp = exp.execute(environment)

                        if exp.tipo.data_type == Data_Type.error or exp.tipo.data_type == Data_Type.non :

                            self.tipo = Type_Expresion(Data_Type.error)
                            self.valorExpresion = None
                            return self.valorExpresion
                        
                        else :

                            self.tipo = exp.tipo
                            self.valorExpresion = valorExp
                            return self.valorExpresion

                else :

                    self.tipo = Type_Expresion(Data_Type.error)
                    self.valorExpresion = None
                    return self.valorExpresion

            valElse = sentenciaElse.hijos[0]            
            valorElse = valElse.execute(environment)

            if valElse.tipo.data_type == Data_Type.error or valElse.tipo.data_type == Data_Type.non :

                self.tipo = Type_Expresion(Data_Type.error)
                self.valorExpresion = None
                return self.valorExpresion

            else :

                self.tipo = valElse.tipo
                self.valorExpresion = valorElse
                return self.valorExpresion

        else :

            for case in listaCase.hijos:
                
                condicional = case.hijos[0]
                exp = case.hijos[1]

                valorCondicional = condicional.execute(environment)

                if condicional.tipo.data_type == Data_Type.boolean :

                    if valorCondicional == True :

                        valorExp = exp.execute(environment)

                        if exp.tipo.data_type == Data_Type.error or exp.tipo.data_type == Data_Type.non :

                            self.tipo = Type_Expresion(Data_Type.error)
                            self.valorExpresion = None
                            return self.valorExpresion
                        
                        else :

                            self.tipo = exp.tipo
                            self.valorExpresion = valorExp
                            return self.valorExpresion

                else :

                    self.tipo = Type_Expresion(Data_Type.error)
                    self.valorExpresion = None
                    return self.valorExpresion
            
            self.tipo = Type_Expresion(Data_Type.character)
            self.valorExpresion = ""
            return self.valorExpresion