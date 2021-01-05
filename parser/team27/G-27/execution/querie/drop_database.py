from execution.abstract.querie import * 
from storageManager import jsonMode as admin

class Drop_Database(Querie):
    """
    name: id de la base de datos a eliminar
    """
    def __init__(self,name, column,row):
        Querie.__init__(self,column, row)
        self.name = name
    #Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos no existente.
    def execute(self, environment):       
        if not isinstance(self.name,str):
            return {'Error': 'El nombre indicado de la base de datos no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        result = 3
        result = admin.dropDatabase(self.name)  #<---------------------------
        if result == 0:
            #Se elimino correctamente la base de datos
            environment.deleteDataBase(self.name)
            return 'Se elimino exitosamente la base de datos: ' + self.name 
        elif result == 1:
            #Error al crear
            return {'Error':'Ocurrió un error en el storage manager. No se pudo eliminar la base de datos:' + self.name, 'Fila':self.row, 'Columna':self.column}
        elif result == 2:
            #Base de datos:oldName no existe
            return {'Error':'No existe la base de datos con el nombre: ' + self.name, 'Fila':self.row, 'Columna':self.column}
        else:
            return {'Error': "Error desconocido en el storage manager.", 'Fila': self.row, 'Columna': self.column}