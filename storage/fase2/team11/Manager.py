from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bPlus
from storage.dict import DictMode as diccionario
from storage.isam import ISAMMode as isam
from storage.hash import HashMode as hash
from storage.json import jsonMode as json
from Binary import verify_string, generate_grapviz
from checksum import checksum_database, checksum_table
import criptografia as crypt
from blockChain import BlockChain
from metadata import Database, Table, FK
from grafo import Graph
import zlib
import os.path as path
from shutil import rmtree
import copy

metadata_db_list = list()
flag_block = False
block_list = list()

mode_dict = {'avl': 1, 'b': 2, 'bplus': 3, 'dict': 4, 'hash': 5, 'isam': 6, 'json': 7}


def save_database_db(database, mode, encondig):
    new_mode = Database(database, mode, encondig)
    metadata_db_list.append(new_mode)


def get_metadata_db(database: str):
    index = 0
    for db in metadata_db_list:
        if db.get_name_database() == database:
            return db, index
        index += 1
    return None, None


def get_metadata_dbmode(database: str, mode: str):
    for db in metadata_db_list:
        if db.get_name_database() == database and db.get_mode() == mode:
            return db
    return None


# -------------------------------------------- --> Get Struct <-- ----------------------------------------------------
# Metodo que retorna la estructura correspondiente al modo
def get_struct(mode: str):
    if mode.lower().strip() == "avl":
        return avl
    elif mode.lower().strip() == "b":
        return b
    elif mode.lower().strip() == "bplus":
        return bPlus
    elif mode.lower().strip() == "dict":
        return diccionario
    elif mode.lower().strip() == "hash":
        return hash
    elif mode.lower().strip() == "isam":
        return isam
    elif mode.lower().strip() == "json":
        return json


# -------------------------------------------- --> <-> <-- -----------------------------------------------------------

def createDatabase(database: str, mode: str, encoding: str):
    if verify_string(database):  # Metodo que verifica el nombre si cumple con las condiciones
        metadata, index = get_metadata_db(database)
        if metadata: return 2  # Verifica que no haya repetidos en el listado de metadata database
        if str(encoding.lower().strip()) == "ascii" or str(encoding.lower().strip()) == "iso-8859-1" \
                or str(encoding.lower().strip()) == "utf8":  # Revisa que cumpla con la codificacion
            if mode_dict.get(mode) is None: return 3  # Revisa que el modo este en el diccionario  si no esta retorno 3
            mode_struct = get_struct(mode)  # Retorna el objeto avl,b,bplus, etc dependiendo el modo
            status = mode_struct.createDatabase(database)  # Crea base de datos de la estructura correspondiente(avl,b)
            if status == 0:  # Si el estatus es el correcto guarda en la lista metadata_db_list
                save_database_db(database, mode.lower().strip(), encoding)  # Guarda en la lista metada_db_list
            return status
        else:
            return 4
    else:
        return 1




def alterDatabaseMode(database: str, mode: str):
    metadata_db, index = get_metadata_db(database)
    metadata_db=copy.copy(metadata_db)
    metadata_db_list.pop(index)
    
    
    if metadata_db:
        oldMode = metadata_db.get_mode()
        old_mode_struct = get_struct(oldMode)
        mode_struct = get_struct(mode)

        if mode not in ["avl", "b", "bplus", "isam", "hash", "json", "dict"]:
            return 4

        tables=list()
        for value in metadata_db.get_tab().values():
            
            tables.append(value.get_name_table())

        createDatabase(database, mode, metadata_db.get_encondig())
        metadata_new, index2 = get_metadata_db(database)        
        
        for tabla in tables:
            
            listaDatos = get_Data2(database, tabla, oldMode,metadata_db)
            numberColumns = metadata_db.get_table(tabla).get_nums_colums()
            insertAlter(database, tabla, numberColumns, mode, listaDatos)
            metadata_new.create_table(tabla,numberColumns,mode)             
            
             
            for fk in metadata_db.get_table(tabla).fk.extractForeign():     
                metadata_new.get_table(tabla).fk.insertFK(fk)
            for unique in metadata_db.get_table(tabla).unique.extractUnique():     
                metadata_new.get_table(tabla).unique.insertUnique(unique)
            for index in metadata_db.get_table(tabla).index.extractIndex():     
                metadata_new.get_table(tabla).index.insertIndex(index)

            metadata_db.drop_table(tabla)
            

        x = old_mode_struct.dropDatabase(database)
        if x != 0:
            return 1
        return 0
    else:
        return 2
        


def insertAlter(database, tabla, numberColumns, mode, listaDatos):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())        
        struct.createTable(database, tabla, numberColumns)
        for data in listaDatos:
            struct.insert(database, tabla, data)


def get_Data(database: str, table: str, mode: str):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())         
        return struct.extractTable(database, table)

def get_Data2(database: str, table: str, mode: str, metadata_db):
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        return struct.extractTable(database, table)


def alterTableMode(database: str, table: str, mode: str):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        oldMode = metadata_db.get_mode()
        encoding = metadata_db.get_encondig()
        if mode not in ["avl", "b", "bplus", "dict", "isam", "hash", "json"]: return 4
        struct = get_struct(metadata_db.get_mode())        
        if metadata_db.get_table(table):
            listaDatos = get_Data(database, table, oldMode)            
            numberColumns = metadata_db.get_table(table).get_nums_colums()            
            if metadata_db.get_table(table).get_pk_list() != []:
                alterAddPK(database, table, metadata_db.get_table(table).get_pk_list())
            createDatabase(database + "_" + mode, mode, encoding)
            metadata_new, index2 = get_metadata_db(database + "_" + mode) 
            createTable(database + "_" + mode, table, numberColumns)
            for i in listaDatos:
                insert(database, table, i)
            
            for fk in metadata_db.get_table(table).fk.extractForeign():     
                metadata_new.get_table(table).fk.insertFK(fk)
            for unique in metadata_db.get_table(table).unique.extractUnique():     
                metadata_new.get_table(table).unique.insertUnique(unique)
            for index in metadata_db.get_table(table).index.extractIndex():     
                metadata_new.get_table(table).index.insertIndex(index)
            struct.dropTable(database, table)
            metadata_db.drop_table(table)

            return 0
        return 3
    else:
        return 2



def alterDatabase(old_db, new_db):
    metadata_db, index_md_db = get_metadata_db(old_db)
    metadata_db_new, index_new_md_db = get_metadata_db(new_db)
    if metadata_db and metadata_db_new is None:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterDatabase(old_db, new_db)
        if status == 0:
            metadata_db.set_name_database(new_db)
        return status
    return 1




def dropDatabase(name_db):
    metadata_db, index_metadata = get_metadata_db(name_db)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.dropDatabase(name_db)
        if status == 0:
            metadata_db_list.pop(index_metadata)
        return status
    else:
        return 2




def createTable(database, name_table, number_columns):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.createTable(database, name_table, number_columns)
        if status == 0:
            metadata_db.create_table(name_table, number_columns, metadata_db.get_mode())
        return status
    else:
        return 2


def showTables(database):
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.showTables(database)
        return status
    return None


def extractTable(database, name_table):
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.extractTable(database, name_table)
        return status
    return None


def extractRangeTable(database, name_table, number_column, lower, upper):
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.extractRangeTable(database, name_table, number_column, lower, upper)
        return status
    return None


def alterAddPK(database, name_table, columns):
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterAddPK(database, name_table, columns)
        if status == 0:
            tabla: Table = metadata_db.get_table(name_table)
            tabla.add_pk_list(columns)
        return status
    return 2


def alterDropPK(database, name_table):
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterDropPK(database, name_table)
        if status == 0:
            tabla: Table = metadata_db.get_table(name_table)
            tabla.add_pk_list([])
        return status
    return 2


def alterTable(database, old_table, new_table):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterTable(database, old_table, new_table)
        if status==0:
            metadata_db.get_table(old_table).fk.alterForeign(new_table)
            metadata_db.alter_table(old_table,new_table)
            
        return status
    else: return 2

def alterAddColumn(database, name_table, default):
    metadata_db, index_metadata = get_metadata_db(database)  
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterAddColumn(database, name_table, default)
        if status==0:
            x = metadata_db.get_table(name_table)
            x.set_nums_colums(x.get_nums_colums()+1)
        return status
    else:
        return 2

def alterDropColumn(database, name_table, number_column): 
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterDropColumn(database, name_table, number_column)
        if status==0:
            x = metadata_db.get_table(name_table)
            x.set_nums_colums(x.get_nums_colums()-1)
        return status
    else:
        return 2

def dropTable(database, name_table):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.dropTable(database, name_table)
        if status==0:
            metadata_db.get_table(name_table).fk.dropForeign()
            metadata_db.drop_table(name_table)
                  
        return status
    else: 
        return 2

def insert(database, name_table, register: list):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        if name_table in metadata_db.get_tab():
            struct = get_struct(metadata_db.get_mode())
            if metadata_db.get_encondig().lower().strip() == "ascii":
                if encodi_ascii_decod(register, "ascii") != 1:
                    status = struct.insert(database, name_table, register)
                    if status == 0:
                        if flag_block:
                            block: BlockChain = get_block_chain(name_table)
                            if block:
                                block.create_block(register)
                                gra = block.graficar()
                                ruta = f"bc_insert_{database}"
                                generate_grapviz(gra, str(ruta))
                    return status
                else:
                    return 1
            elif metadata_db.get_encondig().lower().strip() == "utf8":
                if encodi_utf_decod(register, "utf8") != 1:
                    status = struct.insert(database, name_table, register)
                    if status == 0:
                        if flag_block:
                            block: BlockChain = get_block_chain(name_table)
                            if block:
                                block.create_block(register)
                                gra = block.graficar()
                                ruta = f"bc_insert_{database}"
                                generate_grapviz(gra, str(ruta))
                    return status
                else:
                    return 1
            elif metadata_db.get_encondig().lower().strip() == "iso-8859-1":
                if encodi_iso_decod(register, "iso-8859-1") != 1:
                    status = struct.insert(database, name_table, register)
                    if status == 0:
                        if flag_block:
                            block: BlockChain = get_block_chain(name_table)
                            if block:
                                block.create_block(register)
                                gra = block.graficar()
                                ruta = f"bc_insert_{database}"
                                generate_grapviz(gra, str(ruta))
                    return status
                else:
                    return 1
            else:
                None
        else:
            return 3
    else:
        return 2

#-------------------ENCODING--------------------------------
def alterDatabaseEncoding(database: str, encoding: str):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        tables = struct.showTables(database)
        state = 0
        if encoding not in ["ascii","utf-8","iso-8859-1"]: return 3
        for e in tables:
            tuplas = struct.extractTable(database,e)
            for n in tuplas:
                if encoding == "ascii" and encodi_ascii_decod(n,encoding) !=1:
                    pass
                elif encoding == "utf-8" and encodi_utf_decod(n,encoding) !=1:
                    pass
                elif encoding == "iso-8859-1" and encodi_iso_decod(n,encoding) !=1:
                    pass
                else:
                    return 1
        if state == 0:
             metadata_db.set_encondig(encoding)
             return 0
    else:
        return 2



def encodi_ascii_decod(lista: list ,encoding: str):
    try:
        for i in lista:
            str(i).encode(f'{encoding}').decode(f'{encoding}')
        return 0
    except:
        return 1

def encodi_utf_decod(lista: list ,encoding: str):
    try:
        for i in lista:
            str(i).encode('utf-8').decode('utf-8')
        return 0
    except:
        return 1

def encodi_iso_decod(lista: list ,encoding: str):
    try:
        for i in lista:
            str(i).encode('iso-8859-1').decode('iso-8859-1')
        return lista
    except:
        return 1


def extractRow(database, name_table, columns):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.extractRow(database, name_table, columns)       
        return status
    else: return []


def update(database, name_table, register: dict, columns):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        if name_table in metadata_db.get_tab():
            struct = get_struct(metadata_db.get_mode())
            if metadata_db.get_encondig().lower().strip() == "ascii":
                if encodi_ascii_decod(register.values(), "ascii") != 1:
                    data = struct.extractRow(database, name_table, columns).copy()
                    status = struct.update(database, name_table, register, columns)
                    if status == 0:
                        if flag_block:
                            block: BlockChain = get_block_chain(name_table)
                            id_block = block.get_block(data)
                            if block and id_block:
                                block.update(register, id_block)
                                # block.graficar()
                                gra = block.graficar()
                                ruta = f"bc_update_{database}"
                                generate_grapviz(gra, str(ruta))

                    return status
                else:
                    return 1
            elif metadata_db.get_encondig().lower().strip() == "utf8":
                if encodi_utf_decod(register.values(), "utf8") != 1:
                    data = struct.extractRow(database, name_table, columns).copy()
                    status = struct.update(database, name_table, register, columns)
                    if status == 0:
                        if flag_block:
                            block: BlockChain = get_block_chain(name_table)
                            id_block = block.get_block(data)
                            if block and id_block:
                                block.update(register, id_block)
                                # block.graficar()
                                gra = block.graficar()
                                ruta = f"bc_update_{database}"
                                generate_grapviz(gra, str(ruta))
                    return status
                else:
                    return 1
            elif metadata_db.get_encondig().lower().strip() == "iso-8859-1":
                if encodi_iso_decod(register.values(), "iso-8859-1") != 1:
                    data = struct.extractRow(database, name_table, columns).copy()
                    status = struct.update(database, name_table, register, columns)
                    if status == 0:
                        if flag_block:
                            block: BlockChain = get_block_chain(name_table)
                            id_block = block.get_block(data)
                            if block and id_block:
                                block.update(register, id_block)
                                # block.graficar()
                                gra = block.graficar()
                                ruta = f"bc_update_{database}"
                                generate_grapviz(gra, str(ruta))
                    return status
                else:
                    return 1
            else:
                return 1
        else:
            return 3
    else:
        return 2


def loadCSV(file, database, name_table):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.loadCSV(file, database, name_table)
        return status
    else: return []


def delete(database, name_table, columns):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        data = struct.extractRow(database, name_table, columns).copy()
        status = struct.delete(database, name_table, columns)
        if status == 0:
            if flag_block:
                block: BlockChain = get_block_chain(name_table)
                id_block = block.get_block(data)
                if block and id_block:
                    block.delete_block(id_block)
                    # block.graficar()
                    gra = block.graficar()
                    ruta = f"bc_delete_{database}"
                    generate_grapviz(gra, str(ruta))
        return status
    else:
        return 2


def truncate(database, name_table):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.truncate(database, name_table)
        return status
    else: return 2



#  ------------------------------------------ -> Methods checksum <- -----------------------------------------------

def checksumDatabase(database, mode: str):
    objet_mode, index = get_metadata_db(database)
    if objet_mode is None: return None
    mode_db = objet_mode.get_mode()
    struct = get_struct(mode_db)
    # sha256 -> 1
    # md5 -> 2
    if mode.lower().strip() == "sha256" or mode.lower().strip() == "md5":
        data = ""
        if mode_db != "b":
            data = struct.showTables(database)
        else:
            data = list()
            for tables in struct.showTables(database):
                data.append(struct.extractTable(database, tables))

        return checksum_database(1 if mode.lower().strip() == "sha256" else 2, database, mode_db, data)
    else:
        return None


def checksumTable(database, table: str, mode: str):
    object_mode, index = get_metadata_db(database)
    if object_mode:
        mode_db = object_mode.get_mode()
        struct = get_struct(mode_db)
        if mode.lower().strip() == "sha256" or mode.lower().strip() == "md5":
            data = ""
            if table in struct.showTables(database):
                if mode_db != "b":
                    data = table
                else:
                    data = struct.extractTable(database, table)
            else:
                return None
            return checksum_table(1 if mode.lower().strip() == "sha256" else 2, database, mode_db, data)
        else:
            return None

    else:
        return None


# ------------------------------------ --> Methods  Cryptography <-- ----------------------------------------------
def encrypt(backup: str, password: str):
    return crypt.encrypt(backup, password)


def decrypt(cipherBackup: str, password: str):
    return crypt.decrypt(cipherBackup, password)


# ------------------------------------- --> Methods  BlockChain <-- ----------------------------------------------
def get_block_chain(table: str):
    for block in block_list:
        if table.strip() == block.get_name_table():
            return block
    return None


# Preguntar el que hizo el drop database si lo elimino de la lista de Mode
def safeModeOn(database: str, table: str):
    global flag_block
    metadata_db, index = get_metadata_db(database)
    blockchain: BlockChain = get_block_chain(table)
    if blockchain: return 4
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        if table in struct.showTables(database):
            new_block = BlockChain(table)
            block_list.append(new_block)
            flag_block = not flag_block
            return 0
        else:
            return 3
    else:
        return 2


def safeModeOff(database: str, table: str):
    global flag_block
    blockchain: BlockChain = get_block_chain(table)
    objet_mode, index = get_metadata_db(database)
    if blockchain is None: return 4
    if objet_mode and blockchain:
        struct = get_struct(objet_mode.get_mode())
        if table in struct.showTables(database):
            status = blockchain.delete_json()
            block_list.remove(blockchain)
            flag_block = not flag_block
            return status
        else:
            return 3

    else:
        return 2

#  ----------------------------------------------- -->  <-> <-- -------------------------------------------------------

#-------------------------------------------------------------


def alterDatabaseCompress( database: str, level: int):
    if verify_string(database):
        metadata_db, index_md_db = get_metadata_db(database)
        if metadata_db:
            if (level >= -1) and (level <= 9):
                lista_tablas = showTables(database)
                bandera = False
                for tabla in lista_tablas:
                    tabla_metadatos = metadata_db.get_table(tabla)
                    if tabla_metadatos:
                        if not tabla_metadatos.get_compress():
                            registros = extractTable(database,tabla)
                            if registros:
                                truncate(database, tabla)
                            for tupla in registros:
                                lista_comprimida = []
                                bandera = True
                                for columna in tupla:
                                    if type(columna) == str:
                                        col_compress = zlib.compress(columna.encode("utf-8"), level)
                                        lista_comprimida.append(col_compress)
                                    else:
                                        lista_comprimida.append(columna)
                                try:
                                    insert(database,tabla,lista_comprimida)
                                except:
                                    return 1
                            tabla_metadatos.set_compress(True)
                if bandera:
                    return 0
                else:
                    return 1
            else:
                return 3
        else:
            return 2
    else:
        return 1

def alterDatabaseDecompress( database: str):
    if verify_string(database):
        metadata_db, index_md_db = get_metadata_db(database)
        if  metadata_db:
            lista_tablas = showTables(database)
            bandera = False
            bandera_descompress = True
            for tabla in lista_tablas:
                tabla_metadatos = metadata_db.get_table(tabla)
                if tabla_metadatos:
                    if not tabla_metadatos.get_compress():
                        bandera_descompress = False
            if bandera_descompress:
                for tabla in lista_tablas:
                    tabla_metadatos = metadata_db.get_table(tabla)
                    if tabla_metadatos:
                        registros = extractTable(database,tabla)
                        if registros:
                            truncate(database, tabla)
                        for tupla in registros:
                            lista_descomprimida = []
                            bandera = True
                            for columna in tupla:
                                if type(columna) == bytes:
                                    col_descompress = zlib.decompress(columna).decode("utf-8")
                                    lista_descomprimida.append(col_descompress)
                                else:
                                    lista_descomprimida.append(columna)
                            insert(database,tabla,lista_descomprimida)
                        tabla_metadatos.set_compress(False)
            else:
                return 3
            if bandera:
                return 0
            else:
                return 1
        else:
            return 2
    else:
        return 1

def alterTableCompress(database, table, level):
    if verify_string(database):
        metadata_db, index_md_db = get_metadata_db(database)
        if metadata_db:
            if (level >= -1) and (level <= 9):
                bandera = False
                tabla_metadatos = metadata_db.get_table(table)
                if tabla_metadatos:
                    if not tabla_metadatos.get_compress():
                        registros = extractTable(database, table)
                        if registros:
                            truncate(database, table)
                        for tupla in registros:
                            lista_comprimida = []
                            bandera = True
                            for columna in tupla:
                                if type(columna) == str:
                                    col_compress = zlib.compress(columna.encode("utf-8"), level)
                                    lista_comprimida.append(col_compress)
                                else:
                                    lista_comprimida.append(columna)
                            insert(database, table, lista_comprimida)
                        tabla_metadatos.set_compress(True)
                else:
                    return 3
                if bandera:
                    return 0
                else:
                    return 1
            else:
                return 4
        else:
            return 2
    else:
        return 1

def alterTableDecompress( database: str, table: str):
    if verify_string(database):
        metadata_db, index_md_db = get_metadata_db(database)
        if  metadata_db:
            bandera = False
            tabla_metadatos = metadata_db.get_table(table)
            if tabla_metadatos:
                if tabla_metadatos.get_compress():
                    registros = extractTable(database,table)
                    if registros:
                        truncate(database, table)
                    for tupla in registros:
                        lista_descomprimida = []
                        bandera = True
                        for columna in tupla:
                            if type(columna) == bytes:
                                col_descompress = zlib.decompress(columna).decode("utf-8")
                                lista_descomprimida.append(col_descompress)
                            else:
                                lista_descomprimida.append(columna)
                        insert(database,table,lista_descomprimida)
                    tabla_metadatos.set_compress(False)
                else:
                    return 4
            else:
                return 3

            if bandera:
                return 0
            else:
                return 1
        else:
            return 2
    else:
        return 1

#--------------------------------------------------------<INDICES>--------------------------------------------------
def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:       
        if metadata_db.get_table(table):
            if len(columns) != len(columnsRef):
                return 4                
            
            return metadata_db.get_table(table).fk.insertFK([indexName, table, columns,tableRef,columnsRef])
        else: return 3
    else: return 2

def alterTableDropFK(database: str, table: str, indexName: str):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:       
        if metadata_db.get_table(table):                        
            return metadata_db.get_table(table).fk.deleteFK(indexName)
        else: return 3
    else: return 2
def alterTableAddUnique(database: str, table: str, indexName: str, columns: list):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:       
        if metadata_db.get_table(table):            
            return metadata_db.get_table(table).unique.insertUnique([indexName, table, columns])
        else: return 3
    else: return 2

def alterTableDropUnique(database: str, table: str, indexName: str):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:       
        if metadata_db.get_table(table):                        
            return metadata_db.get_table(table).unique.deleteUnique(indexName)
        else: return 3
    else: return 2

def alterTableAddIndex(database: str, table: str, indexName: str, columns: list):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:       
        if metadata_db.get_table(table):
            return metadata_db.get_table(table).index.insertIndex([indexName, table, columns])
        else: return 3
    else: return 2

def alterTableDropindex(database: str, table: str, indexName: str):
    metadata_db, indexDB = get_metadata_db(database)
    if metadata_db:       
        if metadata_db.get_table(table):                        
            return metadata_db.get_table(table).index.deleteIndex(indexName)
        else: return 3
    else: return 2

    
def showMetadata():
    # db: Database
    # table: Table
    print("----------------------- --> MetaData <-- ----------------------------------")
    for db in metadata_db_list:
        print(f"DataBase:{db.get_name_database()}")
        print(f"Mode:{db.get_mode()}")
        print(f"Encoding:{db.get_encondig()}")
        table_dicc: dict = db.get_tab()
        if len(table_dicc) != 0:
            for key, table in table_dicc.items():
                print("--")
                print(f"\tTable:{table.get_name_table()}")
                print(f"\tNo. Columns:{table.get_nums_colums()}")
                print(f"\tCompress:{table.get_compress()}")
                print(f"\tFK:{table.fk.table}")
                print(f"\t\t{table.fk.extractForeign()}")

        print("")
        print("")


def graphDSD(database: str):
    metadata_db, index = get_metadata_db(database)
    list_aux = list()
    if metadata_db:
        table_dic: dict = metadata_db.get_tab()
        if len(table_dic) != 0:
            grafo = Graph()
            for key, table in table_dic.items():
                list_fk: list = table.fk.extractForeign()
                if len(list_fk) != 0:
                    for data in list_fk:
                        table_1 = data[1]
                        table_2 = data[3]
                        if table_1 not in list_aux:
                            grafo.add_vertex(str(table_1))
                        if table_2 not in list_aux:
                            grafo.add_vertex(str(table_2))

                        grafo.join(str(table_1), str(table_2))
                        # print(f"{str(table_1)},{str(table_2)}")
            gra = grafo.graficar()
            ruta = f"graphDSD_{database}"
            generate_grapviz(gra, str(ruta))
            return 0
        else:
            return None
    else:
        return None
    
def graphDF(database: str, table: str):
    metadata_db, index = get_metadata_db(database)
    if metadata_db:
        table_md: Table = metadata_db.get_table(table)
        if table_md:
            grafo = Graph()
            list_ui = list()
            list_pk = list()
            list_general: list = [x for x in range(table_md.get_nums_colums())]
            pk_list: list = table_md.get_pk_list()
            unique_list: list = table_md.unique.extractUnique()

            for pk in pk_list:
                pk_l = f"pk_{pk}"
                if pk_l not in list_pk:
                    list_pk.append(pk_l)
                grafo.add_vertex(pk_l)
                if pk in list_general:
                    list_general.remove(pk)

            for ui in unique_list:
                for ui_index in ui[2]:
                    ui_l = f"ui_{ui_index}"
                    if ui_l not in list_ui:
                        list_ui.append(ui_l)
                    grafo.add_vertex(ui_l)
                    if ui_index in list_general:
                        list_general.remove(ui_index)

            for general in list_general:
                grafo.add_vertex(general)

            if len(pk_list) == 0:
                hidden_pk = "Hidden_PK"
                grafo.add_vertex(hidden_pk)
                for ui in list_ui:
                    grafo.join(hidden_pk, ui)
                    for normal in list_general:
                        grafo.join(ui, normal)
                        grafo.join(hidden_pk, normal)
            else:
                for pk in list_pk:
                    for ui in list_ui:
                        grafo.join(pk, ui)
                        for normal in list_general:
                            grafo.join(pk, normal)
                for ui in list_ui:
                    for normal in list_general:
                        grafo.join(ui, normal)

                    # print(f"{str(table_1)},{str(table_2)}")
            gra = grafo.graficar()
            ruta = f"graphDF_{database}"
            generate_grapviz(gra, str(ruta))
            return 0
        else:
            return None
    else:
        return None

