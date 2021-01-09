from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.Ends import Ends
from InstruccionesPL.TablaSimbolosPL.ArbolPL import Cuadruplo

class IfsElseIf(InstruccionPL):
    def __init__(self,OperacionLogica,InstrucionesPL, ElseInstrucciones,  tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.OperacionLogica = OperacionLogica
        self.InstruccionesPL = InstrucionesPL
        self.ElseInstrucciones = ElseInstrucciones
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        res = ''
        indTemp1 = arbol.getLast()
        heapResultado  = self.OperacionLogica.traducir(tabla, arbol)
        etiResultado1 =  arbol.generarEtiqueta()
        indTemp2 = arbol.getLast()
        
        res = 'if {0} : goto .{1} \n'.format(heapResultado, etiResultado1)# if tn : goto Ln
        arbol.add3D([res])
        arbol.agregarGeneral(0,'if',heapResultado,etiResultado1)
        cuad = Cuadruplo('if', heapResultado, 'goto',  etiResultado1)
        arbol.agregarCuadruplo(cuad)

        if indTemp1 == indTemp2:
            #Es un ID o un num
            arbol.agregarTripleta(0, 'if', heapResultado, indTemp1+3)
        else:
            indiceTemp = arbol.getLast()
            arbol.agregarTripleta(0, 'if', indiceTemp, indiceTemp+3) #obtener el Indice donde se debe de guarda el label de etiresultado1
        #Procesar otras Operaciones
        etiResultado2 =  arbol.generarEtiqueta()

        res = 'goto .{0}\n'.format(etiResultado2) # goto Ln+1--------> if tn: goto Ln \n goto Ln+1
        arbol.agregarGeneral(0, 'label', etiResultado2, '')
        arbol.agregarTripleta(0, 'label', etiResultado2,'' )
        arbol.add3D([res])
        new_if = arbol.generarIF()
        cuad = Cuadruplo('goto', etiResultado2, '',  '')
        arbol.agregarDicEtiqueta(cuad, new_if)

        res = 'label .{0}'.format(etiResultado1)
        arbol.add3D([res])
        arbol.agregarGeneral(0,'label',etiResultado1,'')
        cuad = Cuadruplo('.', etiResultado1, '',  'label')
        #arbol.agregarCuadruplo(cuad)

        varexp = self.InstruccionesPL
        if type(self.InstruccionesPL) == list:
            for ins in self.InstruccionesPL:
                res += ins.traducir(tabla, arbol)
        else:
            res += ins.traducir(tabla, arbol)

        res = 'label .{0}'.format(etiResultado2)
        arbol.add3D([res])
        arbol.agregarGeneral(0,'label',etiResultado2,'')
        cuad = Cuadruplo('.', etiResultado1, '',  'label')

        arbol.agregarCuadruplo(cuad)
        temp2 = arbol.getLast()+1
        arbol.modificarTripleta(0,'label',etiResultado2,'',temp2)

        if isinstance(self.ElseInstrucciones, Ends.Ends)==False:
            res = self.ElseInstrucciones.traducir(tabla,arbol) 

       
       
        return res