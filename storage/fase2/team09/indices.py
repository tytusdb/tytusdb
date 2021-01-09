from .storage.b import BMode as b
from .storage.hash import HashMode as hash
from .storage.isam import ISAMMode as isam
from .storage.bplus import BPlusMode as bplus
from .storage.avl import avlMode as avl
from .storage.json import jsonMode as json
from .storage.dict import DictMode as dict
import os
import pickle
# from PIL import Image

class Fks:
    def __init__(self,db,tab,index,columns,tableRef,columnRef,ind):
        self.db=db
        self.table = tab
        self.indexName = index
        self.columns = columns
        self.tableRef = tableRef
        self.columnRef = columnRef
        self.colintab = ind
Indices = {}
def __init__():
    global Indices
    if os.path.exists("Data/Indices.bin"):
        Indices = CargarIndicesBIN()


def CargarIndicesBIN():
    # f = open('./data/avlMode/root.dat', 'wb')
    # f.close()
    with open("Data/Indices.bin", "rb") as r:
        content = pickle.load( r)
    return content

def write():
    with open("Data/Indices.bin","wb") as w:
        pickle.dump(Indices, w )

def alterTableAddFK(database, table, indexName, columns,  tableRef, columnsRef, modo, co):
    try:
        lc=len(columns)
        lcr=len(columnsRef)
        if lc==lcr:
            #cantidad exacta entre culumns y columnsRef
            Indices[indexName]=Fks(database, table,indexName,columns,tableRef,columnsRef,co+1)
            actualMod(modo).alterAddColumn(database,table,indexName)
            actualMod(modo).createTable(database, indexName, 4)
            actualMod(modo).insert(database,indexName,[table,columns,tableRef,columnsRef])
            write()
            return 0
        else:
            return 4
    except:
        return 1


def alterTableDropFK(database, table, indexName, modo):
    try:
        if indexName in Indices:
            #si existe el index
            actualMod(modo).alterDropColumn(database, table, Indices[indexName].colintab)
            actualMod(modo).dropTable(database, indexName)
            del Indices[indexName]
            write()
            return 0
        else:
            return 4
    except:
        return 1

def alterTableAddUnique(database, table, indexName, columns, modo,co):
    try:
        lc=len(columns)
        lcr=len(columnsRef)
        if lc==lcr:
            #cantidad exacta entre columns y columnsRef
            if not indexName in Indices:
                #restriccion de unicidad
                Indices[indexName]= Fks(database, table,indexName,columns,None,None,co+1)
                actualMod(modo).alterAddColumn(database,table,indexName)
                actualMod(modo).createTable(database, indexName, 2)
                actualMod(modo).insert(database,indexName,[table,columns])
                write()
                return 0
            else:
                return 5
        else:
            return 4
    except:
        return 1

def alterTableDropUnique(database, table, indexName, modo):
    try:
        if indexName in Indices:
            #nombre de indice si existe
            actualMod(modo).alterDropColumn(database, table, Indices[indexName].colintab)
            actualMod(modo).dropTable(database, indexName)
            del Indices[indexName]
            write()
            return 0
        else:
            return 4
    except:
        return 1

def alterTableAddIndex(database, table, indexName, columns, modo,co):
    try:
        lc=len(columns)
        lcr=len(columnsRef)
        if lc==lcr:
            #cantidad exacta entre columns y columnsRef
            Indices[indexName]= Fks(database, table,indexName,columns,None,None,co+1)
            actualMod(modo).alterAddColumn(database,table,indexName)
            actualMod(modo).createTable(database, indexName, 2)
            actualMod(modo).insert(database,indexName,[table,columns])
            write()
            return 0
        else:
            return 4
    except:
        return 1

def alterTableDropIndex(database, table, indexName, modo):
    try:
        if indexName in Indices:
            #index si existe 
            actualMod(modo).alterDropColumn(database, table, Indices[indexName].colintab)
            actualMod(modo).dropTable(database, indexName)
            del Indices[indexName]
            write()
            return 0
        else:
            return 4
    except:
        return 1


def graphDSD(database):
    try:
        texto = ''''''
        texto += '''digraph G {
            graph [ordering="out"];\n randkdir=TB;\nnode [shape=square];'''
        for d in Indices:
            if d.db == database:
                if not d.tableRef == None:
                    texto+= str(d.table)+''' -> '''+str(d.tableRef)+''';\n'''
        texto += '''\n}'''
        g=open("graphDSD.dot","w")
        g.write(texto)
        g.close()
        os.system('dot -Tpng graphDSD.dot -o graphDSD.png')
        os.system('graphDSD.png')
        img=Image.open("graphDSD.png")
        img.show()
        return texto
    except:
        return None
    
def actualMod(mode):
    if mode == "avl":
        return avl
    elif mode == "b":
        return b
    elif mode == "bplus":
        return bplus
    elif mode == "dict":
        return dict
    elif mode == "isam":
        return isam
    elif mode == "json":
        return json
    elif mode == "hash":
        return hash


def graficar(ncol,database,tablindicese):
    usado=[]
    for d in range(0,ncol):
        usado.append(d)
    col=[]
    llaves=[]
    indicescol=[]
    archivo = open( 'graph.dot', 'w')
    archivo.write('digraph D{\ngraph[bgcolor="#0f1319"]\n')
    #archivo.write(
     #       'node [shape= circle, style= filled, fontname="Century Gothic", color="#006400", fillcolor="#90EE90"]; \n')
    #archivo.write('edge[color="#145A32"]')
    archivo.write(
            "label= <<font color=\"white\">\"  GRAFO DF  DE TABLA '" + tablindicese+ "' BASE -> '"+database+"' \" </font>> fontname=\"Century Gothic\" \n")

    for d in Indices:
        if d.db == database:
            for numero in range(0,d.columns+1):
                col.append(numero)
            for pk in d.columns:
                archivo.write(str(pk)+'[ label ="'+str(pk)+'"];\n')
                llaves.append(pk)
            for i in d.columneRef:
                archivo.write(str(i)+'[ label ="'+str(i)+'"];\n')
                indicescol.append(i)


    for d in llaves:
        for indi in indicescol:
            archivo.write(str(d)+ "->" + str(indi)+"\n")

    for us in usado:
        if us in llaves:
            usado.remove(us)
        if us in indicescol:
            usado.remove(us)
            

    for d in llaves:
        for indi in usado:    
            archivo.write(str(d)+ "->" + str(indi)+"\n")

    for d in indicescol:
        for indi in usado:    
            archivo.write(str(d)+ "->" + str(indi)+"\n")

    os.system('dot -Tpng graph.dot -o graph.png')
    os.system('graph.png')