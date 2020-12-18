class Sentence:
    ''' '''

class CreateDatabase(Sentence):
    def __init__(self, name, ifNotExistsFlag, OrReplace, OwnerMode):
        self.name = name
        self.ifNotExistsFlag = ifNotExistsFlag
        self.OrReplace = OrReplace
        self.OwnerMode = OwnerMode

class ShowDatabases(Sentence):
    ''''''

class DropDatabase(Sentence):
    def __init__(self, name, ifExistsFlag):
        self.name = name
        self.ifExistsFlag = ifExistsFlag

class DropTable(Sentence):
    def __init__(self, name):
        self.name = name

class Use(Sentence):
    def __init__(self, name):
        self.name = name

class AlterDatabaseRename(Sentence):
    def __init__(self, oldname,newname):
        self.oldname = oldname
        self.newname = newname

class AlterDatabaseOwner(Sentence):
    def __init__(self, name, newowner):
        self.name = name
        self.newowner = newowner

class AlterTableDropColumn(Sentence):
    def __init__(self, table, column):
        self.table = table
        self.column = column

class AlterTableAddConstraintUnique(Sentence):
    def __init__(self, table, constraint, column):
        self.table = table
        self.constraint = constraint
        self.column = column

class AlterTableAddForeignKey(Sentence):
    def __init__(self, table, column, rel_table, rel_column):
        self.table = table
        self.column = column
        self.rel_table = rel_table
        self.rel_column = rel_column
        
class AlterTableAlterColumnSetNull(Sentence):
    def __init__(self, table, column, null):
        self.table = table
        self.column = column
        self.null = null

class AlterTableAlterColumnType(Sentence):
    def __init__(self, table, column, newtype):
        self.table = table
        self.column = column
        self.newtype = newtype # type [type,length] or type = [type] 
class AlterTableAddColumn(Sentence):
    def __init__(self, table, column, newtype):
        self.table = table
        self.column = column
        self.type = type # type [type,length] or type = [type] 

class AlterTableDropConstraint(Sentence):
    def __init__(self, table, constraint):
        self.table = table
        self.constraint = constraint

class Insert(Sentence):
    def __init__(self, table, columns, values):
        self.table = table
        self.columns = columns
        self.values = values

class InsertAll(Sentence):
    def __init__(self, table, values):
        self.table = table
        self.values = values

class Delete(Sentence):
    def __init__(self, table, expression):
        self.table = table
        self.expression = expression

class Truncate(Sentence):
    def __init__(self, tables):
        self.tables = tables

class Update(Sentence):
    def __init__(self, table, values, expression):
        self.table = table
        self.values = values #values = [value1,value2,...,valuen] -> value = [id,expression]  
        self.expression = expression

class CreateType(Sentence):
    def __init__(self, name, expressions):
        self.name = name
        self.expressions = expressions #expressions = [expression1,expression2,...,expressionn]

class CreateTable(Sentence):
    def __init__(self, name, columns, inherits):
        self.name = name
        self.columns = columns #columns = [column1,column2,...,columnn] Every Column is an instance of {'id','check','constraint','unique','primary','foreign'}
        self.inherits = inherits
        #Types:
        #column -> {ColumnId,ColumnCheck,ColumnConstraint,ColumnUnique,ColumnPrimaryKey,ColumnForeignKey}

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
class SelectMultiple(Sentence):
    def __init__(self, select1, operator, select2):
        self.select1 = select1
        self.operator = operator
        self.select2 = select2

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

class ColumnCheck(CreateTableOpt):
    def __init__(self, expression):
        self.expression = expression

class ColumnConstraint(CreateTableOpt):
    def __init__(self, name,expression):
        self.name = name
        self.expression = expression

class ColumnUnique(CreateTableOpt):
    def __init__(self, columnslist):
        self.columnslist = columnslist # is and idList [columnname1,columnname2,...,columnnamen]

class ColumnPrimaryKey(CreateTableOpt):
    def __init__(self, columnslist):
        self.columnslist = columnslist # is and idList [columnname1,columnname2,...,columnnamen]

class ColumnForeignKey(CreateTableOpt):
    def __init__(self, columnslist, columnslist_ref):
        self.columnslist = columnslist # is and idList [columnname1,columnname2,...,columnnamen]
        self.columnslist_ref = columnslist_ref # is and idList [refcolumnname1,refcolumnname2,...,refcolumnname
