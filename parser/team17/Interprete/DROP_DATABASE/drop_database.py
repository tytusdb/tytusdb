from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from StoreManager import jsonMode as dbms
from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos
from Interprete.Manejo_errores import ErroresSintacticos


class DropDatabase(NodoArbol):

    def __init__(self, line, column, database_name_):
        super().__init__(line, column)
        self.database_name = database_name_

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        # Se ejecuta el metodo para la eliminar la base de datos
        result = dbms.dropDatabase(self.database_name)
        # Si la operacion fue exitosa
        if result == 0:
            # Si la base de datos actual es la que se va a eliminar
            if entorno.getBD() == self.database_name:
                # Se coloca en nulo ls base de datos actual
                entorno.setBD("")
            cadena = 'tytus> Base de datos \'' + self.database_name + '\' fue eliminada exitosamente'
            print('tytus> Base de datos \'' + self.database_name + '\' fue eliminada exitosamente')
            arbol.console.append(cadena)
            return
        # Si hubo un error en la operacion
        elif result == 1:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            Descripcion: XX000	internal_error (yo creo que seria ese)
            '''
            Error: ErroresSemanticos = ErroresSemanticos("XX01: internal_error", self.linea,
                                                         self.columna,
                                                         'Drop Database')
            arbol.ErroresSemanticos.append(Error)
            print('XX00: internal_error')
            return
        # Si la base de datos no existe
        elif result == 2:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            Descripcion: La base de datos no existe
            '''
            Error: ErroresSemanticos = ErroresSemanticos("XX01: internal_error la db no existe", self.linea,
                                                         self.columna,
                                                         'Drop Database')
            arbol.ErroresSemanticos.append(Error)
            print('La base de datos no existe')
            return
