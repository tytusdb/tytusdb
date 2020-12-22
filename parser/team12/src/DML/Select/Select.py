import sys, os.path

where_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Where')
sys.path.append(where_path)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker')
sys.path.append(storage)

from jsonMode import *
from typeChecker.typeChecker import *
tc = TypeChecker()


from Where import Where


class Info_Tabla():
    def __init__(self, nameTable,aliasTabla = None):
        self.nameTable = nameTable
        self.aliasTabla = aliasTabla
        self.lista = {}

class Info_Column():
    def __init__(self, nameColumn, typeColumn):
        self.nameColumn = nameColumn
        self.typeColumn = typeColumn
        self.valueColumn = None

class Select():
    
    def insertaDatos(self):
        truncate(self.dbUse,'EMPLEADO')
        truncate(self.dbUse,'PUESTO')
        db="EMPLEADO"
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        db = "PUESTO"
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])

    def verificarDBActiva(self):
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        dbUse = config['databaseIndex']
        if dbUse == None:
            print("Se debe seleccionar una base de datos")
            return None
        return dbUse.upper()

    def __init__(self):
        self.listaTablas = {}
        self.dbUse = None
        self.columnas = None
        self.listaTablasStorage = None
        self.listaTablasDatos = []
        
    def obtenerColumnasDictionary(self, tabla):
        listTemp = tc.return_columnsJSON(self.dbUse, tabla)
        listaCols = []
        if listTemp != None:
            for col in listTemp:
                listaCols.append([col['name'], col['type']])
            return listaCols
        return []

    def llenarEstructura(self, parent):
        # Recorrer cada uno de los nodos del padre.
        # Siempre se va a recibir una TABLE_EXPRESION
        # 1. Si el nodo es TABLE, se debe de verificar que exista dentro de las tablas
        #    almacenadas dentro de la DB. Si existe, crear una Info_Tabla con alias.
        # 2. Si el nodo es IDENTIFICADOR, se debe de verificar que exista dentro de las 
        #    tablas almacenadas dentro de la DB. Si existe, crear una Info_Tabla con alias.

        for hijo in parent.hijos:
            if hijo.nombreNodo == "TABLE":
                if not  (hijo.hijos[0].valor.upper() in self.listaTablasStorage):
                    print("Error, no se encuentra en la DB")
                    return
                nuevaTablaInfo = Info_Tabla(hijo.hijos[0].valor.upper(), hijo.hijos[1].valor.upper())
                self.listaTablas[hijo.hijos[0].valor.upper()] = nuevaTablaInfo
            else:
                if not  (hijo.valor.upper() in self.listaTablasStorage):
                    print("Error, no se encuentra en la DB")
                    return
                nuevaTablaInfo = Info_Tabla(hijo.valor.upper())
                self.listaTablas[hijo.valor.upper()] = nuevaTablaInfo
        for tabla in self.listaTablas:
            colDict = self.obtenerColumnasDictionary(tabla)
            for col in colDict:
                self.listaTablas[tabla].lista[col[0]] = Info_Column(col[0], col[1])

    def llenarListaTablaDatos(self):
        for tab in self.listaTablas:
            self.listaTablasDatos.append(extractTable(self.dbUse, tab))
        
    def execute(self, parent, enviroment = None):
        # Se verifican las variables, si esta seleccionada la base de datos 
        # Se llenan las tablas del storage, serán utilizadas mas adelante para
        # busquedas.
        self.dbUse = self.verificarDBActiva()
        if self.dbUse == None:
            print("Error, db no seleccionada")
            return
        self.listaTablasStorage = showTables(self.dbUse)

        # Pasos para llenar las tablas con los datos del storage, realizar producto
        # y realizar producto cartesiano
        # 1. Recorrer todos los hijos, cuando se encuentre TABLE_EXPRESION se debe de realizar
        #    el llenado de los datos
        # 1.1. Llenar las tablas con el método llenarEstructura, esto va a llenar la estructura
        #    que se va a utilizar para la expresión, aunque todavía no se llena ningun valor.
        # 1.2. Llenar listaTablaDatos con los datos del Storage. Se extraen los datos y se le hace append
        #    lo que construye una lista de matrices.
        # 1.3. Realizar producto cartesiano de estas tablas (listaTablasDatos) con la función

        # Datos de Prueba
        self.insertaDatos()


        matrizResultado = []
        for hijo in parent.hijos:
            if hijo.nombreNodo == "TABLE_EXPRESION":
                self.llenarEstructura(hijo)
                self.llenarListaTablaDatos()
                matrizResultado = self.cartesiano(self.listaTablasDatos)
        self.mostrarResultado(matrizResultado)



    def mostrarResultado(self, matrizPivote):
        matResult = []
        for x in matrizPivote:
            for j in range(0, len(x)):
                rowPivot = []
                for i in range(0,len(self.listaTablas)):
                    rowPivot =  rowPivot + self.listaTablasDatos[i][j]
                matResult.append(rowPivot)
        for x in matResult:
            print(x)
        #for i in range(0,len(matrizPivote)):
        #    rowPivot = []
        #    for j in range(1,len(matrizPivote[i])):
                


        

    def agregarTabla(self, parent):
        nuevaTabla = Info_Tabla(parent.valor)
        # Buscar la tabla en el diccionario y en Storage
        self.listaTablas[parent.valor.upper()]=nuevaTabla


    def agregarTablaAlias(self, parent):
        nuevaTabla = Info_Tabla(parent.hijos[0].valor, parent.hijos[1].valor)
        self.listaTablas[parent.hijos[0].valor.upper()]=nuevaTabla


    def cartesiano(self, listaMatrices):
        array = []
        for i in range(0,len(listaMatrices[0])):
            array.append([True,i])
        return self.funcionNXN(listaMatrices,1,array)
    

    def funcionNXN(self, listaMatrices, indice, matrizInicial):
        if indice<len(listaMatrices) :
            matrizPivote = listaMatrices[indice]
            result = []
            for i in range(0,len(matrizInicial)):
                for j in range(0,len(matrizPivote)):
                    a = matrizInicial[i][:]
                    a.append(j)
                    result.append(a)
            return self.funcionNXN(listaMatrices,indice+1,result)
        else:
            return matrizInicial
        


        

