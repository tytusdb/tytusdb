from execution.abstract.querie import Querie
from storageManager import jsonMode as admin
from execution.symbol.typ import *

#{'nombre':nCampo, 'valor': expression} <--- arreglo de assigns

class Update(Querie):
    '''
    idTable: id de la tabla a actualizar
    assignList: lista de diccionarios con el formato: {id:identificador, value:expressiones}
    condition: expression si viene where y True si no viene
    '''
    def __init__(self,idTable, assignList, condition, column, row ) -> None:
        super().__init__( row, column)
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
        #POR CADA TUPLA QUE HAYA
        for tindex in range(len(tuplas)): 
            #POR CADA CAMPO EN LA TUPLA CREO EN LA TABLA DE SIMBOLOS LA VARIABLE DE CADA CAMPO
            for index in range(len(tuplas[tindex])):
                #TIPOS, PROBABLEMENTE SE DEBA CAMBIAR
                tipo = Type.STRING
                if isinstance(tuplas[tindex][index],int):
                    tipo = Type.DECIMAL
                #GUARDAR EN EL ENTORNO UNA VARIALBE CON EL NOMBRE DE LA COLUMNA               
                environment.guardarVariable(table.columns[index].name, tipo, tuplas[tindex][index], None)

            #CREO EL DICCIONARIO CON LOS VALORES A MODIFICAR
            tuplaModificada = {}
            for asign in self.assignList:
                clave = indColumnas[asign['id']]
                valor = asign['value'].execute(environment)['value']
                tuplaModificada[clave] = valor
            print(tuplaModificada)
            #CREO UN ARREGLO CON LA LLAVE PRIMARIA DE ESE REGISTRO
            primaryKey = []
            for val in pkIndexes:
                primaryKey.append(tuplas[tindex][val])
            #VERIFICO LA CONDICIÓN DEL WHERE
            where = True
            if not isinstance(self.condition, bool):
                where = self.condition.execute(environment)['value']
            if where == True:
                res = admin.update(dbname, tbname, tuplaModificada, primaryKey)
                switcher = {
                    0: 'Se ha realizado el update en el registro con la FK: ' + str(primaryKey),
                    1:{'Error': 'Error en la operación update.','Fila':self.row,'Columna':self.column},
                    2:{'Error': 'La base de datos buscada no existe.','Fila':self.row,'Columna':self.column},
                    3:{'Error': 'La tabla ' + self.idTable + ' no existe.','Fila':self.row,'Columna':self.column},
                    4:{'Error': 'No existe el registro buscado: ' + str(primaryKey),'Fila':self.row,'Columna':self.column},
                }
                return switcher.get(res,'Error en la respuesta del update en el StorageManager.')
