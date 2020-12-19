from analizer.symbol import symbol as sym


class Environment:
    """
    Esta clase representa los simbolos que producen los resultados
    de las diferentes ejecuciones (execute()) de las instrucciones y
    expresiones.
    """
    dataFrame = None
    def __init__(self, previous=None) -> None:
        self.previous = previous
        self.variables = {}

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
