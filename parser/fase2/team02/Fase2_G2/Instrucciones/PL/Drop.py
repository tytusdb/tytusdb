from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion
from Instrucciones.PL import Func, Declaracion,Execute,Asignacion,Return,If
from Instrucciones.Identificador import Identificador

class Drop(Instruccion):
    def __init__(self, id,strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        

 

    def getparam(self):
        pass

    def ejecutar(self, tabla, arbol):
        
        pass

    def analizar(self, tabla, arbol):
       
        resultado = None
      
        return resultado
        
    def traducir(self, tabla, arbol):
        cadena = ""
        funcname = ""
        print("agrego  Drop  ",self.id,"......")


        tabla.delFuncion(self.id)
