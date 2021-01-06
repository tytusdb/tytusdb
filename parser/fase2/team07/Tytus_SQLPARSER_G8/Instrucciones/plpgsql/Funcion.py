from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Funcion(Instruccion):
    def __init__(self, id, parametros, tipo, declaraciones, instrucciones, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna, strGram, strSent)
        self.id = id
        self.parametros = parametros
        self.tipo = tipo
        self.declaraciones = declaraciones
        self.instrucciones = instrucciones

    def ejecutar(self, tabla, arbol):
        tabla.setFuncion(self)

    def traducir(self,tabla,arbol,cadenaTraducida):
        codigo = ""

        #Se declara la funcion con el nombre
        codigo += "\tdef " + self.id + "(self,"

        #Se añaden los parametros si es que estos existen
        if self.parametros is not None:
            contadorParametros = 0
            for par in self.parametros[:-1]:
                if par == "$":
                    codigo += "S" + str(contadorParametros) + ","
                else:
                    codigo += par + ","
                contadorParametros = contadorParametros + 1
            
            if self.parametros[-1] == "$":
                codigo += "S" + str(contadorParametros)
            else:
                codigo += self.parametros[-1]


        codigo += "):\n\n"

        #Se agregan las declaraciones
        for dec in self.declaraciones:
            codigo += dec.traducir(tabla,arbol,cadenaTraducida) + "\n"

        #Se agrega todo el contenido traducido a 3D
        for ins in self.instrucciones:
            codigo += ins.traducir(tabla,arbol,cadenaTraducida) + "\n"

        return codigo