
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
import sys
sys.path.append('../Grupo1/Instrucciones')

class pl_Procedimiento(Instruccion):

    def __init__(self, arg0,arg1,nombre,cuerpop):
        self.arg0 = arg0
        self.arg1 = arg1        
        self.nombre = nombre
        self.cuerpop= cuerpop
        
    def execute(self, data):
        data.tablaSimbolos['ProcsTS'] = {'nombre' : self.nombre, 'cuerpo':self.cuerpop}
        return 'tabla de simbolos de procedimientos procesada.'

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
        return 'se ejecuto el procedimiento: '+str(self.nombre)
    
    def __repr__(self):
        return str(self.__dict__)	
		
