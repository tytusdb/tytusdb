import TypeCheck.Enum as Enum

class ListaEnums:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregarEnum(self,nuevo:Enum):
        if self.primero is None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            nuevo.anterior=self.ultimo
            self.ultimo=nuevo
    
    def createEnum(self,nombre:str,tipos:list):
        nuevo = Enum.Enum(nombre,tipos)
        self.agregarEnum(nuevo)

    def existeEnum(self,nombre:str):
        existe = False
        actual = self.primero
        while(actual!=None):
            if actual.nombreEnum == nombre:
                existe = True
                break
            actual = actual.siguiente
        return existe

    def obtenerTipos(self,nombre:str):
        actual = self.primero
        while(actual!=None):
            if actual.nombreEnum == nombre:
                return actual.tipos
            actual = actual.siguiente
        return None