class query:
    '''Esta es una clase abstracta'''

class ShowDatabases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable) :
        self.variable = variable

class Select(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, tipo, operacion) :
        self.tipo = tipo
        self.operacion = operacion

class Select2(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, tipo, operacion1, operacion2) :
        self.tipo = tipo
        self.operacion1 = operacion2
        self.operacion2 = operacion2


class Asignacion(query) :
    '''
        Esta clase representa la instruccion de una asignacion AS
        recibe como parametro el campo y su nuevo nombre a manejar
    '''
    def __init__(self, campo, alias) :
        self.campo = campo
        self.alias = alias

