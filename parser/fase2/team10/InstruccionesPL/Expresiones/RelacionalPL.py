from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.TablaSimbolosPL.TipoPL import TipoPL, Tipo_DatoPL
from InstruccionesPL.TablaSimbolosPL.ArbolPL import Cuadruplo
class RelacionalPL(InstruccionPL):
    def __init__(self, opIzq, opDer, operador, strGram, linea, columna):
        InstruccionPL.__init__(self,None,linea,columna,strGram)
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        indTemp = arbol.getLast() #sabiendo el numero de elementos dentro de la lista
        hop1 = self.opIzq.traducir(tabla, arbol)# ---> Id, numero, .... Terminal  --->si se creo etiquita 
        indTemp2 = arbol.getLast() # si ese numero cambio quiere decir que se genero una etiqueta o una tripleta
        indTri=False
        if indTemp != indTemp2:
            indTri =True #OperadorIzq es una etiqueta
        
        hop2 = self.opDer.traducir(tabla, arbol)
        indTemp3 =arbol.getLast() 
        indTri2=False
        if indTemp2!=indTemp3:
            indTri2 = True

        h1 = arbol.generarHeap()
        ret2 = '{0} = {1} {2} {3}'.format(h1, hop1, self.operador, hop2)
        arbol.add3D([ret2])
        arbol.agregarGeneral(0,self.operador,hop1,hop2)
        cuad = Cuadruplo(self.operador, hop1, hop2, h1)
        arbol.agregarCuadruplo(cuad)
        if indTri2 and indTri:
            arbol.agregarTripleta(0,self.operador,indTemp2,indTemp3)
        elif indTri:
            arbol.agregarTripleta(0,self.operador, indTemp2, hop2)
        elif indTri2:
            arbol.agregarTripleta(0,self.operador,hop1, indTemp3)
        else:
            arbol.agregarTripleta(0,self.operador,hop1, hop2)
        return h1