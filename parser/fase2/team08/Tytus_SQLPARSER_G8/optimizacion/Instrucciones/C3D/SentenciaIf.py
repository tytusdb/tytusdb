from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class SentenciaIf(InstruccionC3D):

    def __init__(self,opIzq, relacional, opDer, instrucciones, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.opIzq = opIzq
        self.relacional = relacional
        self.opDer = opDer
        self.instrucciones = instrucciones
        print("ENTRO A if")
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(" linea: " + str(self.linea) + " columna: " + str(self.columna))
        
        if self.opDer == None :
            return "\rif __name__ == \"__main__\":"
         
        if(self.relacional ==  "="):
             self.relacional = "=="
        
        return "if (" + str(self.opIzq) + " " + self.relacional + " " + str(self.opDer) + "):"
        
