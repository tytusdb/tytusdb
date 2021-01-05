  
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Expresiones.Primitivo import Primitivo
from storageManager.jsonMode import *

class Indice():
    'Esta clase se utiliza para crear un indice'
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.lRestricciones = []
    
    def obtenerNombre(self):
        return self.nombre