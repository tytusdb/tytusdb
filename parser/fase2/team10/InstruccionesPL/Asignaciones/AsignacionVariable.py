from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.TablaSimbolosPL.ArbolPL import Cuadruplo

class AsignacionVariable(InstruccionPL):
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
        
        if self.Valores != None:
            ret =self.Valores.traducir(tabla, arbol)

        res = '{0} = {1} \n'.format(self.id, ret)
        arbol.add3D([res])
        cuad = Cuadruplo('=', self.id, '',  ret)
        arbol.agregarCuadruplo(cuad)

        return res

        