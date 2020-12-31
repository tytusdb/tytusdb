import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Librerias/storageManager')

from instruccion import *
from Lista import *
from TablaSimbolos import *
from jsonMode import *

class Use(Instruccion):

    def __init__(self, dbid):
        self.dbid = dbid

    def execute(self, data):
        databaseList = showDatabases()
        for database in databaseList:
            if self.dbid.column.upper() == database :
                data.databaseSeleccionada = database
                if database in data.tablaSimbolos:
                    ''
                else:
                    data.tablaSimbolos[database] = {'tablas' : {}, 'enum' : {}, 'owner' : 'CURRENT_USER', 'mode' : '1'}
                return 'La database ' + database + ' ha sido seleccionada.'
        return 'Error(???): La database ' + self.dbid.column.upper() + ' no existe.'

    def __repr__(self):
        return str(self.__dict__)
