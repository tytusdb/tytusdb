from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.TablaSimbolosPL.ArbolPL import Cuadruplo

class AsignacionDefault(InstruccionPL):
    def __init__(self, id,Tipo, Valores, tipo,  linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.Tipo= Tipo
        self.Valores = Valores


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)


    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        ret= ' '
        res= ' '
        
        if self.Valores != None:
            ret =self.Valores.traducir(tabla, arbol)

            res += '{0} = {1} \n'.format(self.id, ret)
            cuad = Cuadruplo('=', ret, '',  self.id)
            arbol.agregarCuadruplo(cuad)
        else:
            res = '{0} = ' ' \n'.format(self.id)

        arbol.add3D([res])
        arbol.agregarTripleta(0,'=',self.id, ret)
        arbol.agregarGeneral(0,'=',self.id, ret)

        cuad = Cuadruplo('=', '', '',  self.id)
        arbol.agregarCuadruplo(cuad)

        return res