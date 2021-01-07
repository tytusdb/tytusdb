from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from execution.symbol.typ import *
from storageManager import jsonMode as admin

class Add_Constraint(Querie):
    ''' 
     row = numero de fila
     column = numero de columna
     columnName = espera un nombre de columna debe de ser una cadena
     constraintval = espera un constraint esto seria un dicionario con la siguiente sintaxis:
                    [
                    {'type': 'primary', 'name':nombre para el constraint(cadena) , 'value': nombre de la columna que es la llave primaria(cadena)},-> si es una llave primaria
                    {'type': 'foreign', 'name':nombre para el constraint(cadena), 'value': nombre de la columna que es la llave foranea(cadena), 'references': campo_tabla_extranjera}, -> si es una llave foranea
                    {'type': 'not null', 'name':nombre para el constraint(cadena), 'value': nombre de la columna que es nula(cadena)}, -> si es un NOT NULL
                    {'type': 'check', 'name':nombre para el constraint(cadena), 'value':objetoExpression -> un ojeto exp ejemplo (5>10)}, -> si es un CHECK
                    {'type': 'unique', 'name':nombre para el constraint(cadena),'value': nombre de la columna que va a ser unique(cadena)} si es un UNIQUE
                    ]
                    {'type': 'primary', 'name':'pk_tabla1' , 'value': 'columna_tabla1'}
                    
    '''
    def __init__(self,columnName,constraintVal, row, column):
        Querie.__init__(self, row, column)
        self.columnName = columnName
        self.constraintVal = constraintVal

   # constraintVal es un diccionario {'type': 'unique', 'name':nombre,'value': campo_unico}
    def execute(self, environment,tableName):
        if not isinstance(self.columnName,str):
            return {'Error': 'El nombre indicado de la columna no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        if not isinstance(tableName,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        db_name = environment.getActualDataBase()
        database = environment.readDataBase(db_name)
        table = database.getTable(tableName)

        repetido = False
        for item in table.constraint:
            if item['name'] == self.constraintVal['name']:
                repetido = True
                break
        if repetido == True:
             return {'Error': 'ya existe una restriccion con el mismo nombre', 'Fila':self.row, 'Columna': self.column }
        
        #columna a la que hace referencia menos el check
        if self.constraintVal['type'] != 'check':
            reference = False
            for item in table.columns:
                if item.name == self.constraintVal['value']:
                    reference = True
                    break
            if reference == False:
                return {'Error': 'La columna a la que hace referencia la restriccion no existe en la tabla: '+tableName, 'Fila':self.row, 'Columna': self.column }
        
        if self.constraintVal['type'] == 'primary':
            for item in table.constraint:
                if item['value'] == self.constraintVal['value']:
                    if item['type'] == 'primary':
                        return 'la columna: '+self.columnName +' ya tiene la restriccionde llave primaria'
            result = admin.extractTable(db_name, tableName)
            if isinstance(result,list):
                if len(result) > 0:
                    return {'Error': 'No se puede agregar la llave primaria a la tabla: '+tableName+' porque la tabla ya contiene valores.', 'Fila':self.row, 'Columna': self.column }
            for item in table.constraint:
                if item['type'] == 'primary':
                    self.constraintVal = {'type':self.constraintVal['type'],'name':item['name'],'value':self.constraintVal['value']}
        table.createConstraint(self.constraintVal)

        return 'la restriccion fue insertada en la tabla: '+tableName+' con exito.'




