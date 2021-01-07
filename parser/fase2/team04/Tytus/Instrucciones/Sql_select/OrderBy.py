from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class OrderBy(Instruccion):
    def __init__(self, valor, tipo, strGram,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.tabla = ""
        self.tipo = tipo
        self.orde = ""

    def setTabla(self, nombre):
        self.tabla = nombre
      
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        self.orde = self.tipo
        for x in range(0,len(self.valor)):
            col = self.valor[x].id
            val = arbol.devolverOrdenDeColumna(self.tabla,col)
            #val = self.valor[x].ejecutar(tabla,arbol)
        #print("ORDER BY")
        arbol.setOrder(self.tipo)
        return val
        
    def getCodigo(self,arbol,tabla):
         return self.tipo
    
    def toString(self):
        items =""
        for  item in  self.valor: 
             items += item.toString() 
        return items,self.tipo
  
              
        
'''
instruccion = OrderBy("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''