from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from StoreManager import jsonMode as dbms
from Interprete.Meta import Meta
from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos
from Interprete.Manejo_errores import ErroresSintacticos

#################################
# Patrón intérprete: DROP TABLE #
#################################

# DROP TABLE: modificar atributos de una tabla de acuerdo a una condición


class DropTable(NodoArbol):
    def __init__(self, line, column, table_name_):
        super().__init__(line, column)
        self.table_name = table_name_

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        # Se verifica que se este trabajando sobre una base de datos
        if entorno.BDisNull() is True:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            Descripcion: No se ha seleccionado una base de datos para trabajar.
            '''
            Error: ErroresSemanticos = ErroresSemanticos("XX00: no se a seleccionado base de datos", self.linea,
                                                         self.columna,
                                                         'Drop Database')
            arbol.ErroresSemanticos.append(Error)
            print('No se ha seleccionado una base de datos para trabajar')
            return
        # Si ya se selecciono una base de datos
        else:
            # Se ejecuta el metodo del droptable para obetener un resultado
            result = dbms.dropTable(entorno.getBD(), self.table_name)
            # Si la operacion fue exitosa
            if result == 0:
                message = 'tytus> La tabla \'' + self.table_name + '\' fue eliminada exitosamente'
                print('tytus> La tabla \'' + self.table_name + '\' fue eliminada exitosamente')
                arbol.console.append(message)
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
                Descripcion: Hubo un error en la operacion.
                '''
                Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error ", self.linea,
                                                             self.columna,
                                                             'Drop Table')

                arbol.ErroresSemanticos.append(Error)
                print('Hubo un error en la operacion')
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
                Descripcion: La base de datos no existe.
                '''
                Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error db is not exist", self.linea,
                                                             self.columna,
                                                             'drop Table')
                arbol.ErroresSemanticos.append(Error)
                print('La base de datos no existe')
                return
            # Si la tabla no existe
            elif result == 3:
                '''
                  ______ _____  _____   ____  _____  
                 |  ____|  __ \|  __ \ / __ \|  __ \ 
                 | |__  | |__) | |__) | |  | | |__) |
                 |  __| |  _  /|  _  /| |  | |  _  / 
                 | |____| | \ \| | \ \| |__| | | \ \ 
                 |______|_|  \_\_|  \_\\____/|_|  \_\
                Descripcion: La tabla no existe.
                '''
                Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error table is not exist", self.linea,
                                                             self.columna,
                                                             'Drop Table')
                arbol.ErroresSemanticos.append(Error)
                print('La tabla no existe')
                return
