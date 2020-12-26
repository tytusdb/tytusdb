from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from StoreManager import jsonMode as dbms
from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos
from Interprete.Manejo_errores import ErroresSintacticos

class AlterDatabase(NodoArbol):

    def __init__(self, line, column,  database_name_, new_name_):
        super().__init__(line, column)
        self.database_name = database_name_
        self.new_name = new_name_

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        # Se verifica que la base de datos exista, y que el nuevo id no exista aun. El resultado se obtiene en un int
        result = dbms.alterDatabase(self.database_name, self.new_name)
        # Si la operacion fue exitosa
        if result == 0:
            # Si la base de datos actual es la que recibira el cambio de nombre
            if entorno.BDisNull() is False and entorno.getBD() == self.database_name:
                # Se actualiza el nombre de la base de datos actual
                entorno.setBD(self.new_name)
            cadena = 'tytus> Base de datos \'' + self.database_name + '\' fue renombrada como: \'' + self.new_name + '\''
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
            Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error",self.linea,self.columna, 'Alter Table')
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
            Error: ErroresSemanticos = ErroresSemanticos("La base de datos no existe", self.linea, self.columna,
                                                         'Alter Table')
            arbol.ErroresSemanticos.append(Error)

            print('La base de datos no existe')
            return
        # Si el nuevo nombre ya existe
        elif result == 3:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            Descripcion: El nuevo nombre ya existe
            '''
            Error: ErroresSemanticos = ErroresSemanticos("El nuevo nombre ya existe", self.linea, self.columna,
                                                         'Alter Table')
            arbol.ErroresSemanticos.append(Error)

            print('El nuevo nombre ya existe')
            return
        # Si el retorno fue cualquier otra cosa tambien seria un error
        else:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            Descripcion: Error desconocido
            '''
            Error: ErroresSemanticos = ErroresSemanticos("Error desconocido", self.linea, self.columna,
                                                         'Alter Table')
            arbol.ErroresSemanticos.append(Error)

            print('Error desconocido')
            return
