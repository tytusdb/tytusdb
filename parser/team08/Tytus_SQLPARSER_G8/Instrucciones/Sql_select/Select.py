from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Select(Instruccion):
    #dist  tipo  lcol  lcol  linners where lrows
    def __init__(self, dist, tipo, lcol, lcol2, linners, where, lrows, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.dist = dist
        self.lcol = lcol
        self.lcol2 = lcol2
        self.linners = linners
        self.where = where
        self.lrows = lrows

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if(self.lcol == "*"):
            #vamos a mostrar todos
            #haremos un for 
            val = ""
            val = self.lcol2.devolverTabla(tabla,arbol)
        else:
            #vamos a mostrar por columna
            print("mostrar por  columna")
            
'''
instruccion = Select("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''