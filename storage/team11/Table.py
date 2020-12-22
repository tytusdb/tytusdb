from ArbolAVLR import ArbolAVLR
import csv
import copy
import os.path as path


class Table:
    def __init__(self, name: str, nums_columns):
        self.__table_name = name
        self.__nums__columns = nums_columns
        self.__TableTree = ArbolAVLR()
        self.__list_pk = list()
        self.__isAutoincrement = False
        self.__index = 1  # contador que sumando

    # Sirve para setearle el nuevo nombre
    def set_table_name(self, name):
        self.__table_name = name

    # Retorna el nombre de la tabla
    def get_table_name(self):
        return self.__table_name

    # Guarda el nuevo valor del numero de columnas
    def set_nums_columns(self, nums_columns):
        self.__nums__columns = nums_columns

    # Retorna el numero de columnas
    def get_nums_columns(self):
        return self.__nums__columns

    # Metodo que retorna el indice actual de un registro
    def get__index(self):
        return self.__index

    # Sirve para setear el nuevo valor de index
    def set_index(self, index):
        self.__index = index

    # Retorna las posiciones de la llave primaria
    def get_list_pk(self):
        return self.__list_pk

    # Metodo que funciona para definir las llaves primarias
    def define_pk(self, colmns):
        if len(self.__list_pk) == 0:

            self.__list_pk = colmns
            if self.__TableTree.get_root():

                # Falta validaciones de llave primaria
                lista_data: list = self.__TableTree.extra_table()
                copia_arbol = copy.copy(self.__TableTree)
                self.__TableTree = ArbolAVLR()
                for value in lista_data:
                    x = self.insert(value)
                    if (x == 4):
                        self.__TableTree = copia_arbol
                        return 4
            return 0
        else:
            return 4

    # Metodo privado que retorna la concatenacion de las llaves primarias
    def __get_pk_string(self, data):

        PK_string = ""
        for i in range(len(self.__list_pk)):
            key = self.__list_pk[i]
            if len(self.__list_pk) - 1 == i:
                PK_string += str(data[key])
            else:
                PK_string += str(data[key]) + "_"
        return PK_string

    def extractTable(self):
        if self.__TableTree.get_root():

            return self.__TableTree.extra_table()
        else:
            return []

    # Metodo privado que retorna la concatenacion de las llaves primarias
    def __get_pk_string_alt(self, data):

        PK_string = ""
        for i in range(len(self.__list_pk)):
            key = self.__list_pk[i]
            if len(self.__list_pk) - 1 == i:
                PK_string += str(data[key + 1])
            else:
                PK_string += str(data[key + 1]) + "_"
        return PK_string

    # Metodo privado que retorna la concatenacion de las llaves primarias cuando extrae una tupla
    def __get_pk_string_extract(self, data):
        datastr = list()
        for dat in data:
            datastr.append(str(dat))
        PK_string = "_".join(datastr)
        return PK_string

    def __get_pk_string_2(self, data):
        PK_string = "_".join(str(data))
        return PK_string

    # Metodo para graficar

    def graficar(self):
        return self.__TableTree.grafica()

    # Cargar CSV
    def loadCSV(self, pathX):
        if path.exists(f"{pathX}"):
            file = open(pathX, "r", newline='\n')
            load = csv.reader(file)
            loadCopy = list(load)
            lista = list()

            row_count = 0
            for row in loadCopy:
                if len(row) > 0:
                    row_count += 1

            if row_count > 0:
                for register in loadCopy:
                    lista.append(self.insert(register))
                return lista
            else:
                return []
        else:
            return []

    # Metodo pra extraer una tupla
    def extractRow(self, pkList):

        if isinstance(pkList, int):
            busqueda = self.__TableTree.search_value(str(pkList))
            if busqueda:
                exito = busqueda.get_element().copy()
                exito.pop(0)
                return exito
            else:
                return []

        elif len(pkList) > 0:
            busqueda = self.__TableTree.search_value(self.__get_pk_string_extract(pkList))
            if busqueda:
                exito = busqueda.get_element().copy()
                exito.pop(0)
                return exito
            else:
                return []

        return []

    # Metodo para realizar un update de tupla
    def update(self, register, pkList):

        if isinstance(pkList, int):
            return self.__TableTree.update_node(pkList, register).get_element().insert(
                0, self.__get_pk_string(pkList))

        elif len(pkList) > 0:
            pk = self.__get_pk_string_extract(pkList)
            nodo = self.__TableTree.search_value(pk)
            if nodo:
                nodo_Data = nodo.get_element().copy()
                self.__TableTree.delete_nodo(pk)

                for key in register.keys():
                    nodo_Data[key + 1] = register[key]

                nodo_Data.pop(0)                
                return self.insert(nodo_Data)
            else:
                return 1
        else:
            return 1

    # Metodo para borrar una tupla
    def delete(self, register):

        if isinstance(register, int):
            busqueda = self.__TableTree.search_value(str(register))
            if busqueda:
                self.__TableTree.delete_nodo(str(register))
                return 0
            else:
                return 4

        elif len(register) > 0:
            pk = self.__get_pk_string_extract(register)
            busqueda = self.__TableTree.search_value(pk)
            if busqueda:
                self.__TableTree.delete_nodo(pk)
                return 0
            else:
                return 4

        else:
            return 1

    # Metodo para borrar las tuplas de la tabla
    def truncate(self):
        if self.__TableTree.get_root():
            self.__TableTree.truncate()
        else:
            return 1

    # Sirve para insertar tuplas
    def insert(self, data=list):

        if len(data) == self.__nums__columns:

            if len(self.__list_pk) == 0:
                self.__list_pk.append(0)
                self.__isAutoincrement = True
                self.insert(data)
                return 0

            elif self.__isAutoincrement:

                data.insert(0, str(self.__index))
                self.__TableTree.add(data)
                self.__index += 1
                return 0

            else:
                pk = self.__get_pk_string(data)
                if self.__TableTree.search_value(pk) is None:
                    data.insert(0, pk)
                    self.__TableTree.add(data)
                    return 0
                else:
                    return 4
        else:
            return 5

    def alterDropPK(self):
        self.__isAutoincrement = False
        if len(self.__list_pk) != 0:

            self.__list_pk = list()
            return 0
        else:
            return 4

    def alterAddColumn(self, default):
        self.__nums__columns += 1
        listKeys = self.__TableTree.get_tables()
        for pk in listKeys:
            self.__TableTree.search_value(pk).get_element().append(default)
        return 0    

    def alterDropColumn(self, column):
        if self.__TableTree.get_root():
            count = 0
            if column in range(0, self.__nums__columns):
                if not (self.__list_pk.__contains__(column)) and self.__nums__columns > 1:
                    self.__nums__columns -= 1
                    for pk in self.__list_pk:
                        if column < pk:
                            self.__list_pk[count] = pk - 1

                    listKeys = self.__TableTree.get_tables()
                    for pk in listKeys:
                        self.__TableTree.search_value(
                            pk).get_element().pop(column + 1)
                    count += 1
                    return 0
                return 4
            return 5
        else:
            return 1

    def extractRangeTable(self, column_number, lower, upper):
        if self.__TableTree.get_root():
            if isinstance(column_number, int):
                return self.__TableTree.extractRangeTable(int(column_number), str(lower), str(upper))
            else:
                return []
        else:
            return []
