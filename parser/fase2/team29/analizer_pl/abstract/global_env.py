class FunctionSymbol:
    def __init__(self, id, returnType, params) -> None:
        self.id = id
        self.returnType = returnType
        self.params = params


class GlobalEnvironment:
    def __init__(self) -> None:
        self.functions = {}

    def addFunction(self, id, returnType, params):
        if id not in self.functions:
            self.functions[id] = FunctionSymbol(id, returnType, params)

    def getFunction(self, id):
        """
        Esta funcion retorna el simbolo de funcion asociado al id que recibe.
        """
        if id in self.functions:
            return self.functions[id]