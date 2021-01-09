from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.TablaSimbolosPL.TipoPL import TipoPL, Tipo_DatoPL
from InstruccionesPL.TablaSimbolosPL.ArbolPL import Cuadruplo

class Parametro(InstruccionPL):
    def __init__(self, id, tipo, strGram, linea, columna):
        InstruccionPL.__init__(self,tipo,linea,columna, strGram)
        self.id = id
        self.tipo = tipo

    def ejecutar(self):
        print('ejecutar')

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        vars  = self.tipo.getTipo().value
        #print(vars.value)

        if vars<9:
            res = '{0} = {1} \n'.format(self.id, '0')
            arbol.agregarTripleta(0,'=',self.id,'0')
            arbol.agregarGeneral(0,'asig',self.id,'0')
            arbol.add3D([res])
            cuad = Cuadruplo('=', '0', '', self.id)
            arbol.agregarCuadruplo(cuad)
            
        elif vars>8 and vars<14:
            res = '{0} = {1} \n'.format(self.id, '""')
            arbol.agregarTripleta(0, '=', self.id, '""')
            arbol.agregarGeneral(0, 'asig', self.id, '0')
            arbol.add3D([res])
            cuad = Cuadruplo('=', '0', '""', self.id)
            arbol.agregarCuadruplo(cuad)

        elif vars==18:
            res = '{0} = {1} \n'.format(self.id, 'False')
            arbol.agregarTripleta(0,'=',self.id,'False')
            arbol.agregarGeneral(0,'asig',self.id,'False')
            arbol.add3D([res])
            cuad = Cuadruplo('=', '0', 'False', self.id)
            arbol.agregarCuadruplo(cuad)

        elif vars == 19:
            res = '{0} = {1} \n'.format(self.id, '0')
            arbol.agregarTripleta(0,'=',self.id,'0')
            arbol.agregarGeneral(0,'asig',self.id,'0')
            arbol.add3D([res])
            cuad = Cuadruplo('=', '0', '0', self.id)
            arbol.agregarCuadruplo(cuad)
        else:
            arbol.agregarTripleta(0,'=',self.id,' ')
            arbol.agregarGeneral(0,'asig',self.id,' ')
            res =  '{0} = {1} \n'.format(self.id, ' ')
            arbol.add3D([res])
            cuad = Cuadruplo('=', '0', ' ', self.id)
            arbol.agregarCuadruplo(cuad)

        return res

        #Guardar en Tabla de Simbolos
        #return res