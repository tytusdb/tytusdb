from storage.team07.storageBeans.TableHash import t


# funciones de bases de datos

def createDatabase(database):  # recibo el string con el nombre de  la base de datos
    try:
        if (t.search(database) is False):
            return 0  # la operación es exito
        else:
            return 2  # no realize nada porque la base de datos ya existe
    except:
        return 1  # error en la operación


def showDatabases():  # retornare una lista
    return t.getData()       # metodo que me retorna una lista con los nombres de las bases de datos


def alterDatabase(databaseOld, databaseNew):  # cambio de nombres en las bases de datos , (nodo en la table hash)
    print()

