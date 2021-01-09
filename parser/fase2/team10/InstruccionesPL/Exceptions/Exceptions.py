from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class Exceptions(InstruccionPL):
    def __init__(self, contExpcept, tipo,  linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.contExpcept = contExpcept

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)


    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        #exception when operacion_logica then 
	      #raise exception CADENACARACTER, ID;
        res = ''


        if self.contExpcept != None:
            for excpts in self.contExpcept:
                if type(excpts) == list:
                    for excpt in excpts:
                        excpt.traducir(tabla, arbol)
                else:
                    excpts.traducir(tabla, arbol) 


'''
if operacion_logica goto Ln

Ln:
    t0: Cadenacaracter
    t1: id
'''
