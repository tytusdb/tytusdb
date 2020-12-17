import Tabla as Tabla

class ListaTablas:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregarTabla(self,nuevo:Tabla):
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

    def existeTabla(self, nombre:str):
        existe = False
        actual = self.primero
        while(actual!=None):
            if actual.nombreTabla == nombre:
                existe = True
                break
            actual = actual.siguiente
        return existe
    
    def obtenerTabla(self,table:str):
        actual = self.primero
        while(actual!=None):
            if actual.nombreTabla == table:
                break
            actual = actual.siguiente
        return actual