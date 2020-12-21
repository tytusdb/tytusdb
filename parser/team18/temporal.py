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
    unique = None   #CONSTRAINT UNIQUE
    anulable = None #CONSTRAINT NOT NULL
    default = None  #CONSTRIANT DEFAULT
    primary = None  #CONSTRAINT PRIMARY
    foreign = None  #CONSTRAINT FOREING
    refence = None  #REFERENCES
    check = None    #CONSTRAINT CHECK
    constraint = None

class constraint_name:

    unique = None   #CONSTRAINT UNIQUE
    anulable = None #CONSTRAINT NOT NULL
    default = None  #CONSTRIANT DEFAULT
    primary = None  #CONSTRAINT PRIMARY
    foreign = None  #CONSTRAINT FOREING
    check = None    #CONSTRAINT CHECK

