from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bPlus
from storage.dict import DictMode as diccionario
from storage.isam import ISAMMode as isam
from storage.hash import HashMode as hash
from storage.json import jsonMode as json
from Binary import verify_string

mode_list = list()


class Mode:
    def __init__(self, name_database, mode, enconding):
        self.__name_database = name_database
        self.__mode = mode
        self.__enconding = enconding

    def set_name_database(self, name_database):
        self.__name_database = name_database

    def get_name_database(self):
        return self.__name_database

    def set_mode(self, mode):
        self.__mode = mode

    def get_mode(self):
        return self.__mode

    def set_encondig(self, encondig):
        self.__enconding = encondig

    def get_encondig(self):
        return self.__enconding


def save_mode(database, mode, encondig):
    new_mode = Mode(database, mode, encondig)
    mode_list.append(new_mode)


def exist(database: str):
    for mode in mode_list:
        if mode.get_name_database() == database:
            return True
    return False


def createDatabase(database: str, mode: str, encoding: str):
    if verify_string(database):
        if exist(database): return 2
        if encoding.lower().strip() is "ascii" or encoding.lower().strip() is "iso-8859-1" \
                or encoding.lower().strip() is "utf8":
            status = -1
            if mode.lower().strip() is "avl":
                status = avl.createDatabase(database)
            elif mode.lower().strip() is "b":
                status = b.createDatabase(database)
            elif mode.lower().strip() is "bplus":
                status = bPlus.createDatabase(database)
            elif mode.lower().strip() is "dict":
                status = diccionario.createDatabase(database)
            elif mode.lower().strip() is "isam":
                status = isam.createDatabase(database)
            elif mode.lower().strip() is "json":
                status = json.createDatabase(database)
            elif mode.lower().strip() is "hash":
                status = hash.createDatabase(database)
            else:
                return 3
            if status == 0:
                save_mode(database, mode, encoding)
            return status
        else:
            return 4
    else:
        return 1
