# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16

import os
from ..handler import Handler

def generate(name: str, data: str):
    if not os.path.exists('./_tmp_'):
        os.makedirs('./_tmp_')
    old = name
    name = './_tmp_/' + name
    f = open(name + ".dot", "w")
    f.write(data)
    f.close()
    os.system("dot -Tjpg " + name + ".dot -o " + './_tmp_/' + old + ".jpg")
    os.system('_tmp_\\' + old + ".jpg")

def graphDSD(database: str):
    try:
        handler = Handler()
        if not isinstance(database, str) or handler.invalid(database):
            raise Exception()
        databases = handler.rootinstance()
        db, index = _exist(database, databases)
        if db
            generate("graphDSD", _generateDSD(db.tables, db.fk))
            return "graphDSD"
        return None
    except:
        return None

def _exist(database: str, databases):
    tmp = None
    index = -1
    for db in databases:
        if db.name.upper() == database.upper():
            index = databases.index(db)
            tmp = db
            break
    return tmp, index


def _generateDSD(tables, fks):
    content = "digraph Grafo{\nrankdir=LR;\nnode [shape=record];\n"
    for table in tables:
        aux = table.name + "[label=\""
        for column in range(table.numberColumns):
            if column == 0:
                aux = aux + "<c" + str(column) + ">" + str(column)
            else:
                aux = aux + "| <c" + str(column) + ">" + str(column)
        aux = aux + "\" ]; \n"
        aux = aux + "subgraph \"cluster_error." + table.name + "\" { label =\"" + table.name + "\";" \
                                                                            " " + table.name + ";} \n"
        if fks:
            for fk in table.fk:
                for col in fk[3]:
                    for pk in fk[5]:
                        aux = aux + fk[4] + ":c" + str(pk) + " -> " + fk[1] + ":c" + str(col) + " [color=red] \n"

        content = content + aux
    content = content + "}"
    return content

def graphDF(table):
    try:
        g = 'digraph g{\n    node[shape= circle, style= filled, fontname="Century Gothic", color="#006400", fillcolor="#90EE90"]\n    edge[color="#145A32"]\n    rankdir=LR\n'
        for i in range(table.numberColumns):
            if not i in table.unique:
                for j in table.unique:
                    g += "    " + str(j) + "->" + str(i) + "\n"
        g += '}'
        generate("DF_" + table.name, g)
        return "DF_" + table.name + ".png"
    except:
        return None