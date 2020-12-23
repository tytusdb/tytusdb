import TypeCheck.Tabla as Tabla

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
        while(actual is not None):
            if actual.nombreTabla == table:
                break
            actual = actual.siguiente
        return actual

    def eliminarTabla(self, table:str):
        if self.obtenerTabla(table) is not None:
            actual = self.primero
            while(actual is not None):
                if actual.nombreTabla == table:
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
        return 3