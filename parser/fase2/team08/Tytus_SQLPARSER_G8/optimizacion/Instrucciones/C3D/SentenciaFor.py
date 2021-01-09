from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class SentenciaFor(InstruccionC3D):

    def __init__(self,id, lista, instrucciones, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.id = id
        self.lista = lista
        self.instrucciones = instrucciones
        print("ENTRO A sentenciaFor")
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(" linea: " + str(self.linea) + " columna: " + str(self.columna))
        if self.id == "return":
            return "return"
        else:
            concatenar = ""
            for ins in self.instrucciones:
                concatenar += ins.ejecutar(tabla, arbol)+ "\n"
            
            return "for " + self.id + " in " + ".".join(self.lista) + " :"


