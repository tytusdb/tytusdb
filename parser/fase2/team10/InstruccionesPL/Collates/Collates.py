from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class Collates(InstruccionPL):
    def __init__(self, id,Tipo,id2, Valores, tipo,  linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.Tipo= Tipo
        self.id2 = id2
        self.Valores = Valores


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)


    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        ret= ' '
        
        if self.Valores != None:
            ret =self.Valores.traducir(tabla, arbol)

        res = '{0} = {1} \n'.format(self.id, ret)
        arbol.add3D([self.id, ret])
        arbol.agregarTripleta(0,'=',self.id, ret)
        arbol.agregarGeneral(0,'=',self.id,ret)
        return res
