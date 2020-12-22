from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from StoreManager import jsonMode as dbms
from Interprete.Meta import Meta

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
            if self.TypesCompare(header, values, entorno, arbol):  # Si todos los tipos coinciden
                # Se verifican que los valores dados cumplan las especificaciones de las columnas
                if self.verifyespecs() is True:  # TODO: 1) En este punto hay que ver que cumplan las especificaciones
                    # TODO: 2) En este punto se haria el where y creo, se obtendrian las pks
                    # Si se cumplio cada una de las condiciones, se obtienen los registros y llaves primarias
                    registers = self.createregisters(Meta.getListNumberColumns(columns, header), values, entorno, arbol)
                    pks = []
                    # Se ejecuta el metodo del dbms para actualizar los valores de una tabla
                    dbms.update(entorno.getBD(), self.table_name, registers, pks)

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
                print(' la columna: ' + nameColumn + ' No acepta el ' + str(typeValue))
                result = False
        return result

# ----------------------------------------------------------------------------------------------------------------------

    def verifyespecs(self, columns, values, header):
        # Se verificara cada una de las
        pass

# ----------------------------------------------------------------------------------------------------------------------

    def createregisters(self, columns, values, entorno, arbol):
        registers = {}
        for index in range(len(columns)):
            val = values[index].execute(entorno, arbol)
            registers[columns[index]] = val.data
        return registers


