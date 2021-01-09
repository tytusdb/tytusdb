# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import os
from ..DataAccessLayer.handler import Handler
from ..DataAccessLayer.tree_graph import TreeGraph


def graphicTables(database: str):
    try:
        databases = Handler.rootinstance()
        for i in databases:
            if database == i.name:
                Handler.init_DirReports()
                fname = 'data/graph/db-tables.png'
                tables = open("data/graph/tables.dot", "w")
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
                os.system("dot -Tpng data/graph/tables.dot -o " + fname)
                os.remove('data/graph/tables.dot')
                return fname
    except:
        return None


def graphicDatabases():
    try:
        Handler.init_DirReports()
        databases = Handler.rootinstance()
        fname = 'data/graph/databases.png'
        tables = open("data/graph/databases.dot", "w")
        temporal = 'digraph databases{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                   'fillcolor="#45c2c5", shape="box",fontcolor="black", fontname="Century Gothic", fontsize=18];\n'
        c = 0
        for i in databases:
            temporal += "node" + str(c) + "[label=\"" + str(i.name).replace(' ', '') + "\"];\n"
            c += 1
        temporal += "}"
        tables.write(temporal)
        tables.close()
        os.system("dot -Tpng data/graph/databases.dot -o " + fname)
        os.remove('data/graph/databases.dot')
        return fname
    except:
        return None


def graphAVL(database: str, table: str):
    try:
        Handler.init_DirReports()
        avl = Handler.tableinstance(database, table)
        grafo = TreeGraph(avl)
        grafo.export()
        return 'data/graph/grafo-avl.png'
    except:
        return None


def graphTuple(database: str, table: str, index):
    try:
        Handler.init_DirReports()
        avl = Handler.tableinstance(database, table)
        tupla = avl.search(index)
        fname = 'data/graph/tupla.png'
        tuples = open("data/graph/tupla.dot", "w")
        temporal = 'digraph tables{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                   'fillcolor="#45c2c5",shape="box",fontcolor="black",fontname="Century Gothic", fontsize=18];\n'
        c = 0
        for registro in tupla:
            temporal += "node" + str(c) + "[label=\"" + str(registro).replace(' ', '') + "\"];\n"
            c += 1
        temporal += "}"
        tuples.write(temporal)
        tuples.close()
        os.system("dot -Tpng data/graph/tupla.dot -o " + fname)
        os.remove('data/graph/tupla.dot')
        return fname
    except:
        return None
