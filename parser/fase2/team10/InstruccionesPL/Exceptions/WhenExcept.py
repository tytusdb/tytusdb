from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.TablaSimbolosPL.ArbolPL import Cuadruplo

class WhenExcept(InstruccionPL):
    def __init__(self,OperacionLogica, ResultException, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.OperacionLogica = OperacionLogica
        self.ResultException = ResultException

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        res = ''

        indTemp1 = arbol.getLast()
        heapResultado  = self.OperacionLogica.traducir(tabla, arbol) # operacion_logica de la condicion del case
        indTemp2 = arbol.getLast()

        #Se verifica si en la condicion del when viene un terminal o una etiqueta
        if indTemp1 == indTemp2: # When es terminal
            #arbol.modificarTripletaCase(None,heapResultado,None,None)
            etiResultado1 =  arbol.generarEtiqueta()
            res = 'if {0} : goto {1}'.format(heapResultado, etiResultado1) # tn = opCase == heapResultado
            arbol.add3D([res])
            arbol.agregarTripleta(0,'if',heapResultado,indTemp1+3)
            arbol.agregarGeneral(0,'if',heapResultado,etiResultado1)
            cuad = Cuadruplo('if', heapResultado, 'goto', etiResultado1)
            arbol.agregarCuadruplo(cuad)

        else: # When trae una etiqueta
            #arbol.modificarTripletaCase(None,heapResultado,indTemp2,None)
            etiResultado1 =  arbol.generarEtiqueta()
            res = 'if {0} : goto {1}'.format(heapResultado, etiResultado1) # tn = opCase == heapResultado
            arbol.add3D([res])
            arbol.agregarTripleta(0,'if',arbol.getLast(), indTemp2+4)
            arbol.agregarGeneral(0,'if',heapResultado,etiResultado1) 
            cuad = Cuadruplo('if', heapResultado, 'goto', etiResultado1)
            arbol.agregarCuadruplo(cuad)  
        
        if self.ResultException != None:
            for resultExcs in self.ResultException:
                if type(resultExcs) == list:
                    for resultExc in resultExcs:
                        resultExc.traducir(tabla, arbol)
        else:
            resultExcs.traducir(tabla, arbol) 

        