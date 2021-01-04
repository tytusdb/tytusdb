from Instrucciones.TablaSimbolos.Instruccion import *

class indexFunction(Instruccion):
    def __init__(self,strGram):
        #instanciamos los parametros a utilizar 
        Instruccion.__init__(self,None,None,None,strGram)

    def ejecutar(self,tabla,arbol):
        #agregamos los datos a la lista de reportes
        super().ejecutar(tabla,arbol)

    def generar3D(self,tabla,arbol):
        super().generar3D(tabla,arbol)
        return []