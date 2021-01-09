from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D
from optimizacion.Instrucciones.C3D.ExpresionesOpti import ExpresionesOpti
class PrintC3D(InstruccionC3D):

    def __init__(self,nombre, expresion, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.valor = nombre
        self.expresion = expresion
        print("ENTRO A print")
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(" linea: " + str(self.linea) + " columna: " + str(self.columna))
        cadena = ""
        if isinstance( self.expresion, ExpresionesOpti):
            cadena = self.expresion.ejecutar(tabla, arbol)
        else:
            if(self.valor != None and self.expresion == "f"):
                if(len(self.valor)==5):
                    if(self.valor[0] == "{" and self.valor[1] == "m" and self.valor[2] == "s" and self.valor[3] == "j" and self.valor[4] == "}"):
                        cadena = str(self.expresion) + str(self.valor)
                        return "\tprint(\""+cadena+"\")"
                    else:
                        cadena = str(self.expresion) + str(self.valor)
                else:
                    cadena = str(self.expresion) + str(self.valor)
            else:
                cadena = str(self.expresion)
        
        return "print("+cadena+")"
        
        '''if self.valor == None :
            expresion1 = ""
            if isinstance(self.expresion , ExpresionesOpti):
                expresion1 = self.expresion.ejecutar(tabla, arbol)
            
            return "print("+expresion1+")"
        else:
            return "print(f\""+self.expresion+"\")"
        '''
