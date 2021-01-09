# Copyright (c) 2020 TytusDb Team
import team09.CopyTable as Arreglos
import team09.HelpMain as Help
from .storage.avl import avlMode as avl
from .storage.b import BMode as b
from .storage.bplus import BPlusMode as bplus
from .storage.dict import DictMode as mdict
from .storage.hash import HashMode as thash
from .storage.isam import ISAMMode as isam
from .storage.json import jsonMode as json
from team09 import codificacion
import os, pickle, csv
from team09 import checksum
from team09 import crypto
from team09 import blockchain
import pathlib
from team09 import indices
import zlib
blokFlag = False

def __init__():
    global lista_bases
    global list_table
    lista_bases = []
    list_table = []
    if os.path.exists("Data/BasesG.bin"):
        CargarBaseBIN()
    if os.path.exists("Data/TablasG.bin"):
        CargarTablaBIN()


'''METODO IMPORTANTES'''


def CargarBaseBIN():
    for d in LeerBIN("BasesG"):
        lista_bases.append(d)


def CargarTablaBIN():
    for d in LeerBIN("TablasG"):
        list_table.append(d)


def Actualizar(objeto, nombre):
    file = open("Data/" + nombre + ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()


def LeerBIN(nombre):
    file = open("Data/" + nombre + ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)


def buscartabla(base, tabla):
    bandera = False
    for d in list_table:
        if d.base == base and d.tabla == tabla:
            bandera = True
    return bandera


def buscartablaModo(base, tabla, modo):
    for d in list_table:
        if d.base == base and d.tabla == tabla and d.modo == modo:
            return d


def buscarbase(base):
    bandera = False
    for d in lista_bases:
        if d.base == base:
            bandera = True
    return bandera


def veriMode(modo):
    bandera = False
    if modo in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
        bandera = True
    return bandera


def veriEncoding(modo):
    bandera = False
    if modo in ['ascii', 'iso-8859-1', 'utf8']:
        bandera = True
    return bandera


def loadCSVlista(filepath, tabla) -> list:
    res = []
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            tabla.append(row)


def TransicionTablas(base1, tabla1, modo1, modo2):
    tablaV = buscartablaModo(base1, tabla1, modo1)
    tablaN = Arreglos.Tabla(base1, tabla1, modo2)
    tablaN.fk = tablaV.fk
    tablaN.datos = tablaV.datos
    tablaN.pk = tablaV.pk
    return tablaN


def cambioBaseTotalArreglos(modonuevo, base):
    if veriMode(modonuevo):
        if buscarbase(base):
            for tabla in list_table:
                if tabla.base == base:
                    tabla.modo = modonuevo
            Actualizar(list_table, "tablasG")


def cambioBaseTotal(modoviejo, modonuevo, base):
    eli = Help.eliminainercambio(modoviejo, base)
    cre = Help.CrearBase(modonuevo, base)
    tabla = 845
    pk = 25222
    inse = 98774
    fk = 54788
    t = TablasG(base)
    if cre == 0:
        for datos in lista_bases:
            if datos.base == base:
                datos.modo = modonuevo
                Actualizar(lista_bases, "BasesG")
        cambioBaseTotalArreglos(modonuevo, base)
    if len(t) != 0:
        for tablas in t:
            tabla = createTable(tablas.base, tablas.tabla, tablas.columnas)
            if tablas.pk != None:
                pk = alterAddPK(tablas.base, tablas.tabla, tablas.pk)
            if tablas.fk != None:
                fk = alterAddPK(tablas.base, tablas.tabla, tablas.fk)
            for datatupla in tablas.datos:
                inse = Help.Tupla(tablas.modo, tablas.base, tablas.tabla, datatupla)

            if tabla == 0 and pk == 0 and inse == 0 and fk == 0:
                ''
            elif tabla != 0 and pk == 0 and inse == 0 and fk == 0:
                return tabla
            elif tabla == 0 and pk != 0 and inse == 0 and fk == 0:
                return pk
            elif tabla == 0 and pk == 0 and inse != 0 and fk == 0:
                return inse
            elif tabla == 0 and pk == 0 and inse == 0 and fk != 0:
                return fk
    return 0


def RTUPLA(base, tabla, listadato):
    for d in listadato:
        insert(base, tabla, d)


def TablasG(database: str) -> list:
    tablas = []
    for d in list_table:
        if d.base == database:
            tablas.append(d)
    return tablas


__init__()


## crud de base de datos

def createDatabase(database: str, mode: str, encoding: str) -> int:
    retorno = 1000
    if veriMode:
        if veriEncoding:
            retorno = Help.CrearBase(mode, database)
            if retorno == 0:
                BaseN = Arreglos.Base(database, mode, encoding)
                lista_bases.append(BaseN)
                Actualizar(lista_bases, "BasesG")
            return retorno
        else:
            return 4
    else:
        return 3


def showDatabases() -> list:
    lista = []
    for d in lista_bases:
        lista.append(d.base)
    return lista


def alterDatabase(databaseOld, databaseNew) -> int:
    retorno = 1000
    for d in lista_bases:
        if d.base == databaseOld:
            retorno = Help.CambioNombre(d.modo, databaseOld, databaseNew)
            if retorno == 0:
                base = Arreglos.Base(databaseNew, d.modo, d.encoding)
                lista_bases.remove(d)
                lista_bases.append(base)
                Actualizar(lista_bases, "BasesG")
            return retorno
    else:
        return 2


def alterDatabaseMode(database: str, mode: str) -> int:
    retorno = 1000
    if veriMode:
        if veriEncoding:
            if buscarbase(database):
                for b in lista_bases:
                    if b.base == database:
                        retorno = cambioBaseTotal(b.modo, mode, database)
                return retorno
            else:
                return 2
        else:
            return 4
    else:
        return 3


def dropDatabase(database: str) -> int:
    retorno = 1000
    for d in lista_bases:
        if d.base == database:
            retorno = Help.eliminainercambio(d.modo, database)
            if retorno == 0:
                lista_bases.remove(d)
                Actualizar(lista_bases, "BasesG")
            return retorno
    else:
        return 2


# CRUD DE TABLA

def alterTableMode(database: str, table: str, mode: str) -> int:
    if veriMode(mode):
        if buscarbase(database):
            for d in lista_bases:
                if d.base == database:
                    indice = Arreglos.indices(database, mode)
                    d.index.append(indice)
                    Help.CrearBase(mode, database)
                    Actualizar(lista_bases, "BasesG")
            for d in list_table:
                if d.base == database and d.tabla == table:
                    d.modo = mode
                    Help.Creartabla(mode, database, table, d.columnas)
                    Help.AgregarPK(mode, database, table, d.pk)
                    for tupla in d.datos:
                        Help.Tupla(mode, database, table, tupla)
                    Actualizar(list_table, "tablasG")
            return 0

        else:
            return 2
    else:
        return 4


def TransicionTablas(base1, tabla1, modo1, modo2):
    tablaV = buscartablaModo(base1, tabla1, modo1)
    tablaN = Arreglos.Tabla(base1, tabla1, modo2)
    tablaN.fk = tablaV.fk
    tablaN.datos = tablaV.datos
    tablaN.pk = tablaV.pk
    return tablaN


def createTable(database: str, table: str, numberColumns: int) -> int:
    retorno = 1000
    for d in lista_bases:
        if d.base == database:
            retorno = Help.Creartabla(d.modo, database, table, numberColumns)
            if retorno == 0:
                tablaN = Arreglos.Tabla(database, table, numberColumns, d.modo)
                list_table.append(tablaN)
                Actualizar(list_table, "tablasG")
            return retorno
    else:
        return 2


def showTables(database: str) -> list:
    tablas = []
    for d in list_table:
        if d.base == database:
            tablas.append(d.tabla)
    return tablas


def extractTable(database: str, table: str) -> list:
    for d in list_table:
        if d.base == database:
            if d.tabla == table:
                return Help.ExtraerTabla(d.modo, database, table)
    else:
        return 2


def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    retorno = 1444
    for d in list_table:
        if d.base == database:
            if d.tabla == table:
                retorno = Help.ExtraerRangoTabla(d.mode, database, table, columnNumber, lower, upper)
                return retorno
    else:
        return 2


def alterAddPK(database: str, table: str, columns: list) -> int:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database:
                    if d.tabla == table:
                        retorno = Help.AgregarPK(d.modo, database, table, columns)
                        if retorno == 0:
                            d.pk = columns
                            Actualizar(list_table, "tablasG")

                        return retorno
        else:
            return 3
    else:
        return 2


def alterDropPK(database: str, table: str) -> int:
    retorno = 1444
    for d in list_table:
        if d.base == database:
            if d.tabla == table:
                retorno = Help.EliminarPK(d.modo, database, table)
                if retorno == 0:
                    d.pk = None
                    Actualizar(list_table, "tablasG")
                return retorno
    else:
        return 2


def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    retorno = 1444
    for d in list_table:
        if d.base == database and d.tabla == tableOld:
            retorno = Help.CambiarNombreTabla(d.modo, database, tableOld, tableNew)
            if retorno == 0:
                d.tabla = tableNew
                Actualizar(list_table, "tablasG")
            return retorno
    else:
        return 2


def alterAddColumn(database: str, table: str, default: any) -> int:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    retorno = Help.AgregarColumna(d.modo, database, table, default)
                    if retorno == 0:
                        val = d.columnas
                        d.columnas = val + default
                        Actualizar(list_table, "tablasG")
                    return retorno
        else:
            return 3
    return 2


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    retorno = Help.EliminarColumna(d.modo, database, table, columnNumber)
                    if retorno == 0:
                        colI = d.columnas
                        d.columnas = colI - columnNumber
                        Actualizar(list_table, "tablasG")
                    return retorno
        else:
            return 3
    return 2


def dropTable(database: str, table: str) -> int:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    retorno = Help.EliminarTabla(d.modo, database, table)
                    if retorno == 0:
                        list_table.remove(d)
                        Actualizar(list_table, "tablasG")
                    return retorno
        else:
            return 3
    return 2


'''  CRUD DE LAS TUPLAS'''


def insert(database: str, table: str, register: list) -> int:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    retorno = Help.Tupla(d.modo, database, table, register)
                    if retorno == 0:
                        d.datos.append(register)
                        cod = returnEncoding(database)
                        d.codificado.append(codTupla(register, cod))
                        Actualizar(list_table, "tablasG")
                        if blokFlag:
                            blocdata = extractTable(database, table)
                            blockchain.writeBlockChain(database, table, data)
                    return retorno
        else:
            return 3
    return 2


def loadCSV(file: str, database: str, table: str) -> list:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    retorno = Help.CargandoCsvMode(d.mode, file, database, table)
                    if retorno == 0:
                        loadCSVlista(file, d.datos)
                        Actualizar(list_table, "tablasG")
                    return retorno
        else:
            return 3
    return 2


def extractRow(database: str, table: str, columns: list) -> list:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    retorno = Help.ExtraerFILA(d.mode, database, table, columns)
                    return retorno
        else:
            return 3
    return 2


def update(database: str, table: str, register: dict, columns: list) -> int:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    retorno = Help.actualizarupdate(d.modo, database, table, register, columns)
                    if retorno == 0:
                        d.data.clear()
                        for ta in extractTable(database, table):
                            ta.data.append(d)
                        if blokFlag:
                            blocdata = extractTable(database, table)
                            writeBlockChain(database, table, data)
                    return retorno
        else:
            return 3
    return 2


def delete(database: str, table: str, columns: list) -> int:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    retorno = Help.Deletedatos(d.modo, database, table, columns)
                    if retorno == 0:
                        d.data.clear()
                        for ta in extractTable(database, table):
                            ta.data.append(d)
                    return retorno
        else:
            return 3
    return 2


def truncate(database: str, table: str) -> int:
    retorno = 1444
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    retorno = Help.TruncarTabla(d.modo, database, table)
                    if retorno == 0:
                        d.codificado = []
                        d.datos.clear()
                        Actualizar(list_table, "tablasG")
                    return retorno
        else:
            return 3
    return 2


# crypto functions and blockchain
def checksumDatabase(database: str, mode: str) -> str:
    try:
        e = showTables(database)
        g = []
        for t in e:
            g.extend(extractTable(database, t))
        return checksum.checksum(g, mode)
    except:
        return None


def checksumTable(database: str, table: str, mode: str) -> str:
    try:
        f = extractTable(database, table)
        return checksum.checksum(f, mode)
    except:
        return None


def encrypt(backup: str, password: str) -> str:
    try:
        return crypto.encrypt(backup, password)
    except:
        return None


def decrypt(cipherBackup: str, password: str) -> str:
    try:
        return crypto.decrypt(cipherBackup, password)
    except:
        return None


def safeModeOn(database: str, table: str) -> int:
    try:
        db = showDatabases()
        if database in db:
            t = showTables(database)
            if table in t:
                if not pathlib.Path("blockchain/" + database + "_" + table + ".json").is_file():
                    blokFlag = True
                    data = extractTable(database, table)
                    blockchain.writeBlockChain(database, table, data, falg=False)
                    return 0
                else:
                    return 4
            else:
                return 3
        else:
            return 2
    except:
        return 1


def safeModeOff(database: str, table: str) -> int:
    try:
        db = showDatabases()
        if database in db:
            t = showTables(database)
            if table in t:
                if pathlib.Path("blockchain/" + database + "_" + table + ".json").is_file():
                    blokFlag = False
                    data = extractTable(database, table)
                    blockchain.showBlockChain(database, table, data)
                    return 0
                else:
                    return 4
            else:
                return 3
        else:
            return 2
    except:
        return 1


'''crud de grafo'''


def graphDF(database: str, table: str) -> str:
    if buscarbase(database):
        if buscartabla(database, table):
            for d in list_table:
                if d.base == database and d.tabla == table:
                    Help.Grafico(d.modo, database, table)
        else:
            return 3
    else:
        return 2


def returnEncoding(database):
    for db in lista_bases:
        if db.base == database:
            return db.encoding


# codificacion
def decodificar(lista: list, anteriorEncoding: str) -> list:
    decodificado = []
    for i in lista:
        # "utf8", "ascii", "iso-8859-1"
        try:
            if anteriorEncoding == "ascii":
                decodificado.append(i.decode("ascii"))
            elif anteriorEncoding == "iso-8859-1":
                decodificado.append(i.decode("iso-8859-1"))
            elif anteriorEncoding == "uft8":
                decodificado.append(i.decode("utf-8"))
        except:
            pass

    return decodificado


def alterDatabaseEncoding(database: str, encoding: str) -> int:
    try:
        if veriEncoding:
            if buscarbase(database):  # database existe
                anterioEncoding = "n"
                for d in lista_bases:  # change all databases encoding
                    if d.base == database:
                        if anterioEncoding == "n":
                            anterioEncoding = d.encoding
                        d.encoding = encoding
                for d in list_table:  # change all tables encoding
                    if d.base == database:
                        d.encoding = encoding
                        anterior = d.codificado  # actual lista
                        d.codificado = []  # nueva codificacion
                        for i in anterior:  # tomo cada valor de las tuplas y lo cambio a la nueva codificacion
                            i = decodificar(i, anterioEncoding)
                            d.codificado.append(codTupla(i, encoding))
                        Actualizar(list_table, "tablasG")
                        Actualizar(lista_bases, "BasesG")
                return 0
            else:
                return 2
        else:
            return 3
    except:
        return 1


# fin codificacion

def codTupla(registro: list, cod) -> list:
    codificado = []
    for i in registro:
        if isinstance(i, str):
            # "utf8", "ascii", "iso-8859-1"
            if cod == "ascii":
                codificado.append(codificacion.toASCII(i))
            elif cod == "iso-8859-1":
                codificado.append(codificacion.cod_iso(i))
            elif cod == "utf-8":
                codificado.append(codificacion.utf(i))
    return codificado

# Indices

def alterTableAddFK(database: str, table: str, indexName: str, columns: list, tableRef: str, columnsRef: list) -> int:
    try:
        db = showDatabases()
        if database in db:
            if buscartabla(database, table):
                if buscartabla(database, tableRef):
                    for d in list_table:
                        if d.base == database and d.tabla == table:
                            j = extractTable(database, table) 
                            co=len(j[0])
                            mo = d.modo
                            retorno = indices.alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef,mo,co)
                            if retorno == 0:
                                d.fk=columns
                                Actualizar(list_table, "tablasG")
                            return retorno
                else:
                    return 3
            else:
                return 3
        else:
            return 2
    except:
        return 1


def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    try:
        db = showDatabases()
        if database in db:
            if buscartabla(database, table):
                for d in list_table:
                    if d.base == database and d.tabla == table:
                        retorno = indices.alterTableDropFK(database, table, indexName, d.mode)
                        if retorno == 0:
                            d.fk=None
                            Actualizar(list_table, "tablasG")
                        return retorno
            else:
                return 3
        else:
            return 2
    except:
        return 1


def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        db = showDatabases()
        if database in db:
            if buscartabla(database, table):
                for d in list_table:
                    if d.base == database and d.tabla == table:
                        j = extractTable(database, table) 
                        co=len(j[0])
                        mo = d.modo
                        retorno = indices.alterTableAddUnique(database, table, indexName, columns,mo,co)
                        if retorno == 0:
                            d.fk=columns
                            Actualizar(list_table, "tablasG")
                        return retorno
            else:
                return 3
        else:
            return 2
    except:
        return 1


def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    try:
        db = showDatabases()
        if database in db:
            if buscartabla(database, table):
                for d in list_table:
                    if d.base == database and d.tabla == table:
                        retorno = indices.alterTableDropUnique(database, table, indexName, d.mode)
                        if retorno == 0:
                            d.fk=None
                            Actualizar(list_table, "tablasG")
                        return retorno
            else:
                return 3
        else:
            return 2
    except:
        return 1


def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        db = showDatabases()
        if database in db:
            if buscartabla(database, table):
                for d in list_table:
                    if d.base == database and d.tabla == table:
                        j = extractTable(database, table) 
                        co=len(j[0])
                        mo = d.modo
                        retorno = indices.alterTableAddIndex(database, table, indexName, columns,mo,co)
                        if retorno == 0:
                            d.fk=columns
                            Actualizar(list_table, "tablasG")
                        return retorno
            else:
                return 3
        else:
            return 2
    except:
        return 1


def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    try:
        db = showDatabases()
        if database in db:
            if buscartabla(database, table):
                for d in list_table:
                    if d.base == database and d.tabla == table:
                        retorno = indices.alterTableDropIndex(database, table, indexName, d.mode)
                        if retorno == 0:
                            d.fk=None
                            Actualizar(list_table, "tablasG")
                        return retorno
            else:
                return 3
        else:
            return 2
    except:
        return 1

def comprimidoTabla(base, tabla):
    for d in list_table:
        if d.base == base and d.tabla == tabla:
            if d.compreso:
                return True
    return False


def comprimidoBase(base):
    for d in lista_bases:
        if d.base == base:
            if d.compreso:
                return True
    return False


def alterDatabaseCompress(database: str, level: int) -> int:
    if (-1 <= level or level > 9):
        if (buscarbase(database)):
            try:
                if (comprimidoBase(database)):
                    print("La base de datos ya ha sido comprimida")
                    return 4  # Base de datos ya comprimida
                else:
                    for d in lista_bases:
                        if d.base == database:
                            d.compreso = True

                    Actualizar(lista_bases, "basesG")
                    for d in list_table:
                        if d.base == database:
                            arregloTupla = d.codificado
                            d.codificado = []
                            for i in arregloTupla:
                                if isinstance(i, str):
                                    NuevoValor = zlib.compress(i, level)
                                    d.codificado.append(NuevoValor)
                            d.compreso = True
                    Actualizar(list_table, "tablasG")

                    return 0  # operación exitosa
            except:
                print("Error en la compresion de la base de datos")
                return 1  # Error en la operación
        else:
            return 2  # Database no existe
    else:
        return 3  # level incorrecto

def alterDatabaseDecompress(database: str) -> int:
    if (buscarbase(database)):
        if (comprimidoBase(database)):
            try:
                for d in lista_bases:
                    if d.base == database:
                        d.compreso = False
                        Actualizar(lista_bases, "basesG")
                for d in list_table:
                    if d.base == database:
                        arregloTupla = d.codificado
                        d.codificado = []
                        for i in arregloTupla:
                            if isinstance(i, str):
                                NuevoValor = zlib.decompress(i)
                                d.codificado.append(NuevoValor)
                        d.compreso = False
                Actualizar(list_table, "tablasG")
                return 0  # operación exitosa
            except:
                print("Error en la descompresion de la base de datos")
                return 1  # Error en la operación
        else:
            return 3  # Sin compresion
    else:
        return 2  # Database no existe


def alterTableDecompress(database: str, table: str) -> int:
    if (buscarbase(database)):
        if (buscartabla(database, table)):
            if (comprimidoTabla(database, table)):
                try:
                    for d in list_table:
                        if d.base == database and d.tabla == table:
                            arregloTupla = d.codificado
                            d.codificado = []
                            for i in arregloTupla:
                                if isinstance(i, str):
                                    NuevoValor = zlib.decompress(i)
                                    d.codificado.append(NuevoValor)
                            d.compreso = False
                    Actualizar(list_table, "tablasG")
                    return 0  # operación exitosa
                except:
                    return 1  # Error en la operación
            else:
                return 4  # Sin compresion
        else:
            return 3  # Table no existe

    else:
        return 2  # Database no existe


def alterTableCompress(database: str, table: str, level: int) -> int:
    if (-1 <= level or level > 9):
        if (comprimidoTabla(database, table)):
            return 5  # tabla ya comprimida
        else:
            if (buscarbase(database)):
                if (buscartabla(database, table)):
                    try:
                        for d in list_table:
                            if d.base == database and d.tabla == table:
                                arregloTupla = d.codificado
                                d.codificado = []
                                for i in arregloTupla:
                                    if isinstance(i, str):
                                        NuevoValor = zlib.compress(i, level)
                                        d.codificado.append(NuevoValor)
                                d.compreso = True
                        Actualizar(list_table, "tablasG")
                        return 0  # operación exitosa
                    except:
                        print("Error en la compresion de la tabla")
                        return 1  # Error en la operación
                else:
                    return 3  # Table no existe
            else:
                return 2  # Database no existe
    else:
        return 4  # level incorrecto

# Grafos
def graphDSD(database: str) -> str:
    try:
        return indices.graphDSD(database)
    except:
        return None

def devolvercol(base,tabla):
    for d in list_table:
        if d.base==base and d.tabla==tabla:
            return d.columnas

def graphDF(database: str, table: str) -> str:
    try:
        return indices.graficar(devolvercol(database,table),database,table)
    except:
        return None
