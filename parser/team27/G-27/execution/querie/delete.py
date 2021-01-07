from execution.abstract.querie import Querie
from storageManager import jsonMode as admin
from execution.symbol.typ import *

class Delete(Querie):

    def __init__(self, idTable, condition, column, row):
        Querie.__init__(self,row, column)
        self.idTable = idTable
        self.condition = condition
    
    def execute(self, environment):
        dbname = environment.getActualDataBase()
        db = environment.readDataBase(dbname)
        if(db == None):
            return {'Error': 'No se encuentra una base de datos referenciada.'}
        tbname = self.idTable
        table = db.getTable(self.idTable)
        indColumnas = {}
        for c in range(len(table.columns)):
            indColumnas[table.columns[c].name] = c
        pkNames = []
        for con in table.constraint:
            if con['type'] == 'primary':
                pkNames.append(con['value'])
        
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
            
            #CREO UN ARREGLO CON LA LLAVE PRIMARIA DE ESE REGISTRO
            primaryKey = []
            for val in pkIndexes:
                primaryKey.append(tuplas[tindex][val])
            
            #VERIFICO LA CONDICIÓN DEL WHERE
            where = True
            if not isinstance(self.condition, bool):
                where = self.condition.execute(environment)['value']
            if where == True:
                res = admin.delete(dbname, tbname, primaryKey)
                switcher = {
                    0: 'Se ha realizado el delete en el registro con la FK: ' + str(primaryKey),
                    1:{'Error': 'Error en la operación delete.','Fila':self.row,'Columna':self.column},
                    2:{'Error': 'La base de datos' + dbname + 'no existe.','Fila':self.row,'Columna':self.column},
                    3:{'Error': 'La tabla ' + self.idTable + ' no existe.','Fila':self.row,'Columna':self.column},
                    4:{'Error': 'No existe el registro buscado: ' + str(primaryKey),'Fila':self.row,'Columna':self.column},
                }
                return switcher.get(res,'Error en la respuesta del update en el StorageManager.')
        
        return 'se realizo el delete en la tabla: '+ self.idTable+', correctamente'