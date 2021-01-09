from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion

class Return(Instruccion):
    def __init__(self, expresion, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.expresion = expresion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        if self.expresion != None:
            resultado = self.expresion.analizar(tabla, arbol)
            if isinstance(resultado, Excepcion):
                return resultado
            self.tipo = resultado
            return self
        
    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        if self.expresion != None:
            arbol.addComen("Se asigna el valor a la posición de return")
            r = tabla.getSimboloVariable("return")
            exp = self.expresion.traducir(tabla, arbol)
            temporal = tabla.getTemporal()
            arbol.addc3d(f"{temporal} = P + {r.posicion}")
            arbol.addc3d(f"Pila[{temporal}] = {exp.temporalAnterior}")
            arbol.addc3d(f"goto .{arbol.etiqueta_fin}")
        return Nodo3D()
            
