import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\C3D\\')
sys.path.append(c3d_dir)

ent_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\ENTORNO\\')
sys.path.append(ent_dir)

from Nodo import Nodo
from Tipo_Expresion import *
from Entorno import Entorno
from Label import *

class Sentencia_Else(Nodo):

    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
    
    def execute(self, enviroment):
        bloque = self.hijos[0]
        
        # Entorno Local
        entornoLocal = Entorno(enviroment)
        entornoLocal.nombreEntorno = 'else ' + enviroment.nombreEntorno
        entornoLocal.Global = enviroment.Global
        enviroment.entornosLocales.append(entornoLocal)

        return bloque.execute(entornoLocal)

    def compile(self,enviroment):

        bloque = self.hijos[0]

        # Entorno Local
        entornoLocal = Entorno(enviroment)
        entornoLocal.nombreEntorno = 'else ' + enviroment.nombreEntorno
        entornoLocal.Global = enviroment.Global
        enviroment.entornosLocales.append(entornoLocal)
        
        return bloque.compile(enviroment)

    def getText(self):
        pass