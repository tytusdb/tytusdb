# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


class Node:
    def __init__(self, index, content):
        self.__index = index
        self.__content = content
        self.__left = None
        self.__right = None
        self.__height = 0

    # region properties
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, val):
        self.__index = val

    @index.deleter
    def index(self):
        self.__index = None

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, val):
        self.__content = val

    @content.deleter
    def content(self):
        self.__content = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, val):
        self.__left = val

    @left.deleter
    def left(self):
        self.__left = None

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, val):
        self.__right = val

    @right.deleter
    def right(self):
        self.__right = None

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val

    @height.deleter
    def height(self):
        self.__height = None
    # endregion
