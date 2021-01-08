import reglas as r

class Encabezado():
    def __init__(self, cadena):
        self.cadena = cadena

    def optimizacion(self):
        r.Reglas.optimizado = r.Reglas.optimizado + self.cadena + '\n'