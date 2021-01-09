from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from StoreManager import jsonMode as dbms
from Interprete.Manejo_errores.ErroresSemanticos import  ErroresSemanticos

class ShowDatabases(NodoArbol):

    def __init__(self, line, column):
        super().__init__(line, column)

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        # Se ejecuta el metodo que devuelve lista de bases de datos
        result = dbms.showDatabases()
        # Si no hay bases de datos o hay un error
        if not result:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            Descripcion: No hay bases de datos
            '''
            Error: ErroresSemanticos = ErroresSemanticos("XX00: no hay base de datos", self.linea,
                                                         self.columna,
                                                         'show database')
            arbol.ErroresSemanticos.append(Error)
            print('No hay bases de datos')
            return
        # Si la operacion fue exitosa
        else:
            cad = ""
            for db in result:
                cad += " | " + db
            cad += " |"
            print("tytus> Las bases de datos en el sistema son: " + cad)
            arbol.console.append("tytus> Las bases de datos en el sistema son: " + cad)
