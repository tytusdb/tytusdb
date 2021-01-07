class SimboloNuevoTipo():

    def __init__(self,nombre,posiblesValores):
        self.nombre = nombre
        self.posiblesValores = posiblesValores

    def setearNuevoValor(self,valor):
        if len(self.posiblesValores) == 0:
            self.posiblesValores.append(valor)            
            return 1
        else:

            for nodoValor in self.posiblesValores:

                if nodoValor.valor.lower() == valor.valor.lower():
                    return 0
            
            self.posiblesValores.append(valor)
            return 1