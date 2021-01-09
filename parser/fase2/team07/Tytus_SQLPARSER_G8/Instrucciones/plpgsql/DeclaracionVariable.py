from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class DeclaracionVariable(Instruccion):
    def __init__(self, id, constante, tipo, isnull, asignacion_valor, strGram, linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.id = id
        self.constante = constante
        self.tipo = tipo
        self.isnull = isnull
        self.asignacion_valor = asignacion_valor

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self,tabla,arbol,cadenaTraducida):
        codigo = ""

        #Tiene un valor asignado
        if self.asignacion_valor is not None:
            simbolo = self.asignacion_valor.traducir(tabla,arbol,cadenaTraducida)
            codigo += simbolo.codigo
            codigo += "\t" + self.id + " = " + simbolo.temporal + "\n"
        
        #Al no asignarsele nada se inicializa como None
        else:
            codigo += "\t" + self.id + " = None\n"

        return codigo