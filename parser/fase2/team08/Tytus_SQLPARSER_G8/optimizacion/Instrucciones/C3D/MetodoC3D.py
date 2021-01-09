from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class MetodoC3D(InstruccionC3D):

    def __init__(self,nombre, instrucciones, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.nombre = nombre
        self.instrucciones = instrucciones
        print("ENTRO A metodo")
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.nombre + " linea: " + str(self.linea) + " columna: " + str(self.columna))
        '''concatenar = ""
        for ins in self.instrucciones:
            concatenar += "\-------\t"+ins.ejecutar(tabla, arbol) 
        '''
        return "\ndef " + self.nombre + "():"
'''
    def getC3D(self):
        cadenaC3D = "procedure " + self.id + " begin\n"
        for ins in self.instrucciones:
            cadenaC3D = cadenaC3D + ins.getC3D()
        
        cadenaC3D = cadenaC3D + "end\n"

        return cadenaC3D
'''