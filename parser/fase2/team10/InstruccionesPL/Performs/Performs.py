from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL


class Performs(InstruccionPL):
    def __init__(self, id,ListId, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.ListId = ListId
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')
        super().traducir(tabla, arbol)

        #Perform id (listid);
        res = ''
        heapResultado  = self.id
        etiResultado1 =  arbol.generarEtiqueta() #Tendria que ser la etiqueta que contenga a la funcion de la cual hace referencia el Perform

        parametros = ''
        if self.ListId != None:
            for par in self.ListId:
                parametros += par.traducir(tabla, arbol)

        res = 'Perform {0} ({1}) : goto .{2} \n'.format(heapResultado, parametros, etiResultado1)# perform id(parametros) Goto Ln
        arbol.add3D([res])
        arbol.agregarGeneral(0,'perform',heapResultado, etiResultado1)
        #indiceTemp = arbol.getLast()
        #arbol.agregarTripleta(0, 'perform', indiceTemp, indiceTemp+3) #obtener el Indice donde se debe de guarda el label de etiresultado1


        