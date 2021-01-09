from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class RecursorPL(InstruccionPL):
    def __init__(self,id, cadena , tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.cadena = cadena

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        res= ' '
        
        if self.Valores != None:
            ret =self.Valores.traducir(tabla, arbol)

            res += '{0} = {1} \n'.format(self.id, ret)
            arbol.add3D([self.id, ret])
            arbol.agregarTripleta(0,'=',self.id, ret)
            arbol.agregarGeneral(0,'=', self.id,ret)
        else:
            res = self.id
            arbol.add3D([self.id, ''])
            arbol.agregarTripleta(0,'=',self.id, '')
            arbol.agregarGeneral(0,'=',self.id, '')

        return res