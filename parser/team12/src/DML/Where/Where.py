import sys, os.path

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\storageManager')
sys.path.append(storage)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker')
sys.path.append(storage)

from jsonMode import *
from typeChecker.typeChecker import *
tc = TypeChecker()

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
class Where():
    def __init__(self):
        self.listaTablas = {}
        self.dbUse = None
        self.matEncabezados = []


    def ejeExpNone(self,parent, matrizMult, listaTablas, listaColumnas, matriz3DData):
        # Siempre se va a recibir una E
        # Se debe de recorrer la matriz de datos resultado del producto cartesiano
        matrizResult = []
        matEncabezados = []
        insertar = True
        for fila in matrizMult:
            for i in range(1,len(fila)):
                for j in range(0,len(listaColumnas[i-1])):
                    if insertar : 
                        matEncabezados.append([listaTablas[i-1][0],listaTablas[i-1][1],listaColumnas[i-1][j][0],listaColumnas[i-1][j][1]])
                    self.listaTablas[listaTablas[i-1][0]].lista[listaColumnas[i-1][j][0]].valueColumn=matriz3DData[i-1][fila[i]][j]

            rowRes = []
            for i in range(1,len(fila)):
                rowRes = rowRes + matriz3DData[i-1][fila[i]]
            matrizResult.append(rowRes)
            insertar = False

        self.matEncabezados = matEncabezados
        return matrizResult

    #region Ejecución de las expresiones
    def ejeExpCols(self,parent, matrizMult, listaTablas, listaColumnas, matriz3DData):
        # Siempre se va a recibir una E
        # Se debe de recorrer la matriz de datos resultado del producto cartesiano
        matrizResult = []
        matEncabezados = []
        insertar = True
        for fila in matrizMult:
            for i in range(1,len(fila)):
                for j in range(0,len(listaColumnas[i-1])):
                    #print("NoTabla:",i-1)
                    #print("Tabla:",listaTablas[i-1][0])
                    #print("NoFila:",fila[i])
                    #print("NoColumna:",j)
                    #print("Columna:", listaColumnas[i-1][j][0])
                    #print(matriz3DData[i-1][fila[i]][j],",",end='')
                    if insertar : 
                        matEncabezados.append([listaTablas[i-1][0],listaTablas[i-1][1],listaColumnas[i-1][j][0],listaColumnas[i-1][j][1]])
                    self.listaTablas[listaTablas[i-1][0]].lista[listaColumnas[i-1][j][0]].valueColumn=matriz3DData[i-1][fila[i]][j]

            resBoolean = parent.execute(self.listaTablas)
            fila[0] = resBoolean
            if resBoolean:
                rowRes = []
                for i in range(1,len(fila)):
                    rowRes = rowRes + matriz3DData[i-1][fila[i]]
                matrizResult.append(rowRes)
            insertar = False

        self.matEncabezados = matEncabezados
        return matrizResult
                


    #endregion
    #region Estructura a Enviar
    def llenarEstructura(self, listaTablas, listaColumnas):
        
        for i in range(0,len(listaTablas)):
            infTab = Info_Tabla(listaTablas[i][0],listaTablas[i][1])
            for j in range(0,len(listaColumnas[i])):
                infCol = Info_Column(listaColumnas[i][j][0],listaColumnas[i][j][1])
                infTab.lista[listaColumnas[i][j][0]] = infCol
            self.listaTablas[listaTablas[i][0]] = infTab

    #endregion
    

    def execute(self, parent, matriz3DData, listaTablas, listaColumnas, matrizMult):
        # Para el atributo WHERE se obtendrá el nodo SENTENCIA_WHERE, la cual siempre tendrá
        # un hijo expresión, todo esto se pasa en el parametro "parent"
        # La matrizData es la matriz 3D de datos obtenidos de los métodos extraer de
        # la STORAGE o si se necesitan otras validaciones, filas y columnas tal y como se extraen, por ejemplo, si se tienen 3 tablas,
        # la matrizData tendrá 3 filas(que representan cada tabla), las cuales tienen N filas 
        # más (fila de datos) la cual es un arreglo de columnas.  En el caso de ser una 
        # El parámetro listaTablas será una lista[] que contenga el nombre y alias de la tabla 
        # de las tablas. Por lo tanto se puede interpretar como una matriz de dos posiciones,
        # por ejemplo [[Tabla1, Alias1][Tabla2, Alias2]]. En el caso de que no tengan Alias,
        # colocar el nombre de la tabla, y en caso de no tener el nombre de la tabla (una subconsulta)
        # colocar el nombre del alias como nombre de la tabla y alias con alias (Que no queden None)
        # listaColumnas tendrá una lista con las columnas de las tablas junto con el tipo de dato
        # que tienen, a modo que quede un array de arrays de arrays. Ejemplo:
        # ([[[col1,type1],[col2,type2]],[[col1,type1],[col2,type2]]])
        # en donde listaTablas y listaColumnas se relacionen por el índice que poseen        

        # Este método Execute tendrá una lista de datos (de la misma forma que matriz3DData) la cual
        # ya estará filtrada, faltaría mostrar o ejecutar cada una de las acciones como corresponden.
        # Además se tendrá un índice, el cual indique el número de fila al que pertenece (que vendrá
        # en la posición 0, para que se puedan manejar los atributos, es decir el índice de la columna
        # dentro de Storage)

        # Pasos para el WHERE:
        # 1. Realizar el producto Cartesiano de matriz3DData
        
        if matrizMult == None:
            array = []
            for i in range(0,len(matriz3DData)):
                array.append([True,i])
            matrizMult = array
        
        self.llenarEstructura(listaTablas,listaColumnas)
        if parent != None:
            for hijo in parent.hijos:
                if hijo.nombreNodo == "E":
                    self.ejeExpCols(hijo, matrizMult, listaTablas, listaColumnas, matriz3DData)
                    return matrizMult
        else:
            self.ejeExpNone(None, matrizMult, listaTablas, listaColumnas, matriz3DData)
            return matrizMult
        #Tenemos la estructura llena, sin valores.

    def compile(self,parent):
        textoRetorno = " WHERE "
        if parent != None:
            for hijo in parent.hijos:
                if hijo.nombreNodo == "E":
                    textoRetorno = textoRetorno + hijo.getText()
        return textoRetorno