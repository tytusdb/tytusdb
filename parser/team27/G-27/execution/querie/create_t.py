from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from storageManager import jsonMode as admin
import copy

class Create_Table(Querie):
    """
    table: id con el nombre de la nueva tabla
    fields: arreglo que contiene objetos column o diccionarios de restriccion

    Formato de los diccionarios de cada restriccion:
    DEPENDE EN CADA PRODUCCIÓN DE LOS CAMPOS QUE SE AGREGARAN
    {'type': 'primary', 'name':nombre, 'value': id_campo2},
    {'type': 'foreign', 'name':nombre, 'value': campo_tabla1, 'references': campo_tabla_extranjera},
    {'type': 'not null', 'name':nombre, 'value': campo_no_nulo},
    {'type': 'check', 'name':nombre, 'value':objetoExpression},
    {'type': 'unique', 'name':nombre,'value': campo_unico}
    """
    def __init__(self, table, fields,herencia, row, column):
        Querie.__init__(self, row, column)
        self.table = table
        self.fields = fields
        self.herencia = herencia

    def execute(self, environment):
        if not isinstance(self.table,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        columnas = []
        restricciones = []
        colHerencia =[]
        
        if self.herencia != None:
            db_name = environment.getActualDataBase()
            database = environment.readDataBase(db_name)
            if database == None:
                return {'Error': 'Error al buscar en la base de datos, la herencia', 'Fila':self.row, 'Columna': self.column }                     
            table = database.getTable(self.herencia)
            if table == None:
                return {'Error': 'La tabla: '+self.herencia+' no existe en la base de datos, no se puede realizar la herencia.','Fila':self.row, 'Columna': self.column }
            colHerencia = copy.copy(table.columns)
            for col in colHerencia:
                if isinstance(col,Column):
                    columnas.append(col)  
   

        for column in self.fields:
            if isinstance(column,Column):
                columnas.append(column)
            else:
                restricciones.append(column)
        
        for it in restricciones:
            print(str(it))

        for i in range(len(columnas)):
            if i+1 < len(columnas):
                for j in range(i+1, len(columnas)):
                    if columnas[i].name == columnas[j].name:
                        return {'Error': 'El nombre de columna ya está siendo utilzado' , 'Fila':self.row, 'Columna': self.column}

        name = environment.getActualDataBase()
        result = 4
        result = admin.createTable(name, self.table, len(columnas))
        if result == 0:            
            #Se creo la tabla en la base de datos correctamente.
            #Creo una nueva database en la metadata
            database = environment.readDataBase(name)
            #Creo una nueva tabla con el nombre solicitado
            newTable = Table(self.table,columnas,restricciones)
            if self.herencia != None:
                newTable.herencia = self.herencia
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
                #return('Llave primaria agregada exitosamenta a la tabla' + self.table )
                return('La tabla: '+ self.table+' se ha creado con exito.' )
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
        elif result == 4:
            #Error al crear
            return {'Error':'Error desconocido al crear la tabla.', 'Fila':self.row, 'Columna':self.column}
