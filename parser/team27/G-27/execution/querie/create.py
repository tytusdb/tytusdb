import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/storage')
from querie import * 
from storageManager import jsonMode as admin

class Create(Querie):
    def __init__(self,replace, mode, name, column,row):
        Querie.__init__(self,column, row)
        self.replace = replace
        self.mode = mode
        self.name = name
    
    def execute(self, environment):
        if not isinstance(self.name,str):
            return {'Error': 'El nombre indicado de la base de datos no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        result = 3
        result = admin.createDatabase(self.name)  #<---------------------------
        if result == 0:
            #Se creo la base de datos correctamente.
            return 'La base de datos ' + self.name + ' ha sido creada con éxito.' 
        elif result == 1:
            #Error al crear
            return {'Error':'Ocurrió un error en el storage manager.' + self.name + ' no pudo ser creada.', 'Fila':self.row, 'Columna':self.column}
        elif result == 2:
            #Base de datos existente
            if self.replace == True:
                admin.dropDatabase(self.name) #<--------------------------------
                result = admin.createDatabase(self.name) #<--------------------------
                switcher = {
                    '0':'La base de datos' + self.name +' ha sido reemplazada con éxito',
                    '1':{'Error':'Ocurrió un error en el storage manager.' + self.name + ' no pudo ser reemplazada.', 'Fila':self.row, 'Columna':self.column},
                    '2':{'Error':'La Base de datos' + self.name +'no pudo ser reemplazada.', 'Fila':self.row, 'Columna':self.column}
                }
                return switcher.get(result, {'Error':'Error desconocido al intentar realizar el replace de ' + self.name,'Fila': self.row, 'Columna': self.column})
            else:
                return {'Error': "La base de datos que se desea crear ya existe.", 'Fila': self.row, 'Columna': self.column}
        else:
            return {'Error': "Error desconocido en el storage manager.", 'Fila': self.row, 'Columna': self.column}