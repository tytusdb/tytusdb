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
    def __init__(self):
        self.listaTablas = {}
    

    def execute(self, parent, enviroment = None):
        # Se le busca la base de datos que se esté usando
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        dbUse = config['databaseIndex'].upper()
        if dbUse == None:
            print("Se debe seleccionar una base de datos")
            return

        
        # Se llenan los datos a manera de probar el Select, comentar cuando se tenga el insert.
        # Datos de prueba para insertar
        truncate(dbUse,'empleado')
        for i in range(0,10):
            listEmpleado = [i,"Empleado"]
            insert(dbUse,'empleado',listEmpleado)
        
        

        # Se recorre cada nodo buscando las tablas utilizadas. Se hace un for primero porque
        # Las tablas se utilizarán tanto para el where y las columnas de retorno
        for hijo in parent.hijos:
            if hijo.nombreNodo == "TABLE_EXPRESION":
                for tabla in hijo.hijos:
                    if tabla.nombreNodo == "TABLE":
                        self.agregarTablaAlias(tabla)
                    else:
                        self.agregarTabla(tabla)
        
        # Se construye una estructura (la cual se enviará a expresión) con tal de poder buscar más
        # fácilmente los identificadores. Para ello se crean tuplas que tendrán la siguiente estructura:
        # listaTablas{"nameTable":{nameTabla, alias, lista:{//Columnas (el valor se agrega después)}}}
        listaMatrices = []
        for tabla in self.listaTablas:
            if tabla in showTables(dbUse):
                listaColumnas = tc.return_columnsJSON(dbUse,tabla.upper())
                for columna in listaColumnas:
                    nuevaCol = Info_Column(columna['name'],columna['type'])
                    self.listaTablas[tabla].lista[columna['name']] = nuevaCol
                listaMatrices.append(extractTable(dbUse,tabla.upper()))
            else:
                print("No se encontro la tabla ",tabla)
                return


        
        



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
        


        

