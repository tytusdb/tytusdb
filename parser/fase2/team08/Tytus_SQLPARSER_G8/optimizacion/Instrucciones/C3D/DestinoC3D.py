from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class DestinoC3D(InstruccionC3D):

    def __init__(self,etiqueta, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.etiqueta = etiqueta
        print("ENTRO A destino")
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("linea" + str(self.linea) + " columna: " + str(self.columna))
