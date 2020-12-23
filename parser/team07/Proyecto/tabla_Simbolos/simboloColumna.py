from enum import Enum

class TiposDatos(Enum):
    smallInt = 0
    integer = 1
    bigInit = 2
    decimal = 3
    numeric = 4
    real = 5
    double_precision= 6
    money = 7
    varchar = 8
    character = 9
    text = 10    
    date = 11
    time_No_zone = 12
    time_si_zone = 13
    boolean = 14
    columna = 15
    interval = 16    
    timestamp = 17
    nulo = 18
    default = 19



class SimboloColumna():

    def __init__(self,nombre,tipoDat):
        self.nombre = nombre
        self.tipoDato = tipoDat
        self.defaultValue = None            # DefaultValue = None -->> Columna no tiene un valor por default
        self.null = False                   # null = false --->> NO acepta valores null
        self.primaryKey = False             # primaryKey = false --->> NO es llavaPrimaria
        self.unique = False                 # unique = false ---->> NO es columnaUnique
        self.tablaForanea = None            # tablaForanea --->> Guarda el nombre de la tabla a la que  hace referencia la llave foránea
        self.columnasForanea = []           # columnaFornea --->> Guarda el nombre de la columnas a la que hace referencia la llave foránea
        self.nombreConstraint = None        # nombre del constraint, si tuviera
        self.check = None                   # instancia de clase expresion


    def crearLlavePrimaria(self):
        self.null = False
        self.primaryKey = True
        self.unique = True

    def setearTablaForanea(self, nombreTablaForanea):
        self.tablaForanea = nombreTablaForanea
    
    def setearColumnaForanea(self, nombreColumna):
        self.columnasForanea.append(nombreColumna)
    
    def setDefaultValue(self, valorDefault):
        self.defaultValue = valorDefault

    def setPropiedadNull(self):
        self.null = True
    
    def setPropiedadUnique(self):
        self.unique = True

    def setNombreConstraint(self, nombreCons):
        self.nombreConstraint = nombreCons
    
    def setNombreColumna(self, nombreColum):
        self.nombre = nombreColum
    
    def setTipoDato(self, tipoDato):
        self.tipoDato = tipoDato
    

    


    
        
    