
class TabladeSimbolos:
    def __init__(self, ambit):
        self.ambit = ambit
        self.size = 0
        self.simbolos = []


    def push(self, nuevo):
        if self.exists(nuevo.nombre):      # antes de insertar, valida si ya existe en la tabla de simbolos
            return False
        else:
            self.simbolos.insert(0, nuevo)
            return True


    def exists(self, nombre):
        for variable in self.simbolos:
            if variable.nombre == nombre and variable.ambito == self.ambit:
                return True
        return False


    def get(self, nombre):
        for simbolo in self.simbolos:
            if simbolo.nombre == nombre and (simbolo.ambito == self.ambit or simbolo.ambito == 'global'):
                return simbolo
        return None

