class temporal:
    '''This is an abstract class'''

class MensajeOut:
    tipo='normal'
    mensaje=''
    codigo=''

class MensajeTs:
    instruccion=''
    identificador=''
    tipo=''
    unique=''
    referencia=''
    dimension=''
    columnas=''
    orden=''

class Tabla_run:
    def __init__(self, basepadre, nombre, atributos=[]): 
        self.basepadre = basepadre
        self.nombre = nombre
        self.atributos = atributos
        
class constraint_name:
    
    unique = None   #CONSTRAINT UNIQUE
    anulable = None #CONSTRAINT NOT NULL
    default = None  #CONSTRIANT DEFAULT
    primary = None  #CONSTRAINT PRIMARY
    foreign = None  #CONSTRAINT FOREING
    check = None    #CONSTRAINT CHECK


class Columna_run:
    nombre = ''
    tipo = ''
    size = None
    precision = None
    unique = None   #CONSTRAINT UNIQUE
    anulable = None #CONSTRAINT NOT NULL
    default = None  #CONSTRIANT DEFAULT
    primary = None  #CONSTRAINT PRIMARY
    foreign = None  #CONSTRAINT FOREING
    refence = None  #REFERENCES
    check = None    #CONSTRAINT CHECK
    constraint = None

    def __init__(self):
        global constraint
        self.constraint = constraint_name()
        self.constraint.unique=None
        self.constraint.anulable=None
        self.constraint.default=None
        self.constraint.primary=None
        self.constraint.foreign=None
        self.constraint.refence=None
        self.constraint.check=None
        
class Funcion_run:
    def __init__(self, nombre, tipo, contenido, parametros=[]):
        self.nombre=nombre
        self.tipo=tipo
        self.contenido=contenido
        self.parametros=parametros
class Parametro_run:
        nombre=None
        tipo=None
        tamano=None
        valor=None
        def __init__(self):
            '' 

class contenido_run:
        declaraciones=[]
        contenido=None

class Procedure_run:
    def __init__(self, nombre, contenido, parametros=[]):
        self.nombre=nombre
        self.contenido=contenido
        self.parametros=parametros
