from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class OrderBy(Instruccion):
    def __init__(self, valor, tipo, strGram,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.tabla = ""


    def setTabla(self, nombre):
        self.tabla = nombre

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        val=""
        for x in range(0,len(self.valor)):
            col = self.valor[x].id
            val = arbol.devolverOrdenDeColumna(self.tabla,col)
            #val = self.valor[x].ejecutar(tabla,arbol)
        print("ORDER BY")
        arbol.setOrder(self.tipo)
        return val

    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        return super().traducir(tabla, arbol)