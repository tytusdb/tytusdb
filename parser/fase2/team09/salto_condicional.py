import instrucciones as inst
import op_relacionales as relacion
import reglas as r

class Salto_con():
    def __init__(self, expresion, etiqueta, linea):
        self.expresion = expresion
        self.etiqueta = etiqueta
        self.linea = linea

    def optimizacion(self):
        rela = relacion.Relacional(self.expresion, self.linea).optimizacion()

        if r.Reglas.regla3:
            print('regla2')

        elif r.Reglas.regla4:
            return 'if (' + rela + ') : goto ' + self.etiqueta

        elif r.Reglas.regla5:
            return 'if (' + rela + ') : goto ' + self.etiqueta
        else:
            return 'if (' + rela + ') : goto ' + self.etiqueta

        return ''