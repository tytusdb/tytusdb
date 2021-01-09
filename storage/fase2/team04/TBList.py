# Package:      Storage Manager
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Alexis Peralta

from TBNode import TBNode

# Las listas TBList son listas simplemente enlazadas con adaptaciones para
# almacenar de forma organizada referencias de la información de las tablas
# almacenadas en los distintos modos del administrador de almacenamiento de
# TytusDB.
class TBList:
    def __init__(self):
        self.first = None
    
    # Descripción:
    #     Crea un nuevo nodo con la información de la tabla
    # Parámetros:
    #     name:str - El nombre de la tabla
    # Retorno:
    #     0 - Nodo creado exitosamente
    #     1 - Ya existe un nodo con el nombre indicado (tabla repetida)
    def create(self, name, columns):
        node = TBNode(name, columns)
        if self.first == None:
            self.first = node
        else:
            aux = self.first
            while True:
                if aux.name == node.name:
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
            print("[Nombre: {0} | PK: {1} | Columns: {2}]".format(aux.name, aux.pk, aux.columns))
            aux = aux.next

    # Descripción:
    #     Busca un nodo en la lista utilizando su nombre como parámetro de búsqueda
    # Parámetros:
    #     name:str - El nombre de la tabla que se desea buscar
    # Retorno:
    #     TBNode - El nodo con la información de la tabla
    #     None - No se encontró ninguna tabla con el nombre indicado
    def search(self, name):
        aux = self.first
        while aux != None:
            if aux.name == name:
                return aux
            aux = aux.next
        return None

    # Descripción:
    #     Elimina de la lista el nodo que tenga el nombre indicado
    # Parámetros:
    #     name:str - El nombre de la tabla cuyo nodo se desea eliminar
    # Retorno:
    #     0 - Nodo eliminado exitosamente
    #     1 - No se encontró ninguna tabla con ese nombre
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
    #     Modifica la información contenida en un nodo
    # Parámetros:
    #     name:str - El nombre de la tabla cuyo nodo se desea modificar
    #     new_pk:list - La nueva lista de llaves primarias que se desea
    # Retorno:
    #     0 - Modificación realizada exitosamente
    #     1 - No se encontró ninguna tabla con el nombre indicado
    def modify(self, name, new_pk, new_columns):
        aux = self.first
        while aux != None:
            if aux.name == name:
                aux.pk = new_pk
                aux.columns = new_columns
                return 0
            aux = aux.next
        return 1