from ast.Expresion import Expresion
from ast.Symbol import Symbol
from ast.Expresion import Expresion
from ast.Symbol import TIPOVAR as Tipo
from ast.Sentencia import Sentencia
import Reportes.Nodo as N

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
        var=""
        try: 
              f = open("var.txt", "r")
              var=str(f.read())
              f.close()
              execr = N.Nodo()
              r=execr.addencabezado("Insercion Tabla: "+self.id,var) 
              

              c= int(var)+1

              f = open ('var.txt', "w")        
              f.write(str(c))
              f.close()
        except:
              pass
        

        for key in self.sentencias:
            try:       
                    print(" yn")
                    y = key.getValor(entorno,tree) 
                    print(" y= "+str(y))
                    ty="1"

                    try: 
                           ty = key.getTipo(entorno,tree) 
                    except:
                           pass

                    try: 
                           print("ingresara sentencia graphiz")
                           execr = N.Nodo()
                           r=execr.append(ty,y) 
                           print("salio graphiz")

                           execr.apuntar(var,r)

                    except:
                           pass

                    
            except:
                    pass
                     
        
        tree.agregarnodos(self)
        return False
