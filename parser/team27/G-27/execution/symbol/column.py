class Column(object):
    def __init__(self, name, tipo, default, primary, foreign, unique, check, nullable):
        self.name = name
        self.tipo = tipo
        self.default = default
        self.primary = primary 
        self.foreign = foreign
        self.unique = unique
        self.check = check
        self.nullable = nullable