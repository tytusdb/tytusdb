from storage.b import BMode as b_mode
from storage.bplus import BPlusMode as bplus_mode
from storage.isam import ISAMMode as isam_mode
from storage.hash import HashMode as hash_mode
from storage.avl import AVLMode as avl_mode
from storage.dict import DictMode as dict_mode
from storage.json import jsonMode as json_mode
import hashlib
import zlib
import pickle
# AVL: AVLMode
# B: BMode
# B+: BPlusMode
# ISAM: ISAMMode
# TablasHash: HashMode

Bases = {}
Tablas = {}

def createDatabase(database, mode, encoding):
    val = 1
    if encoding != "ascii" and encoding != "iso-8859-1" and encoding != "utf8":
        val = 4
    else:
        if mode == "avl":
            # Grupo 16
            val = avl_mode.createDatabase(database)
        elif mode == "b":
            # Grupo 17
            val = b_mode.createDatabase(database)
        elif mode == "bplus":
            # Grupo 18
            val = bplus_mode.createDatabase(database)
        elif mode == "dict":
            # Auxiliar
            val = dict_mode.createDatabase(database)
        elif mode == "isam":
            # Grupo 14
            val = isam_mode.createDatabase(database)
        elif mode == "json":
            # Ingeniero
            val = json_mode.createDatabase(database)
        elif mode == "hash":
            # Grupo 15
            val = hash_mode.createDatabase(database)
        else:
            val = 3
        if val == 0:
            global Bases
            try:
                # Leemos el archivo binario de los registros de bases de datos
                fichero_lectura = open("BD_register", "rb")
                Bases = pickle.load(fichero_lectura)
                Bases.update({database: {"mode": mode, "encoding": encoding}})
                # Actualizamos el archivo binario de los registros de bases de datos
                fichero_escritura = open("BD_register", "wb")
                pickle.dump(Bases, fichero_escritura)
                fichero_escritura.close()
            except:
                Bases.update({database: {"mode": mode, "encoding": encoding}})
                # Actualizamos el archivo binario de los registros de bases de datos
                fichero_escritura = open("BD_register", "wb")
                pickle.dump(Bases, fichero_escritura)
                fichero_escritura.close()
    return val

def dropDatabase(database):
    mode = None
    for i in range(7):
        mode = obtenerBase(database,i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.dropDatabase(database)
    elif mode == "b":
        # Grupo 17
        val = b_mode.dropDatabase(database)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.dropDatabase(database)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.dropDatabase(database)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.dropDatabase(database)
    elif mode == "json":
        # Ingeniero
        val = json_mode.dropDatabase(database)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.dropDatabase(database)
    else:
        val = 3
    if val == 0:
        global Bases
        global Tablas
        try:
            # Leemos el archivo binario de los registros de bases de datos
            fichero_lectura = open("BD_register", "rb")
            Bases = pickle.load(fichero_lectura)
            Bases.pop(database)
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("BD_register", "wb")
            pickle.dump(Bases, fichero_escritura)
            fichero_escritura.close()
            try:
                # Leemos el archivo binario de los registros de tablas
                fichero_lectura = open("TB_register", "rb")
                Tablas = pickle.load(fichero_lectura)
                try:
                    Tablas.pop(database)
                except:
                    """"""
                # Actualizamos el archivo binario de los registros de tablas
                fichero_escritura = open("TB_register", "wb")
                pickle.dump(Tablas, fichero_escritura)
                fichero_escritura.close()
            except:
                try:
                    Tablas.pop(database)
                except:
                    """"""
                # Actualizamos el archivo binario de los registros de tablas
                fichero_escritura = open("TB_register", "wb")
                pickle.dump(Tablas, fichero_escritura)
                fichero_escritura.close()
        except:
            Bases.pop(database)
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("BD_register", "wb")
            pickle.dump(Bases, fichero_escritura)
            fichero_escritura.close()
            try:
                # Leemos el archivo binario de los registros de tablas
                fichero_lectura = open("TB_register", "rb")
                Tablas = pickle.load(fichero_lectura)
                try:
                    Tablas.pop(database)
                except:
                    """"""
                # Actualizamos el archivo binario de los registros de tablas
                fichero_escritura = open("TB_register", "wb")
                pickle.dump(Tablas, fichero_escritura)
                fichero_escritura.close()
            except:
                try:
                    Tablas.pop(database)
                except:
                    """"""
                # Actualizamos el archivo binario de los registros de tablas
                fichero_escritura = open("TB_register", "wb")
                pickle.dump(Tablas, fichero_escritura)
                fichero_escritura.close()
    return val

def extractTable(database, table):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.extractTable(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.extractTable(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.extractTable(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.extractTable(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.extractTable(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.extractTable(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.extractTable(database, table)
    else:
        val = 3
    return val

def truncate(database, table):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.truncate(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.truncate(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.truncate(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.truncate(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.truncate(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.truncate(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.truncate(database, table)
    else:
        val = 3
    return val

def insert(database, table, register):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.insert(database, table, register)
    elif mode == "b":
        # Grupo 17
        val = b_mode.insert(database, table, register)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.insert(database, table, register)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.insert(database, table, register)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.insert(database, table, register)
    elif mode == "json":
        # Ingeniero
        val = json_mode.insert(database, table, register)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.insert(database, table, register)
    else:
        val = 3
    return val

def alterDatabaseMode(database, mode):
    diccionario = {"avl":0, "b":1, "bplus":2, "dict":3, "isam":4, "json":5, "hash":6}
    if mode in diccionario:
        modo_anterior = None
        for i in diccionario:
            modo_anterior = obtenerBase(database, diccionario[i])
            if modo_anterior != []:
                break
        if modo_anterior == []:
            return 2
        else:
            modo_actual = diccionario[mode]
            if modo_anterior == modo_actual:
                return 1
            else:
                temp_tablas = obtenerTablas(database, modo_anterior)
                temp_fila_tabla = []
                for tabla in temp_tablas:
                    temp_fila_tabla.append([tabla, extractTable(database, tabla)])
                dropDatabase(database)
                createDatabase(database, mode, "utf8")
                for dato in temp_fila_tabla:
                    nombre_tabla = dato[0]
                    registros = dato[1]
                    if registros != []:
                        createTable(database, nombre_tabla, len(registros[0]))
                    for registro in registros:
                        insert(database, nombre_tabla, registro)
                return 0
    else:
        return 4

# Cambia el modo de almacenamiento de una tabla de una base de datos especificada. (UPDATE)
# Parámetro database: es el nombre de la base de datos a utilizar.
# Parámetro mode: es un string indicando el modo 'avl', 'b', 'bplus', 'dict', 
# 'isam', 'json', 'hash'.
# Valor de retorno: 0 operación exitosa, 1 error en la operación, 
# 2 database no existente, 3 table no existente, 4 modo incorrecto.
def alterTableMode(database, table, mode):
    print("alterTableMode")

def obtenerAtributosTabla(database, table):
    mode = None
    for i in range(7):
        mode = obtenerBase(database,i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.dropTable(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.dropTable(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.dropTable(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.dropTable(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.dropTable(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.dropTable(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.dropTable(database, table)
    else:
        val = 3
    return val

def createTable(database, table, numColumns):
    mode = None
    for i in range(7):
        mode = obtenerBase(database,i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.createTable(database, table, numColumns)
    elif mode == "b":
        # Grupo 17
        val = b_mode.createTable(database, table, numColumns)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.createTable(database, table, numColumns)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.createTable(database, table, numColumns)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.createTable(database, table, numColumns)
    elif mode == "json":
        # Ingeniero
        val = json_mode.createTable(database, table, numColumns)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.createTable(database, table, numColumns)
    else:
        val = 3
    if val == 0:
        global Tablas
        try:
            # Leemos el archivo binario de los registros de bases de datos
            lectura = open("TB_register", "rb")
            Tablas = pickle.load(lectura)
            try:
                Tablas[database].update({table: {"PK": None, "FK": None}})
            except:
                Tablas.update({database:{table: {"PK": None, "FK": None}}})
            # Actualizamos el archivo binario de los registros de bases de datos
            escritura = open("TB_register", "wb")
            pickle.dump(Tablas, escritura)
            escritura.close()
        except:
            try:
                Tablas[database].update({table: {"PK": None, "FK": None}})
            except:
                Tablas.update({database: {table: {"PK": None, "FK": None}}})
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
    return val

def dropTable(database, table):
    mode = None
    for i in range(7):
        mode = obtenerBase(database,i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.dropTable(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.dropTable(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.dropTable(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.dropTable(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.dropTable(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.dropTable(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.dropTable(database, table)
    else:
        val = 3
    if val == 0:
        global Tablas
        try:
            # Leemos el archivo binario de los registros de bases de datos
            fichero_lectura = open("TB_register", "rb")
            Tablas = pickle.load(fichero_lectura)
            Tablas[database].pop(table)
            if len(Tablas[database])==0:
                Tablas.pop(database)
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
        except:
            Tablas[database].pop(table)
            if len(Tablas[database])==0:
                Tablas.pop(database)
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
    return val

def loadCSV(file,database,table):
    mode = None
    for i in range(7):
        mode = obtenerBase(database,i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.loadCSV(file, database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.loadCSV(file, database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.loadCSV(file, database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.loadCSV(file, database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.loadCSV(file, database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.loadCSV(file, database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.loadCSV(file, database, table)
    else:
        val = 3
    return val

def checksumDatabase(database, mode):
    import hashlib
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if mode.lower() == "sha256":
                hash = hashlib.sha256()
            elif mode.lower() == "md5":
                hash = hashlib.md5()
            else:
                return None
            try:
                hash.update(database.encode("UTF-8"))
            except:
                return None
            break
    tables = obtenerTablas(database, var)
    try:
        if tables == []:
            return None
        else:
            contenido = ""
            for i in range(len(tables)):
                contenidoTabla = obtenerContenidoTabla(database, tables[i], var)
                hash.update(tables[i].encode("UTF-8"))
                contenido += contenidoTabla
            contenido = contenido.replace("[", "").replace("]", "").replace("'", "").replace(" ", "").replace(",", "")
        hash.update(contenido.encode("UTF-8"))
    except:
        return None
    return hash.hexdigest()

def showDatabases():
    print("AVL")
    print(avl_mode.showDatabases())
    print("b")
    print(b_mode.showDatabases())
    print("b+")
    print(bplus_mode.showDatabases())
    print("dict")
    print(dict_mode.showDatabases())
    print("isam")
    print(isam_mode.showDatabases())
    print("json")
    print(json_mode.showDatabases())
    print("hash")
    print(hash_mode.showDatabases())

def showTables():
    val = dict_mode.showTables("Base1AVL")
    print(val)

def obtenerBase(database,estructura):
    val = []
    if estructura == 0:
        val = avl_mode.showDatabases()
    elif estructura == 1:
        val = b_mode.showDatabases()
    elif estructura == 2:
        val = bplus_mode.showDatabases()
    elif estructura == 3:
        val = dict_mode.showDatabases()
    elif estructura == 4:
        val = isam_mode.showDatabases()
    elif estructura == 5:
        val = json_mode.showDatabases()
    elif estructura == 6:
        val = hash_mode.showDatabases()
    if val == []:
        return val
    else:
        for i in range(len(val)):
            if val[i].lower()==database.lower():
                return estructura
    return []

def obtenerContenidoTabla(database, table, estructura):
    val = []
    if estructura == 0:
        val = avl_mode.extractTable(database,table)
    elif estructura == 1:
        val = b_mode.extractTable(database,table)
    elif estructura == 2:
        val = bplus_mode.extractTable(database,table)
    elif estructura == 3:
        val = dict_mode.extractTable(database,table)
    elif estructura == 4:
        val = isam_mode.extractTable(database,table.lower())
    elif estructura == 5:
        val = json_mode.extractTable(database,table)
    elif estructura == 6:
        val = hash_mode.extractTable(database,table)
    if val == []:
        return ""
    contenido = ""
    for i in range(len(val)):
        contenido+=str(val[i])
    return contenido

def obtenerTablas(database, estructura):
    val = []
    if estructura == 0:
        val = avl_mode.showTables(database)
    elif estructura == 1:
        val = b_mode.showTables(database)
    elif estructura == 2:
        val = bplus_mode.showTables(database)
    elif estructura == 3:
        val = dict_mode.showTables(database)
    elif estructura == 4:
        val = isam_mode.showTables(database)
    elif estructura == 5:
        val = json_mode.showTables(database)
    elif estructura == 6:
        val = hash_mode.showTables(database)
    return val

def checksumTable(database, table, mode):
    import hashlib
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if mode.lower() == "sha256":
                hash = hashlib.sha256()
            elif mode.lower() == "md5":
                hash = hashlib.md5()
            else:
                return None
            break
    try:
        contenido = ""
        contenidoTabla = obtenerContenidoTabla(database, table, var)
        hash.update(table.encode("UTF-8"))
        contenido += contenidoTabla
        contenido = contenido.replace("[", "").replace("]", "").replace("'", "").replace(" ", "").replace(",", "")
        hash.update(contenido.encode("UTF-8"))
    except:
        return None
    return hash.hexdigest()

def alterDatabaseCompress(database, level):
    if level < 0 or level > 9:
        return 4
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if var >= 0 and var <= 6:
                break
            else:
                return 3
    tables = obtenerTablas(database, var)
    if tables == []:
        return None
    else:
        try:
            for i in range(len(tables)):
                contenidoTabla = extractTable(database, tables[i])
                #print(contenidoTabla)
                for j in range(len(contenidoTabla)):
                    tupla = contenidoTabla[j]
                    for k in range(len(tupla)):
                        if type(tupla[k]) == str:
                            tupla[k] = zlib.compress(tupla[k].encode(), level)
                    contenidoTabla[j] = tupla
                truncate(database, tables[i])
                for registro in contenidoTabla:
                    insert(database, tables[i], registro)
            return 0
        except:
            return 1

def alterDatabaseDecompress(database):
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if var >= 0 and var <= 6:
                break
            else:
                return 3
    tables = obtenerTablas(database, var)
    if tables == []:
        return None
    else:
        try:
            comprimido = False
            for i in range(len(tables)):
                contenidoTabla = extractTable(database, tables[i])
                for j in range(len(contenidoTabla)):
                    tupla = contenidoTabla[j]
                    for k in range(len(tupla)):
                        if type(tupla[k]) == str or type(tupla[k]) == int or type(tupla[k]) == float or type(tupla[k]) == bool:
                            continue
                        else:
                            valor = zlib.decompress(tupla[k])
                            tupla[k] = valor.decode()
                            comprimido = True
                    contenidoTabla[j] = tupla
                if comprimido == True:
                    truncate(database, tables[i])
                    for registro in contenidoTabla:
                        insert(database, tables[i], registro)
                else:
                    return 3
            return 0
        except:
            return 1

def alterTableCompress(database, table, level):
    if level < 0 or level > 9:
        return 4
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if var >= 0 and var <= 6:
                break
            else:
                return 3
    tabla = extractTable(database,table)
    if tabla == 3:
        return None
    else:
        try:
            for i in range(len(tabla)):
                tupla = tabla[i]
                for j in range(len(tupla)):
                    if type(tupla[j]) == str:
                        tupla[j] = zlib.compress(tupla[j].encode(), level)
                tabla[i] = tupla
            truncate(database, table)
            for registro in tabla:
                insert(database, table, registro)
            return 0
        except:
            return 1

def alterTableDecompress(database, table):
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if var >= 0 and var <= 6:
                break
            else:
                return 3
    tabla = extractTable(database,table)
    if tabla == []:
        return None
    else:
        comprimido = False
        try:
            for i in range(len(tabla)):
                tupla = tabla[i]
                for j in range(len(tupla)):
                    if type(tupla[j]) == str or type(tupla[j]) == int or type(tupla[j]) == float or type(tupla[j]) == bool:
                        continue
                    else:
                        valor = zlib.decompress(tupla[j])
                        tupla[j] = valor.decode()
                        comprimido = True
                tabla[i] = tupla
            if comprimido == True:
                truncate(database, table)
                for registro in tabla:
                    insert(database, table, registro)
                return 0
            else:
                return 3
        except:
            return 1

