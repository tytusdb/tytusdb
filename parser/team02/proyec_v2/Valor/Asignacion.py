from ast.Sentencia import Sentencia
from ast.Declarevar import Declarevar

class Asignacion(Sentencia):

    def __init__(self,id,value,line,column,tipo):
        self.id = id
        self.type = tipo
        self.line = line
        self.column = column
        self.value = value
        self.ambito = None      

    def setAmbito(self,ambito):
        self.ambito = ambito

    def ejecutar(self,entorno,tree):
        print("1001 ")
        simbolo = entorno.get(str(self.id))#sino esta en la tabla de symbol
        print("tt6 ")
        #print("tt6 "+self.value)

        y= {}
       # if(not isinstance(self.value,dict)):
        y = self.value.getValor(entorno,tree) 
        print("tt6zp9 con y= ")
        print(y)

        print("tt6z ")

        if(simbolo == None):
                print("1002b ")
                print("1002b symbolline="+self.line)
                print("1002b symbolcolumn="+self.column)
                declarar = Declarevar(str(self.id),str(y),self.line,self.column,self.type)
                print("1002k ")
                declarar.ejecutar(entorno,tree)

        else:
                    print("1002c ")
                    simbolo.value = value
                    entorno.replacesymbol(simbolo)

        return False
