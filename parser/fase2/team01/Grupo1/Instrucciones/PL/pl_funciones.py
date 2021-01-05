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

class pl_Funcion(Instruccion):

    def __init__(self, nombre,parametros, tipo):
        self.nombre = nombre
        self.parametros =parametros
        self.tipo = tipo
        
    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)
		
