from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class LabelC3D(InstruccionC3D):

    def __init__(self, valor, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.valor = valor
        print("ENTRO A GLOBAL")
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
        return "label ."+self.valor