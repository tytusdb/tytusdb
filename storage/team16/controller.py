from avltree_structure import AVLTreeStructure


class Controller:

    def __init__(self):
        self.structure = AVLTreeStructure()

    def execute(self, args, action):
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
            return self.structure.extractRangeTable(args[0], args[1], args[2], args[3])
        elif action == actions[9]:
            return self.structure.alterAddPK(args[0], args[1], args[2].split(','))
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
        #
        elif action == actions[17]:
            return self.structure.insert(args[0], args[1], args[2].split(','))
        # elif action == actions[18]:
        #     return self.structure.loadCSV(args[0], args[1], args[2])
        # elif action == actions[19]:
        #     return self.structure.extractRow(args[0], args[1], args[2].split(','))
        # elif action == actions[20]:
        #     return self.structure.update(args[0], args[1], args[2], args[3].split(','))
        elif action == actions[21]:
            return self.structure.delete(args[0], args[1], args[2].split(','))
        elif action == actions[22]:
            return self.structure.truncate(args[0], args[1])
        #
        # endregion

        else:
            return 6


class Enums:
    actions = {
        1: "Create DB",
        2: "Show DB",
        3: "Alter DB",
        4: "Drop DB",
        5: "Create Table",
        6: "Show Tables",
        7: "Extract Table",
        8: "Extract Range Table",
        9: "Add PK",
        10: "Drop PK",
        11: "Add FK",
        12: "Add Index",
        13: "Alter Table",
        14: "Add Column",
        15: "Drop Column",
        16: "Drop Table",
        17: "Inserts",
        18: "Load CSV",
        19: "Extract Row",
        20: "Update",
        21: "Delete",
        22: "Truncate"
    }
