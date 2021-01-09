from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Identificador import Identificador

class Where(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if not arbol.getUpdate():
            arbol.setWhere(True)
            val = self.valor.ejecutar(tabla,arbol)
            arbol.setWhere(False)
            return val
            
        val = self.valor.ejecutar(tabla,arbol)
        print("hola me ejecuto en el where porque ahora soy un update")
        return val
        
    def analizar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol):
        cadena ="WHERE "
        if isinstance(self.valor.opDer, Identificador):
            tempIdentificador = self.valor.opDer.traducir(tabla, arbol)
            cadena += self.valor.opIzq.concatenar(tabla,arbol)
            cadena += self.valor.operador
            cadena += "{str("+tempIdentificador.temporalAnterior+")}"
        else:
            cadena += self.valor.concatenar(tabla,arbol)
        return cadena

'''
instruccion = Where("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''