import TypeCheck.Base as Base

class ListaBases:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def agregarBase(self,nuevo:Base):
        if self.primero is None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            nuevo.anterior=self.ultimo
            self.ultimo=nuevo

    def estaVacia(self):
        if self.primero is None:
            return True
        else: 
            return False

    def existeBaseDatos(self, nombre:str):
        existe = False
        actual = self.primero
        while(actual!=None):
            if actual.nombreBase == nombre:
                existe = True
                break
            actual = actual.siguiente
        return existe

    def modificarNombreBase(self,antiguo:str, nuevo:str):
        if not self.existeBaseDatos(antiguo):
            return 2
        elif self.existeBaseDatos(nuevo):
            return 3
        else:
            actual = self.primero
            while(actual!=None):
                if actual.nombreBase == antiguo:
                    actual.nombreBase = nuevo
                    return 0
                actual = actual.siguiente
            return 1

    def modificarOwnerBase(self,database:str,nuevoOwner:str):
        if self.existeBaseDatos(database):
            actual = self.primero
            while (actual != None):
                if actual.nombreBase == database:
                    actual.owner = nuevoOwner
                    return 0
                actual = actual.siguiente
            return 1
        else:
            return 2

    def eliminarBaseDatos(self,nombre:str):
        if not self.existeBaseDatos(nombre):
            return 2
        else: 
            actual = self.primero
            while(actual!=None):
                if actual.nombreBase == nombre:
                    if self.primero == self.ultimo:
                        self.primero = self.ultimo = None
                    elif actual == self.primero:
                        self.primero = self.primero.siguiente
                        self.primero.anterior = None
                    elif actual == self.ultimo:
                        self.ultimo = self.ultimo.anterior
                        self.ultimo.siguiente = None
                    else:
                        actual.siguiente.anterior = actual.anterior
                        actual.anterior.siguiente = actual.siguiente
                    return 0
                actual = actual.siguiente
            return 1