#clase para la tabla que guardará los errores
class ListaErrores():
    def __init__(self, errores={}):
        self.errores = errores

    def agregar(self, error):
        self.errores[error.id] = error
    
    def obtRepp(self):
        return self.errores
    
    def printRep(self):
        cadena = []
        for x in self.errores.keys():
            Errores = self.errores[x]
            print(getattr(Errores, 'tipo'))
            print(getattr(Errores, 'descripcion'))
            print(getattr(Errores, 'linea'))
    
    def getsize(self):
        return len(self.errores)

    def obtener(self, id):
        if not id in self.errores:
            print('[Error]: variable ', id, ' no definida.')
        
        return self.errores[id]
    
    def actualizar(self, error):
        self.errores[error.id] = error

    def clearErrores(self):
        self.errores.clear()

#clase específica para el error y sus atributos
class Error():

    def __init__(self, id, tipo, descripcion, linea):
        self.id = id
        self.tipo = tipo
        self.descripcion = descripcion
        self.linea = linea
    