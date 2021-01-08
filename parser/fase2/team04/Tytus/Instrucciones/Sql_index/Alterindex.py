from storageManager.jsonMode import *
from Instrucciones.Tablas.Tablas import Tablas
from Instrucciones.TablaSimbolos.Tipo import Tipo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tabla import Tabla

class AlterIndex(Instruccion):
    def __init__(self,num,tipo,nombre,col,linea,columna,strGram):
        Instruccion.__init__(self,tipo,linea,columna,strGram)
        self.num = num
        self.nombre = nombre
        self.tipo = tipo
        self.col = col
        self.linea = linea 
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if(self.num == 1):  
            db = arbol.getBaseDatos()
            bandera = 0
            lista_index = arbol.getIndex()
            for x in range(0,len(lista_index)):
                for item in lista_index[x]:
                    if item['Base'] == db:
                        if item['Nombre'] == self.nombre:
                            item['Nombre'] = self.col
                            bandera = 1
                            break 
                if(bandera == 1):
                    break                  
            if bandera == 1 :
                print(f"ALTER INDEX : SE ACTUALIZO CORRECTAMENTE")
            else:     
                print(f"ERROR ALTER: El index no existe o es una base de datos equivocada")

        if(self.num == 2):
            db = arbol.getBaseDatos()
            bandera = 0
            lista_index = arbol.getIndex()
            for x in range(0,len(lista_index)):
                for item in lista_index[x]:
                    if item['Base'] == db:
                        if item['Nombre'] == self.nombre:
                            item['Columna'] = [self.col]
                            bandera = 1
                            break       
                if(bandera == 1):
                    break                  
            if bandera == 1 :
                print(f"ALTER INDEX : SE ACTUALIZO CORRECTAMENTE")
            else:     
                print(f"ERROR ALTER: El index no existe o es una base de datos equivocada")
                       
    def getCodigo(self, tabla, arbol):
        if(self.num == 1):  
            db = arbol.getBaseDatos()
            bandera = 0
            lista_index = arbol.getIndex()
            for x in range(0,len(lista_index)):
                for item in lista_index[x]:
                    if item['Base'] == db:
                        if item['Nombre'] == self.nombre:
                            item['Nombre'] = self.col
                            bandera = 1
                            break 
                if(bandera == 1):
                    break                  
            if bandera == 1 :
                print(f"ALTER INDEX : SE ACTUALIZO CORRECTAMENTE")
            else:     
                print(f"ERROR ALTER: El index no existe o es una base de datos equivocada")

        if(self.num == 2):
            db = arbol.getBaseDatos()
            bandera = 0
            lista_index = arbol.getIndex()
            for x in range(0,len(lista_index)):
                for item in lista_index[x]:
                    if item['Base'] == db:
                        if item['Nombre'] == self.nombre:
                            item['Columna'] = [self.col]
                            bandera = 1
                            break 
                if(bandera == 1):
                    break                  
            if bandera == 1 :
                print(f"ALTER INDEX : SE ACTUALIZO CORRECTAMENTE")
            else:     
                print(f"ERROR ALTER: El index no existe o es una base de datos equivocada") 
            return ""    