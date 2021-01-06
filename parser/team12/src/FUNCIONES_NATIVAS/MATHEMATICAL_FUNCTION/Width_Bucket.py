import sys, os.path
import math

dir_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\EXPRESION\\EXPRESION\\')
sys.path.append(dir_nodo)

ent_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(ent_nodo)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion

class Function_Width_Bucket(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)
    
    def execute(self, enviroment):
        exp = self.hijos[0]
        minValue = self.hijos[1]
        maxValue = self.hijos[2]
        num_buckets = self.hijos[3]
        
        valorExp = exp.execute(enviroment)
        valorMinValue = minValue.execute(enviroment)
        valorMaxValue = maxValue.execute(enviroment)
        valorNum_Buckets = num_buckets.execute(enviroment)

        if exp.tipo.data_type == Data_Type.numeric and minValue.tipo.data_type == Data_Type.numeric and maxValue.tipo.data_type == Data_Type.numeric and num_buckets.tipo.data_type == Data_Type.numeric :

            rango = valorMaxValue - valorMinValue

            if rango == 0 :

                self.tipo = Type_Expresion(Data_Type.error)
                self.valorExpresion = None
                return self.valorExpresion
            
            else :

                if valorNum_Buckets == 0 :
                    
                    self.tipo = Type_Expresion(Data_Type.error)
                    self.valorExpresion = None
                    return self.valorExpresion
                
                else :

                    try:

                        enteroValorNum_Buckets = int(valorNum_Buckets)
                        interval = (rango * 1.0) / (enteroValorNum_Buckets * 1.0)

                        variableAuxiliar = valorMinValue
                        valorMax = 0
                        valorMin = 0
                        auxiliar = 1
                        #print("Rango: " + str(rango))
                        #print("Interval: "+str(interval))
                        
                        

                        if rango > 0 :                                                            

                            self.tipo = Type_Expresion(Data_Type.numeric)

                            if valorExp < valorMinValue :                            
                                self.valorExpresion = 0
                                return self.valorExpresion

                            while variableAuxiliar <= valorMaxValue :

                                #print("Aux: "+str(auxiliar))                                         
                                #print("Valor Pos: "+str(variableAuxiliar))

                                valorMin = variableAuxiliar
                                valorMax = variableAuxiliar + interval

                                if valorExp >= valorMin and valorExp < valorMax :

                                    self.valorExpresion = auxiliar
                                    return self.valorExpresion

                                variableAuxiliar = variableAuxiliar + interval
                                auxiliar = auxiliar + 1

                            self.valorExpresion = auxiliar
                            return self.valorExpresion
                        
                        else : 

                            self.tipo = Type_Expresion(Data_Type.numeric)

                            if valorExp > valorMinValue :            

                                self.valorExpresion = 0
                                return self.valorExpresion

                            while variableAuxiliar >= valorMaxValue :

                                #print("Aux: "+str(auxiliar))                                                           
                                #print("Valor Neg: "+str(variableAuxiliar))
                                valorMin = variableAuxiliar
                                valorMax = variableAuxiliar + interval

                                if valorExp <= valorMin and valorExp > valorMax :

                                    self.valorExpresion = auxiliar
                                    return self.valorExpresion

                                variableAuxiliar = variableAuxiliar + interval
                                auxiliar = auxiliar + 1

                            self.valorExpresion = auxiliar
                            return self.valorExpresion

                    except:

                        self.tipo = Type_Expresion(Data_Type.error)
                        self.valorExpresion = None
                        return self.valorExpresion

        else :

            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            return self.valorExpresion

    def compile(self, enviroment):
        print("compile")
    
    def getText(self):

        exp = self.hijos[0]
        exp2 = self.hijos[1]
        exp3 = self.hijos[2]
        exp4 = self.hijos[3]

        stringReturn = 'width_bucket(' + exp.getText() + ',' + exp2.getText() + ',' + exp3.getText() + ',' + exp4.getText() +')'
        return stringReturn