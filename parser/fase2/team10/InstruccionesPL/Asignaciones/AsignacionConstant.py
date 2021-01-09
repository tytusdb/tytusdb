from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class AsignacionesConstant(InstruccionPL):
    def __init__(self, id,Tipo, tipo,  linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.Tipo= Tipo


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)

        if self.Tipo.getTipo()<9:
            res = '{0} = {1} \n'.format(self.id, '0')
            arbol.add3D([res])
            arbol.agregarTripleta(0, '=', self.id, '0')
            arbol.agregarGeneral('=', '0', '', self.id)
            
        elif self.Tipo.getTipo()>8 and self.tipo.getTipo()<14:
            res = '{0} = {1} \n'.format(self.id, '""')
            arbol.add3D([res])
            arbol.agregarTripleta(0,'=',self.id,' ')
            arbol.agregarGeneral('=','0','',self.id)

        elif self.Tipo.getTipo() == 18:
            res = '{0} = {1} \n'.format(self.id, 'False')
            arbol.add3D([res])
            arbol.agregarTripleta(0, '=', self.id, 'False')
            arbol.agregarGeneral('=', '0', self.id, 'False')

        elif self.Tipo.getTipo() == 19:
            res = '{0} = {1} \n'.format(self.id, '0')
            arbol.add3D([res])
            arbol.agregarTripleta(0, '=', self, id, '0')
            arbol.agregarGeneral(0, '=', self, id, '0')

        return res