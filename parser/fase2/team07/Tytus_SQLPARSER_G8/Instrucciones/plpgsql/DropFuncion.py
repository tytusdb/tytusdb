from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class DropFuncion(Instruccion):
    def __init__(self, id, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna, strGram, strSent)
        self.id = id
        

    def ejecutar(self, tabla, arbol):
        tabla.dropFuncion(self, arbol)

    def traducir(self,tabla,arbol,cadenaTraducida):
        tabla.dropFuncion(self, arbol)
        codigo = ""

        #Se declara la eliminacion con el nombre
        codigo += "\tdel " + self.id + "\n"

        return codigo