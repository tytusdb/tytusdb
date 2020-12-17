class Constraint:
    def __init__(self,nombre,condicion,columna):
        self.nombre = nombre
        self.condicion = condicion
        self.columna = columna
        self.siguiente = None
        self.anterior = None

    @classmethod
    def iniciar_SinColumna(cls,nombre,condicion):
        nuevo = cls.__new__(cls)
        nuevo.nombre = nombre
        nuevo.condicion = condicion
        nuevo.columna = None
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo
    
    @classmethod
    def iniciar_Check(cls,condicion):
        nuevo = cls.__new__(cls)
        nuevo.nombre = None
        nuevo.condicion = condicion
        nuevo.columna = None
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo
        