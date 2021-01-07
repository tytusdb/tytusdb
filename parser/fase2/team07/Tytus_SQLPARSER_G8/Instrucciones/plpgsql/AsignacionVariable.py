from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class AsignacionVariable(Instruccion):
    def __init__(self, id, exprecion, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna, strGram, strSent)
        self.id = id
        self.exprecion = exprecion

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self,tabla,arbol,cadenaTraducida):
        codigo = ""

        simbolo = self.exprecion.traducir(tabla,arbol,cadenaTraducida)
        codigo += simbolo.codigo
        codigo += "\t" + self.id + " = " + simbolo.temporal + "\n"
        
        return codigo