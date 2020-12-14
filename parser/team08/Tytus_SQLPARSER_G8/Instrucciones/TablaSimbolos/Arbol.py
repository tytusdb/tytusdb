class Arbol():
    'Esta clase almacenará todas las instrucciones, errores y mensajes.'
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.excepciones = []
        self.consola = []
