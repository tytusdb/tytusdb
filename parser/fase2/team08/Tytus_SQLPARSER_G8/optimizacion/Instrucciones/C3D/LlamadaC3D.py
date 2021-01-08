from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class LlamadaC3D(InstruccionC3D):

    def __init__(self, id,linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.id = id
        print("ENTRO A expresiones")
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(" linea: " + str(self.linea) + " columna: " + str(self.columna))
        if self.id != None :
            if(self.id == "main"):
                return self.id + "()"
            else:
                return self.id +"()"

