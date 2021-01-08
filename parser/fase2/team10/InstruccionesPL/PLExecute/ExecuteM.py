from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL


class ExecuteM(InstruccionPL):
    def __init__(self, id,  listId,tipo,linea, columna, strGram):
        InstruccionPL.__init__(self, tipo,linea, columna,strGram)
        self.id =id
        self.listId = listId


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)

    def traducir(self, tabla, arbol):
        #EXECUTE sp_validainsert(sadfs);
        super.traducir(tabla, arbol)
        res = ''

        if self.listId != None: #Tiene parametros
            for par in self.listId:
                par.traducir(tabla, arbol) #Crea las etiquetas para los parametros y los guarda
            
            res = '{0} () \n'.format(self.id) 

        else: #Ejecuta el procedure sin parametros
            res = '{0} () \n'.format(self.id) 
        # Create Procedure ID.... ---> def 
        # Execute ID(); -----> goto Ln
        arbol.agregarGeneral(0, 'Procedure', self.id, '')
        arbol.add3D([res])
'''
defetiquetaID = arbol.listaCuadruplos[id]

def funcion1(param1 , param2)


def funcion1():
    t1= p
    t2=p2

funcion1(par1, par2)
p= par1
p2=par2
funcion1()
'''