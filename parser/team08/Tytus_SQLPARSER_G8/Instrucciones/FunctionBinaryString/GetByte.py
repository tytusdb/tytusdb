from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class GetByte(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bytes(self.valor, 'utf-8')
        return bytes(self.valor,'utf-8')

instruccion = GetByte("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)