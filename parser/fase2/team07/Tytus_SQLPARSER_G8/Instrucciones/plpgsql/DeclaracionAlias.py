from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class DeclaracionAlias(Instruccion):
    def __init__(self, id, var_origen, num_origen, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna, strGram, strSent)
        self.id = id
        self.var_origen = var_origen
        self.num_origen = num_origen

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self,tabla,arbol,cadenaTraducida):
        codigo = ""
        
        if self.var_origen is not None:
            codigo += "\t" + self.id + " = " + self.var_origen + "\n"
        elif self.num_origen is not None:
            codigo += "\t" + self.id + " = " + "S" + str(self.num_origen) + "\n"

        return codigo