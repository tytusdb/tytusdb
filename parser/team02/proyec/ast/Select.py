from ast.Expresion import Expresion
from ast.Symbol import Symbol
from ast.Expresion import Expresion
from ast.Symbol import TIPOVAR as Tipo
from ast.Sentencia import Sentencia
import Reportes.ReporteD as Sentencias

class Select(Sentencia):
    #SELECT selectclausules FROM  selectbody wherecondicion
    #Selecttable : SELECT selectclausules FROM  selectbody wherecondicion
    #St[0] = Select(t[2],t[4],t.slice[1].lineno,find_column(t.slice[1]),t[5])

    def __init__(self,id,value,line, column,declare):

        self.id = id
        self.line= line
        self.column = column
        self.value = value
        self.type = declare
       
    def ejecutar(self,entorno,tree):
        print("zVV Select")
        
        #print("sentencias v "+Expres.id)     

        y= {} 
        try:         
            if self.id.type=="*":
                print("xxc")
                try:       
                    print("zVV 1")
                    if self.value.type=="ID":
                        y =  self.value.value 
                        print(" y= "+str(y))
                        SentenciasR = Sentencias.ReporteD()
                        print("7000a ")
                        SentenciasR.write(y,"Select*from "+y,entorno,tree)
                        print("7001 ")
                except:
                        pass
        except:
            pass
                     
        
        tree.agregarnodos(self)
        return False
