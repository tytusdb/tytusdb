from InstruccionesPL.TablaSimbolosPL import InstruccionPL, ArbolPL
from InstruccionesPL import IdentificadorPL, OutIdentificador,  InOutIdentificador
from InstruccionesPL.Expresiones import Parametro

class CreatePL(InstruccionPL.InstruccionPL):
    def __init__(self, id, parametros, retornos, declare, begin, tipo, linea, columna, strGram):
        #InstruccionPL.__init__(tipo, linea, columna, strGram)        
        self.id = id
        self.parametros = parametros
        self.retornos = retornos
        self.begin = begin
        self.declare = declare

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol) 
        ret = ''
        
        arbol.declararDiccionario(self.id)
        arbol.setDefEtiqueta(self.id)

        if self.parametros != None:
            for par in self.parametros:
                par.traducir(tabla, arbol)
                
        ret += 'def {0}():\n'.format(self.id)
        arbol.add3D(['def {0}():\n'.format(self.id)])
        arbol.agregarGeneral(0,'Metodo', self.id, '')
        if self.retornos !=None:
            for rets in self.retornos:
                rets.traducir(tabla, arbol)
                #Definir el modelo de return variable a regresar aqui se obtiene el tipo de variable pero no se define su ID
        if self.declare != None:
            for declas in self.declare:
                declas.traducir(tabla, arbol)
                
        if self.begin != None:
            for begs in self.begin:
                if type(begs) == list:
                    for beg in begs:
                        beg.traducir(tabla, arbol)
                else:
                    begs.traducir(tabla, arbol)    
