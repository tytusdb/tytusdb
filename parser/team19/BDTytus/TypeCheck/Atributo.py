class Atributo:
    def __init__(self,nombre,tipo):
        self.columnNumber = None
        self.nombre = nombre
        self.tipo = tipo
        self.isPrimary = False
        self.ForeignTable = None
        self.default = None
        self.isNull = True
        self.isUnique = False
        #Punteros
        self.siguiente = None
        self.anterior = None

    @classmethod
    def iniciar_esPrimary(cls,nombre,tipo):
        nuevo = cls.__new__(cls)
        nuevo.nombre = nombre
        nuevo.tipo = tipo
        nuevo.isPrimary = True
        nuevo.ForeignTable = None
        nuevo.default = None
        nuevo.isNull = False
        nuevo.isUnique = True
        #Punteros
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo

    @classmethod
    def iniciar_esForeign(cls,nombre,tipo, tabla):
        nuevo = cls.__new__(cls)
        nuevo.nombre = nombre
        nuevo.tipo = tipo
        nuevo.isPrimary = False
        nuevo.ForeignTable = tabla
        nuevo.default = None
        nuevo.isNull = False
        nuevo.isUnique = False
        #Punteros
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo

    @classmethod
    def iniciar_Default(cls,nombre,tipo,default):
        nuevo = cls.__new__(cls)
        nuevo.nombre = nombre
        nuevo.tipo = tipo
        nuevo.isPrimary = False
        nuevo.foreignTable = None
        nuevo.default = default
        nuevo.isNull = False
        nuevo.isUnique = False
        #Punteros
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo

    @classmethod
    def iniciar_NotNull(cls,nombre,tipo):
        nuevo = cls.__new__(cls)
        nuevo.nombre = nombre
        nuevo.tipo = tipo
        nuevo.isPrimary = False
        nuevo.ForeignTable = None
        nuevo.default = None
        nuevo.isNull = True
        nuevo.isUnique = False
        #Punteros
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo

    @classmethod
    def iniciar_esUnique(cls,nombre,tipo):
        nuevo = cls.__new__(cls)
        nuevo.nombre = nombre
        nuevo.tipo = tipo
        nuevo.isPrimary = False
        nuevo.ForeignTable = None
        nuevo.default = None
        nuevo.isNull = True
        nuevo.isUnique = True
        #Punteros
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo

    @classmethod
    def iniciar_Primary_Default(cls,nombre,tipo,default):
        nuevo = cls.__new__(cls)
        nuevo.nombre = nombre
        nuevo.tipo = tipo
        nuevo.isPrimary = True
        nuevo.ForeignTable = None
        nuevo.default = default
        nuevo.isNull = False
        nuevo.isUnique = True
        #Punteros
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo

    @classmethod
    def iniciar_Default_NotNull_Unique(cls,nombre,tipo,default):
        nuevo = cls.__new__(cls)
        nuevo.nombre = nombre
        nuevo.tipo = tipo
        nuevo.isPrimary = False
        nuevo.ForeignTable = None
        nuevo.default = default
        nuevo.isNull = False
        nuevo.isUnique = True
        #Punteros
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo

    @classmethod
    def iniciar_Default_Null(cls,nombre,tipo,default):
        nuevo = cls.__new__(cls)
        nuevo.nombre = nombre
        nuevo.tipo = tipo
        nuevo.isPrimary = False
        nuevo.ForeignTable = None
        nuevo.default = default
        nuevo.isNull = True
        nuevo.isUnique = False
        #Punteros
        nuevo.siguiente = None
        nuevo.anterior = None
        return nuevo

    @classmethod
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
        return nuevo