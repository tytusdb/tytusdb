from ArbolAVLR import ArbolAVLR
import csv

class Table:
    def __init__(self, name: str, nums_columns):
        self.__table_name = name
        self.__nums__columns = nums_columns
        self.__TableTree = ArbolAVLR()
        self.__list_pk = list()
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
        self.__list_pk = colmns

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

    # Metodo privado que retorna la concatenacion de las llaves primarias
    def __get_pk_string_alt(self, data):

        PK_string = ""
        for i in range(len(self.__list_pk)):
            key = self.__list_pk[i]
            if len(self.__list_pk) - 1 == i:
                PK_string += str(data[key+1])
            else:
                PK_string += str(data[key+1]) + "_"
        return PK_string

     # Metodo privado que retorna la concatenacion de las llaves primarias cuando extrae una tupla
    def __get_pk_string_extract(self, data):
        PK_string = "_".join(data)
        return PK_string

    # Metodo para graficar
    def graficar(self):
        self.__TableTree.grafica()

    # Cargar CSV
    def loadCSV(self, path):
                
        file = open(path+".csv", newline='\n')
        load = csv.reader(file)
        for register in load:
            self.insert(register)

    # Metodo pra extraer una tupla
    def extractRow(self, pkList):

        if isinstance(pkList, int):
            self.__TableTree.search_value(pkList)
            return 0

        elif len(pkList) > 0:
            self.__TableTree.search_value(self.__get_pk_string_extract(pkList))
            return 0

        return 1

    # Metodo para realizar un update de tupla
    def update(self, register, pkList):

        if isinstance(pkList, int):
            self.__TableTree.update_node(pkList, register).get_element().insert(
                0, self.__get_pk_string(pkList))
            return 0

        elif len(pkList) > 0:
            x = self.__TableTree.update_node(
                self.__get_pk_string_extract(pkList), register).get_element()
            x[0] = self.__get_pk_string_alt(x)
            return 0

        else:
            return 1

    # Metodo para borrar una tupla
    def delete(self, register):

        if isinstance(register, int):
            self.__TableTree.delete_nodo(register)
            return 0

        elif len(register) > 0:
            self.__TableTree.delete_nodo(
                self.__get_pk_string_extract(register))
            return 0

        else:
            return 1

    # Metodo para borrar las tuplas de la tabla
    def truncate(self):

        self.__TableTree.truncate()

    # Sirve para insertar tuplas
    def insert(self, data=list):

        if len(data) == self.__nums__columns:

            if len(self.__list_pk) == 0:
                data.insert(0, self.__index)
                self.__TableTree.add(data)
                self.__index += 1

                return 0
            else:
                data.insert(0, self.__get_pk_string(data))
                self.__TableTree.add(data)
                return 0
        else:
            return 5
