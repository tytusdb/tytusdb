from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class CreateOrReplace(InstruccionPL):

    def __init__(self, id, ListId,id2, Declaraciones, ContBegin, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo,linea, columna, strGram)
        self.id =  id 
        self.ListId = ListId
        self.id2 = id2
        self.Declaraciones = Declaraciones
        self.ContBegin = ContBegin
    

    def ejecutar(self,tabla,arbol):
        super().ejecutar(tabla,arbol)
        print('')

    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        ret = ''
        if self.ListId != None:
            for par in self.ListId:
                par.traducir(tabla, arbol)
                
        ret += 'def {0}():\n'.format(self.id)
        arbol.add3D(['def {0}():\n'.format(self.id)])
        arbol.agregarGeneral(0,'Metodo', self.id, '')
        if self.id2 !=None:
            for rets in self.id2:
                rets.traducir(tabla, arbol)
                #Definir el modelo de return variable a regresar aqui se obtiene el tipo de variable pero no se define su ID
        if self.Declaraciones != None:
            for declas in self.Declaraciones:
                declas.traducir(tabla, arbol)
                
        if self.ContBegin != None:
            for begs in self.ContBegin:
                if type(begs) == list:
                    for beg in begs:
                        beg.traducir(tabla, arbol)
                else:
                    begs.traducir(tabla, arbol) 

