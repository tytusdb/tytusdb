from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bplus
from storage.hash import HashMode as hash
from storage.isam import ISAMMode as isam
from storage.json import jsonMode as json
from storage.dict import DictMode as dict

modos = ["avl", "b", "bplus", "hash", "isam", "json", "dict"]
encoding = ["ascii", "utf8", "iso-8859-1"]

def __init__():
    global lista_db
    lista_db = []
    
__init__()

def buscar(nombre):
    for db in lista_db:
        if nombre == db[0]:
            return db
    else:
        return None

def createdatabase(db,modo,cod):
    if not modo in modos:
        return 3
    if not cod in encoding:
        return 4
    if buscar(db) == None:
        if modo == "avl":
            tmp = avl.createDatabase(db)

        elif modo == "b":
            tmp = b.createDatabase(db)

        elif modo == "bplus":
            tmp = bplus.createDatabase(db)

        elif modo == "hash":
            tmp = hash.createDatabase(db)

        elif modo == "isam":
            tmp = isam.createDatabase(db)

        elif modo == "json":
            tmp = json.createDatabase(db)

        elif modo == "dict":
            tmp = dict.createDatabase(db)
    else:
        return 2

    if tmp == 0:
        lista_db.append([db,modo,cod])
        return 0
    else:
        return 1


