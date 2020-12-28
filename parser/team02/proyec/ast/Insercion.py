from ast.Expresion import Expresion
from ast.Symbol import Symbol
from ast.Expresion import Expresion
from ast.Symbol import TIPOVAR as Tipo
from ast.Sentencia import Sentencia

class Insercion(Sentencia):

    def __init__(self,id,value,line, column,declare):

        self.id = id
        self.line= line
        self.column = column
        self.sentencias = value
        self.type = declare
        self.ambito = ""
       


    def setAmbito(self,ambito):
        self.ambito = ambito


    def ejecutar(self,entorno,tree):
        print("zz1 Insercion")
        
        print("sentencias vpp ")      

        y= {}      
        for key in self.sentencias:
            try:       
                    print(" yn")
                    y = key.getValor(entorno,tree) 
                    print(" y= "+str(y))
                    
            except:
                    pass
                     
        
        tree.agregarnodos(self)
        return False
