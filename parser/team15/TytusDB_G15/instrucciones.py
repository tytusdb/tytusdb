class Instruccion:
    ''' Esta sera la clase de Instrucciones '''

class Definicion(Instruccion):
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id

class CreateDatabase(Instruccion):
    def __init__(self, nombre, usuario, modo = 1):
        self.nombre = nombre
        self.usuario = usuario
        self.modo = modo