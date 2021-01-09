from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Columna(Instruccion):
    def __init__(self, id, tipo, strGram ,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.tipo = tipo

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

    def analizar(self, tabla, arbol):
        pass
        #super().ejecutar(tabla,arbol)

    def traducir(self, tabla, arbol):
        cadena = ""
        if self.tipo == 'DROP':
            cadena += " drop column "
        cadena += self.id
        return cadena
    
    def getTipo(self):
        print("holis")
        return self.tipo.tipo
        