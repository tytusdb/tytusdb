from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class DeclaracionC3D(InstruccionC3D):

    def __init__(self,id, expre, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.id = id
        self.expresion = expre
        print("ENTRO A destino")
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("linea" + str(self.linea) + " columna: " + str(self.columna))
