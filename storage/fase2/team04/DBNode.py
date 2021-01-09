# Package:      Storage Manager
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Alexis Peralta

from TBList import TBList

# Nodos utilizados en las listas DBList
class DBNode:
    def __init__(self, name, mode, encoding):
        self.main_db = False
        self.name = name
        self.mode = mode
        self.compress = False
        self.encoding = encoding
        self.tables = TBList()
        self.next = None