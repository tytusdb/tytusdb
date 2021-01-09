from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bplus
from storage.hash import HashMode as hash
from storage.isam import ISAMMode as isam
from storage.json import jsonMode as json
from storage.dict import DictMode as dict
import pickle
import os
import zlib
import hashlib
from cryptography.fernet import Fernet
import base64

modos = ["avl", "b", "bplus", "hash", "isam", "json", "dict"]
encoding = ["ascii", "utf8", "iso-8859-1"]

def commit(objeto, nombre):
    file = open(nombre + ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()

def rollback(nombre):
    file = open(nombre + ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)

def __init__():
    global lista_db
    lista_db = []
    #lista_db = rollback("prueba")
__init__()



def buscar(nombre):
    for db in lista_db:
        if nombre == db[0]:
            return db
    else:
        return None

def verificarmodo(mode):
    if mode == 'avl':
        return avl
    elif mode == 'b':
        return b
    elif mode == 'bplus':
        return bplus
    elif mode == 'dict':
        return dict
    elif mode == 'isam':
        return isam
    elif mode == 'json':
        return json
    elif mode == 'hash':
        return hash

def createDatabase(db,modo,cod):
    if not modo in modos:
        return 3
    if not cod in encoding:
        return 4
    if buscar(db) == None:
        try:
            if cod == "ascii":
                cod = "ASCII"
            elif cod =="utf8":
                cod = "utf-8"
            db.encode(cod)
            tmp = verificarmodo(modo).createDatabase(db)
            if tmp == 0:
                lista_db.append([db, modo, cod, {}, [], [], []])
                return tmp
            else:
                return tmp
        except:
            return 1
    else:
        return 2

def cambiardatos(db, modo,modonuevo):
    nodo = buscar(db)
    verificarmodo(modonuevo).createDatabase(db)
    tablas=verificarmodo(modo).showTables(db)
    listapk = nodo[4]
    if len(tablas)>0:
        for tabla in tablas:
            registros = verificarmodo(modo).extractTable(db,tabla)
            if len(registros) !=0:
                verificarmodo(modonuevo).createTable(db, tabla, len(registros[0]))
                for pk in listapk:
                    if db in pk and tabla in pk:
                        verificarmodo(modonuevo).alterAddPK(db, tabla, pk[2])
                if len(registros) > 0:
                    for registro in registros:
                        verificarmodo(modonuevo).insert(db, tabla, registro)
            else:
                verificarmodo(modonuevo).createTable(db, tabla, 4)

def alterDatabaseMode(db, modo):
    nodo = buscar(db)
    if nodo != None:
        if modo in modos:
            try:
                cambiardatos(db,nodo[1],modo)
                verificarmodo(nodo[1]).dropDatabase(db)
                nodo[1] = modo
                dict = nodo[3]
                for i in dict:
                    tablas = verificarmodo(dict[i]).extractTable(db,i)
                    verificarmodo(nodo[1]).createTable(db,i,len(tablas[0]))
                    for registro in tablas:
                        verificarmodo(nodo[1]).insert(db,i,registro)

                for i in dict:
                    if dict[i] != modo:
                        verificarmodo(dict[i]).dropDatabase(db)

                nodo[3]={}
                return 0
            except:
                return 1
        else:
            return 4
    else:
        return 2

def alterDatabaseEncoding(db,cod):
    nodo = buscar(db)
    if nodo != None:
        if cod in encoding:
            try:
                nodo[2]=cod
                return 0
            except:
                return 1
        else:
            return 3
    else:
        return 2

def alterTableMode(db,tabla, modo):
    nodo = buscar(db)
    if nodo != None:
        if modo in modos:
            try:
                dic = nodo[3]
                dic[tabla]=modo
                verificarmodo(modo).createDatabase(db)
                tablas = verificarmodo(nodo[1]).extractTable(db,tabla)
                verificarmodo(modo).createTable(db, tabla,len(tablas[0]))
                for registro in tablas:
                    verificarmodo(modo).insert(db,tabla,registro)
                verificarmodo(nodo[1]).dropTable(db,tabla)
                return 0
            except:
                return 1
        else:
            return 4
    else:
        return 2

def showDatabases():
    lista= []
    for db in lista_db:
        lista.append(db[0])

    return lista

def dropDatabase(db):
    nodo = buscar(db)
    if nodo != None:
        num = 0
        for i in lista_db:
            try:
                if i[0]==db:
                    verificarmodo(nodo[1]).dropDatabase(db)
                    lista_db.pop(num)
                return 0
            except:
                return 1
            num = num + 1
    else:
        return 2

def alterDatabase(db,nuevadb):
    nodo = buscar(db)
    nodonuevo = buscar(nuevadb)
    if nodonuevo is None:
        if nodo != None:
            try:
                if Codtexto(db,nuevadb) is True:
                    res = verificarmodo(nodo[1]).alterDatabase(db,nuevadb)
                    nodo[0]=nuevadb
                    return res
                else:
                    return 1
            except:
                return 1
        else:
            return 2
    else:
        return 3

def createTable(db,tabla,columnas):
    nodo = buscar(db)
    if nodo != None:
        try:
            if Codtexto(db,tabla) is True:
                res = verificarmodo(nodo[1]).createTable(db, tabla, columnas)
                return res
            else:
                return 1
        except:
            return 1
    else:
        return 2

def showTables(db):
    nodo = buscar(db)
    if nodo != None:
        try:
            lista = verificarmodo(nodo[1]).showTables(db)
            dict = nodo[3]
            for tabla in dict:
                lista.append(tabla)
            return lista
        except:
            return []
    else:
        return []

def extractTable(db,tabla):
    nodo = buscar(db)
    if nodo != None:
        try:
            dict = nodo[3]
            if tabla in dict:
                lista = verificarmodo(dict[tabla]).extractTable(db,tabla)
                return lista
            else:
                lista = verificarmodo(nodo[1]).extractTable(db,tabla)
                return lista
        except:
            return []
    else:
        return []

def extractRangeTable(db,tabla,columna,menor,mayor):
    nodo = buscar(db)
    if nodo != None:
        try:
            dict = nodo[3]
            if tabla in dict:
                lista = verificarmodo(dict[tabla]).extractRangeTable(db,tabla,columna,menor,mayor)
                return lista
            else:
                lista = verificarmodo(nodo[1]).extractRangeTable(db,tabla,columna,menor,mayor)
                return lista
        except:
            return []
    else:
        return []

def alterAddPK(db,tabla,columnas):
    nodo = buscar(db)
    if nodo != None:
        try:
            dict = nodo[3]
            if tabla in dict:
                res = verificarmodo(dict[tabla]).alterAddPK(db, tabla, columnas)
                if res == 0:
                    lista = nodo[4]
                    lista.append([tabla, columnas])
                return res
            else:
                res = verificarmodo(nodo[1]).alterAddPK(db, tabla, columnas)
                if res == 0:
                    lista = nodo[4]
                    lista.append([tabla, columnas])
                return res
        except:
            return 1
    else:
        return 2

def alterDropPK(db,tabla):
    nodo = buscar(db)
    if nodo != None:
        try:
            dict = nodo[3]
            if tabla in dict:
                res = verificarmodo(dict[tabla]).alterDropPK(db, tabla)
                if res == 0:
                    c = 0
                    listapk = nodo[4]
                    for pk in listapk:
                        if tabla in pk:
                            listapk.pop(c)
                    c = c + 1
                return res
            else:
                res = verificarmodo(nodo[1]).alterDropPK(db, tabla)
                if res == 0:
                    c = 0
                    listapk = nodo[4]
                    for pk in listapk:
                        if tabla in pk:
                            listapk.pop(c)
                    c = c + 1
                return res
        except:
            return 1
    else:
        return 2

def alterTable(db,tabla,tablanueva):
    nodo = buscar(db)
    if nodo != None:
        try:
            if Codtexto(db,tabla) is True:
                dict = nodo[3]
                if tabla in dict:
                    res = verificarmodo(dict[tabla]).alterTable(db, tabla,tablanueva)
                    tabla = tablanueva
                    return res
                else:
                    res = verificarmodo(nodo[1]).alterTable(db, tabla, tablanueva)
                    return res
            else:
                return 1
        except:
            return 1
    else:
        return 2

def alterAddColumn(db,tabla,valor):
    nodo = buscar(db)
    if nodo != None:
        try:
            dict = nodo[3]
            if tabla in dict:
                res = verificarmodo(dict[tabla]).alterAddColumn(db, tabla,valor)
                return res
            else:
                res = verificarmodo(nodo[1]).alterAddColumn(db, tabla, valor)
                return res
        except:
            return 1
    else:
        return 2

def alterDropColumn(db,tabla,valor):
    nodo = buscar(db)
    if nodo != None:
        try:
            dict = nodo[3]
            if tabla in dict:
                res = verificarmodo(dict[tabla]).alterDropColumn(db, tabla,valor)
                return res
            else:
                res = verificarmodo(nodo[1]).alterDropColumn(db, tabla, valor)
                return res
        except:
            return 1
    else:
        return 2

def dropTable(db,tabla):
    nodo = buscar(db)
    if nodo != None:
        try:
            dict = nodo[3]
            if tabla in dict:
                res = verificarmodo(dict[tabla]).dropTable(db,tabla)
                del dict[tabla]
                return res
            else:
                res = verificarmodo([nodo[1]]).dropTable(db,tabla)
                return res
        except:
            return 1
    else:
        return 2

def loadCSV(file,db,tabla):
    nodo = buscar(db)
    if nodo != None:
        dict = nodo[3]
        if tabla in dict:
            res = verificarmodo(dict[tabla]).loadCSV(file,db,tabla)
            return res
        else:
            res = verificarmodo(nodo[1]).loadCSV(file,db,tabla)
            return res
    else:
        return 2

def extractRow(db,tabla,lista):
    nodo = buscar(db)
    if nodo != None:
        dict = nodo[3]
        if tabla in dict:
            res = verificarmodo(dict[tabla]).extractRow(db,tabla,lista)
            return res
        else:
            res = verificarmodo(nodo[1]).extractRow(db,tabla,lista)
            return res
    else:
        return []

def update(db,tabla,dict,lista):
    nodo = buscar(db)
    if nodo != None:
        dict = nodo[3]
        if tabla in dict:
            res = verificarmodo(dict[tabla]).update(db,tabla,dict,lista)
            return res
        else:
            res = verificarmodo(nodo[1]).update(db,tabla,dict,lista)
            return res
    else:
        return 2

def delete(db,tabla,lista):
    nodo = buscar(db)
    if nodo != None:
        dict = nodo[3]
        if tabla in dict:
            res = verificarmodo(dict[tabla]).delete(db,tabla,lista)
            return res
        else:
            res = verificarmodo(nodo[1]).delete(db,tabla,lista)
            return res
    else:
        return 2

def truncate(db,tabla,lista):
    nodo = buscar(db)
    if nodo != None:
        dict = nodo[3]
        if tabla in dict:
            res = verificarmodo(dict[tabla]).truncate(db,tabla)
            return res
        else:
            res = verificarmodo(nodo[1]).truncate(db,tabla)
            return res
    else:
        return 2

def insert(db,tabla,lista):
    nodo = buscar(db)
    if nodo != None:
        r = []
        for i in lista:
            r.append(Codtexto(db,i))
        if False in r:
            return 1
        else:
            dict = nodo[3]
            if tabla in dict:
                res = verificarmodo(dict[tabla]).insert(db,tabla,lista)
                return res
            else:
                res = verificarmodo(nodo[1]).insert(db,tabla,lista)
                return res
    else:
        return 2

def alterTableAddUnique(database, table, indexName, columns):
    nodo = buscar(database)
    if nodo != None:
        lista = showTables(database)
        if lista != None:
            if table in lista:
                if nodo[5] != None:
                    dict = nodo[3]
                    if table in dict:
                        tab = verificarmodo(dict[table]).extractTable(database, table)
                    else:
                        tab = verificarmodo(nodo[1]).extractTable(database, table)
                    try:
                        for columna in columns:
                            if columna > len(tab[0]):
                                return 4
                        nodo[5].append([table,indexName,columns])
                        return 0
                    except:
                        return 1
    else:
        return 2

def alterTableDropUnique(database, table, indexName):
    nodo = buscar(database)
    if nodo != None:
        lista = showTables(database)
        if table in lista:
            try:
                if nodo[5] != None:
                    indice = nodo[5]
                    c=0
                    for i in indice:
                        if i[0] == table:
                            indice.pop(c)
                        c = c + 1
                        return 0
            except:
                return 1
        else:
            return 3
    else:
        return 2

def alterTableAddIndex(database, table, indexName, columns):
    nodo = buscar(database)
    if nodo != None:
        lista = showTables(database)
        if table in lista:
            if nodo[3]!=None:
                dict = nodo[3]
                if table in dict:
                    tab = verificarmodo(dict[table]).extractTable(database, table)
                else:
                    tab = verificarmodo(nodo[1]).extractTable(database, table)
                try:
                    if len(tab)!=0:
                        for columna in columns:
                            if columna > len(tab[0]):
                                return 4
                    nodo[5].append([table, indexName, columns])
                    return 0
                except:
                    return 1
        else:
            return 3
    else:
        return 2


def alterTableAddFK(database, table, indexName, columns,  tableRef, columnsRef):
    nodo = buscar(database)
    if nodo != None:
        try:
            lista = showTables(database)
            if table in lista and tableRef in lista:
                if nodo[5]!=None:
                    indices = nodo[5]
                    for i in indices:
                        if i[0] == table and i[1]==indexName:
                            if len(columns) != len(columnsRef):
                                return 4
                            else:
                                fk = nodo[6]
                                fk.append([indexName,table,columns,tableRef,columnsRef])
            else:
                return 3
            return 0
        except:
            return 1
    else:
        return 2

def alterTableDropFK(database, table, indexName):
    nodo = buscar(database)
    if nodo != None:
        lista = showTables(database)
        if table in lista:
            try:
                if nodo[6]!=None:
                    indice = nodo[6]
                    c = 0
                    for i in indice:
                        if i[0] == indexName and i[1]==table:
                            indice.pop(c)
                        c = c + 1
                        return 0
            except:
                return 1
        else:
            return 3
    else:
        return 2


def alterTableDropIndex(database, table, indexName):
    nodo = buscar(database)
    if nodo != None:
        lista = showTables(database)
        if table in lista:
            try:
                if nodo[5] != None:
                    indice = nodo[5]
                    c=0
                    for i in indice:
                        if i[0] == indexName and i[1] == table:
                            indice.pop(c)
                        c = c + 1
                        return 0

            except:
                return 1
        else:
            return 3
    else:
        return 2
    
def graphDSD(database):
    nodo = buscar(database)
    if nodo != None:
        grafica = "digraph g { \ngraph [ \nrankdir = LR\n]; \nnode [\nfontsize = 16 \nshape = record \n];\nedge [\n];\n"
        lista = showTables(database)
        for tabla in lista:
            grafica += tabla + "[\nlabel="+tabla+"\nshape=record\n];\n"
        fk = nodo[6]
        c = 0
        bandera = False
        for tabla in lista:
            for t in nodo[6]:
                if bandera == False:
                    if tabla == t[3]:
                        grafica += t[1]+":f1 -> "+tabla+":f2 [\nid = "+str(c)+"\n];\n"
                        bandera = True
                bandera = False
            c = c + 1

        grafica +="}"
    else:
        return None
    if grafica != "":
        tabGen = open("grafoDB.dot","w")
        tabGen.write(grafica)
        tabGen.close()
        tab = open("grafoDB.cmd","w")
        tab.write("dot -Tpng grafoDB.dot -o grafoDB.png")
        tab.close()
        try:
            os.system('grafoDB.cmd')
            os.system('grafoDB.png')
        except:
            return None
    return grafica

def graphDF(database, table):
    grafica = ""
    nodo = buscar(database)
    if nodo != None:
        lista = showTables(database)
        if table in lista:
            grafica = "digraph g { \ngraph [ \nrankdir = LR\n]; \nnode [\nfontsize = 16 \nshape = record \n];\nedge [\n];\n"
            for tabla in lista:
                if tabla == table:
                    grafica += tabla + "[\nlabel=" + tabla + "\nshape=record\n];\n"
            fk = nodo[6]
            c = 0
            bandera = False
            for tabla in lista:
                if tabla ==table:
                    for t in nodo[6]:
                        if bandera == False:
                            if tabla == t[3]:
                                grafica += t[1] + ":f1 -> " + tabla + ":f2 [\nid = " + str(c) + "\n];\n"
                                bandera = True
                        bandera = False
                    c = c + 1
                    
            for tabla in lista:
            if tabla ==table:
                for t in nodo[6]:
                    if bandera == False:
                        if tabla == t[1]:
                            grafica += t[1] + ":f1 -> " + t[3] + ":f2 [\nid = " + str(c) + "\n];\n"
                            bandera = True
                    bandera = False
                c = c + 1   
            grafica += "}"
    else:
        return None
    
    if grafica != "":
        tabGen = open("grafoTABLE.dot","w")
        tabGen.write(grafica)
        tabGen.close()
        tab = open("grafoTABLE.cmd","w")
        tab.write("dot -Tpng grafoTABLE.dot -o grafoTABLE.png")
        tab.close()
        try:
            os.system('grafoTABLE.cmd')
            os.system('grafoTABLE.png')
        except:
            return None
    return grafica

def decrypt(cipherbackup,clave):
    encrypt=""
    devuelve = ""
    try:
        if cipherbackup == None or cipherbackup == "":
            archivo=open(clave+".txt","r")
            encrypt=archivo.read()

        else:
            encrypt=cipherbackup

        llave = open(clave+".key","r").read()
        f = Fernet(llave)
        decrypted = f.decrypt(encrypt.encode())
        textoOriginal = decrypted.decode()
        devuelve = "0\n"+textoOriginal
    except:
        devuelve = "1"
    return devuelve

def encrypt(backup,clave):
    devuelve = ""
    encoded = backup.encode()
    key = Fernet.generate_key()
    llaveBin = open(clave+".key","wb")
    llaveBin.write(key)
    try:
        f = Fernet(key)
        encrypted = f.encrypt(encoded)
        encriptado = encrypted.decode()
        archivo = open(clave+".txt","w")
        archivo.write(encrypted.decode())
        archivo.close()
        devuelve = "0\n"+encriptado
    except:
        devuelve = "1"
    return devuelve

def checksumDatabase(database , mode):
    texto = ""
    if buscar(database) is not None:
        if mode == "MD5" or mode == "SHA256":
            lista = showTables(database)
            texto = texto + database
            for i in lista:
                texto = texto + i
                for j in extractTable(database, i):
                    texto = texto + "".join(j)
            #print(texto)
            if mode == "MD5":
                return md5str(texto)
            else:
                return sha256str(texto)
        else:
            return None
    else:
        return None

def checksumTable(database, table, mode):
    texto = ""
    if buscar(database) is not None:
        if mode == "MD5" or mode == "SHA256":
            lista = showTables(database)
            for i in lista:
                if (i == table):
                    texto = texto + i
                for j in extractTable(database, i):
                    if (i == table):
                        texto = texto + "".join(j)

            #print(texto)
            if mode == "MD5":
                return md5str(texto)
            else:
                return sha256str(texto)
        else:
            return None
    else:
        return None

def md5str(cadena):
    md5_hash = hashlib.md5()
    md5_hash.update(cadena.encode('utf8'))
    digest = md5_hash.hexdigest()
    return digest

def sha256str(cadena):
    md5_hash = hashlib.sha256()
    md5_hash.update(cadena.encode('utf8'))
    digest = md5_hash.hexdigest()
    return digest

def alterDatabaseEncoding(database , en):
    if not en in encoding:
        return 3
    else:
        db = buscar(database)
        if db is None:
            return 2
        else:
            db[2] = en
            return 0

def Codtexto(database , texto):
    for db in lista_db:
        if database == db[0]:
            try:
                texto.encode(db[2])
                return True
            except:
                return False

            
class bloque:
    def __init__(self, numero, data, anterior, hashid):
        self.id = numero
        self.data = data
        self.anterior = anterior
        self.hash = hashid

    def get(self):
        return [self.id, self.data, self.anterior, self.hash]

class blockchain:
    def __init__(self):
        self.id_bloques = 1
        self.anterior = 0000000000
        self.bloques = []

    def insertar(self, tablas):
        id_hash = sha256str(tablas)
        nuevo = bloque(self.id_bloques, tablas, self.anterior, id_hash)
        self.id_bloques +=1
        self.bloques.append(nuevo)
        file = open("bloques.json", "w+")
        file.write(json.dumps([j.get() for j in self.bloques]))
        self.anterior = id_hash

    def update(self, tabla, registro):
        file = open("bloques.json", "r")
        lista = json.loads(file.read())
        file.close()
        for bloque in lista:
            if registro == bloque[0]:
                bloque[1] = tabla
                bloque[3] = sha256str(tabla)

        file = open("bloques.json", "w+")
        file.write(json.dumps(lista))
        file.close()

    def retornarbloques(self):
        return self.bloques

    def graficarChain(self):
        code = "digraph g { \ngraph [ \nrankdir = LR\n]; \nnode [\nfontsize = 16 \nshape = record \n];\nedge [\n];\n"
        code += "node"+str(self.bloques[0].id)+" [ color=green, label = \"Hash actual: "+str(self.bloques[0].hash)+"\\nHash anterior: "+str(self.bloques[0].anterior)+"\"];\n"
        pos = 1
        while pos != len(self.bloques):
            if self.bloques[pos].anterior == self.bloques[pos-1].hash:
                code += "node"+str(self.bloques[pos].id)+" [ color=green, label = \"Hash actual: "+str(self.bloques[pos].hash)+"\\nHash anterior: "+str(self.bloques[pos].anterior)+"\"];\n"
                code += "node"+str(self.bloques[pos-1].id)+"->"+"node"+str(self.bloques[pos].id)+"\n"
                pos += 1
            else:
                code += "node"+str(self.bloques[pos].id)+" [ color=red, label = \"Hash actual: "+str(self.bloques[pos].hash)+"\\nHash anterior: "+str(self.bloques[pos].anterior)+"\"];\n"
                code += "node"+str(self.bloques[pos-1].id)+"->"+"node"+str(self.bloques[pos].id)+"\n"
                break
        code += "}"
        print(code)
        if code != "":
            tabGen = open("block.dot","w")
            tabGen.write(code)
            tabGen.close()
            tab = open("block.cmd","w")
            tab.write("dot -Tpng block.dot -o blockChain.png")
            tab.close()
        try:
            os.system('block.cmd')
            os.system('blockChain.png')
        except:
            return print("ERROR EN CORRER CMD O PNG")

def safeModeOn(database , table):
    if buscar(database) is not None:
        lista = showTables(database)
        for i in lista:
            for j in extractTable(database, i):
                if (i == table):
                    bc.insertar("".join(j))
                    bc.graficarChain()
    else:
        return None
            
bc = blockchain()
os.system('cls')
print(encrypt("este es el mensaje","llave"))
print(decrypt("","llave"))
