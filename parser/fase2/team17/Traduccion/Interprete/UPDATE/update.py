from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from StoreManager import jsonMode as dbms
from Interprete.Meta import Meta
from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos


#############################
# Patrón intérprete: UPDATE #
#############################

# UPDATE: modificar atributos de una tabla de acuerdo a una condición


class Update(NodoArbol):
    def __init__(self, line, column, table_name_, exp_list_, where_=None):
        super().__init__(line, column)
        self.table_name = table_name_
        self.exp_list = exp_list_
        self.where = where_

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
                                                         'Update')
            arbol.ErroresSemanticos.append(Error)
            print('No se ha seleccionado una base de datos para trabajar')
            return
        # Se verifica que exista la tabla a actualizar
        else:
            # Si la tabla existe
            if Meta.existTable(entorno.getBD(), self.table_name) is True:
                # Se obtiene los encabezados de la tabla, las columnas y sus valores a actualizar
                header = dbms.extractTable(entorno.getBD(), self.table_name)[0]
                columns, values = [], []
                self.getdata(columns, values, entorno, arbol)
                # Si no hay condicional where
                if self.where is None:
                    pass
                # Si hay condicional where
                else:
                    self.whithwhere(columns, header, values, entorno, arbol)
            # Si la tabla no existe se termina la ejecucion

# ----------------------------------------------------------------------------------------------------------------------

    def whithoutwhere(self, columns, header, values):
        pass

# ----------------------------------------------------------------------------------------------------------------------

    def whithwhere(self, columns, header, values, entorno, arbol):
        # Se verifica que existan las columnas y que no se repitan
        if Meta.existColumn(self.table_name, columns, header):  # Si existen
            # Se verifica que los tipos de valores de las columnas coincidan con los tipos de valores dados
            Meta.databaseName = entorno.getBD()
            Meta.tableName = self.table_name
            if self.TypesCompare(self.setheaders(columns), values, entorno, arbol):  # Si todos los tipos coinciden
                # Se verifican que los valores dados cumplan las especificaciones de las columnas
                if self.verifyespecs(columns, values, header) is True:  # TODO: 1) Hay que ver que se cumplan todas
                    # Se selecciona la tabla de la que se extraeran los registros en la tabla de simbolos
                    entorno.settable(dbms.extractTable(entorno.getBD(), self.table_name))
                    # Se resuelven los where y se obtiene un posible resultado
                    pks = self.where.execute(entorno, arbol)  # TODO: 2) Validar todos los operacionales para el where
                    # Si no hubieron coincidencias en la busqueda del where
                    if not pks:
                        print("tytus> No hubieron coincidencias en la búsqueda")
                    # Si hubo un error en la busqueda del where
                    elif pks is None:
                        return
                    # Si hubieron coincidencias en la busqueda del where
                    else:
                        # Si se cumplio cada una de las condiciones, se obtienen los registros y llaves primarias
                        registers = self.createregisters(Meta.getListNumberColumns(columns, header), values, entorno,
                                                         arbol)
                        for pk in pks:
                            # Se ejecuta el metodo del dbms para actualizar los valores de una tabla
                            dbms.update(entorno.getBD(), self.table_name, registers, pk)
                        message = "tytus> Se modificaron las columnas exitosamente"
                        arbol.console.append(message)
                        print("tytus> Se modificaron las columnas exitosamente")

# ----------------------------------------------------------------------------------------------------------------------

    def getdata(self, columns, values, entorno, arbol):
        # Se recorre la lista de expresiones
        for exp in self.exp_list:
            # Se guarda el diccionario
            dic = exp.execute(entorno, arbol)
            # Se recorre el diccionario y se obtienen ambos valores
            for col in dic:
                columns.append(col)
                values.append(dic[col])

# ----------------------------------------------------------------------------------------------------------------------

    def TypesCompare(self, headColumns, listValues, entorno, arbol) -> bool:
        result: bool = True
        typeColumns = Meta.getTypeHeadColumns(headColumns)
        typeValues  = Meta.getTypes(listValues, entorno, arbol)
        nameColumns = Meta.getNameColumns(headColumns)
        for i in range(len(typeColumns)):
            nameColumn: str = nameColumns[i]
            typeColumn: int = typeColumns[i]
            typeValue: int = typeValues[i]
            if typeColumn != typeValue:
                '''
                  ______ _____  _____   ____  _____  
                 |  ____|  __ \|  __ \ / __ \|  __ \ 
                 | |__  | |__) | |__) | |  | | |__) |
                 |  __| |  _  /|  _  /| |  | |  _  / 
                 | |____| | \ \| | \ \| |__| | | \ \ 
                 |______|_|  \_\_|  \_\\____/|_|  \_\
                borra el print de abajo o comentalo xd
                Descripcion: la columna: %nameColumn% No acepta el %value.tipo%
                '''
                Error: ErroresSemanticos = ErroresSemanticos("XX45: la columna "+nameColumn+ " no acepta el valor ", self.linea,
                                                             self.columna,
                                                             'Drop Database')
                arbol.ErroresSemanticos.append(Error)
                print(' la columna: ' + nameColumn + ' No acepta el ' + str(typeValue))
                result = False
        return result

# ----------------------------------------------------------------------------------------------------------------------

    def verifyespecs(self, columns, values, header):
        # Se recorren todas las columnas a evaluar
        for column in range(len(columns)):
            # Si la columna posee restricción not null
            if Meta.isNotNullByName(columns[column]) is True:
                # Si la tabla no cumple con el not null
                if Meta.checkNotNull(self.table_name, [columns[column]], [values[column]], header) is False:
                    return False
            # Si la columna posee restricción unique
            if Meta.isUniqueByName(columns[column]) is True:
                # Si la tabla no cumple con el unique
                if Meta.checkUnique([columns[column]], [values[column]], Meta.getHeadByName(columns[column])) is False:
                    return False
            # Si se cumple con todas las especificaciones
        return True

# ----------------------------------------------------------------------------------------------------------------------

    def createregisters(self, columns, values, entorno, arbol):
        registers = {}
        for index in range(len(columns)):
            val = values[index].execute(entorno, arbol)
            registers[columns[index]] = val.data
        return registers

# ----------------------------------------------------------------------------------------------------------------------

    def setheaders(self, columns):
        heads = []
        for column in columns:
            head = Meta.getHeadByName(column)
            heads.append(head)
        return heads
