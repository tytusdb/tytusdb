from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.TablaSimbolosPL.ArbolPL import Cuadruplo

class WhenPL(InstruccionPL):
    index = 0
    def __init__(self,ListOp, InstruccionPL12, ContCase, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.ListOP = ListOp
        self.InstruccionPL12 = InstruccionPL12
        self.ContCase = ContCase

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        vars1 = arbol.getTripletaCase()
        #arbol.eliminarTripleta()
        indTemp1 = arbol.getLast()
        if self.ListOP!=None:
            for listopp in self.ListOP:
                heapResultado = listopp.traducir(tabla, arbol)
        indTemp2 = arbol.getLast()

        if vars1.verficar(None,None,None,None): #quiere decir que el case no tiene ID o Expresion 
            if indTemp1 == indTemp2:
                etiResultado1 =  arbol.generarEtiqueta()
                res = 'if {0} : goto {1}'.format(heapResultado, etiResultado1) # tn = opCase == heapResultado
                arbol.add3D([res])
                arbol.agregarTripleta(0,'if',heapResultado,indTemp1+3)
                arbol.agregarGeneral(0,'if',heapResultado,etiResultado1)
                cuad = Cuadruplo('if', heapResultado, 'goto', etiResultado1)
                arbol.agregarCuadruplo(cuad)
            else:
                etiResultado1 =  arbol.generarEtiqueta()
                res='if {} : goto {}'.format(heapResultado,etiResultado1)
                arbol.agregarTripleta(0, 'if', indTemp2, indTemp2+3) #obtener el Indice donde se debe de guarda el label de etiresultado1
                cuad = Cuadruplo('if', heapResultado, 'goto', etiResultado1)
                arbol.agregarCuadruplo(cuad)
        
        else:   #quiere decir que el case cuenta con una condicion debemos generar una nueva etiqueta si no es un ID o un num. 
            if indTemp1 == indTemp2: #when es un terminal
                if vars1.getOp1() == None: #case es un terminal
                    etiResultado1 =  arbol.generarEtiqueta()
                    heapResultado2= arbol.generarHeap()#tn....
                    res= '{0}={1}=={2}'.format(heapResultado2, vars1.getOper(), heapResultado)#t1 = id==id2
                    arbol.add3D([res])
                    arbol.agregarTripleta(0,'==', vars1.getOper(), heapResultado)
                    arbol.agregarGeneral(0,'==', vars1.getOper(), heapResultado)#ingresamos operacion de igualacion
                    cuad = Cuadruplo('==', vars1.getOper(), heapResultado, heapResultado2)
                    arbol.agregarCuadruplo(cuad)
                    
                    res = 'if {0} : goto {1}'.format(heapResultado2, etiResultado1) # tn = opCase == heapResultado
                    arbol.add3D([res])
                    arbol.agregarTripleta(0,'if',heapResultado,indTemp1+4)
                    arbol.agregarGeneral(0,'if',heapResultado,etiResultado1)

                    cuad = Cuadruplo('if', heapResultado2, 'goto', etiResultado1)
                    arbol.agregarCuadruplo(cuad)
                    
                else: #el case tiene una condicion con etiqueta y el when es un terminal

                    etiResultado1 =  arbol.generarEtiqueta()
                    heapResultado2= arbol.generarHeap()#tn....
                    res= '{0}={1}=={2}'.format(heapResultado2, vars1.getOper(), heapResultado)
                    arbol.add3D([res])
                    arbol.agregarTripleta(0,'==', vars1.getOp1(), heapResultado)
                    arbol.agregarGeneral(0,'==', vars1.getOper(), heapResultado)#ingresamos operacion de igualacion
                    cuad = Cuadruplo('==', vars1.getOper(), heapResultado, heapResultado2)
                    arbol.agregarCuadruplo(cuad)
    
                    res = 'if {0} : goto {1}'.format(heapResultado2, etiResultado1) # tn = opCase == heapResultado
                    arbol.add3D([res])
                    arbol.agregarTripleta(0,'if',arbol.getLast(), indTemp2+4)
                    arbol.agregarGeneral(0,'if',heapResultado,etiResultado1)
                    cuad = Cuadruplo('if', heapResultado2, 'goto', etiResultado1)
                    arbol.agregarCuadruplo(cuad)  
                    
            else: #el case tiene una condicion con etiqueta y el when es una etiqueta
                etiResultado1 =  arbol.generarEtiqueta()
                heapResultado2= arbol.generarHeap()#tn....
                res= '{0}={1}=={2}'.format(heapResultado2, vars1.getOper(), heapResultado)
                arbol.add3D([res])
                arbol.agregarTripleta(0,'==', vars1.getOp1(), arbol.getLast())
                arbol.agregarGeneral(0,'==', vars1.getOper(), heapResultado)#ingresamos operacion de igualacion
                cuad = Cuadruplo('==', vars1.getOper(), heapResultado, heapResultado2)
                arbol.agregarCuadruplo(cuad)
    
                res = 'if {0} : goto {1}'.format(heapResultado2, etiResultado1) # tn = opCase == heapResultado
                arbol.add3D([res])
                arbol.agregarTripleta(0,'if',arbol.getLast(), indTemp2+4)
                arbol.agregarGeneral(0,'if',heapResultado,etiResultado1) 
                cuad = Cuadruplo('if', heapResultado2, 'goto', etiResultado1)
                arbol.agregarCuadruplo(cuad)  

        
        etiResultado2 =  arbol.generarEtiqueta()
        new_end = arbol.generarEND()

        res = 'goto .{0}\n'.format(etiResultado2) # goto Ln+1--------> if tn: goto Ln \n goto Ln+1
        arbol.agregarGeneral(0, 'label', etiResultado2, '')
        arbol.agregarTripleta(0, 'label', etiResultado2,'' )
        arbol.add3D([res])
        cuad = Cuadruplo('goto', etiResultado2, '', '')
        new_if = arbol.generarIF()
        arbol.agregarDicEtiqueta(cuad, new_if)

        res = 'label .{0}'.format(etiResultado1)
        arbol.add3D([res])
        arbol.agregarGeneral(0,'label',etiResultado1,'')
        cuad = Cuadruplo('.', etiResultado1, '', 'label')
        #new_if = arbol.generarIF()
        #arbol.agregarCuadruplo(cuad)
        #varexp = self.InstruccionesPL12
        if type(self.InstruccionPL12) == list:
            for ins in self.InstruccionPL12:
                res += ins.traducir(tabla, arbol)
        else:
            res += ins.traducir(tabla, arbol)

        res = 'label .{0}'.format(etiResultado2)
        arbol.add3D([res])
        arbol.agregarGeneral(0,'label',etiResultado2,'')
        temp2 = arbol.getLast()+1
        arbol.modificarTripleta(0,'label',etiResultado2,'',temp2)
        new_end = arbol.generarEND()
        cuad = Cuadruplo('.', etiResultado1, '', 'label')
        #new_if = arbol.generarIF()
        arbol.agregarCuadruplo(cuad)
        return res

'''
if cond : goto Ln
goto Ln+1
label ln


label Ln+1

'''




            
