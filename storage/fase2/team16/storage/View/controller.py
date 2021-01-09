# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from . import reports
# from ..Modules.Complements import graph
from .. import storage as s


# from ..DataAccessLayer.handler import Handler


class Controller:

    @staticmethod
    def execute(args, action):
        try:
            actions = Enums.actions

            # region Database
            if action == actions[1]:
                pass
                return s.createDatabase(args[0], args[1], args[2])
            elif action == actions[2]:
                tmp = s.showDatabases()
                print("Databases:")
                print(tmp)
                return tmp
            elif action == actions[3]:
                return s.alterDatabase(args[0], args[1])
            elif action == actions[4]:
                return s.dropDatabase(args[0])
            # endregion

            # region Tables
            elif action == actions[5]:
                return s.createTable(args[0], args[1], int(args[2]))
            elif action == actions[6]:
                tmp = s.showTables(args[0])
                print("Tables from " + args[0] + ":")
                print(tmp)
                return tmp
            elif action == actions[7]:
                tmp = s.extractTable(args[0], args[1])
                print("Data from " + args[0] + "\\" + args[1] + ":")
                print(tmp)
                return tmp
            elif action == actions[8]:
                tmp = s.extractRangeTable(args[0], args[1], int(args[2]), args[3], args[4])
                print("Data from " + args[0] + "\\" + args[1] + " with range " + args[3] + " - " + args[4])
                print(tmp)
                return tmp
            elif action == actions[9]:
                return s.alterAddPK(args[0], args[1], list(map(int, args[2].split(','))))
            elif action == actions[10]:
                return s.alterDropPK(args[0], args[1])
            elif action == actions[13]:
                return s.alterTable(args[0], args[1], args[2])
            elif action == actions[14]:
                return s.alterAddColumn(args[0], args[1], args[2])
            elif action == actions[15]:
                return s.alterDropColumn(args[0], args[1], int(args[2]))
            elif action == actions[16]:
                return s.dropTable(args[0], args[1])
            # endregion

            # region Tuples
            elif action == actions[17]:
                return s.insert(args[0], args[1], args[2].split(','))
            elif action == actions[18]:
                tmp = s.loadCSV(args[0], args[1], args[2])
                print("csv:")
                print(tmp)
                return tmp
            elif action == actions[19]:
                tmp = s.extractRow(args[0], args[1], list(map(int, args[2].split(','))))
                print("Tuple from " + args[0] + "\\" + args[1] + ":")
                print(tmp)
                return tmp
            elif action == actions[20]:
                return s.update(args[0], args[1], args[2], list(map(int, args[3].split(','))))
            elif action == actions[21]:
                return s.delete(args[0], args[1], list(map(int, args[2].split(','))))
            elif action == actions[22]:
                return s.truncate(args[0], args[1])
            elif action == actions[23]:
                s.dropAll()
            elif action == actions[24]:
                return s.alterDatabaseMode(args[0],args[1])
            elif action == actions[25]:
                return s.alterTableMode(args[0],args[1],args[2])
            elif action == actions[26]:
                return s.alterTableCompress(args[0],args[1],int(args[2]))
            elif action == actions[27]:
                return s.alterTableDecompress(args[0],args[1])
            elif action == actions[28]:
                return s.graphDSD(args[0])
            elif action == actions[29]:
                return s.graphDF(args[0],args[1])
            # endregion
            else:
                return 6
        except:
            return 7
    
    @staticmethod
    def getDBS_Security() -> list:
        return s.DBS_Safe()
    
    @staticmethod
    def getTBS_Security(database: str) -> list:
        return s.TBL_Safe(database)

    @staticmethod
    def reportDB():
        return reports.graphicDatabases()

    @staticmethod
    def reportTBL(database: str):
        return reports.graphicTables(database)

    @staticmethod
    def reportMode(database: str, table: str):
        return reports.graphicMode(database, table)

    @staticmethod
    def reportTPL(tuples):
        tuples = tuples.split(",")
        return reports.graphTuple(tuples)

    @staticmethod
    def getIndexes(database: str, table: str):
        return s.extractTable(database, table)
    
    @staticmethod
    def graphBlockchain(database: str, table: str):
        return reports.graphBlockchain(database, table)
    
    @staticmethod
    def getGraph(graph: str):
        return '_tmp_/' + str(graph) + '.png'



class Enums:
    actions = {
        1: "Create database",
        2: "Show databases",
        3: "Alter database",
        4: "Drop database",
        5: "Create table",
        6: "Show tables",
        7: "Extract table",
        8: "Extract range",
        9: "Alter add PK",
        10: "Alter drop PK",
        11: "Alter add FK",
        12: "Alter add index",
        13: "Alter table",
        14: "Add column",
        15: "Drop column",
        16: "Drop table",
        17: "Insert",
        18: "Load CSV",
        19: "Extract row",
        20: "Update",
        21: "Delete",
        22: "Truncate",
        23: "Format DMS",
        24: "Alter DB mode",
        25: "Alter TBL mode",
        26: "Alt compress",
        27: "Alt decompress",
        28: "graphDSD -> Estructuras",
        29: "graphDF -> Dependencias"
    }
