
from reporteErrores.errorReport import ErrorReport
from reporteErrores.instance import listaErrores
class Arbol:
    def __init__(self  , instrucciones):
        self.instrucciones = instrucciones
    
    def ejecutar(self):
        #es el primer ejecutar que se llama
        ts = [] #por el momento , pero deberia de ser otro tipo de tabla de simbolos
        for instruccion in self.instrucciones:
            nodoSintetizado = instruccion.ejecutar(ts)
            print(nodoSintetizado.val)
            if isinstance(nodoSintetizado , ErrorReport):
                listaErrores.addError(nodoSintetizado)
                print(nodoSintetizado.description)
            else:
                print("instruccion OK")
    
    def dibujar(self):# no se como se inicia a graficar :v 
        g = "diagraph g {" +'\n'
        identificador = str(hash(self))
        g+=identificador + "[ label = \"Init\"];"
        
        for instruccion in self.instrucciones:
            print(instruccion)
            #g+= identificador + "->" + instruccion.dibujar()

        
        
        g+='\n'+"}"
        print(g)
        