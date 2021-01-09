from analizer.symbol import symbol as sym
from analizer.typechecker.Metadata import Struct


class Environment:
    """
    Esta clase representa los simbolos que producen los resultados
    de las diferentes ejecuciones (execute()) de las instrucciones y
    expresiones.
    """

    dataFrame = None
    groupCols = 0

    def __init__(self, previous=None, database="") -> None:
        self.database = database
        self.previous = previous
        self.variables = {}
        self.tables = []
        self.types = {}
        self.conta_temp = 0
        self.conta_exec = 0
        self.conta_etiqueta = 0
        self.codigo = "from goto import with_goto \nimport C3D \n\n@with_goto  # Decorador necesario\n"
        self.count_tabs = []

    def updateVar(self, id, value, type_):
        """
        Actualiza el valor de una llave en la tabla de simbolos
        """
        env = self
        while env != None:
            if id in env.variables:
                symbol = env.variables[id]
                symbol = sym.Symbol(id, value, type_, symbol.row, symbol.column)
                env.variables[id] = symbol
                return True
            env = env.previous
        return None

    def addVar(self, id, value, type_, row, column):
        """
        Inserta un nuevo simbolo en la tabla de simbolos
        """
        env = self
        if id in env.variables:
            return None
        symbol = sym.Symbol(value, type_, row, column)
        env.variables[id] = symbol
        return symbol

    def addSymbol(self, id, symbol):
        """
        Inserta un simbolo en la tabla de simbolos
        """
        env = self
        if id in env.variables:
            return None
        env.variables[id] = symbol
        return symbol

    def dropSymbol(self, id):
        """
        Elimina un simbolo en la tabla de simbolos
        """
        env = self
        if id in env.variables:
            del env.variables[id]
            return True
        return None    

    def addTable(self, table):
        """
        Inserta una nueva tabla
        """
        env = self
        env.tables.append(table)

    def ambiguityBetweenColumns(self, column):
        """
        Encargada de buscar ambiguedad de una columna entre todas
        las tablas de la clausula FROM
        """
        env = self
        i = 0
        table = None
        for t in env.tables:
            lst = Struct.extractColumns(env.database, t)
            for l in lst:
                if l.name == column:
                    i += 1
                    table = t
                    break
        if i > 1:
            print("Error: Existe ambiguedad entre la culumna:", column)
            return [True, None]
        return [False, table]

    def getType(self, table, column):
        """
        Encargada de buscar ambiguedad de una columna entre todas
        las tablas de la clausula FROM
        """
        env = self
        type = None
        while env != None:
            if table in env.variables:
                symbol = env.variables[table].value
                type = env.types[symbol + "." + column]
                break
            env = env.previous
        return type

    def updateVar(self, id, sym):
        env = self
        env.variables[id] = sym

    def getVar(self, id):
        env = self
        while env != None:
            if id in env.variables:
                symbol = env.variables[id]
                return symbol
            env = env.previous
        return None

    def getGlobal(self):
        """
        Obtiene el entorno global
        """
        env = self
        while env != None:
            env = env.previous
        return env

    def getColumn(self, table, column):
        env = self
        while env != None:
            if table in env.variables:
                symbol = env.variables[table]
                return env.dataFrame[symbol.value + "." + column]
            env = env.previous
        return None

    def getTableColumn(self, table, column):
        env = self
        while env != None:
            if table in env.variables:
                symbol = env.variables[table]
                return symbol.value + "." + column
            env = env.previous
        return None

    def getTemp(self):
        env = self
        env.conta_temp += 1
        return "t"+str(env.conta_temp) 

    def getEtiqueta(self):
        env = self
        env.conta_etiqueta += 1
        return "L"+str(env.conta_etiqueta)

