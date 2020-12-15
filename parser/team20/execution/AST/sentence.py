class Sentencia:
    ''' '''

class CreateDatabase(Sentencia):
    def __init__(self, name, ifexistsNotFlag):
        self.name = name
        self.ifexistsNotFlag = ifexistsNotFlag

# class Select(Sentencia):
#     def __init__(self, id):
#         self.id = id
#         aqui se agregan los valores necesarios para un select como valores a mostrar, tablas, condiciones de filtrado, etc