
from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL


class Execute(InstruccionPL):
    def __init__(self, cadena, into,strict,id, listId,tipo,linea, columna, strGram):
        InstruccionPL.__init__(self, tipo,linea, columna,strGram)
        self.cadena =cadena
        self.into = into
        self.strict  = strict
        self.id  = id
        self.listId = listId


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super.traducir(tabla, arbol)
        res = ''

        if self.listId != None: #Tiene parametros
            for par in self.listId:
                par.traducir(tabla, arbol) #Crea las etiquetas para los parametros y los guarda
            
            res = '{0} () \n'.format(self.cadena) 

        else: #Ejecuta el procedure sin parametros
            res = '{0} () \n'.format(self.id) 
        # Create Procedure ID.... ---> def 
        # Execute ID(); -----> goto Ln
        arbol.agregarGeneral(0, 'Metodo', self.cadena, '')
        arbol.add3D([res])