import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Utils')
sys.path.append('../Grupo1/Librerias/storageManager')

from instruccion import *
from Lista import *
from TablaSimbolos import *
from jsonMode import *
from c3dGen import *

class Use(Instruccion):

    def __init__(self,arg0,arg1, dbid):
        self.dbid = dbid
        self.arg0 = arg0
        self.arg1 = arg1

    def execute(self, data):
        databaseList = showDatabases()
        for database in databaseList:
            if self.dbid.column.upper() == database :
                data.databaseSeleccionada = database                
                if database in data.tablaSimbolos:
                    ''
                else:
                    data.tablaSimbolos[database] = {'tablas' : {}, 'enum' : {}, 'owner' : 'CURRENT_USER', 'mode' : '1'}
                resultado= useC3D(database)
                return 'La database ' + database + ' ha sido seleccionada.'
        return 'Error(???): La database ' + self.dbid.column.upper() + ' no existe.'

    def executec3d(self, data):
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
