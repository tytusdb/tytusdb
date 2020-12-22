import TypeCheck.ListaConstraints as ListaConstraints

class Atributo:
    def __init__(self,nombre:str,tipo:str):
        self.numero = None
        self.nombre = nombre
        self.tipo = tipo
        self.listaConstraints = ListaConstraints.ListaConstraints()
        #Punteros
        self.siguiente = None
        self.anterior = None

    '''@classmethod
    def iniciar_Solo_Default(cls,default:any):
        nuevo = cls.__new__(cls)
        nuevo.columnNumber = None
        nuevo.nombre = None
        nuevo.tipo = None
        nuevo.isPrimary = False
        nuevo.ForeignTable = None
        nuevo.default = default
        nuevo.isNull = True
        nuevo.isUnique = False
        # Punteros
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo'''