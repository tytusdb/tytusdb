from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL


class Ends(InstruccionPL):
    def __init__(self,  tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        

        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        print(';')