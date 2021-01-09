class TablaSimbolos:
    'Clase abstracta'

class TableData(TablaSimbolos):
    def __init__(self, name, type, size, pk, fk, default, null, unique, check):
        self.name = name
        self.type = type
        self.size = size
        self.pk = pk
        self.fk = fk
        self.default = default
        self.null = null
        self.check = check
        self.unique = unique

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class DatabaseData(TablaSimbolos):
        def __init__(self, name, owner, mode, use):
            self.name = name
            self.owner = owner
            self.use = use

        def execute(self):
            return self

        def __repr__(self):
            return str(self.__dict__)

class EnumData(TablaSimbolos):
        def __init__(self, name, val, database):
            self.name = name
            self.owner = owner
            self.use = use

        def execute(self):
            return self

        def __repr__(self):
            return str(self.__dict__)

class ConstraintData(TablaSimbolos):
        def __init__(self, name, val, tipo):
            self.name = name
            self.val = val
            self.tipo = tipo

        def execute(self):
            return self

        def __repr__(self):
            return str(self.__dict__)


class  FuncionesTS(TablaSimbolos):
		def __init__(self, nombre,parametros,tipo):
			self.nombre = nombre
			self.parametros = parametros
			self.tipo = tipo

		def execute(self):
			return self

		def __repr__(self):
			return str(self.__dict__)


class  IndicesTS(TablaSimbolos):
    def __init__(self, namecom,nombreindice,tablaname,unique,colname,tipoAscDes,specs,tipoindice):
        self.namecom = namecom
        self.nombreindice = nombreindice
        self.tablaname = tablaname
        self.unique = unique
        self.colname = colname
        self.tipoAscDes = tipoAscDes
        self.specs = specs
        self.tipoindice = tipoindice

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)            