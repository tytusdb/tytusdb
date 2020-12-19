import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/execution/querie')
sys.path.append('../tytus/storage')
from querie import * 
from environment import *
from table import *
from column import *
from storageManager import jsonMode as admin

class Create_Table(Querie):
    def __init__(self, table, fields, row, column):
        Querie.__init__(self, row, column)
        self.table = table
        self.fields = fields

    def execute(self, environment):
        if not isinstance(self.table,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        columnas = []
        restricciones = []

        for column in self.fields:
            if isinstance(column,Column):
                columnas.append(column)
            else:
                restricciones.append(column)
        
        for i in range(len(columnas)):
            if i+1 < len(columnas):
                for j in range(i+1, len(columnas)):
                    if columnas[i].name == columnas[j].name:
                        return {'Error': 'El nombre de columna ya está siendo utilzado' , 'Fila':self.row, 'Columna': self.column}

        name = environment.getActualDataBase()
        result = 3
        result = admin.createTable(name, self.table, len(columnas))
        if result == 0:            
            #Se creo la tabla en la base de datos correctamente.
            #Creo una nueva database en la metadata
            database = environment.readDataBase(name)
            #Creo una nueva tabla con el nombre solicitado
            newTable = Table(self.table,columnas,restricciones)
            #Agrego a la tabla las columnas pertenecientes a la misma
            primaryKeys = []
            ids = []
            for const in newTable.constraint:
                if const['type'] == "primary":
                    ids.append(const['value'])
            for index in range(len(newTable.columns)):
                for id in ids:
                    if newTable.columns[index].name == id:
                        primaryKeys.append(index)
            #Agrego la nueva tabla a la base de datos.
            database.addTable(newTable)
            
            create = admin.alterAddPK(name,self.table,primaryKeys)
            if (create == 0):
                return('Llave primaria agregada exitosamenta a la tabla' + self.table )
            elif (create == 1):
                return {'Error':'Tabla ' + self.table + ' creada, pero ocurrio un error al ingresar llaves primarias', 'Fila':self.row, 'Columna':self.column}
            elif (create == 2):
                return {'Error':'No se encontro la Base de datos, en agregar tabla', 'Fila':self.row, 'Columna':self.column}
            elif (create == 3):
                return {'Error':'No se pudo agregar llaves pirmarias a '+ self.table + ', Tabla no existente', 'Fila':self.row, 'Columna':self.column}
            elif (create == 4):
                return {'Error':'Llave Primaria ya existente en Tabla ' + self.table, 'Fila':self.row, 'Columna':self.column}
            elif (create == 5):
                return {'Error':'Columnas fuera del límites', 'Fila':self.row, 'Columna':self.column}
            return 'La Tabla ' + self.table + ' ha sido creada con éxito.' 
        elif result == 1:
            #Error al crear
            return {'Error':'Ocurrió un error en el storage manager Tabla' + self.table + ' no pudo ser creada.', 'Fila':self.row, 'Columna':self.column}
        elif result == 2:
            #Error al crear
            return {'Error':'Tabla' + self.table + ' no se encuentra en la base de datos.', 'Fila':self.row, 'Columna':self.column}
        elif result == 3:
            #Error al crear
            return {'Error':'Tabla' + self.table + 'ya existente, no pudo ser creada.', 'Fila':self.row, 'Columna':self.column}
