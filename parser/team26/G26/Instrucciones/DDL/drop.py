import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Librerias/storageManager')

from jsonMode import *

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

                print('DB Eliminada éxitosamente')
                return 'DB Eliminada éxitosamente'

            elif retorno == 1:
                'Error'
                #Algo salió mal imprimir error
                print('Salió mal')
                return 'Error(???): unknown_error'

            elif retorno == 2:
                'No existe'
                #No existe alv sjsjs xdxd
                print('no existe la base de datos')
                return 'Error(???): no existe la base de datos'
        else :
            print('eliminar Tabla ' + str(self.id.column.upper()))
            retorno = 0
            retorno = dropTable(str(data.databaseSeleccionada), str(self.id.column.upper()))
            if retorno == 0 :
                'Éxito'
                if self.id.column.upper() in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
                    del data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.id.column.upper()]
                
                print('Table Eliminada éxitosamente')
                return 'Table Eliminada éxitosamente'
            elif retorno == 1:
                'Error'
                print('Salió mal')
                return 'Error(???): unknown_error'
            elif retorno == 2:
                'No existe DB'
                print('no existe la base de datos')
                return 'Error(???): no existe la base de datos'
            elif retorno == 2:
                'No existe tabla'
                print('no existe la tabla')
                return 'Error(???): no existe la tabla'

        return self.id

    def __repr__(self):
        return str(self.__dict__)