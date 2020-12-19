import AVLTree
import BplusTree
import os
import pickle
import Serializable as serializable
import re
import shutil


def checkData():
    if not os.path.isdir("./Data"):
        os.mkdir("./Data")
    if not os.path.isfile("./Data/Databases.bin"):
        with open("./Data/Databases.bin", 'wb') as f:
            dataBaseTree = AVLTree.AVLTree()
            pickle.dump(dataBaseTree, f)


# Checks if the name is a valid SQL Identifier
def validateIdentifier(identifier):
    # Returns true if is valid
    try:
        return not re.search(r"[^a-zA-Z0-9_@#$]+|^[\s0-9@<>%$]", identifier)
    except:
        return False


def createDatabase(database):
    checkData()
    if database and validateIdentifier(database):
        dataBaseTree = serializable.Read('./Data/', 'Databases')
        root = dataBaseTree.getRoot()
        if dataBaseTree.search(root, database.upper()):
            return 2
        else:
            dataBaseTree.add(root, database.upper())
            serializable.write('./Data/', database, AVLTree.AVLTree())
            serializable.update('./Data/', 'Databases', dataBaseTree)
        return 0
    else:
        return 1


def showDatabases():
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    root = dataBaseTree.getRoot()
    dbKeys = dataBaseTree.postOrder(root)
    return [] if len(dbKeys) == 0 else dbKeys[:-1].split("-")


def alterDatabase(dataBaseOld, dataBaseNew) -> int:
    checkData()
    if validateIdentifier(dataBaseOld) and validateIdentifier(dataBaseNew):
        dataBaseTree = serializable.Read('./Data/', "Databases")
        root = dataBaseTree.getRoot()
        if not dataBaseTree.search(root, dataBaseOld.upper()):
            return 2
        if dataBaseTree.search(root, dataBaseNew.upper()):
            return 3
        dataBaseTree.delete(root, dataBaseOld.upper())
        serializable.Rename('./Data/', dataBaseOld, dataBaseNew)
        dataBaseTree.add(root, dataBaseNew.upper())
        serializable.update('./Data/', 'Databases', dataBaseTree)
        return 0
    else:
        return 1


def dropDatabase(database):
    checkData()
    if validateIdentifier(database):
        dataBaseTree = serializable.Read('./Data/', "Databases")
        root = dataBaseTree.getRoot()
        if not dataBaseTree.search(root, database.upper()):
            return 2
        dataBaseTree.delete(root, database.upper())
        serializable.delete('./Data/' + database)
        serializable.update('./Data/', 'Databases', dataBaseTree)
        return 0
    else:
        return 1
    
# ---------------CRUD TABLE----------------#
# ----------------Erick--------------------#

def createTable(database, table, numberColumns):
    # Validates identifier before searching
    if validateIdentifier(database) and validateIdentifier(table) and numberColumns >= 0:
        checkData()
        # Get the databases tree
        dataBaseTree = serializable.Read('./Data/', "Databases")
        # Get the dbNode
        databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database.upper())
        # If DB exist
        if databaseNode:
            tablesTree = serializable.Read(f"./Data/{database}/", database)
            if tablesTree.search(tablesTree.getRoot(), table.upper()):
                return 3
            else:
                # Creates new table node
                tablesTree.add(tablesTree.getRoot(), table.upper())
                serializable.update(f"./Data/{database}/", database, tablesTree)
                # Creates bin file for the new table
                serializable.write(f"./Data/{database}/", table, BplusTree.BPlusTree(5, numberColumns))
                return 0
        else:
            return 2
    else:
        return 1


def showTables(database):
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    if dataBaseTree.search(dataBaseTree.getRoot(), database.upper()):
        db = serializable.Read(f"./Data/{database}/", database)
        dbKeys = db.postOrder(db.getRoot())
        return [] if len(dbKeys) == 0 else dbKeys[:-1].split("-")
    else:
        return None


def extractTable(database, table):
    checkData()
    # Get the databases tree
    dataBaseTree = serializable.Read('./Data/', "Databases")
    # Get the dbNode
    databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database.upper())
    # If DB exist
    if databaseNode:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if tablesTree.search(tablesTree.getRoot(), table.upper()):
            table = serializable.Read(f'./Data/{database}/{table}/', table)
            return list(table.lista().values())
        else:
            return None
    else:
        return None


def extractRangeTable(database, table, columnNumber, lower, upper):
    checkData()
    # Get the databases tree
    dataBaseTree = serializable.Read('./Data/', "Databases")
    # Get the dbNode
    databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database.upper())
    # If DB exist
    if databaseNode:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if tablesTree.search(tablesTree.getRoot(), table.upper()):
            table = serializable.Read(f'./Data/{database}/{table}/', table)
            tableList = list(table.lista().values())
            validList = []

            if columnNumber < 0 or columnNumber >= len(tableList):
                return None
            try:
                for i in tableList:
                    if type(i[columnNumber]) == str:
                        if str(i[columnNumber]) <= str(upper) and str(i[columnNumber]) >= str(lower):
                            validList.append(i)
                    elif type(i[columnNumber]) == float:
                        if float(i[columnNumber]) <= float(upper) and float(i[columnNumber]) >= float(lower):
                            validList.append(i)
                    elif type(i[columnNumber]) == int:
                        if int(i[columnNumber]) <= int(upper) and int(i[columnNumber]) >= int(lower):
                            validList.append(i)
                    elif type(i[columnNumber]) == bool:
                        if bool(i[columnNumber]) <= bool(upper) and bool(i[columnNumber]) >= bool(lower):
                            validList.append(i)
            except:
                return None
            return validList

        else:
            return None
    else:
        return None


# ---------------Dyllan--------------------#
# ---------------CRUD TUPLA----------------#
# ---------------Rudy----------------------#
# ---------------Marcos--------------------#
