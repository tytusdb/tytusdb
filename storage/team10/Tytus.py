class Tytus:
    def __init__(self):
        self.databases = []

    # @description | Devuelve una lista de los nombres de la base de datos, el nombre es único.
    def showDatabases(self):
        print("showDatabases")

    # @description | Cambia el nombre de una base de datos.
    def alterDatabase(self, old, new):
        print("alterDatabase")

    # @desciption | Crea una base de datos.
    def createDatabase(self, name):
        print("createDatabase")

    # @desciption | Elimina por completo la base de datos indicada. 
    def dropDatabase(self, name):
        print("dropDatabase")
    
    # @desciption | Crea una tabla según el modo de almacenamiento, la base de datos debe existir, y solo se define el número de columnas.
    def createTable(self, db, name, nCols):
        print("createTable")

    # @desciption | Cambia el nombre de una base de datos.
    def alterTable(self, db, old, new):
        print("alterTable")

    # @desciption | Elimina por completo la tabla indicada.
    def dropTable(self, db, name):
        print("dropTable")
    
    # @desciption | Agrega una columna a cada registro de la tabla.
    def alterAdd(self, db, name, columnName):
        print("alterTable")

    # @desciption | Elimina un n-esima columna de cada registro de la tabla.
    def alterDrop(self, db, name, column):
        print("alterDrop")

    # @desciption | Extrae y devuelve en una lista de listas el contenido de la tabla
    def extractTable(self, db, name, column):
        print("extractTable")
    
    # @desciption | Carga un archivo csv de una ruta especificada indicando la ruta de la base de datos y en qué tabla será guardada. Si la tabla
    #               existe verifica la cantidad de columnas, si no corresponde da error. Si la tabla no existe, la crea. Si la base de datos no existe,
    #               la crea con el modo especificado.
    def loadCSV(self, fileCSV, db, table, mode):#mode debe ser un int
        print("chargueCSV")

    # @desciption | Inserta un registro en la estructura de datos persistente, database es el nombre de la base de datos, table es el nombre de la tabla
    #               y columns es una lista de campos a insertar. Devuelve un True si no hubo problema y una False si no se logró insertar.
    def insertTuple(self, db, table, campos):
        print("insertTuple")

    # @desciption | Actualiza el valor de una columna x en un registro id de una tabla de una base de datos. Devuelve True si se actualió correctamente
    #               y False si no se logró actualizar.
    def updateTuple(self, db, table, id, nCol, val):
        print("updateTuple")

    # @desciption | Elimina un nodo o elemento de página indicado de una tabla y base de datos especificada.
    def deleteTuple(self, db, table, id):
        print("deleteTuple")

    # @desciption | Vacía la tabla de todos los registros.
    def truncateTuple(self, db, table):
        print("truncateTuple")

    # @desciption | Extrae y devuelve una tupla especificada
    def extractRow(db, table, id):
        print("extractRow")
    
    def extractTuple(self, table, idTuple):
        print("extractTuple")

class Database:
    
    def __init__(self):
        self.tables = []

    def showTable(self):
        print("showTable")

    def alterDatabase(self, new):
        print("alterDatabase")
    
    def createTable(self, name, nCols):
        print("createTable")
    
    def alterTable(self, old, new):
        print("alterTable")

    def dropTable(self, name):
        print("dropTable")

    def alterAdd(self, name, columnName):
        print("alterAdd")

    def alterDrop(self, name, column):
        print("alterDrop")
    
    def extractTable(self, name, column):
        print("extractTable")

class HashTable:

    def __init__(self):
        self.lenght = 0
        self.percentage = 0.0
        arrayNodes = []

    def funcionHash(key):
        print("funcionHash")

    def addNode(value):
        print("addNode")
    
    def rehashing():
        print("rehashing")

    def searchValue(key):
        print("searchValue")

    def deleteNode(key):
        print("deleteNode")

    def updateNode(key):
        print("updateNode")

    def generateGraph():
        print("generateGraph")

class Table:

    def __init__(self):
        self.arrayTuples = []
        self.position = 0
        self. key = 0
        self.name = ""
        self.arrayColumns = []
        self.idTable = 0

    def createTable(name, nCols):
        print("createTable")

    def alterTable(new):
        print("alterTable")

    def alterAdd(colunmName):
        print("alterAdd")

    def alterDrop(column):
        print("alterDrop")

    def extractTable():
        print("extractTable")

class Column:
    def __init__(self):
        self.name = ""
        self.index = 0

    def createColumn(self, name):
        print("createColumn")

class Tuple:

    def __init__(self):
        self.id = 0
        self.values = []

    def updateTuple(nCol, val):
        print("updateTuple")
