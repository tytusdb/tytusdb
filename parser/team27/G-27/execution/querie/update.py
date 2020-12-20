import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/storage')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
from querie import Querie
from storageManager import jsonMode as admin
from typ import *

#{'nombre':nCampo, 'valor': expression} <--- arreglo de assigns

class Update(Querie):
    '''
    idTable: id de la tabla a actualizar
    assignList: lista de diccionarios con el formato: {id:identificador, value:expressiones}
    condition: expression si viene where y True si no viene
    '''
    def __init__(self,idTable, assignList, condition, column, row ) -> None:
        super().__init__(self, row, column)
        self.idTable = idTable
        self.assignList = assignList
        self.condition = condition
    
    def execute(self, environment):
        #NOMBRE DE LA BD
        dbname = environment.getActualDataBase()
        db = environment.readDataBase(dbname)
        if(db == None):
            return {'Error':'No se encuentra una base de datos en uso', 'Fila': self.row, 'Columna': self.column}
        #NOMBRE DE LA TABLA
        tbname = self.idTable
        #LISTA CON LOS INDEX DE LAS COLUMNAS QUE SON LLAVES PRIMARIAS
        table = db.getTable(self.idTable)
        #Diccionario con las clave el nombre de la tabla y valor el indice
        indColumnas = {}
        for c in range(len(table.columns)):
            indColumnas[table.columns[c].name] = c 
        #--Busco los nombres de los campos que son primary key
        pkNames = []
        for con in table.constraint:
            if con['type'] == 'primary':
                pkNames.append(con['value'])
        #--Busco los indices de los campos correspondientes
        pkIndexes = []
        for i in range(len(table.columns)):
            for item in pkNames:
                if table.columns[i].name == item:
                    pkIndexes.append(i)
        #LISTA DE LLAVE VALOR
        tuplas = admin.extractTable(dbname,tbname)
        if len(tuplas) == 0:
            return {'Error':'La tabla no contiene registros a actualizar.','Fila':self.row,'Columna':self.column} 
        if tuplas == None:
            return {'Error':'La tabla no ha podido encontrarse, error en el Storage.','Fila':self.row,'Columna':self.column}
        for tindex in range(len(tuplas)):
            for index in range(len(tuplas[tindex])):
                tipo = Type.STRING
                if isinstance(tuplas[tindex][index],int):
                    tipo = Type.DECIMAL
                environment.guardarVariable(table.columns[index].name,tipo.STRING,tuplas[tindex][index])
                #REGISTRO MODIFICADO XD
                tuplaModificada = {}
                for asign in self.assignList:
                    clave = indColumnas[asign['id']]
                    valor = asign['value'].execute(environment)['value']
                    tuplaModificada[clave] = valor
                
                primaryKey = []
                for val in pkIndexes:
                    primaryKey.append(tuplas[tindex][val])
                
                where = True
                if not isinstance(self.condition, bool):
                    where = self.condition.execute(environment)
                if where == True:
                    res = admin.update(dbname, tbname, tuplaModificada, primaryKey)
                    switcher = {
                        1:'',
                        2:'',
                        3:'',
                        4:'',
                    }
