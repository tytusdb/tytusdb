class Instruccion:
    '''This is an abstract class'''

class Crear_BD(Instruccion):
    '''
        Esta clase representa la instruccion de creacion de una BD.
        La instruccion Crear_BD unicamente tiene como parametro un identificador.
    '''
    def __init__(self,  id) :
        self.id = id


class Cambio_BD(Instruccion):
    '''
        Esta clase representa la instruccion del Cambio de una BD.
        La instruccion Cambio_BD unicamente tiene como parametro un identificador.
    '''
    def __init__(self,  id) :
        self.id = id


class Select_All(Instruccion):
    '''
        Esta clase representa la instruccion de Consulta general para tabla.
        La instruccion Select_All unicamente tiene como parametro un identificador.
    '''
    def __init__(self,  id) :
        self.id = id


class Delete_incondicional(Instruccion):
    '''
        Esta clase representa la instruccion de Delete general para tabla.
        La instruccion Delete_incondicional unicamente tiene como parametro un identificador.
    '''
    def __init__(self,  id) :
        self.id = id

class Delete_condicional(Instruccion) :
    '''
        Esta clase representa la instrucción Delete_incondicional.
    '''

    def __init__(self, expLogica, id) :
        self.expLogica = expLogica
        self.id = id

