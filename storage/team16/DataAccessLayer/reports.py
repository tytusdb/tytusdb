# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import os
from DataAccessLayer.handler import Handler
from DataAccessLayer.tree_graph import TreeGraph


def graphicTables(database: str):
    try:
        databases = Handler.rootinstance()
        for i in databases:
            if database == i.name:
                Handler.init_DirReports()
                fname = 'DataAccessLayer/imaging/db-tables.png'
                tables = open("DataAccessLayer/imaging/tables.dot", "w")
                temporal = 'digraph tables{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                           'fillcolor="#45c2c5",shape="box",fontcolor="black",fontname="Century Gothic", ' \
                           'fontsize=18];\n'
                c=0
                for table in i.tablesName:
                    temporal += "node" + str(c) + "[label=\"" + str(table).replace(' ', '') + "\"];\n"
                    c += 1
                temporal += "}"
                tables.write(temporal)
                tables.close()
                os.system("dot -Tpng DataAccessLayer/imaging/tables.dot -o " + fname)
                os.remove('DataAccessLayer/imaging/tables.dot')
                return fname
    except:
        return None


def graphicDatabases():
    try:
        Handler.init_DirReports()
        databases = Handler.rootinstance()
        fname = 'DataAccessLayer/imaging/databases.png'
        tables = open("DataAccessLayer/imaging/databases.dot", "w")
        temporal = 'digraph databases{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                   'fillcolor="#45c2c5", shape="box",fontcolor="black", fontname="Century Gothic", fontsize=18];\n'
        c = 0
        for i in databases:
            temporal += "node" + str(c) + "[label=\"" + str(i.name).replace(' ', '') + "\"];\n"
            c += 1
        temporal += "}"
        tables.write(temporal)
        tables.close()
        os.system("dot -Tpng DataAccessLayer/imaging/databases.dot -o " + fname)
        os.remove('DataAccessLayer/imaging/databases.dot')
        return fname
    except:
        return None


def graphAVL(database: str, table: str):
    try:
        Handler.init_DirReports()
        avl = Handler.tableinstance(database, table)
        grafo = TreeGraph(avl)
        grafo.export()
        return 'DataAccessLayer/imaging/grafo-avl.png'
    except:
        return None


def graphTuple(database: str, table: str, index):
    try:
        Handler.init_DirReports()
        avl = Handler.tableinstance(database, table)
        tupla = avl.search(index)
        fname = 'DataAccessLayer/imaging/tupla.png'
        tuples = open("DataAccessLayer/imaging/tupla.dot", "w")
        temporal = 'digraph tables{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                   'fillcolor="#45c2c5",shape="box",fontcolor="black",fontname="Century Gothic", fontsize=18];\n'
        c = 0
        for registro in tupla:
            temporal += "node" + str(c) + "[label=\"" + str(registro).replace(' ', '') + "\"];\n"
            c += 1
        temporal += "}"
        tuples.write(temporal)
        tuples.close()
        os.system("dot -Tpng DataAccessLayer/imaging/tupla.dot -o " + fname)
        os.remove('DataAccessLayer/imaging/tupla.dot')
        return fname
    except:
        return None
