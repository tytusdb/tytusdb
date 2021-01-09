from storageManager.jsonMode import *
from Instrucciones.Tablas.Tablas import Tablas
from Instrucciones.TablaSimbolos.Tipo import Tipo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tabla import Tabla

class CreateIndex(Instruccion):
    def __init__(self,tipo,nombre,tabla,col,linea,columna,strGram):
        Instruccion.__init__(self,tipo,linea,columna,strGram)
        self.tipo    = tipo
        self.nombre  = nombre
        self.tabla   = tabla
        self.col     = col
       
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        columnas = []
        restrict = []
        colNotExists = []
        orden = None
        bandera = 0
        
        db = arbol.getBaseDatos()
        if db != None:
            existe = arbol.getExists(self.nombre)
            if(existe == 0):
                resultado =  arbol.devolviendoTablaDeBase(self.tabla)
                if(resultado != 0):
                    for item in self.col: 
                        for val in item:
                            if val.lower() == 'nulls': 
                                restrict.append(val)
                            elif val.lower() == 'first':  
                                restrict.append(val)
                            elif val.lower() == 'last':
                                restrict.append(val)
                            elif val.lower() == 'lower':  
                                restrict.append(val)
                            elif val.lower() == 'asc': 
                                orden = val
                            elif val.lower() =='desc':
                                orden = val
                            else:
                                columnas.append(val)
                    
                    for fs in columnas :
                        for tbcol in resultado.lista_de_campos:  
                            if tbcol.nombre == fs:
                                bandera +=1

                    if bandera == len(columnas):             
                        arbol.setIndex([{'Base':db,'Tipo':self.tipo,'Nombre': self.nombre,'Tabla':self.tabla,'Orden':orden, 'Columna':columnas, 'Restrict':restrict}]) 
                        print(f"CREATE INDEX : {self.nombre} SE CREO CORRECTAMENTE")
                    else:
                        print(f"ERROR  INDEX: NOMBRE DE COLUMNAS NO EXISTE")     
                else:
                    print(f"ERROR  INDEX : TABLA '{self.tabla}' NO EXISTE")
            else:
                print(f"ERROR  INDEX : NOMBRE DE INDEX '{self.nombre}' YA EXISTE")
        
        else: 
            print(f"ERROR : BASE DE DATOS NO SELECCIONADA")
        
    def getCodigo(self, tabla, arbol):
        columnas = []
        restrict = []
        colNotExists = []
        orden = None
        bandera = 0
        
        db = arbol.getBaseDatos()
        if db != None:
            existe = arbol.getExists(self.nombre)
            if(existe == 0):
                resultado =  arbol.devolviendoTablaDeBase(self.tabla)
                if(resultado != 0):
                    for item in self.col: 
                        for val in item:
                            if val.lower() == 'nulls': 
                                restrict.append(val)
                            elif val.lower() == 'first':  
                                restrict.append(val)
                            elif val.lower() == 'last':
                                restrict.append(val)
                            elif val.lower() == 'lower':  
                                restrict.append(val)
                            elif val.lower() == 'asc': 
                                orden = val
                            elif val.lower() =='desc':
                                orden = val
                            else:
                                columnas.append(val)
                    
                    for fs in columnas :
                        for tbcol in resultado.lista_de_campos:  
                            if tbcol.nombre == fs:
                                bandera +=1

                    if bandera == len(columnas):             
                        arbol.setIndex([{'Base':db,'Tipo':self.tipo,'Nombre': self.nombre,'Tabla':self.tabla,'Orden':orden, 'Columna':columnas, 'Restrict':restrict}]) 
                        print(f"CREATE INDEX : {self.nombre} SE CREO CORRECTAMENTE")
                    else:
                        print(f"ERROR  INDEX: NOMBRE DE COLUMNAS NO EXISTE")     
                else:
                    print(f"ERROR  INDEX : TABLA '{self.tabla}' NO EXISTE")
            else:
                print(f"ERROR  INDEX : NOMBRE DE INDEX '{self.nombre}' YA EXISTE")
        
        else: 
            print(f"ERROR : BASE DE DATOS NO SELECCIONADA")
        return ""
            

        