from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class Cases(InstruccionPL):
    def __init__(self,OperacionLogica, ContCase,EndCase, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.OperacionLogica = OperacionLogica
        self.ContCase = ContCase
        self.EndCase = EndCase

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol): # case <expresion> when <operacion_logica> then <InstruccionPL> else <InstruccionPL> end case;    
        super().traducir(tabla, arbol)
        res = ''

        if self.OperacionLogica!=None:
            indTemp1 = arbol.getLast()
            heapResultado  = self.OperacionLogica.traducir(tabla, arbol) # operacion_logica de la condicion del case
            indTemp2 = arbol.getLast()

            if indTemp1 == indTemp2:
                arbol.modificarTripletaCase(None,heapResultado,None,None)
            else:
                arbol.modificarTripletaCase(None,heapResultado,indTemp2,None)
        else:
            #arbol.agregarTripleta(None, None, None, None)
            #no se hace nada ya que se cuenta con la tripleta case
            print('flujo case sin modificar la tripleta case')

        if self.ContCase != None:
            for begs in self.ContCase:
                if type(begs) == list:
                    for beg in begs:
                        beg.traducir(tabla, arbol)
                else:
                    begs.traducir(tabla, arbol) 

        arbol.modificarTripletaCase(None,None,None,None)

        """ res = 'case {0} when {1} : goto .{2} \n'.format(heapResultado, heapResultado2, etiResultado1)# case tn when tn: goto Ln
        arbol.add3D([res])
        arbol.agregarGeneral(0,'case',heapResultado2,etiResultado1)
        indiceTemp = arbol.getLast()
        arbol.agregarTripleta(0, 'case', indiceTemp, indiceTemp+3) #obtener el Indice donde se debe de guarda el label de etiresultado1
        #Procesar otras Operaciones
        etiResultado2 =  arbol.generarEtiqueta()

        res = 'goto .{0}\n'.format(etiResultado2) # goto Ln+1--------> case tn when tn: goto Ln \n goto Ln+1
        arbol.agregarGeneral(0, 'label', etiResultado2, '')
        arbol.agregarTripleta(0, 'label', etiResultado2,'' )
        arbol.add3D([res])

        #Etiqueta 1, salto Then ->
        res = 'label .{0}'.format(etiResultado1)
        arbol.add3D([res])
        arbol.agregarGeneral(0,'label',etiResultado1,'')
        #varexp = self.InstruccionesPL #Instrucciones que vienen dentro de la primera etiqueta
        #Traduce todas las instrucciones que vengan despues del then
        if type(self.InstruccionesPL) == list:
            for ins in self.InstruccionesPL:
                res += ins.traducir(tabla, arbol)
        else:
            res += ins.traducir(tabla, arbol)
        
        #Etiqueta de salto Else ->
        res = 'label .{0}'.format(etiResultado2)
        arbol.add3D([res])
        arbol.agregarGeneral(0,'label',etiResultado2,'')
        temp2 = arbol.getLast()+1
        arbol.modificarTripleta(0,'label',etiResultado2,'',temp2) """
        return res
'''
Generacion de Switch: cuenta con diferentes instancias de case ----> cada case cuenta con diferentes instrucciones a ejecutar
case op1 === when 
if op1 === expr:

if op1 == expre2:


'''