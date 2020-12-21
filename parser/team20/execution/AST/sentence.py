class Sentence:
    ''' '''

class CreateDatabase(Sentence):
    def __init__(self, name, ifNotExistsFlag, OrReplace, OwnerMode):
        self.name = name
        self.ifNotExistsFlag = ifNotExistsFlag
        self.OrReplace = OrReplace
        self.OwnerMode = OwnerMode
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
    def graphAST(self, dot, parent):
      return ""

class DropTable(Sentence):
    def __init__(self, name):
        self.name = name
    def graphAST(self, dot, parent):
      return ""

class Use(Sentence):
    def __init__(self, name):
        self.name = name
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
      return ""

class AlterDatabaseOwner(Sentence):
    def __init__(self, name, newowner):
        self.name = name
        self.newowner = newowner
    def graphAST(self, dot, parent):
      return ""

class AlterTableDropColumn(Sentence):
    def __init__(self, table, column):
        self.table = table
        self.column = column
    def graphAST(self, dot, parent):
      return ""

class AlterTableAddConstraintUnique(Sentence):
    def __init__(self, table, constraint, column):
        self.table = table
        self.constraint = constraint
        self.column = column
    def graphAST(self, dot, parent):
      return ""

class AlterTableAddForeignKey(Sentence):
    def __init__(self, table, column, rel_table, rel_column):
        self.table = table
        self.column = column
        self.rel_table = rel_table
        self.rel_column = rel_column
    def graphAST(self, dot, parent):
      return ""
        
class AlterTableAlterColumnSetNull(Sentence):
    def __init__(self, table, column, null):
        self.table = table
        self.column = column
        self.null = null
    def graphAST(self, dot, parent):
      return ""

class AlterTableAlterColumnType(Sentence):
    def __init__(self, table, column, newtype):
        self.table = table
        self.column = column
        self.newtype = newtype # type [type,length] or type = [type]
    def graphAST(self, dot, parent):
      return "" 
class AlterTableAddColumn(Sentence):
    def __init__(self, table, column, newtype):
        self.table = table
        self.column = column
        self.type = type # type [type,length] or type = [type]
    def graphAST(self, dot, parent):
      return "" 

class AlterTableDropConstraint(Sentence):
    def __init__(self, table, constraint):
        self.table = table
        self.constraint = constraint
    def graphAST(self, dot, parent):
      return ""

class Insert(Sentence):
    def __init__(self, table, columns, values):
        self.table = table
        self.columns = columns
        self.values = values
    def graphAST(self, dot, parent):
      return ""

class InsertAll(Sentence):
    def __init__(self, table, values):
        self.table = table
        self.values = values
    def graphAST(self, dot, parent):
      return ""

class Delete(Sentence):
    def __init__(self, table, expression):
        self.table = table
        self.expression = expression
    def graphAST(self, dot, parent):
      return ""

class Truncate(Sentence):
    def __init__(self, tables):
        self.tables = tables
    def graphAST(self, dot, parent):
      return ""

class Update(Sentence):
    def __init__(self, table, values, expression):
        self.table = table
        self.values = values #values = [value1,value2,...,valuen] -> value = [id,expression]  
        self.expression = expression
    def graphAST(self, dot, parent):
      return ""

class CreateType(Sentence):
    def __init__(self, name, expressions):
        self.name = name
        self.expressions = expressions #expressions = [expression1,expression2,...,expressionn]
    def graphAST(self, dot, parent):
      return ""

class CreateTable(Sentence):
    def __init__(self, name, columns, inherits):
        self.name = name
        self.columns = columns #columns = [column1,column2,...,columnn] Every Column is an instance of {'id','check','constraint','unique','primary','foreign'}
        self.inherits = inherits
        #Types:
        #column -> {ColumnId,ColumnCheck,ColumnConstraint,ColumnUnique,ColumnPrimaryKey,ColumnForeignKey}
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
        return dot

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
    def graphAST(self, dot, parent):
      return ""
class SelectMultiple(Sentence):
    def __init__(self, select1, operator, select2):
        self.select1 = select1
        self.operator = operator
        self.select2 = select2
    def graphAST(self, dot, parent):
      return ""

class CreateTableOpt:
    ''' '''
class ColumnId(CreateTableOpt):
    def __init__(self, name, typo, options):
        self.name = name
        self.type = typo
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
    def graphAST(self, dot, parent):
      return ""

class ColumnCheck(CreateTableOpt):
    def __init__(self, expression):
        self.expression = expression
    def graphAST(self, dot, parent):
      return ""

class ColumnConstraint(CreateTableOpt):
    def __init__(self, name,expression):
        self.name = name
        self.expression = expression
    def graphAST(self, dot, parent):
      return ""

class ColumnUnique(CreateTableOpt):
    def __init__(self, columnslist):
        self.columnslist = columnslist # is and idList [columnname1,columnname2,...,columnnamen]
    def graphAST(self, dot, parent):
      return ""

class ColumnPrimaryKey(CreateTableOpt):
    def __init__(self, columnslist):
        self.columnslist = columnslist # is and idList [columnname1,columnname2,...,columnnamen]
    def graphAST(self, dot, parent):
      return ""

class ColumnForeignKey(CreateTableOpt):
    def __init__(self, columnslist, columnslist_ref):
        self.columnslist = columnslist # is and idList [columnname1,columnname2,...,columnnamen]
        self.columnslist_ref = columnslist_ref # is and idList [refcolumnname1,refcolumnname2,...,refcolumnname
    def graphAST(self, dot, parent):
      return ""
