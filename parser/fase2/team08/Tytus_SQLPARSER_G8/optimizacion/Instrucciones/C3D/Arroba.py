from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class Arroba(InstruccionC3D):

    def __init__(self, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        print("ENTRO A ARROBA")
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return "@with_goto"
        print(" linea: " + str(self.linea) + " columna: " + str(self.columna))
