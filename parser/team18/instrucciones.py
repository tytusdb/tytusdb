class Instruccion:
    '''This is an abstract class'''

class Imprimir(Instruccion) :
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self,  cad) :
        self.cad = cad


class CrearBD(Instruccion) :
    '''
        Esta clase representa la funcion para crear una base de datos solo recibe el nombre de la BD
    '''
    def __init__(self, nombre) :
        self.nombre = nombre


class CrearTabla(Instruccion) :
     '''
        Esta clase representa la funcion para crear una nueva tabla
     '''
     def __init__(self,cad) :
         self.cad = cad