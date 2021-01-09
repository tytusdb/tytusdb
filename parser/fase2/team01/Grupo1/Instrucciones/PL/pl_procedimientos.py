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
procedimientos=list()
class pl_Procedimiento(Instruccion):

    def __init__(self, arg0,arg1,nombre,parametros,cuerpop):
        self.arg0 = arg0
        self.arg1 = arg1        
        self.nombre = nombre
        self.parametros = parametros
        self.cuerpop= cuerpop
        
    def execute(self, data):
        cad=""
        def ExisteProcedure(key, dicObj):
            if key in dicObj:
                cad = "El procedimiento: "+str(self.nombre)+" Ya Existe!!"
                return  cad
            else:
                parametros = []
                procedimientos.append(self.nombre)
                createProcedureC3D(data.databaseSeleccionada,self.nombre, self.parametros, self.cuerpop)				
                data.tablaSimbolos[self.nombre] = {'nombre' : self.nombre, 'parametros' : self.parametros,'cuerpo':self.cuerpop} 
                cad= "Se creo el procedimiento: "+str(self.nombre)
                return cad
                
        a=ExisteProcedure(self.nombre,data.tablaSimbolos)   
        return a        


    def __repr__(self):
        return str(self.__dict__)
		
class pl_CuerpoProcedimiento(Instruccion):
    def __init__(self,arg0,arg1,instrucciones):
        self.instrucciones =instrucciones
        self.arg0 = arg0
        self.arg1 = arg1        

    def __repr__(self):
        return str(self.__dict__)	
		
class pl_EjecutarProcedimiento(Instruccion):
    def __init__(self,arg0,arg1, nombre,argumentos):
        self.nombre = nombre
        self.argumentos =argumentos
        self.arg0 =arg0
        self.arg1 =arg1

    def execute(self, data):
        select_procedureC3D(self.nombre,self.argumentos)
        return 'se ejecuto el procedimiento: '+str(self.nombre)
    
    def __repr__(self):
        return str(self.__dict__)	
		