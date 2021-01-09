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
    os.system("dot -Tpng " + name + ".dot -o " + './_tmp_/' + old + ".png")
    # os.system('_tmp_\\' + old + ".jpg")


def graphDSD(database: str):
    try:
        handler = Handler()
        if not isinstance(database, str) or handler.invalid(database):
            raise Exception()
        databases = handler.rootinstance()
        db, index = _exist(database, databases)
        if db:
            generate("graphDSD", _generateDSD(db.tables, db.fk))
            return "/_tmp_/graphDSD.dot"
        return None
    except:
        return None


def graphDF(database: str, table: str):
    try:
        handler = Handler()
        if not isinstance(database, str) or handler.invalid(database):
            raise Exception()
        databases = handler.rootinstance()
        db, index = _exist(database, databases)
        if db:
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if _table:
                generate("graphDF", _generateDF(_table))
                return "/_tmp_/graphDF.dot"
            return None
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
                for col in fk[2]:
                    for pk in fk[4]:
                        aux = aux + fk[3] + ":c" + str(pk) + " -> " + fk[1] + ":c" + str(col) + " [color=red] \n"

        content = content + aux
    content = content + "}"
    return content


def _generateDF(table):
    g = 'digraph g{\n  graph[bgcolor="#0f1319"]\n  node[shape= circle, style= filled, fontname="Century Gothic", ' \
        'color="#006400", ' \
        'fillcolor="#90EE90"]\n    edge[color="#145A32"]\n    rankdir=LR\n'
    columns = [x[2] for x in table.unique]
    tmp = []
    for t in columns:
        for y in t:
            tmp.append(y)
    for i in range(table.numberColumns):
        if not i in tmp:
            for j in tmp:
                g += "    " + str(j) + "->" + str(i) + "\n"
    g += '}'
    return g
