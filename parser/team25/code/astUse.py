from useDB import instanciaDB
from storageManager import jsonMode as j
from reporteErrores.errorReport import ErrorReport
import sqlErrors
class Use:
    def __init__(self, name_data_base, linea = 0 ):
        self.name_data_base = name_data_base
        self.linea = linea
        
    def dibujar(self):
        identificador = str(hash(self))
        nodo = "\n" + identificador + "[ label = \"" + self.name_data_base + "\" ];"
        return nodo
    
    def ejecutar(self, ts):
        res = j.createDatabase(self.name_data_base)
        if res == 0: # no existia entonces hay que borrarla 
            j.dropDatabase(self.name_data_base)
            errorSql = sqlErrors.sql_error_fdw_error.fdw_schema_not_found
            return ErrorReport('semantico', 'ERROR: '+errorSql.value + ' , ' + errorSql.name, self.linea)
        elif res ==1:
            print("error con la Espino database :v ")
        elif res == 2:# ya existe , OK
            instanciaDB.DB_ACTUAL.name = self.name_data_base
        return # en este caso no retorno nada
            