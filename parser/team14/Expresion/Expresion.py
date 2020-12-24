
from Nodo import Nodo
from Entorno import Entorno
class Expresion(Nodo):
    '''
        Esta clase representa una expresión
    '''

    'Todas las Instrrucciones tienen un valor y un tipo'
    def __init__(self):
        'Obtener el valor de la Instrruccion'
        self.valor=None
        self.tipo=None

    def getval(self,entorno):
            'Metodo Abstracto para obtener el valor de la Instrruccion'

    def getTipo(self, entorno):
        'metodo abstracto getTipo'
