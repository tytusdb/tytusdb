from storage.team07.storageBeans.TableHash import Hash

# funciones de bases de datos
t = Hash()  # hash para almacenar base de datos , estructura incial


# dabatase  functions , only name database
def createDatabase(database: str) -> int:  # recibo el string con el nombre de  la base de datos
    try:
        if type(database) is str:
            if (t.search(database) is False):
                t.insert(database)
                return 0  # la operación es exito
            else:
                return 2  # no realize nada porque la base de datos ya existe
        else:
            return 1  # error porque no es string
    except:
        return 1  # error en la operación


def showDatabases():  # retornare una lista
    return t.getData()  # metodo que me retorna una lista con los nombres de las bases de datos


def alterDatabase(databaseOld, databaseNew):  # cambio de nombres en las bases de datos , (nodo en la table hash)
    try:
        if t.search(databaseOld):  # chech if the old database exist
            if t.search(databaseNew):  # check if the new database doesn´t exist
                return 3  # new database exist , so is like an error
            else:  # if all is correct , change the name of database
                if t.updateName(databaseNew, databaseOld):
                    return 0  # succesfull
                else:
                    return 1  # error
        else:
            return 2  # database doesn´t exist
    except:
        return 2  # error


def dropDatabase(database):
    try:
        if t.search(database):  # means that the database exist
            t.delete(database)
            return 0  # succesfull operation delete
        else:  # database doesn´t exist
            return 2
    except:
        return 1  # error


# ----------------------------------------------------------

def createTable(database, table, numberColumns):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                return 3  # table exist
            else:
                data.BHash.insertTable(table, numberColumns)  # se inserto una nueva tabla
                return 0
        else:
            return 2  # database doesn´t exist
    except:
        return 1


def showTables(database):
    if t.search(database):
        data = t.getDataBase(database)  # get the database
        return data.BHash.getDataTables()  # return name of tables
    else:
        return None


def dropTable(database, table):
    try:
        if t.search(database):
            data = t.getDataBase(database)
            if data.BHash.searchTable(table):
                data.BHash.deleteTable(table)
                return 0
            else:
                return 3  # table doesn´t exist
        else:
            return 2  # database doesn´t exist
    except:
        return 1


def alterTable(database, tableOld, tableNew):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # get the database
            if data.BHash.searchTable(tableOld):  # table exist
                if data.BHash.searchTable(tableNew):  # new table exist
                    return 4
                else:
                    data.BHash.updateNameTable(tableNew, tableOld)  # all data is correct  -> change the name of table
                    return 0
            else:  # table doesn´t exist
                return 3
        else:
            return 2
    except:
        return 1


def insert(database, table, register):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree
                if len(register) == avl.noColumnas:  # la columna si existe
                    avl.agregar(register)  # inserto un nuevo registro
                    # avl.preorden()
                    return 0
                else:  # columnas fuera de limites
                    return 5
            else:
                return 3  # table doesn´t exist
        else:
            return 2  # database doesn´t exist
    except:
        return 1  # cualquier error


def alterAddPK(database, table, columns):  # retorna una lista
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree
                if avl.pk is None:
                    avl.pk = columns  # primary key sera una lista
                    # if avl.raiz is not None:
                    #     if len(columns) == avl.noColumnas:  # porque ya habia ingresado datos
                    #         avl.recalcularIndices()  # HACER ESTA FUNCION EN CASA
                    #         return 0
                    #     else:  # columnas fuera de limites
                    #         return 5
                    return 0
                else:  # error ya tenia pk
                    return 4
            else:
                return 3  # table doesn´t exist
        else:
            return 2  # database doesn´t exist
    except:
        return 1  # cualquier error


def extractTable(database, table):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree  # obtengo el arbol que contiene las tuplas
                return avl.getTuplas()  # obtengo todas las tuplas registradas
            else:
                return None  # table doesn´t exist
        else:
            return None  # database doesn´t exist
    except:
        return None


def truncate(database, table):
    from storage.team07.storageBeans.AVLtree import arbolAVL
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree
                noColumnas = avl.noColumnas
                tabla.AVLtree = None
                tabla.AVLtree = arbolAVL(noColumnas)  # un nuevo arbol en la tabla, que esta vacio
                return 0
            else:
                return 3  # table doesn´t exist
        else:
            return 2  # database doesn´t exist
    except:
        return 1  # cualquier error


# hasta estas funciones interfaz


def alterDropPK(database, table):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree
                if avl.pk is None:
                    return 4  # pk no existia
                else:  # si existe pk
                    avl.pk = None
                    return 0
            else:
                return 3  # table doesn´t exist
        else:
            return 2  # database doesn´t exist
    except:
        return 1  # cualquier error


def alterAddColumn(database, table, default):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree
                avl.noColumnas += 1
                avl.addNewColumna(default)  # default , es el nuevo valor que todos tendran en sus tuplas
                return 0
            else:
                return 3  # table doesn´t exist
        else:
            return 2  # database doesn´t exist
    except:
        return 1  # cualquier error


def alterDropColumn(database, table, columnNumber):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree
                if 0 <= columnNumber < avl.noColumnas:  # la columna si existe
                    if avl.noColumnas > 1:
                        if avl.pk is not None:
                            for i in avl.pk:
                                if i == columnNumber:  # significa que esta tratando de eliminar una columna que es pk
                                    return 4
                        # significa que no hay conflictos
                        avl.eliminarColumna(columnNumber)
                        return 0
                    else:
                        return 4  # error porque se quedara sin columnas
                else:  # columnas fuera de limites
                    return 5
            else:
                return 3  # table doesn´t exist
        else:
            return 2  # database doesn´t exist
    except:
        return 1  # cualquier error


# hasta aqui puedo mandar a llamar , a la interfaz

def loadCSV(file, database, table):
    lista = []
    try:
        archivo = open(file, "r")
        contador = 0
        for linea in archivo.readlines():
            linea.split(sep=',')
            lineaCompleta = ""
            i = 0
            for _ in linea:
                if i > 1:
                    lineaCompleta += str(linea[i])
                i += 1
            lista.append(insert(database, table, lineaCompleta))
            contador += 1
        archivo.close()
        if contador > 0:
            return lista
        else:
            lista = []
            return lista
    except:
        lista = []
        return lista


def extractRow(database, table, columns):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree
                if avl.search(columns):  # significa que existe el registro
                    return avl.getRegistro(columns)  # el metodo se ejecuto con exito
                else:
                    lista = []
                    return lista
            else:
                lista = []
                return lista  # table doesn´t exist
        else:
            lista = []
            return lista  # database doesn´t exist
    except:
        lista = []
        return lista  # cualquier error


def update(database, table, register, columns):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree

                if avl.search(columns):  # si existe el registro entonces , hago el update
                    listaUpdate = []
                    for i in range(avl.noColumnas):
                        listaUpdate.append(None)
                    for clave in register:  # recorro el diccionario enviado
                        valor = register[clave]
                        id_clave = int(clave)
                        listaUpdate[id_clave] = valor
                    avl.updateTupla(listaUpdate)
                    return 0
                else:  # no existe el registro , la llave que se envio no existe
                    return 4
            else:
                return 3  # table doesn´t exist
        else:
            return 2  # database doesn´t exist
    except:
        return 1  # cualquier error


def delete(database, table, columns):
    try:
        if t.search(database):
            data = t.getDataBase(database)  # obtengo la base de datos
            if data.BHash.searchTable(table):
                tabla = data.BHash.getTable(table)  # obtengo la tabla
                avl = tabla.AVLtree

                if avl.search(columns):  # si existe el registro entonces , hago el update
                    avl.eliminarTupla(columns)
                    return 0
                else:  # no existe el registro , la llave que se envio no existe
                    return 4
            else:
                return 3  # table doesn´t exist
        else:
            return 2  # database doesn´t exist
    except:
        return 1  # cualquier error


