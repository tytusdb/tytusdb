from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class CreateFuncion(InstruccionPL):
    def __init__(self, id , parametros, retornos, begin, declare, tipo, linea, strGram, columna):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.parametros = parametros
        self.retornos = retornos
        self.begin = begin
        self.declare = declare

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')