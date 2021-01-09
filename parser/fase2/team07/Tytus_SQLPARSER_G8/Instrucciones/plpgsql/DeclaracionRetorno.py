from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class DeclaracionRetorno(Instruccion):
    def __init__(self, exprecion, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna, strGram, strSent)
        self.exprecion = exprecion

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self,tabla,arbol,cadenaTraducida):
        codigo = ""

        if self.exprecion is None:
            codigo += "\treturn\n"
        else:
            simbolo = self.exprecion.traducir(tabla,arbol,cadenaTraducida)
            codigo += simbolo.codigo
            codigo += "\treturn " + simbolo.temporal + "\n"

        return codigo