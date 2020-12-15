from enum import Enum

class TiposDatos(Enum):
    smallInt = 1
    integer = 2
    bigInit = 3
    decimal = 4
    numeric = 5
    real = 6
    double_precision= 7
    money = 8
    character = 9
    varchar = 10
    text = 11
    timestamp = 12
    date = 13
    time = 14
    interval = 15
    boolean = 16
    columna = 17



class SimboloColumna():

    def __init__(self,nombre,tipoDat):
        self.nombre = nombre
        self.tipoDato = tipoDat
        self.defaultValue = None            # DefaultValue = None -->> Columna no tiene un valor por default
        self.null = False                   # null = false --->> NO acepta valores null
        self.primaryKey = False             # primaryKey = false --->> NO es llavaPrimaria
        self.unique = False                 # unique = false ---->> NO es columnaUnique
        self.tablaForanea = None            # tablaForanea --->> Guarda el nombre de la tabla a la que  hace referencia la llave foránea
        self.columnasForanea = []       # columnaFornea --->> Guarda el nombre de la columnas a la que hace referencia la llave foránea
        self.nombreConstraint = None        # nombre del constraint, si tuviera


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
    

    


    
        
    