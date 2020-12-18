
from reporteErrores.errorReport import ErrorReport
class Arbol:
    def __init__(self  , instrucciones):
        self.instrucciones = instrucciones
    
    def ejecutar(self):
        #es el primer ejecutar que se llama
        ts = [] #por el momento , pero deberia de ser otro tipo de tabla de simbolos
        for instruccion in self.instrucciones:
            nodoSintetizado = instruccion.ejecutar(ts)
            if isinstance(nodoSintetizado , ErrorReport):
                print(nodoSintetizado.description)
            else:
                print("instruccion OK")
    def dibujar(self):# no se como se inicia a graficar :v 
        pass