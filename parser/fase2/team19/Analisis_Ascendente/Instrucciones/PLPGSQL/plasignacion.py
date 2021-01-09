from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion

class Plasignacion(Instruccion):
    def __init__(self,id,expresion):
        self.id = id
        self.expresion = expresion

    def getC3D(self, lista_optimizaciones_C3D):
        igualado = ''
        if isinstance(self.expresion, Expresion.Expresion):
            igualado = self.expresion.getC3D(lista_optimizaciones_C3D)
            return '''    %s
    %s = %s''' % (igualado['code'], self.id, igualado['tmp'])
        else:
            igualado = self.expresion.getC3D(lista_optimizaciones_C3D)
        return '    %s = %s' % (self.id, igualado)

    def get_quemado(self):
        return '    %s = %s' % (self.id, self.expresion.get_quemado())
