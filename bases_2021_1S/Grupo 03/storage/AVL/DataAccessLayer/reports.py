# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import os
from storage.AVL.DataAccessLayer.handler import Handler
from storage.AVL.DataAccessLayer.tree_graph import TreeGraph


def graphicTables(database: str):
    try:
        databases = Handler.rootinstance()
        for i in databases:
            if database == i.name:
                Handler.init_DirReports()
                fname = 'tmp/db-tables.png'
                tables = open("tmp/tables.dot", "w")
                temporal = 'digraph tables{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                           'fillcolor="#45c2c5",shape="box",fontcolor="black",fontname="Century Gothic", ' \
                           'fontsize=18];\n'
                c = 0
                for table in i.tablesName:
                    temporal += "node" + \
                        str(c) + "[label=\"" + \
                        str(table).replace(' ', '') + "\"];\n"
                    c += 1
                temporal += "}"
                tables.write(temporal)
                tables.close()
                os.system("dot -Tpng tmp/tables.dot -o " + fname)
                os.remove('tmp/tables.dot')
                return fname
    except:
        return None


def graphicDatabases():
    try:
        Handler.init_DirReports()
        databases = Handler.rootinstance()
        fname = 'tmp/databases.png'
        tables = open("tmp/databases.dot", "w")
        temporal = 'digraph databases{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                   'fillcolor="#45c2c5", shape="box",fontcolor="black", fontname="Century Gothic", fontsize=18];\n'
        c = 0
        for i in databases:
            temporal += "node" + \
                str(c) + "[label=\"" + str(i.name).replace(' ', '') + "\"];\n"
            c += 1
        temporal += "}"
        tables.write(temporal)
        tables.close()
        os.system("dot -Tpng tmp/databases.dot -o " + fname)
        os.remove('tmp/databases.dot')
        return fname
    except:
        return None


def graphAVL(database: str, table: str):
    try:
        Handler.init_DirReports()
        avl = Handler.tableinstance(database, table)
        grafo = TreeGraph(avl)
        grafo.export()
        return 'tmp/grafo-avl.png'
    except:
        return None


def graphTuple(database: str, table: str, index):
    try:
        Handler.init_DirReports()
        avl = Handler.tableinstance(database, table)
        tupla = avl.search(index)
        fname = 'tmp/tupla.png'
        tuples = open("tmp/tupla.dot", "w")
        temporal = 'digraph tables{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                   'fillcolor="#45c2c5",shape="box",fontcolor="black",fontname="Century Gothic", fontsize=18];\n'
        c = 0
        for registro in tupla:
            temporal += "node" + \
                str(c) + "[label=\"" + \
                str(registro).replace(' ', '') + "\"];\n"
            c += 1
        temporal += "}"
        tuples.write(temporal)
        tuples.close()
        os.system("dot -Tpng tmp/tupla.dot -o " + fname)
        os.remove('tmp/tupla.dot')
        return fname
    except:
        return None
