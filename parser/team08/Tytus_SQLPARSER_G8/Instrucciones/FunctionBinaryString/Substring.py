from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Substring(Instruccion):
    def __init__(self, valor, inicio, fin, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("SUBSTRING")
        print(self.valor[self.inicio:self.fin])
        return self.valor[self.inicio:self.fin]

instruccion = Substring("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)