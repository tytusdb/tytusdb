from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class ClaseOperador(InstruccionPL):
    def __init__(self, id , indice1,indice2,indice3,valor,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.indice1 = indice1
        self.indice2 = indice2
        self.indice3 = indice3 
        self.valor = valor
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')