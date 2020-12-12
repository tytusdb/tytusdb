class query:
    '''Esta es una clase abstracta'''

class ShowDatabases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable) :
        self.variable = variable
