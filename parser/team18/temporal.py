class temporal:
    '''This is an abstract class'''

class MensajeOut:
    tipo='normal'
    mensaje=''
    codigo=''


class Tabla_run:
    def __init__(self, basepadre, nombre, atributos=[]): 
        self.basepadre = basepadre
        self.nombre = nombre
        self.atributos = atributos
        
class Columna_run:
    nombre = ''
    tipo = ''
    size = ''
    precision = None
    unique = None
    anulable = None
    default = None
    primary = None
    foreign = None
    refence = None
    check = None
    constraint = None

