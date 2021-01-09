# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import os
from ..Modules.handler import Handler
from .modes.avl_graph import AVLGraph
from .modes.bplus_graph import BplusGraph
from .modes.b_graph import BGraph
from .modes.hash_graph import HashGraph
from .modes.isam_graph import ISAMGraph

handler = Handler()


def init_DirReports():
    if not os.path.exists('_tmp_'):
        os.makedirs('_tmp_')


def graphicDatabases():
    try:
        init_DirReports()
        databases = Handler.rootinstance()
        fname = '_tmp_/databases.png'
        tables = open("_tmp_/databases.dot", "w")
        temporal = 'digraph databases{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                   'fillcolor="#45c2c5", shape="box",fontcolor="black", fontname="Century Gothic", fontsize=18];\n'
        c = 0
        for i in databases:
            temporal += "node" + str(c) + "[label=\"[" + i.mode + "]" + str(i.name).replace(' ', '') + "\"];\n"
            c += 1
        temporal += "}"
        tables.write(temporal)
        tables.close()
        os.system("dot -Tpng _tmp_/databases.dot -o " + fname)
        os.remove('_tmp_/databases.dot')
        return fname
    except:
        return None


def graphicTables(database: str):
    try:
        init_DirReports()
        databases = Handler.rootinstance()
        for i in databases:
            if i.name == database:
                fname = '_tmp_/db-tables.png'
                tables = open("_tmp_/tables.dot", "w")
                temporal = 'digraph tables{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                           'fillcolor="#45c2c5",shape="box",fontcolor="black",fontname="Century Gothic", ' \
                           'fontsize=18];\n'
                c = 0
                for table in i.tables:
                    temporal += "node" + str(c) + "[label=\"[" + table.mode + "]" + \
                                str(table.name).replace(' ', '') + "\"];\n"
                    c += 1
                temporal += "}"
                tables.write(temporal)
                tables.close()
                os.system("dot -Tpng _tmp_/tables.dot -o " + fname)
                os.remove('_tmp_/tables.dot')
                return fname
    except:
        return None


def graphicMode(database: str, table: str):
    init_DirReports()
    databases = Handler.rootinstance()
    db = None
    for i in databases:
        if i.name == database:
            db = i
            break
    _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
    structure = handler.tableinstance(_table.mode, database, table)
    action = "graph" + _table.mode + "(structure)"
    return eval(action)


def graphavl(table):
    try:
        grafo = AVLGraph(table)
        grafo.export()
        return '_tmp_/grafo-avl.png'
    except:
        return None


def graphbplus(table):
    try:
        grafo = BplusGraph(table)
        grafo.export()
        return '_tmp_/grafo-bplus.png'
    except:
        return None


def graphb(table):
    try:
        grafo = BGraph(table)
        grafo.export()
        return '_tmp_/grafo-b.png'
    except:
        return None


def graphhash(table):
    try:
        grafo = HashGraph(table)
        grafo.export()
        return '_tmp_/grafo-hash.png'
    except:
        return None


def graphisam(table):
    try:
        grafo = ISAMGraph(table)
        grafo.export()
        return '_tmp_/grafo-isam.png'
    except:
        return None


#
#
def graphTuple(data):
    try:
        init_DirReports()
        fname = '_tmp_/tupla.png'
        tuples = open("_tmp_/tupla.dot", "w")
        temporal = 'digraph tables{\ngraph[bgcolor="#0f1319"] \nnode[style="filled",color="black", ' \
                   'fillcolor="#45c2c5",shape="box",fontcolor="black",fontname="Century Gothic", fontsize=18];\n'
        c = 0
        for registro in data:
            temporal += "node" + str(c) + "[label=\"" + str(registro).replace(' ', '') + "\"];\n"
            c += 1
        temporal += "}"
        tuples.write(temporal)
        tuples.close()
        os.system("dot -Tpng _tmp_/tupla.dot -o " + fname)
        os.remove('_tmp_/tupla.dot')
        return fname
    except:
        return None


def graphBlockchain(database, table):
    try:
        fname = '_tmp_/blockchain.png'
        dot = open("_tmp_/blockchain.dot", "w")
        blocks = handler.readJSON(database, table)
        diag = 'digraph G{graph[bgcolor="#0f1319"]\n\n{rank=\"same\"}\n'
        diag += 'rankdir="LR"\nnode[shape="box", fontname="Century Gothic", fontsize=26, ' \
                'height=1.5, width=1.2];\nedge[penwidth=2, color="#145A32"];'
        first = True
        count = 0
        for block in blocks:
            if first:
                diag += str(block['id']) + "[style=\"filled\", fillcolor=\" " + block['color'] + "\"]\n"
                first = None
            else:
                diag += str(block['id']) + "[style=\"filled\", fillcolor=\" " + block['color'] + "\"]\n"
                diag += str(blocks[count - 1]['id']) + "->" + str(block['id']) + "\n"
            count += 1
        diag += "}"
        dot.write(diag)
        dot.close()
        os.system("dot -Tpng _tmp_/blockchain.dot -o " + fname)
        os.remove('_tmp_/blockchain.dot')
        return fname
    except:
        None
