from ast.Sentencia import Sentencia
from ast.Declarevar import Declarevar

class Asignacion(Sentencia):
    def __init__(self,id,value,line,column):
        self.id = id
        self.line = line
        self.column = column
        self.value = value
        self.declared = None

    def setAmbito(self,ambito):
        self.declared = ambito

    def ejecutar(self,entorno,tree):

        simbolo = entorno.get(str(self.id))
        y= {}
        y = self.value.getValor(ent,tree)
        if(simbolo == None):
                declarar = Declarevar(str(self.id),y,self.line,self.column,"",self.declared)
                declarar.ejecutar(entorno,tree)
        else:
                    simbolo.value = value
                    entorno.replacesymbol(simbolo)

        return False
