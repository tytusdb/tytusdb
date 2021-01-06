# Package:      Storage Manager
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Alexis Peralta

from DBNode import DBNode

# Las listas DBList son listas simplemente enlazadas con adaptaciones para
# almacenar de forma organizada referencias de las bases de datos almacenadas en
# los distintos modos del administrador de almacenamiento de TytusDB.
class DBList:
    def __init__(self):
        self.first = None
    
    # Descripción:
    #     Crea un nuevo nodo con la información de la base de datos
    # Parámetros:
    #     name:str - El nombre de la base de datos
    #     mode:str - El tipo de la base de datos
    #     encoding:str - El tipo de codificación que utiliza la base de datos
    # Retorno:
    #     0 - Nodo creado exitosamente
    #     1 - Ya existe un nodo con el nombre indicado (base de datos repetida)
    def create(self, name, mode, encoding):
        node = DBNode(name, mode, encoding)
        if self.first == None:
            self.first = node
        else:
            aux = self.first
            while True:
                if aux.name == node.name and aux.mode == mode:
                    return 1
                if aux.next == None:
                    break
                aux = aux.next
            aux.next = node
        return 0

    # Descripción:
    #     Imprime en consola la información de todos los nodos en la lista
    def show(self):
        aux = self.first
        while aux != None:
            print("[Nombre: {0} | Tipo: {1}]".format(aux.name, aux.mode))
            aux = aux.next

    # Descripción:
    #     Busca un nodo en la lista utilizando su nombre como parámetro de búsqueda
    # Parámetros:
    #     name:str - El nombre de la base de datos que se desea buscar
    # Retorno:
    #     DBNode - El nodo con la información de la base de datos
    #     None - No se encontró ninguna base de datos con el nombre indicado
    def search(self, name):
        aux = self.first
        while aux != None:
            if aux.name == name:
                return aux
            aux = aux.next
        return None
    
    # Descripción:
    #     Devuelve una lista con todos los nodos correspondientes a una misma base de datos
    # Parámetros:
    #     name:str - El nombre de la base de datos cuyos nodos se desean obtener
    # Retorno:
    #     Si existe al menos un nodo para esa base de datos, devuelve una lista con todos los nodos
    #     Si no existe ningún nodo para esa base de datos, devuelve una lista vacía
    def find_all(self, name):
        databases = []
        aux = self.first
        while aux != None:
            if aux.name == name:
                databases.append(aux)
            aux = aux.next
        return databases

    # Descripción:
    #     Devuelve una lista con los nombres de todas las bases de datos sin repetición.
    # Valores de retorno:
    #     Si existe al menos una base de datos, devuelve una lista con todas las bases de datos almacenadas
    #     Si no existe ninguna base de datos, devuelve una lista vacía
    def list_databases_diff(self):
        databases = []
        aux = self.first
        while aux != None:
            if aux.name not in databases:
                databases.append(aux.name)
            aux = aux.next
        return databases

    # Descripción:
    #     Elimina de la lista el nodo que tenga el nombre indicado
    # Parámetros:
    #     name:str - El nombre de la base de datos cuyo nodo se desea eliminar
    # Retorno:
    #     0 - Nodo eliminado exitosamente
    #     1 - No se encontró ninguna base de datos con ese nombre
    def delete(self, name):
        if self.first == None:
            return 1

        if self.first.name == name:
            if self.first.next == None:
                self.first = None
            else:
                self.first = self.first.next
            return 0

        aux = self.first
        while True:
            if aux.next == None:
                return 1
            if aux.next.name == name:
                aux.next = aux.next.next
                return 0
            aux = aux.next

    # Descripción:
    #     Elimina de la lista el nodo que tenga el nombre y modo indicados
    # Parámetros:
    #     name:str - El nombre de la base de datos cuyo nodo se desea eliminar
    #     mode:str - El modo de almacenamiento de la base de datos
    # Retorno:
    #     0 - Nodo eliminado exitosamente
    #     1 - No se encontró ninguna base de datos con ese nombre
    def delete_sp(self, name, mode):
        if self.first == None:
            return 1

        if self.first.name == name and self.first.mode == mode:
            if self.first.next == None:
                self.first = None
            else:
                self.first = self.first.next
            return 0

        aux = self.first
        while True:
            if aux.next == None:
                return 1
            if aux.next.name == name and aux.next.mode == mode:
                aux.next = aux.next.next
                return 0
            aux = aux.next

    # Descripción:
    #     Modifica la información contenida en un nodo
    # Parámetros:
    #     name:str - El nombre de la base de datos cuyo nodo se desea modificar
    #     new_mode:str - El nuevo valor que se quiere asignar a la propiedad mode
    # Retorno:
    #     0 - Modificación realizada exitosamente
    #     1 - No se encontró ninguna base de datos con el nombre indicado
    def modify(self, name, new_mode, new_encoding):
        aux = self.first
        while aux != None:
            if aux.name == name:
                aux.mode = new_mode
                aux.encoding = new_encoding
                return 0
            aux = aux.next
        return 1
    
    # Descripción:
    #     Devuelve el TBNode cuyo nombre coincida con el indicado
    # Parámetros:
    #     database:str - El nombre de la base de datos a la que pertenece la tabla
    #     table:str - El nombre de la tabla cuyo nodo se desea encontrar
    # Valores de retorno:
    #     TBNode - El nodo cuyo name coincide con el nombre de la tabla
    #     None - Si no encuentra ningúna tabla con el nombre indicado
    def find_table(self, database, table):
        dbs = self.find_all(database)
        for db in dbs:
            tb = db.tables.search(table)
            if tb != None:
                return tb
        return None