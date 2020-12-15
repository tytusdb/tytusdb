import AVLTree
import os
import pickle
import re


# Check if the data files exist
def checkData():
    if not os.path.isdir("./Data"):
        os.mkdir("./Data")
    if not os.path.isfile("./Data/Databases.bin"):
        with open('./Data/Databases.bin', 'wb') as f:
            dataBaseTree = AVLTree.AVLTree()
            pickle.dump(dataBaseTree, f)


# Checks if the name is a valid SQL Identifier
def validateIdentifier(identifier):
    # Returns true if is valid
    return not re.search(r"[^a-zA-Z0-9 ]+|^[\s]", identifier)


def createDatabase(database):
    checkData()
    if database and validateIdentifier(database):
        with open("./Data/Databases.bin", "rb") as f:
            dataBaseTree = pickle.load(f)
            root = dataBaseTree.getRoot()
            if dataBaseTree.search(root, database):
                return 2
            else:
                dataBaseTree.add(root, database)
        with open("./Data/Databases.bin", "wb") as f:
            pickle.dump(dataBaseTree, f)
        return 0
    else:
        return 1


def showDatabases():
    checkData()
    with open("./Data/Databases.bin", "rb") as f:
        dataBaseTree = pickle.load(f)
        root = dataBaseTree.getRoot()
        dbKeys = dataBaseTree.postOrder(root)
        dataBaseTree.graph()
        return dbKeys[:-1].split("-")


def alterDatabase(dataBaseOld, dataBaseNew) -> int:
    checkData()
    if validateIdentifier(dataBaseOld) and validateIdentifier(dataBaseNew):
        with open("./Data/Databases.bin", "rb") as f:
            dataBaseTree = pickle.load(f)
            root = dataBaseTree.getRoot()
            if not dataBaseTree.search(root, dataBaseOld):
                return 2
            if dataBaseTree.search(root, dataBaseNew):
                return 3
            dataBaseTree.delete(root, dataBaseOld)
            dataBaseTree.add(root, dataBaseNew)
        with open("./Data/Databases.bin", "wb") as f:
            pickle.dump(dataBaseTree, f)
            return 0
    else:
        return 1

#
# print(createDatabase("   Queso"))
# print(createDatabase("_#B"))
# print(createDatabase("Ca&&&&sa"))
# print(createDatabase("_Zanahoria"))
# print(createDatabase("Base1"))
# print(createDatabase("Base datos 2"))
# print(createDatabase("Base1"))

#print(showDatabases())
#print(alterDatabase("Base datos 2", "Base10"))
#print(showDatabases())
