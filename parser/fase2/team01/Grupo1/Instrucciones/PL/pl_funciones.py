import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Utils')
sys.path.append('../Grupo1/Librerias/storageManager')

from instruccion import *
from Lista import *
from TablaSimbolos import *
from Primitivo import *
from Error import *
from jsonMode import *
from c3dGen import *
import sys
sys.path.append('../Grupo1/Instrucciones')

funciones=list()
class pl_Funcion(Instruccion):

    def __init__(self,arg0,arg1,arg2,arg3, nombre,parametros, tipo, cuerpof):
        self.nombre = nombre
        self.parametros =parametros
        self.tipo = tipo
        self.arg0 = arg0
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3  
        self.cuerpof = cuerpof                      
        
    def execute(self, data):
        cad=""
        def ExisteFunc(key, dicObj):
            if key in dicObj:
                cad = "La funcion: "+str(self.nombre)+" Ya Existe!!"
                return  cad
            else:
                print("self")
                createFunctionC3D(data.databaseSeleccionada,self.nombre,self.arg0,self.parametros,self.arg2,self.arg3, self.cuerpof)
                funciones.append(self.nombre)
                data.tablaSimbolos[self.nombre] = {'nombre' : self.nombre, 'parametros' : self.parametros, 'tipo':self.tipo,'cuerpo':self.cuerpof} 
                cad= "Se creo la funcion: "+str(self.nombre)
                return cad
                
        a=ExisteFunc(self.nombre,data.tablaSimbolos)   
        return a        


    def __repr__(self):
        return str(self.__dict__)
		
class pl_CuerpoFuncion(Instruccion):
    def __init__(self, arg0,arg1,declare,instrucciones):
        self.arg0 = arg0
        self.arg1 = arg1        
        self.declare = declare
        self.instrucciones =instrucciones

    def __repr__(self):
        return str(self.__dict__)	
class pl_CuerpoFuncion2(Instruccion):
    def __init__(self, declaraciones,instrucciones):
        self.declaraciones = declaraciones
        self.instrucciones =instrucciones

    def __repr__(self):
        return str(self.__dict__)
		
class pl_Declarar3(Instruccion):
    def __init__(self, arg0,arg1,nombre1, tipo,nombre2):
        self.arg0 = arg0
        self.arg1 = arg1        
        self.nombre1 = nombre1
        self.tipo =tipo
        self.nombre2 =nombre2

    def __repr__(self):
        return str(self.__dict__)	
		
		
class pl_callFuncion(Instruccion):
    def __init__(self,arg0, arg1, tipo,nombre,argumentos):
        self.tipo =tipo
        self.nombre = nombre
        self.argumentos = argumentos
        self.arg0 = arg0
        self.arg1 = arg1

    def execute(self, data):
        self.argumentos
        select_functionC3D(self.nombre,self.argumentos)
        
        return 'se ejecuto la funcion: '+str(self.nombre)

    def __repr__(self):
        return str(self.__dict__)		
		
		
class pl_dropFuncion(Instruccion):

    def __init__(self, arg0, arg1,nombre,parametros):
        self.nombre = nombre
        self.parametros =parametros
        self.arg0 = arg0
        self.arg1 = arg1
        
    def execute(self, data):        
        cad=""
        def ExisteFunc(key, dicObj):
            if key in dicObj:
                for i in funciones:
                    funciones.remove(str(key))
                    
                del data.tablaSimbolos[key]
                cad = "Se elimino la funcion: "+str(self.nombre)
                return  cad
            else:
                cad= "Not existe la funcion: "+str(self.nombre)
                return cad
                
        a=ExisteFunc(self.nombre,data.tablaSimbolos)   
        return a
 
     
    def __repr__(self):
        return str(self.__dict__)		
		