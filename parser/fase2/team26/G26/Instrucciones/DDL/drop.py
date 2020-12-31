import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Librerias/storageManager')
sys.path.append('../G26/Utils')

from jsonMode import *
from Error import *
from instruccion import *

class Drop(Instruccion):
    #False: Drop table
    #True: Drop database
    def __init__(self, id, dropopt = False):
        self.dropopt = dropopt
        self.id = id

    def execute(self, data):
        #print(data)
        if self.dropopt == True :
            print('eliminar DB ' + str(self.id.column.upper()))
            retorno = 0
            retorno = dropDatabase(str(self.id.column.upper()))
            if retorno == 0 :
                'Éxito'
                #Buscar en la tabla de simbolos si existe
                if self.id.column.upper() in data.tablaSimbolos :
                    del data.tablaSimbolos[self.id.column.upper()]
                    
                if self.id.column.upper() == data.databaseSeleccionada :
                    data.databaseSeleccionada = ''
                return 'DB Eliminada éxitosamente'

            elif retorno == 1:
                'Error'
                error = Error('Semántico', 'Error(???): unknown_error', 0, 0)
                return error

            elif retorno == 2:
                'No existe'
                error = Error('Semántico', 'Error(???): no existe la base de datos', 0, 0)
                return error
        else :
            #print('eliminar Tabla ' + str(self.id.column.upper()))
            tbname = self.id.column.upper()
            if not tbname in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
                error = Error('Semántico', 'Error(???): no existe la tabla ' + tbname, 0, 0)
                return error

            pks = []
            for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
                if not colu.pk == None :
                    pks.append(colu.name)

            for id in pks :
                for table in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] : 
                    for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][table]['columns'] :
                        if col.fk == None :
                            continue
                        for fk in col.fk:
                            if fk == None : 
                                continue
                            if fk.tipo == 'fk' :
                                if fk.val.column == id.upper() :
                                    error = Error('Semántico', 'Error(???): La PK es FK en la tabla ' + table, 0, 0)
                                    return error

            retorno = 0
            retorno = dropTable(str(data.databaseSeleccionada), str(self.id.column.upper()))
            if retorno == 0 :
                'Éxito'
                if self.id.column.upper() in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
                    del data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.id.column.upper()]
                
                return 'Table Eliminada éxitosamente'
            elif retorno == 1:
                'Error'
                error = Error('Storage', 'Error(1): unknown_error.', 0, 0)
                return error
            elif retorno == 2:
                'No existe DB'
                error = Error('Storage', 'Error(2): no existe la base de datos.', 0, 0)
                return error
            elif retorno == 2:
                'No existe tabla'
                error = Error('Storage', 'Error(3): No existe la tabla.', 0, 0)
                return error

        return self.id

    def __repr__(self):
        return str(self.__dict__)