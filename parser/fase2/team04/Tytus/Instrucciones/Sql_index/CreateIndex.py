from storageManager.jsonMode import *
from Instrucciones.Tablas.Tablas import Tablas
from Instrucciones.TablaSimbolos.Tipo import Tipo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tabla import Tabla

class CreateIndex(Instruccion):
    def __init__(self,num,nombre,tipo,col,orden,linea,columna):
        Instruccion.__init__(self,tipo,nombre,linea,columna)
        self.num = num
        self.nombre = nombre
        self.tipo = tipo
        self.col = col
        self.orden = orden
        self.linea = linea 
        self.columna = columna

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if(self.num == 1):
           # arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: "+ str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
                if(orden != 'asc'):
                   arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
                   break       

        if(self.num == 2):
            #arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: "+ str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
                if(orden != 'asc'):        
                    arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
                    break     
        if(self.num == 3):
            arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: " + str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
                arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
                break     
        if(self.num == 4):
           # arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: " + str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
                arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
                break     
        if(self.num == 5):            
            #arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: " + str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
                        
            arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
               
        
    def getCodigo(self, tabla, arbol):
        if(self.num == 1):
            #arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: "+ str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
                if(orden != 'asc'):
                   arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
                   break       

        if(self.num == 2):
            #arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: "+ str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
                if(orden != 'asc'):        
                    arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
                    break     
        if(self.num == 3):
            #arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: " + str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
                arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
                break     
        if(self.num == 4):
            #arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: " + str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
                arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
                break     
        if(self.num == 5):            
            #arbol.consola.append("SE EJECUTO CREATE INDEX TIPO: " + str(self.tipo))
            orden = "desc"
            for item in self.orden: 
                for i in item:
                       if i.lower() == 'asc':
                           orden = 'asc'
                           arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea])
                           break
            arbol.setIndex([self.nombre,self.tipo,self.col,orden,item,self.linea]) 
               
        
        
          
        