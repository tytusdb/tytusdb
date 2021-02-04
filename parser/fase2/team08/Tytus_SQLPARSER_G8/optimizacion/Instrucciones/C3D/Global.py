from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class Global(InstruccionC3D):

    def __init__(self, valor, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.valor = valor
        print("ENTRO A GLOBAL")
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        
        return "global "+self.valor
