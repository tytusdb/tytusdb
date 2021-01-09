import reglas as r

class Salto_in():
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta

    def optimizacion(self):
        if r.Reglas.regla3:
            print('regla2')
        elif r.Reglas.regla4:
            return 'goto ' + str(self.etiqueta)
        elif r.Reglas.regla5:
            return 'goto ' + str(self.etiqueta)
        elif r.Reglas.regla2:
            r.Reglas.pendiente = r.Reglas.pendiente + 'goto ' + str(self.etiqueta) + '\n'
            return 'goto ' + str(self.etiqueta)
        
        return 'goto ' + str(self.etiqueta)