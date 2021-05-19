from parserT28.controllers.linked_list import SingleLinkedList

# Clase nodo para generar el ast temporal


class Node:
    def __init__(self, value):
        self.__id = 0
        self.__value = value
        self.__childrens = SingleLinkedList()
        self.__production = ''

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_childrens(self):
        return self.__childrens

    def set_childrens(self, childrens):
        self.__childrens = childrens

    def add_childrens(self, children):
        self.__childrens.insert_end(children)

    @property
    def production(self):
        return self.__production

    @production.setter
    def production(self, production):
        self.__production = production
