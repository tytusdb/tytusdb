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
    enum = 20



class SimboloColumna():

    def __init__(self,indice,nombre,tipoDat):
        if (tipoDat.lower()=="smallint"):
            self.tipoDato = TiposDatos.smallInt
        elif tipoDat.lower() ==  "integer":
            self.tipoDato = TiposDatos.integer
        elif tipoDat.lower() == "biginit":
            self.tipoDato = TiposDatos.bigInit
        elif tipoDat.lower() == "decimal":
            self.tipoDato = TiposDatos.decimal
        elif tipoDat.lower() == "numeric":
            self.tipoDato = TiposDatos.numeric
        elif tipoDat.lower() == "real":
            self.tipoDato = TiposDatos.real
        elif tipoDat.lower() == "double":
            self.tipoDato = TiposDatos.double_precision
        elif tipoDat.lower() == "money":
            self.tipoDato = TiposDatos.money
        elif tipoDat.lower() == "varchar":
            self.tipoDato = TiposDatos.varchar
        elif tipoDat.lower() == "character":
            self.tipoDato = TiposDatos.character
        elif tipoDat.lower() == "text":
            self.tipoDato = TiposDatos.text
        elif tipoDat.lower() == "timestamp":
            self.tipoDato = TiposDatos.time_si_zone
        elif tipoDat.lower() == "time":
            self.tipoDato = TiposDatos.time_No_zone
        elif tipoDat.lower() == "date":
            self.tipoDato = TiposDatos.date
        elif tipoDat.lower() == "boolean":            
            self.tipoDato = TiposDatos.boolean
        elif tipoDat.lower() == "interval":
            self.tipoDato = TiposDatos.interval
        else:
            self.tipoDato = TiposDatos.enum

        self.indice = indice
        self.nombre = nombre        
        self.defaultValue = None            # DefaultValue = None -->> Columna no tiene un valor por default
        self.null = False                   # null = false --->> NO acepta valores null
        self.primaryKey = False             # primaryKey = false --->> NO es llavaPrimaria
        self.unique = False                 # unique = false ---->> NO es columnaUnique
        self.tablaForanea = None            # tablaForanea --->> Guarda el nombre de la tabla a la que  hace referencia la llave foránea
        self.columnasForanea = []           # columnaFornea --->> Guarda el nombre de la columnas a la que hace referencia la llave foránea
        self.nombreConstraint = None        # nombre del constraint, si tuviera
        self.check = None                   # instancia de clase expresion
        self.tipoDatoNOprimitivo = None


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
        
    def setPropiedadNotNull(self):
        self.null = False
    
    def setPropiedadUnique(self):
        self.unique = True

    def setNombreConstraint(self, nombreCons):
        self.nombreConstraint = nombreCons
    
    def setNombreColumna(self, nombreColum):
        self.nombre = nombreColum
    
    def setTipoDato(self, tipoDato):
        self.tipoDato = tipoDato
    
    def setCheck(self,check):
        self.check = check
        
    def setIndice(self,indice):
        self.indice = indice
    


    
        
    
