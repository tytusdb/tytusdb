import DataAccessLayer.reports as Reports
import avlMode as AVLTreeStructure
from DataAccessLayer.handler import Handler
from Models.avl_tree import AVLTree

class Controller:

    def __init__(self):
        self.structure = AVLTreeStructure

    def execute(self, args, action):
        try:
            actions = Enums.actions

            # region Database
            if action == actions[1]:
                return self.structure.createDatabase(args[0])
            elif action == actions[2]:
                return self.structure.showDatabases()
            elif action == actions[3]:
                return self.structure.alterDatabase(args[0], args[1])
            elif action == actions[4]:
                return self.structure.dropDatabase(args[0])
            # endregion

            # region Tables
            elif action == actions[5]:
                return self.structure.createTable(args[0], args[1], int(args[2]))
            elif action == actions[6]:
                return self.structure.showTables(args[0])
            elif action == actions[7]:
                return self.structure.extractTable(args[0], args[1])
            elif action == actions[8]:
                return self.structure.extractRangeTable(args[0], args[1], int(args[2]), args[3], args[4])
            elif action == actions[9]:
                return self.structure.alterAddPK(args[0], args[1], list(map(int,args[2].split(','))))
            elif action == actions[10]:
                return self.structure.alterDropPK(args[0], args[1])
            elif action == actions[13]:
                return self.structure.alterTable(args[0], args[1], args[2])
            elif action == actions[14]:
                return self.structure.alterAddColumn(args[0], args[1], args[2])
            elif action == actions[15]:
                return self.structure.alterDropColumn(args[0], args[1], int(args[2]))
            elif action == actions[16]:
                return self.structure.dropTable(args[0], args[1])
            # endregion

            # region Tuples
            elif action == actions[17]:
                return self.structure.insert(args[0], args[1], args[2].split(','))
            elif action == actions[18]:
                return self.structure.loadCSV(args[0], args[1], args[2])
            elif action == actions[19]:
                return self.structure.extractRow(args[0], args[1], list(map(int,args[2].split(','))))
            elif action == actions[20]:
                return self.structure.update(args[0], args[1], args[2], list(map(int,args[3].split(','))))
            elif action == actions[21]:
                return self.structure.delete(args[0], args[1], list(map(int,args[2].split(','))))
            elif action == actions[22]:
                return self.structure.truncate(args[0], args[1])
            elif action == actions[23]:
                self.structure.dropAll()
            # endregion
            else:
                return 6
        except:
            return 7
    
    def reportDB(self):
        return Reports.graphicDatabases()
    
    def reportTBL(self, database: str):
        return Reports.graphicTables(database)
    
    def reportAVL(self, database: str, table: str):
        return Reports.graphAVL(database, table)
    
    def reportTPL(self, database: str, table: str, llave):
        return Reports.graphTuple(database, table, llave)
    
    def getIndexes(self, database: str, table:str):
        avl_temp = Handler.tableinstance(database, table)
        return avl_temp.indexes()


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
        23: "Format DMS"
    }