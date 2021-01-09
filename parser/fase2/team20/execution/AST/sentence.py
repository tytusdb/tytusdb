from io import StringIO  # Python3
import sys

class Sentence:
    ''' '''

class CreateDatabase(Sentence):
    def __init__(self, name, ifNotExistsFlag, OrReplace, OwnerMode):
        self.name = name
        self.ifNotExistsFlag = ifNotExistsFlag
        self.OrReplace = OrReplace
        self.OwnerMode = OwnerMode
    def __str__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.OwnerMode)
        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        #print(output)
        return "executeSentence(CreateDatabase,CreateDatabase('"+self.name+"',"+str(self.ifNotExistsFlag)+","+str(self.OrReplace)+","+str(output)[:-1]+"))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"CreateDatabase\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CREATE") + hash(self)) + '\n'
        dot += str(hash("CREATE") + hash(self)) + \
            '[label=\"' + "CREATE" + '\"]\n'
        if(self.OrReplace):
            dot += str(hash(self)) + '->' + \
            str(hash("OR") + hash(self)) + '\n'
            dot += str(hash("OR") + hash(self)) + \
                '[label=\"' + "OR" + '\"]\n'
            dot += str(hash(self)) + '->' + \
            str(hash("REPLACE") + hash(self)) + '\n'
            dot += str(hash("REPLACE") + hash(self)) + \
                '[label=\"' + "REPLACE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DATABASE") + hash(self)) + '\n'
        dot += str(hash("DATABASE") + hash(self)) + \
            '[label=\"' + "DATABASE" + '\"]\n'
        if(self.ifNotExistsFlag):
            dot += str(hash(self)) + '->' + \
            str(hash("IF") + hash(self)) + '\n'
            dot += str(hash("IF") + hash(self)) + \
                '[label=\"' + "IF" + '\"]\n'        
            dot += str(hash(self)) + '->' + \
            str(hash("NOT") + hash(self)) + '\n'
            dot += str(hash("NOT") + hash(self)) + \
                '[label=\"' + "NOT" + '\"]\n'        
            dot += str(hash(self)) + '->' + \
            str(hash("EXISTS") + hash(self)) + '\n'
            dot += str(hash("EXISTS") + hash(self)) + \
                '[label=\"' + "EXISTS" + '\"]\n'        
        dot += str(hash(self)) + '->' + \
            str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        if(self.OwnerMode[0] != None or self.OwnerMode[1] != None):
            dot += str(hash(self)) + '->' + \
            str(hash("ownerMode") + hash(self)) + '\n'
            dot += str(hash("ownerMode") + hash(self)) + \
                '[label=\"' + "ownerMode" + '\"]\n'
            if(self.OwnerMode[0] != None):
                dot += str(hash("ownerMode") + hash(self)) + '->' + \
                str(hash("OWNER") + hash("ownerMode") + hash(self)) + '\n'
                dot += str(hash("OWNER") + hash("ownerMode") + hash(self)) + \
                    '[label=\"' + "OWNER" + '\"]\n'
                dot += str(hash("ownerMode") + hash(self)) + '->' + \
                str(hash(self.OwnerMode[0]) + hash("ownerMode") + hash(self)) + '\n'
                dot += str(hash(self.OwnerMode[0]) + hash("ownerMode") + hash(self)) + \
                    '[label=\"' + self.OwnerMode[0] + '\"]\n'
            if(self.OwnerMode[1] != None):
                dot += str(hash("ownerMode") + hash(self)) + '->' + \
                str(hash("MODE") + hash("ownerMode") + hash(self)) + '\n'
                dot += str(hash("MODE") + hash("ownerMode") + hash(self)) + \
                    '[label=\"' + "MODE" + '\"]\n'
                dot+= self.OwnerMode[1].graphAST('',hash("ownerMode") + hash(self))
        return dot

class ShowDatabases(Sentence):
    ''''''
    def __str__(self):
        return "executeSentence(ShowDatabases,ShowDatabases())"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"ShowDatabases\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("SHOW") + hash(self)) + '\n'
        dot += str(hash("SHOW") + hash(self)) + \
            '[label=\"' + "SHOW" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DATABASES") + hash(self)) + '\n'
        dot += str(hash("DATABASES") + hash(self)) + \
            '[label=\"' + "DATABASES" + '\"]\n'
        return dot

class DropDatabase(Sentence):
    def __init__(self, name, ifExistsFlag):
        self.name = name
        self.ifExistsFlag = ifExistsFlag
    def __str__(self):
        return "executeSentence(DropDatabase,DropDatabase('"+self.name+"',"+str(self.ifExistsFlag)+"))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"DropDatabase\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DROP") + hash(self)) + '\n'
        dot += str(hash("DROP") + hash(self)) + \
            '[label=\"' + "DROP" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DATABASE") + hash(self)) + '\n'
        dot += str(hash("DATABASE") + hash(self)) + \
            '[label=\"' + "DATABASE" + '\"]\n'
        if(self.ifExistsFlag):
            dot += str(hash(self)) + '->' + \
            str(hash("IF") + hash(self)) + '\n'
            dot += str(hash("IF") + hash(self)) + \
                '[label=\"' + "IF" + '\"]\n'
            dot += str(hash(self)) + '->' + \
            str(hash("EXISTS") + hash(self)) + '\n'
            dot += str(hash("EXISTS") + hash(self)) + \
                '[label=\"' + "EXISTS" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        return dot

class DropTable(Sentence):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "executeSentence(DropTable,DropTable('"+self.name+"'))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"DropTable\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DROP") + hash(self)) + '\n'
        dot += str(hash("DROP") + hash(self)) + \
            '[label=\"' + "DROP" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TABLE") + hash(self)) + '\n'
        dot += str(hash("TABLE") + hash(self)) + \
            '[label=\"' + "TABLE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        return dot

class Use(Sentence):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "executeSentence(Use,Use('"+self.name+"'))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Use\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("USE") + hash(self)) + '\n'
        dot += str(hash("USE") + hash(self)) + \
            '[label=\"' + "USE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        return dot

class AlterDatabaseRename(Sentence):
    def __init__(self, oldname,newname):
        self.oldname = oldname
        self.newname = newname
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AlterDatabaseRename\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTER") + hash(self)) + '\n'
        dot += str(hash("ALTER") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DATABASE") + hash(self)) + '\n'
        dot += str(hash("DATABASE") + hash(self)) + \
            '[label=\"' + "DATABASE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.oldname) + hash(self)) + '\n'
        dot += str(hash(self.oldname) + hash(self)) + \
            '[label=\"' + self.oldname + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("RENAME") + hash(self)) + '\n'
        dot += str(hash("RENAME") + hash(self)) + \
            '[label=\"' + "RENAME" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TO") + hash(self)) + '\n'
        dot += str(hash("TO") + hash(self)) + \
            '[label=\"' + "TO" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.newname) + hash(self)) + '\n'
        dot += str(hash(self.newname) + hash(self)) + \
            '[label=\"' + self.newname + '\"]\n'
        return dot

class AlterDatabaseOwner(Sentence):
    def __init__(self, name, newowner):
        self.name = name
        self.newowner = newowner
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AlterDatabaseOwner\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTER") + hash(self)) + '\n'
        dot += str(hash("ALTER") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DATABASE") + hash(self)) + '\n'
        dot += str(hash("DATABASE") + hash(self)) + \
            '[label=\"' + "DATABASE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("OWNER") + hash(self)) + '\n'
        dot += str(hash("OWNER") + hash(self)) + \
            '[label=\"' + "OWNER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TO") + hash(self)) + '\n'
        dot += str(hash("TO") + hash(self)) + \
            '[label=\"' + "TO" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.newowner) + hash(self)) + '\n'
        dot += str(hash(self.newowner) + hash(self)) + \
            '[label=\"' + self.newowner + '\"]\n'
        return dot

class AlterTableDropColumn(Sentence):
    def __init__(self, table, column):
        self.table = table
        self.column = column
    def __str__(self):
        return "executeSentence(AlterTableDropColumn,AlterTableDropColumn('"+self.table+"','"+self.column+"'))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AlterTableDropColumn\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTER") + hash(self)) + '\n'
        dot += str(hash("ALTER") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TABLE") + hash(self)) + '\n'
        dot += str(hash("TABLE") + hash(self)) + \
            '[label=\"' + "TABLE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.table) + hash(self)) + '\n'
        dot += str(hash(self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DROP") + hash(self)) + '\n'
        dot += str(hash("DROP") + hash(self)) + \
            '[label=\"' + "DROP" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("COLUMN") + hash(self)) + '\n'
        dot += str(hash("COLUMN") + hash(self)) + \
            '[label=\"' + "COLUMN" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("C"+self.column) + hash(self)) + '\n'
        dot += str(hash("C"+self.column) + hash(self)) + \
            '[label=\"' + self.column + '\"]\n'
        return dot

class AlterTableAddConstraintUnique(Sentence):
    def __init__(self, table, constraint, column):
        self.table = table
        self.constraint = constraint
        self.column = column
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AlterTableAddConstraintUnique\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTER") + hash(self)) + '\n'
        dot += str(hash("ALTER") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TABLE") + hash(self)) + '\n'
        dot += str(hash("TABLE") + hash(self)) + \
            '[label=\"' + "TABLE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.table) + hash(self)) + '\n'
        dot += str(hash(self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ADD") + hash(self)) + '\n'
        dot += str(hash("ADD") + hash(self)) + \
            '[label=\"' + "ADD" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CONSTRAINT") + hash(self)) + '\n'
        dot += str(hash("CONSTRAINT") + hash(self)) + \
            '[label=\"' + "CONSTRAINT" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.constraint) + hash(self)) + '\n'
        dot += str(hash(self.constraint) + hash(self)) + \
            '[label=\"' + self.constraint + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("UNIQUE") + hash(self)) + '\n'
        dot += str(hash("UNIQUE") + hash(self)) + \
            '[label=\"' + "UNIQUE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.column) + hash(self)) + '\n'
        dot += str(hash(self.column) + hash(self)) + \
            '[label=\"' + self.column + '\"]\n'
        return dot

class AlterTableAddForeignKey(Sentence):
    def __init__(self, table, column, rel_table, rel_column):
        self.table = table
        self.column = column
        self.rel_table = rel_table
        self.rel_column = rel_column
    def __str__(self):
        return "executeSentence(AlterTableAddForeignKey,AlterTableAddForeignKey('"+self.table+"','"+self.column+"','"+self.rel_table+"','"+self.rel_column+"'))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AlterTableAddForeignKey\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTER") + hash(self)) + '\n'
        dot += str(hash("ALTER") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TABLE") + hash(self)) + '\n'
        dot += str(hash("TABLE") + hash(self)) + \
            '[label=\"' + "TABLE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("T"+self.table) + hash(self)) + '\n'
        dot += str(hash("T"+self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ADD") + hash(self)) + '\n'
        dot += str(hash("ADD") + hash(self)) + \
            '[label=\"' + "ADD" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("FOREIGN") + hash(self)) + '\n'
        dot += str(hash("FOREIGN") + hash(self)) + \
            '[label=\"' + "FOREIGN" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("KEY") + hash(self)) + '\n'
        dot += str(hash("KEY") + hash(self)) + \
            '[label=\"' + "KEY" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("C"+self.column) + hash(self)) + '\n'
        dot += str(hash("C"+self.column) + hash(self)) + \
            '[label=\"' + self.column + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("REFERENCES") + hash(self)) + '\n'
        dot += str(hash("REFERENCES") + hash(self)) + \
            '[label=\"' + "REFERENCES" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.rel_table) + hash(self)) + '\n'
        dot += str(hash(self.rel_table) + hash(self)) + \
            '[label=\"' + self.rel_table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("RC"+self.rel_column) + hash(self)) + '\n'
        dot += str(hash("RC"+self.rel_column) + hash(self)) + \
            '[label=\"' + self.rel_column + '\"]\n'
        return dot
        
class AlterTableAlterColumnSetNull(Sentence):
    def __init__(self, table, column, null):
        self.table = table
        self.column = column
        self.null = null
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AlterTableAlterColumnSetNull\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTER") + hash(self)) + '\n'
        dot += str(hash("ALTER") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TABLE") + hash(self)) + '\n'
        dot += str(hash("TABLE") + hash(self)) + \
            '[label=\"' + "TABLE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("T"+self.table) + hash(self)) + '\n'
        dot += str(hash("T"+self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTERC") + hash(self)) + '\n'
        dot += str(hash("ALTERC") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("COLUMN") + hash(self)) + '\n'
        dot += str(hash("COLUMN") + hash(self)) + \
            '[label=\"' + "COLUMN" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.column) + hash(self)) + '\n'
        dot += str(hash(self.column) + hash(self)) + \
            '[label=\"' + self.column + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("SET") + hash(self)) + '\n'
        dot += str(hash("SET") + hash(self)) + \
            '[label=\"' + "SET" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("null") + hash(self)) + '\n'
        dot += str(hash("null") + hash(self)) + \
            '[label=\"' + "null" + '\"]\n'
        dot += str(hash("null") +hash(self)) + '->' + \
        str(hash("null") + hash(str(self.null)) + hash(self)) + '\n'
        dot += str(hash("null") + hash(str(self.null)) + hash(self)) + \
            '[label=\"' + str(self.null) + '\"]\n'
        return dot

class AlterTableAlterColumnType(Sentence):
    def __init__(self, table, column, newtype):
        self.table = table
        self.column = column
        self.newtype = newtype # type [type,length] or type = [type]
    def __str__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.newtype)
        ty = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "executeSentence(AlterTableAlterColumnType,AlterTableAlterColumnType('"+self.table+"','"+self.column+"',"+ty+"))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AlterTableAlterColumnType\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTER") + hash(self)) + '\n'
        dot += str(hash("ALTER") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TABLE") + hash(self)) + '\n'
        dot += str(hash("TABLE") + hash(self)) + \
            '[label=\"' + "TABLE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("T"+self.table) + hash(self)) + '\n'
        dot += str(hash("T"+self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTERC") + hash(self)) + '\n'
        dot += str(hash("ALTERC") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("COLUMN") + hash(self)) + '\n'
        dot += str(hash("COLUMN") + hash(self)) + \
            '[label=\"' + "COLUMN" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("C"+self.column) + hash(self)) + '\n'
        dot += str(hash("C"+self.column) + hash(self)) + \
            '[label=\"' + self.column + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TYPE") + hash(self)) + '\n'
        dot += str(hash("TYPE") + hash(self)) + \
            '[label=\"' + "TYPE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.newtype[0]) + hash(self)) + '\n'
        dot += str(hash(self.newtype[0]) + hash(self)) + \
            '[label=\"' + self.newtype[0] + '\"]\n'
        return dot 
class AlterTableAddColumn(Sentence):
    def __init__(self, table, column, type):
        self.table = table
        self.column = column
        self.type = type # type [type,length] or type = [type]
    def __str__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.type)
        ty = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "executeSentence(AlterTableAddColumn,AlterTableAddColumn('"+self.table+"','"+self.column+"',"+ty+"))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AlterTableAddColumn\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTER") + hash(self)) + '\n'
        dot += str(hash("ALTER") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TABLE") + hash(self)) + '\n'
        dot += str(hash("TABLE") + hash(self)) + \
            '[label=\"' + "TABLE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("T"+self.table) + hash(self)) + '\n'
        dot += str(hash("T"+self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ADD") + hash(self)) + '\n'
        dot += str(hash("ADD") + hash(self)) + \
            '[label=\"' + "ADD" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("COLUMN") + hash(self)) + '\n'
        dot += str(hash("COLUMN") + hash(self)) + \
            '[label=\"' + "COLUMN" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("C"+self.column) + hash(self)) + '\n'
        dot += str(hash("C"+self.column) + hash(self)) + \
            '[label=\"' + self.column + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.type[0]) + hash(self)) + '\n'
        dot += str(hash(self.type[0]) + hash(self)) + \
            '[label=\"' + self.type[0] + '\"]\n'
        return dot 

class AlterTableDropConstraint(Sentence):
    def __init__(self, table, constraint):
        self.table = table
        self.constraint = constraint
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AlterTableDropConstraint\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ALTER") + hash(self)) + '\n'
        dot += str(hash("ALTER") + hash(self)) + \
            '[label=\"' + "ALTER" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TABLE") + hash(self)) + '\n'
        dot += str(hash("TABLE") + hash(self)) + \
            '[label=\"' + "TABLE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("T"+self.table) + hash(self)) + '\n'
        dot += str(hash("T"+self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DROP") + hash(self)) + '\n'
        dot += str(hash("DROP") + hash(self)) + \
            '[label=\"' + "DROP" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CONSTRAINT") + hash(self)) + '\n'
        dot += str(hash("CONSTRAINT") + hash(self)) + \
            '[label=\"' + "CONSTRAINT" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("C"+self.constraint) + hash(self)) + '\n'
        dot += str(hash("C"+self.constraint) + hash(self)) + \
            '[label=\"' + self.constraint + '\"]\n'
        return dot

class AlterIndex(Sentence):
    def __init__(self,index,oldname, newname):
        self.index= index
        self.oldname = oldname #id
        self.newname = newname #id
    def __str__(self):
        return "executeSentence(AlterIndex,AlterIndex('"+str(self.index)+"','"+str(self.oldname)+"','"+str(self.newname)+"'))"
    def graphAST(self,dot,parent):
        return ""
    

class Insert(Sentence):
    def __init__(self, table, columns, values):
        self.table = table
        self.columns = columns
        self.values = values
    def __str__(self):
        return "executeSentence(Insert,Insert('"+str(self.table)+"',"+str(self.columns)+","+str(self.values)+"))"
    
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Insert\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("INSERT") + hash(self)) + '\n'
        dot += str(hash("INSERT") + hash(self)) + \
            '[label=\"' + "INSERT" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("INTO") + hash(self)) + '\n'
        dot += str(hash("INTO") + hash(self)) + \
            '[label=\"' + "INTO" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.table) + hash(self)) + '\n'
        dot += str(hash(self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("Columns") + hash(self)) + '\n'
        dot += str(hash("Columns") + hash(self)) + \
            '[label=\"' + "Columns" + '\"]\n'
        for column in self.columns:
            dot += str(hash("Columns") + hash(self)) + '->' + \
            str(hash("Columns") + hash(self) + hash(column)) + '\n'
            dot += str(hash("Columns") + hash(self)+hash(column)) + \
                '[label=\"' + column + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("VALUES") + hash(self)) + '\n'
        dot += str(hash("VALUES") + hash(self)) + \
            '[label=\"' + "VALUES" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("Values") + hash(self)) + '\n'
        dot += str(hash("Values") + hash(self)) + \
            '[label=\"' + "Values" + '\"]\n'
        for value in self.values:
            dot+= value.graphAST('',str(hash("Values") + hash(self)))
        return dot

class InsertAll(Sentence):
    def __init__(self, table, values):
        self.table = table
        self.values = values
    def __str__(self):
        return "executeSentence(InsertAll,InsertAll('"+str(self.table)+"',"+str(self.values)+"))"

    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"InsertAll\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("INSERT") + hash(self)) + '\n'
        dot += str(hash("INSERT") + hash(self)) + \
            '[label=\"' + "INSERT" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("INTO") + hash(self)) + '\n'
        dot += str(hash("INTO") + hash(self)) + \
            '[label=\"' + "INTO" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.table) + hash(self)) + '\n'
        dot += str(hash(self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("VALUES") + hash(self)) + '\n'
        dot += str(hash("VALUES") + hash(self)) + \
            '[label=\"' + "VALUES" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("Values") + hash(self)) + '\n'
        dot += str(hash("Values") + hash(self)) + \
            '[label=\"' + "Values" + '\"]\n'
        for value in self.values:
            dot+= value.graphAST('',str(hash("Values") + hash(self)))
        return dot

class Delete(Sentence):
    def __init__(self, table, expression):
        self.table = table
        self.expression = expression
    def __str__(self):
        return "executeSentence(Delete,Delete('"+str(self.table)+"',"+str(self.expression)+"))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Delete\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("DELETE") + hash(self)) + '\n'
        dot += str(hash("DELETE") + hash(self)) + \
            '[label=\"' + "DELETE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("FROM") + hash(self)) + '\n'
        dot += str(hash("FROM") + hash(self)) + \
            '[label=\"' + "FROM" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.table) + hash(self)) + '\n'
        dot += str(hash(self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("WHERE") + hash(self)) + '\n'
        dot += str(hash("WHERE") + hash(self)) + \
            '[label=\"' + "WHERE" + '\"]\n'
        dot += self.expression.graphAST('',str(hash("WHERE") + hash(self)))
        return dot   

class Truncate(Sentence):
    def __init__(self, tables):
        self.tables = tables
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Truncate\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TRUNCATE") + hash(self)) + '\n'
        dot += str(hash("TRUNCATE") + hash(self)) + \
            '[label=\"' + "TRUNCATE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("Tables") + hash(self)) + '\n'
        dot += str(hash("Tables") + hash(self)) + \
            '[label=\"' + "Tables" + '\"]\n'
        for table in self.tables:
            dot += str(hash("Tables") + hash(self)) + '->' + \
            str(hash("Tables") + hash(self) + hash(table)) + '\n'
            dot += str(hash("Tables") + hash(self) + hash(table)) + \
                '[label=\"' + table + '\"]\n'
        return dot

class Update(Sentence):
    def __init__(self, table, values, expression):
        self.table = table
        self.values = values #values = [value1,value2,...,valuen] -> value = [id,expression]  
        self.expression = expression
    def __str__(self):
        return "executeSentence(Update,Update('"+self.table+"',"+str(self.values)+","+str(self.expression)+"))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Update\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("UPDATE") + hash(self)) + '\n'
        dot += str(hash("UPDATE") + hash(self)) + \
            '[label=\"' + "UPDATE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.table) + hash(self)) + '\n'
        dot += str(hash(self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("SET") + hash(self)) + '\n'
        dot += str(hash("SET") + hash(self)) + \
            '[label=\"' + "SET" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("Values") + hash(self)) + '\n'
        dot += str(hash("Values") + hash(self)) + \
            '[label=\"' + "Values" + '\"]\n'
        for value in self.values:
            dot += str(hash("Values") + hash(self)) + '->' + \
            str(hash("Values") + hash(self) + hash(value[0])) + '\n'
            dot += str(hash("Values") + hash(self) + hash(value[0])) + \
                '[label=\"' + value[0] + '\"]\n'
            dot+= value[1].graphAST('',str(hash("Values") + hash(self)))
        dot += str(hash(self)) + '->' + \
        str(hash("WHERE") + hash(self)) + '\n'
        dot += str(hash("WHERE") + hash(self)) + \
            '[label=\"' + "WHERE" + '\"]\n'
        dot += self.expression.graphAST('',str(hash("WHERE") + hash(self)))        
        return dot

class CreateType(Sentence):
    def __init__(self, name, expressions):
        self.name = name
        self.expressions = expressions #expressions = [expression1,expression2,...,expressionn]
    def __str__(self):
       
        return "executeSentence(CreateType,CreateType('"+str(self.name)+"',"+str(self.expressions)+"))"
    
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"CreateType\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CREATE") + hash(self)) + '\n'
        dot += str(hash("CREATE") + hash(self)) + \
            '[label=\"' + "CREATE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TYPE") + hash(self)) + '\n'
        dot += str(hash("TYPE") + hash(self)) + \
            '[label=\"' + "TYPE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("AS") + hash(self)) + '\n'
        dot += str(hash("AS") + hash(self)) + \
            '[label=\"' + "AS" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ENUM") + hash(self)) + '\n'
        dot += str(hash("ENUM") + hash(self)) + \
            '[label=\"' + "ENUM" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("expressions") + hash(self)) + '\n'
        dot += str(hash("expressions") + hash(self)) + \
            '[label=\"' + "expressions" + '\"]\n'
        for expression in self.expressions:
            dot+= expression.graphAST('',str(hash("expressions") + hash(self)))
        return dot

class CreateTable(Sentence):
    def __init__(self, name, columns, inherits):
        self.name = name
        self.columns = columns #columns = [column1,column2,...,columnn] Every Column is an instance of {'id','check','constraint','unique','primary','foreign'}
        self.inherits = inherits
        #Types:
        #column -> {ColumnId,ColumnCheck,ColumnConstraint,ColumnUnique,ColumnPrimaryKey,ColumnForeignKey}
    def __str__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.columns)
        col = new_stdout.getvalue()
        sys.stdout = old_stdout
        #print(col)
        inh="None"
        if self.inherits != None:
            inh="'"+self.inherits+"'"
        return "executeSentence(CreateTable,CreateTable('"+self.name+"',"+str(col)[:-1]+","+str(inh)+"))"
    
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"CreateTable\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CREATE") + hash(self)) + '\n'
        dot += str(hash("CREATE") + hash(self)) + \
            '[label=\"' + "CREATE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("TABLE") + hash(self)) + '\n'
        dot += str(hash("TABLE") + hash(self)) + \
            '[label=\"' + "TABLE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("columns") + hash(self)) + '\n'
        dot += str(hash("columns") + hash(self)) + \
            '[label=\"' + "columns" + '\"]\n'
        for column in self.columns:
            dot+= column.graphAST('',str(hash("columns") + hash(self)))
        return dot

class CreateIndex(Sentence):
    def __init__(self, name,table,ascdesc):
        self.name = name #id
        self.table= table #id
        self.ascdesc = ascdesc #ASC |DESC
    def __str__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.ascdesc)
        asdc = new_stdout.getvalue()
        sys.stdout = old_stdout
        return "executeSentence(CreateIndex,CreateIndex('"+self.name+"','"+self.table+"',"+str(asdc)[:-1]+"))"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"CreateIndex\"]\n'
        return dot

class DropIndex(Sentence):
    def __init__(self, name,ifExistsFlag):
        self.name = name #id
        self.ifExistsFlag= ifExistsFlag  #bool
    def __str__(self):
        return "executeSentence(DropIndex,DropIndex('"+self.name+"',"+str(self.ifExistsFlag)+"))"
    def graphAST(self,dot,parent):
        return ""
    

class Select(Sentence):
    def __init__(self, columns, distinct, tables, options):
        self.columns = columns
        self.distinct = distinct
        self.tables = tables
        self.options = options # options = {'where','orderby','limit','offset','groupby','having'} or None
        # options se puede acceder a los items de la forma options['nombrepropiedad'] si no existe devuelve 'nombrepropiedad'
        # where -> Expression
        # orderby -> SortExpressionList
            # sortExpressionList -> lista de expresiones de la forma [Expression,ASC/DESC]
        # limit -> Expression/ALL ALL is the same as omitting the LIMIT clause
        # offset -> Expression OFFSET says to skip that many rows before beginning to return rows. OFFSET 0 is the same as omitting the OFFSET clause. 
            # If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        # groupby -> ExpressionList
        # having -> Expression
    def __str__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.columns)
        col = new_stdout.getvalue()
        sys.stdout = old_stdout
        tab="None"
        opt="None"
        if self.tables!=None:
            old_stdout = sys.stdout
            new_stdout = StringIO()
            sys.stdout = new_stdout
            print(self.tables)
            tab = new_stdout.getvalue()[:-1]
            sys.stdout = old_stdout
        if self.options!=None:
            old_stdout = sys.stdout
            new_stdout = StringIO()
            sys.stdout = new_stdout
            print(self.options)
            opt = new_stdout.getvalue()[:-1]
            sys.stdout = old_stdout
        #print(output)
        return "executeSentence(Select,Select("+col[:-1]+","+str(self.distinct)+","+tab+","+opt+"))"
    
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Select\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("SELECT") + hash(self)) + '\n'
        dot += str(hash("SELECT") + hash(self)) + \
            '[label=\"' + "SELECT" + '\"]\n'
        if(self.distinct):
            dot += str(hash(self)) + '->' + \
            str(hash("DISTINCT") + hash(self)) + '\n'
            dot += str(hash("DISTINCT") + hash(self)) + \
                '[label=\"' + "DISTINCT" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("Columns") + hash(self)) + '\n'
        dot += str(hash("Columns") + hash(self)) + \
            '[label=\"' + "Columns" + '\"]\n'
        for column in self.columns:
            dot += column.graphAST('',str(hash("Columns") + hash(self)))
        if(self.tables != None):
            dot += str(hash(self)) + '->' + \
            str(hash("Tables") + hash(self)) + '\n'
            dot += str(hash("Tables") + hash(self)) + \
                '[label=\"' + "Tables" + '\"]\n'
            for table in self.tables:
                dot += table.graphAST('',str(hash("Tables") + hash(self)))
            if (bool(self.options)):
                dot += str(hash(self)) + '->' + \
                str(hash("Options") + hash(self)) + '\n'
                dot += str(hash("Options") + hash(self)) + \
                    '[label=\"' + "Options" + '\"]\n'
                try:
                    self.options['where']
                    dot += str(hash("Options") +hash(self)) + '->' + \
                    str(hash("WhereClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("WhereClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "WhereClause" + '\"]\n'
                    dot += str(hash("WhereClause") + hash("Options") +hash(self)) + '->' + \
                    str(hash("WHERE")+hash("WhereClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("WHERE")+hash("WhereClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "WHERE" + '\"]\n'
                    dot += self.options['where'].graphAST('',str(hash("WhereClause") + hash("Options") +hash(self)))
                except:
                    pass
                try:
                    self.options['limit']
                    dot += str(hash("Options") +hash(self)) + '->' + \
                    str(hash("LimitClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("LimitClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "LimitClause" + '\"]\n'
                    dot += str(hash("LimitClause") + hash("Options") +hash(self)) + '->' + \
                    str(hash("LIMIT")+hash("LimitClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("LIMIT")+hash("LimitClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "LIMIT" + '\"]\n'
                    if(self.options['limit']!='ALL'):
                        dot += self.options['limit'].graphAST('',str(hash("LimitClause") + hash("Options") +hash(self)))
                    else:
                        dot += str(hash("LimitClause") + hash("Options") +hash(self)) + '->' + \
                        str(hash("ALL")+hash("LimitClause") + hash("Options") +hash(self)) + '\n'
                        dot += str(hash("ALL")+hash("LimitClause") + hash("Options") +hash(self)) + \
                            '[label=\"' + "ALL" + '\"]\n'
                except:
                    pass
                try:
                    self.options['offset']
                    dot += str(hash("Options") +hash(self)) + '->' + \
                    str(hash("OffsetClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("OffsetClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "OffsetClause" + '\"]\n'
                    dot += str(hash("OffsetClause") + hash("Options") +hash(self)) + '->' + \
                    str(hash("OFFSET")+hash("OffsetClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("OFFSET")+hash("OffsetClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "OFFSET" + '\"]\n'
                    dot += self.options['offset'].graphAST('',str(hash("OffsetClause") + hash("Options") +hash(self)))
                except:
                    pass
                try:
                    self.options['orderby']
                    dot += str(hash("Options") + hash(self)) + '->' + \
                    str(hash("OrderByClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("OrderByClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "OrderByClause" + '\"]\n'
                    dot += str(hash("OrderByClause") + hash("Options") +hash(self)) + '->' + \
                    str(hash("ORDER")+hash("OrderByClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("ORDER")+hash("OrderByClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "ORDER" + '\"]\n'
                    dot += str(hash("OrderByClause") + hash("Options") +hash(self)) + '->' + \
                    str(hash("BY")+hash("OrderByClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("BY")+hash("OrderByClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "BY" + '\"]\n'
                    for sortexpression in self.options['orderby']:
                        dot += sortexpression[0].graphAST('',str(hash("OrderByClause") + hash("Options") +hash(self)))
                        dot += str(hash("OrderByClause") + hash("Options") +hash(self)) + '->' + \
                        str(hash(sortexpression[0])+hash(sortexpression[1])+hash("OrderByClause") + hash(self)) + '\n'
                        dot += str(hash(sortexpression[0])+hash(sortexpression[1])+hash("OrderByClause") + hash(self)) + \
                            '[label=\"' + sortexpression[1] + '\"]\n'
                except:
                    pass
                try:
                    self.options['groupby']
                    dot += str(hash("Options") +hash(self)) + '->' + \
                    str(hash("GroupbyClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("GroupbyClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "GroupbyClause" + '\"]\n'
                    dot += str(hash("GroupbyClause") + hash("Options") +hash(self)) + '->' + \
                    str(hash("GROUP")+hash("GroupbyClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("GROUP")+hash("GroupbyClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "GROUP" + '\"]\n'
                    dot += str(hash("GroupbyClause") + hash("Options") +hash(self)) + '->' + \
                    str(hash("BY")+hash("GroupbyClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("BY")+hash("GroupbyClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "BY" + '\"]\n'
                    for expression in self.options['groupby']:
                        dot += expression.graphAST('',str(hash("GroupbyClause") + hash("Options") +hash(self)))
                except:
                    pass
                try:
                    self.options['having']
                    dot += str(hash("Options") +hash(self)) + '->' + \
                    str(hash("HavingClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("HavingClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "HavingClause" + '\"]\n'
                    dot += str(hash("HavingClause") + hash("Options") +hash(self)) + '->' + \
                    str(hash("HAVING")+hash("HavingClause") + hash("Options") +hash(self)) + '\n'
                    dot += str(hash("HAVING")+hash("HavingClause") + hash("Options") +hash(self)) + \
                        '[label=\"' + "HAVING" + '\"]\n'
                    dot += self.options['having'].graphAST('',str(hash("HavingClause") + hash("Options") +hash(self)))
                except:
                    pass
        return dot
class SelectMultiple(Sentence):
    def __init__(self, select1, operator, select2):
        self.select1 = select1
        self.operator = operator
        self.select2 = select2
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"'+self.operator+'\"]\n'
        dot += self.select1.graphAST('',str(hash(self)))
        dot += self.select2.graphAST('',str(hash(self)))
        return dot

class CreateTableOpt:
    ''' '''
class ColumnId(CreateTableOpt):
    def __init__(self, name, type, options):
        self.name = name
        self.type = type
        self.options = options #options = {'default','null','primary','reference','unique','constraint','check'}
        # options se puede acceder a los items de la forma options['nombrepropiedad'] si no existe devuelve 'nombrepropiedad'
        # default -> Expression
        # null -> True/False
        # primary -> True
        # reference -> ID
        # unique -> True
        # constraintunique -> ID
        # check -> Expression
        # constraintcheck -> ID,Expression
    def __repr__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.type)
        ty = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.options)
        val2 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "ColumnId('"+self.name+"',"+ty+","+val2+")"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"ColumnId\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.type[0]) + hash(self)) + '\n'
        dot += str(hash(self.type[0]) + hash(self)) + \
            '[label=\"' + self.type[0] + '\"]\n'
        if(bool(self.options)):
            dot += str(hash(self)) + '->' + \
            str(hash("Options") + hash(self)) + '\n'
            dot += str(hash("Options") + hash(self)) + \
                '[label=\"' + "Options" + '\"]\n'
            try:
                self.options['default']
                dot += str(hash("Options") + hash(self)) + '->' + \
                str(hash("Options") + hash(self) + hash("default")) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("default")) + \
                    '[label=\"' + "default" + '\"]\n'
                dot += self.options['default'].graphAST('',str(hash("Options") + hash(self)+ hash("default")))
            except:
                pass
            try:
                self.options['null']
                dot += str(hash("Options") + hash(self)) + '->' + \
                str(hash("Options") + hash(self) + hash("null")) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("null")) + \
                    '[label=\"' + "null" + '\"]\n'
                dot += str(hash("Options") + hash(self)+ hash("null")) + '->' + \
                str(hash("Options") + hash(self) + hash("null")+ hash(str(self.options['null']))) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("null") + hash(str(self.options['null']))) + \
                    '[label=\"' + str(self.options['null']) + '\"]\n'
            except:
                pass
            try:
                self.options['primary']
                dot += str(hash("Options") + hash(self)) + '->' + \
                str(hash("Options") + hash(self) + hash("primarykey")) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("primarykey")) + \
                    '[label=\"' + "primarykey" + '\"]\n'
                dot += str(hash("Options") + hash(self)+ hash("primarykey")) + '->' + \
                str(hash("Options") + hash(self) + hash("primarykey")+ hash(str(self.options['primary']))) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("primarykey") + hash(str(self.options['primary']))) + \
                    '[label=\"' + str(self.options['primary']) + '\"]\n'
            except:
                pass
            try:
                self.options['reference']
                dot += str(hash("Options") + hash(self)) + '->' + \
                str(hash("Options") + hash(self) + hash("reference")) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("reference")) + \
                    '[label=\"' + "reference" + '\"]\n'
                dot += str(hash("Options") + hash(self)+ hash("reference")) + '->' + \
                str(hash("Options") + hash(self) + hash("reference")+ hash(str(self.options['reference']))) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("reference") + hash(str(self.options['reference']))) + \
                    '[label=\"' + str(self.options['reference']) + '\"]\n'
            except:
                pass
            try:
                self.options['unique']
                dot += str(hash("Options") + hash(self)) + '->' + \
                str(hash("Options") + hash(self) + hash("unique")) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("unique")) + \
                    '[label=\"' + "unique" + '\"]\n'
                dot += str(hash("Options") + hash(self)+ hash("unique")) + '->' + \
                str(hash("Options") + hash(self) + hash("unique")+ hash(str(self.options['unique']))) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("unique") + hash(str(self.options['unique']))) + \
                    '[label=\"' + str(self.options['unique']) + '\"]\n'
            except:
                pass
            try:
                self.options['constraintunique']
                dot += str(hash("Options") + hash(self)) + '->' + \
                str(hash("Options") + hash(self) + hash("constraintunique")) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("constraintunique")) + \
                    '[label=\"' + "constraintunique" + '\"]\n'
                dot += str(hash("Options") + hash(self)+ hash("constraintunique")) + '->' + \
                str(hash("Options") + hash(self) + hash("constraintunique")+ hash(str(self.options['constraintunique']))) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("constraintunique") + hash(str(self.options['constraintunique']))) + \
                    '[label=\"' + str(self.options['constraintunique']) + '\"]\n'
            except:
                pass
            try:
                self.options['check']
                dot += str(hash("Options") + hash(self)) + '->' + \
                str(hash("Options") + hash(self) + hash("check")) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("check")) + \
                    '[label=\"' + "check" + '\"]\n'
                dot += self.options['check'].graphAST('',str(hash("Options") + hash(self)+ hash("check")))
            except:
                pass
            try:
                self.options['constraintcheck']
                dot += str(hash("Options") + hash(self)) + '->' + \
                str(hash("Options") + hash(self) + hash("constraintcheck")) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("constraintcheck")) + \
                    '[label=\"' + "constraintcheck" + '\"]\n'
                dot += str(hash("Options") + hash(self)+ hash("constraintcheck")) + '->' + \
                str(hash("Options") + hash(self) + hash("constraintcheck")+ hash(str(self.options['constraintcheck'][0]))) + '\n'
                dot += str(hash("Options") + hash(self)+ hash("constraintcheck") + hash(str(self.options['constraintcheck'][0]))) + \
                    '[label=\"' + str(self.options['constraintunique'][0]) + '\"]\n'
                dot += self.options['constraintcheck'][1].graphAST('',str(hash("Options") + hash(self)+ hash("constraintcheck")))
            except:
                pass
        return dot

class ColumnCheck(CreateTableOpt):
    def __init__(self, expression):
        self.expression = expression
    def __repr__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.expression)
        val2 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "ColumnCheck("+str(val2)+")"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"ColumnCheck\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CHECK") + hash(self)) + '\n'
        dot += str(hash("CHECK") + hash(self)) + \
            '[label=\"' + "CHECK" + '\"]\n'
        dot +=  self.expression.graphAST('',str(hash(self)))
        return dot

class ColumnConstraint(CreateTableOpt):
    def __init__(self, name,expression):
        self.name = name
        self.expression = expression
    def __repr__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.expression)
        val2 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "ColumnConstraint('"+self.name+"',"+str(val2)+")"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"ColumnConstraint\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CONSTRAINT") + hash(self)) + '\n'
        dot += str(hash("CONSTRAINT") + hash(self)) + \
            '[label=\"' + "CONSTRAINT" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CHECK") + hash(self)) + '\n'
        dot += str(hash("CHECK") + hash(self)) + \
            '[label=\"' + "CHECK" + '\"]\n'
        dot +=  self.expression.graphAST('',str(hash(self)))
        return dot

class ColumnUnique(CreateTableOpt):
    def __init__(self, columnslist):
        self.columnslist = columnslist # is and idList [columnname1,columnname2,...,columnnamen]
    def __repr__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.columnslist)
        val2 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "ColumnUnique("+str(val2)+")"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"ColumnUnique\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("UNIQUE") + hash(self)) + '\n'
        dot += str(hash("UNIQUE") + hash(self)) + \
            '[label=\"' + "UNIQUE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("idList") + hash(self)) + '\n'
        dot += str(hash("idList") + hash(self)) + \
            '[label=\"' + "idList" + '\"]\n'
        for column in self.columnslist:
            dot += str(hash("idList") + hash(self)) + '->' + \
            str(hash("idList") + hash(self) + hash(column)) + '\n'
            dot += str(hash("idList") + hash(self) + hash(column)) + \
                '[label=\"' + column + '\"]\n'
        return dot

class ColumnPrimaryKey(CreateTableOpt):
    def __init__(self, columnslist):
        self.columnslist = columnslist # is and idList [columnname1,columnname2,...,columnnamen]
    def __repr__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.columnslist)
        val2 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "ColumnPrimaryKey("+str(val2)+")"
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"ColumnPrimaryKey\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("PRIMARY") + hash(self)) + '\n'
        dot += str(hash("PRIMARY") + hash(self)) + \
            '[label=\"' + "PRIMARY" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("KEY") + hash(self)) + '\n'
        dot += str(hash("KEY") + hash(self)) + \
            '[label=\"' + "KEY" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("idList") + hash(self)) + '\n'
        dot += str(hash("idList") + hash(self)) + \
            '[label=\"' + "idList" + '\"]\n'
        for column in self.columnslist:
            dot += str(hash("idList") + hash(self)) + '->' + \
            str(hash("idList") + hash(self) + hash(column)) + '\n'
            dot += str(hash("idList") + hash(self) + hash(column)) + \
                '[label=\"' + column + '\"]\n'
        return dot

class ColumnForeignKey(CreateTableOpt):
    def __init__(self, columnslist, table, columnslist_ref):
        self.columnslist = columnslist # is and idList [columnname1,columnname2,...,columnnamen]
        self.table = table
        self.columnslist_ref = columnslist_ref # is and idList [refcolumnname1,refcolumnname2,...,refcolumnname
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"ColumnForeignKey\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("FOREIGN") + hash(self)) + '\n'
        dot += str(hash("FOREIGN") + hash(self)) + \
            '[label=\"' + "FOREIGN" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("KEY") + hash(self)) + '\n'
        dot += str(hash("KEY") + hash(self)) + \
            '[label=\"' + "KEY" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("idList") + hash(self)) + '\n'
        dot += str(hash("idList") + hash(self)) + \
            '[label=\"' + "idList" + '\"]\n'
        for column in self.columnslist:
            dot += str(hash("idList") + hash(self)) + '->' + \
            str(hash("idList") + hash(self) + hash(column)) + '\n'
            dot += str(hash("idList") + hash(self) + hash(column)) + \
                '[label=\"' + column + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("REFERENCES") + hash(self)) + '\n'
        dot += str(hash("REFERENCES") + hash(self)) + \
            '[label=\"' + "REFERENCES" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.table) + hash(self)) + '\n'
        dot += str(hash(self.table) + hash(self)) + \
            '[label=\"' + self.table + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("idRefList") + hash(self)) + '\n'
        dot += str(hash("idRefList") + hash(self)) + \
            '[label=\"' + "idList" + '\"]\n'
        for column in self.columnslist_ref:
            dot += str(hash("idRefList") + hash(self)) + '->' + \
            str(hash("idRefList") + hash(self) + hash(column)) + '\n'
            dot += str(hash("idRefList") + hash(self) + hash(column)) + \
                '[label=\"' + column + '\"]\n'
        return dot
