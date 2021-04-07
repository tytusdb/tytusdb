from Simbolo import *
from Tipo import *
# ****************************** CLASE ENTORNO ******************************
class Entorno():

    def __init__(self, previus):
        self.previus = previus
        self.Global = None
        self.tablaSimbolos = {}
        self.entornosLocales = []
        self.nombreEntorno = ''

    def ingresar_simbolo(self, id, simbolo):        
        if id in self.tablaSimbolos.keys():
            print("Id existente")
        else:
            print("id no existente")
            self.tablaSimbolos[id] = simbolo

    def obtener_simbolo(self,id):
        return self.tablaSimbolos[id]

    def actualizar_simbolo(self, id, simbolo):
        self.tablaSimbolos[id] = simbolo
    
    def existeSimboloEntornoActual(self, id):
        if id in self.tablaSimbolos.keys():
            return True
        else:
            return False
        
        pass
    
    def obtenerSimbolo(self, id):

        entornoAnalizar = self

        while entornoAnalizar != None :            

            if entornoAnalizar.existeSimboloEntornoActual(id) :
                return entornoAnalizar.obtener_simbolo(id)

            entornoAnalizar = entornoAnalizar.previus
        
        return None            

    def buscar_variable(self,id):
        pass
        
    def recorrerEntorno(self):
        i = 1
        print('Nombre Entorno: ', self.nombreEntorno)
        for clave in self.tablaSimbolos:
            valor = self.tablaSimbolos[clave]
            print('------',i,'------\n')
            print(valor.id)
            print(valor.data_type.data_type)
            print(valor.data_type.data_specific)
            print(valor.valor)
            i = i + 1
            pass

        for entornoLocal in self.entornosLocales:
            entornoLocal.recorrerEntorno()
            pass

        pass        
# ***************************************************************************


# entornoLocal = Entorno(None)
# data = Data_Type.numeric
# tipo = Type(data,1)
# sim =  Symbol('nombre1','smalling',tipo,5)

# entornoLocal.ingresar_simbolo('nombre1',sim)
# entornoLocal.ingresar_simbolo('nombre1',sim)