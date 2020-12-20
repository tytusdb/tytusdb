import os
from DataAccessLayer.handler import Handler
def graphicTables(database: str):
    try:
        databases = Handler.leerArchivoDB()
        for i in databases:
            if database == i.name:
                if not os.path.exists("DataAccessLayer/imaging"):
                    os.makedirs("DataAccessLayer/imaging")
                tables = open("DataAccessLayer/imaging/tables.dot", "w")
                temporal = 'digraph tables{\nnode[style="filled",fillcolor="black",shape="box",fontcolor="white"];\n'
                for table in i.tablesName:
                    temporal += table + ";\n"
                temporal += "}"
                tables.write(temporal)
                tables.close()
                os.system("dot -Tpng DataAccessLayer/imaging/tables.dot -o DataAccessLayer/imaging/tables.png")
    except:
        None

def graphicDatabases():
    try:
        databases = Handler.leerArchivoDB()
        if not os.path.exists("DataAccessLayer/imaging"):
            os.makedirs("DataAccessLayer/imaging")
        tables = open("DataAccessLayer/imaging/databases.dot", "w")
        temporal = 'digraph databases{\nnode[style="filled",fillcolor="black",shape="box",fontcolor="white"];\n'
        for i in databases:
            temporal += str(i.name) + ";\n"
        temporal += "}"
        tables.write(temporal)
        tables.close()
        os.system("dot -Tpng DataAccessLayer/imaging/databases.dot -o DataAccessLayer/imaging/databases.png")
    except:
        None