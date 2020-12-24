from ast.Expresion import Expresion
from Valor.Asignacion import Asignacion
from ast.Declarevar import Declarevar


class Label(Expresion) :
  
    
    def __init__(self, id, ins,line,column,tipo) :
        print("va a recorrer con "+id)

        for Expres in ins:
            print("vasent1")
              
        self.id = id
        self.sentencias = ins
        self.line = line
        self.column = column
        self.ambito = tipo
        self.type = tipo
        self.value = ""

    def setAmbito(self,ambito):
        self.ambito = ambito

    def ejecutar(self,entorno,tree):
        salir = False
        print("100 ej")

        for Expres in self.sentencias:
            print("100 eoo "+Expres.id)        

           # if(isinstance(Expres,Declarevar.Declarevar) ):
            Expres.setAmbito(self.id)
            print("100 wj")

            try:
                print("100 zz")
                Expres.ejecutar(entorno,tree)
                 #if(Expres.ejecutar(entorno,tree) == True):
                  #  return True
            except:
                pass

        return False


def getTipo(self):
        return "LABEL"
