class Columna:
    def __init__(self, nombre_, tipo_, atributos_=None):
        self.nombre = nombre_
        self.tipo = tipo_
        self.atributos = atributos_


class Default:
    def __init__(self, valor_):
        self.valor = valor_


class Null:
    def __init__(self):
        pass


class NotNull:
    def __init__(self):
        pass


class Unique:
    def __init__(self, constraint_=None):
        self.constraint = constraint_


class UniqueC:
    def __init__(self, columnas_):
        self.columnas = columnas_


class Check:
    def __init__(self, exp_, constraint_=None):
        self.exp = exp_
        self.constraint = constraint_


class Constraint:
    def __init__(self, nombre_):
        self.nombre = nombre_


class PrimaryKey:
    def __init__(self):
        pass


class References:
    def __init__(self, table_, columnas_=None):
        self.table = table_
        self.columnas = columnas_


class PrimaryKeyC:
    def __init__(self, keys_):
        self.keys = keys_


class ForeignKeyC:
    def __init__(self, references_, keys_):
        self.references = references_
        self.keys = keys_


class Inherits:
    def __init__(self, tabla_=None):
        self.tabla = tabla_