from analizer_pl import grammar
class FunctionSymbol:
    def __init__(self, type_, id, returnType, params) -> None:
        self.id = id
        self.returnType = returnType
        self.params = params
        self.type = type_


class GlobalEnvironment:
    def __init__(self) -> None:
        self.functions = {}
        self.isBlock = False

    def addFunction(self, type_, id, returnType, params):
        if id not in self.functions:
            self.functions[id] = FunctionSymbol(type_, id, returnType, params)

    def getFunction(self, id):
        """
        Esta funcion retorna el simbolo de funcion asociado al id que recibe.
        """
        if id in self.functions:
            return self.functions[id]
        grammar.PL_errors.append("Error P0000: No se encontro la funcion"+id)
        grammar.semantic_errors.append(["No se encontro la funcion "+id,""])

    def dropFunction(self, id):
        """
        Esta funcion elimina un simbolo de la tabla.
        """
        if id in self.functions:
            del self.functions[id]
            return True
        grammar.PL_errors.append("Error P0000: No se pudo eliminar "+id)
        grammar.semantic_errors.append(["No se pudo eliminar "+id,""])
        return None