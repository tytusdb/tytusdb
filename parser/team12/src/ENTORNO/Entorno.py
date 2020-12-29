from Simbolo import *
from Tipo import *
# ****************************** CLASE ENTORNO ******************************
class Entorno():

    def __init__(self, previus):
        self.previus = previus
        self.Global = None
        self.tablaSimbolos = {}

    def ingresar_simbolo(self, id, simbolo):        
        if id in self.tablaSimbolos.keys():
            print("Id existente")
        else:
            print("id no existente")
            self.tablaSimbolos[id] = simbolo

    def obtener_simbolo(self):
        return ""

# ***************************************************************************


# entornoLocal = Entorno(None)
# data = Data_Type.numeric
# tipo = Type(data,1)
# sim =  Symbol('nombre1','smalling',tipo,5)

# entornoLocal.ingresar_simbolo('nombre1',sim)
# entornoLocal.ingresar_simbolo('nombre1',sim)