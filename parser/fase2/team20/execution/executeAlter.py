from .storageManager import jsonMode
from .storageManager.TypeChecker import TCalterDatabase,TCSearchDatabase,TCalterDropPk,TCgetDatabase,TCaltertype,TCAlterIndex,TCcreateFunction,TCgetFunctions,TCdeleteFunction
from storageManager.TypeChecker_Manager import *
from .AST.error import * 
from .executeExpression import executeExpression,Relational

import os 
import json

import sys
sys.path.append("../")
from console import * 

def executeAlterDatabaseRename(self,database):
    mode=TCSearchDatabase(database)
    if(mode==1):
        return jsonMode.alterDatabase(database.oldname,database.newname)
    elif(mode==2):
        return jsonMode.alterDatabase(database.oldname,database.newname)
    elif(mode==3):
        return jsonMode.alterDatabase(database.oldname,database.newname)
    elif(mode==4):
        return jsonMode.alterDatabase(database.oldname,database.newname) 
    elif(mode==8):
        return jsonMode.alterDatabase(database.oldname,database.newname)
    else:
        print_error("SEMANTIC ERROR",'Mode between 1-5',2)
        return 1

def executeAlterTableDropPK(self,table):
    database=TCgetDatabase()
    mode=TCSearchDatabase(database)
    if(mode==1):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    elif(mode==2):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    elif(mode==3):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    elif(mode==4):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    elif(mode==8):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    else:
        print_error("SEMANTIC ERROR",'Mode between 1-5',2)
        return 1


def executeAlterType(self,table):
    database=TCgetDatabase()
    mode=TCSearchDatabase(database)
    if(mode==1):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5
    elif(mode==2):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5 
    elif(mode==3):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5
    elif(mode==4):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5 
    elif(mode==8):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5
    else:
        print_error("SEMANTIC ERROR",'Mode between 1-5',2)
        return 1


#def alterAddColumn(database: str, table: str, default: any) -> int:
#0 -> Successful operation
#1 -> Operation error
#2 -> Database does not exist
#3 -> Table does not exist

def executeAlterTableAddColumn(self, AlterTableAddColumn_):

    # AlterTableAddColumn : {
    #     table: "table_name",
    #     column: "column_name",
    #     type: "type_name"
    # }

    alterTableAddColumn: AlterTableAddColumn = AlterTableAddColumn_
    table_name = alterTableAddColumn.table
    column_name = alterTableAddColumn.column
    type_name = alterTableAddColumn.type
        
    TypeChecker_Manager_ = get_TypeChecker_Manager()

    if  TypeChecker_Manager_ != None:

        use_: str = get_use(TypeChecker_Manager_)
        if use_ != None:

            database_ = get_database(use_, TypeChecker_Manager_)
            if database_ != None:

                table_ = get_table(table_name, database_)
                if table_ != None:

                    column_ = get_column(column_name, table_)
                    if column_ == None:

                        try:
                            #success
                            result_AlterTableAddColumn = jsonMode.alterAddColumn(database_.name, table_.name, None)
                            if result_AlterTableAddColumn == 0:
                                new_column = column(column_name, [])
                                new_column.type_ = type_name
                                table_.columns.append(new_column)
                                save_TypeChecker_Manager(TypeChecker_Manager_)
                                print_success("QUERY", str(column_name) + " column added to " + str(table_.name) + " table",2)
                            elif result_AlterTableAddColumn == 1:
                                print_error("UNKNOWN ERROR", "Operation error",2)
                            elif result_AlterTableAddColumn == 2:
                                print_error("SEMANTIC ERROR", "Database does not exist",2)
                            elif result_AlterTableAddColumn == 3:
                                print_error("SEMANTIC ERROR", "Table does not exist",2)
                            else:
                                print_error("UNKNOWN ERROR", "Operation error",2)
                        except Exception as e:
                            print_error("UNKNOWN ERROR", "instruction not executed",2)
                            #print(e)

                    else:
                        print_error("SEMANTIC ERROR", "Column named " + column_.name + " already exists in the " + table_.name + " table",2)

                else:
                    print_error("SEMANTIC ERROR", "Table does not exist",2)

            else:
                print_error("SEMANTIC ERROR", "Database to use does not exist",2)

        else:
            print_warning("RUNTIME ERROR", "Undefined database to use",2)
        
    else:
        print_error("UNKNOWN ERROR", "instruction not executed",2)


#def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
#0 -> Successful operation
#1 -> Operation error
#2 -> Database does not exist
#3 -> Table does not exist
#4 -> The key cannot be deleted or the table will be without columns
#5 -> Column out of bounds

def executeAlterTableDropColumn(self, AlterTableDropColumn_):



    # AlterTableDropColumn : {
    #     table: "table_name",
    #     column: "column_name"
    # }

    alterTableDropColumn_: AlterTableDropColumn = AlterTableDropColumn_
    table_name = alterTableDropColumn_.table
    column_name = alterTableDropColumn_.column
        
    TypeChecker_Manager_ = get_TypeChecker_Manager()

    if  TypeChecker_Manager_ != None:

        use_: str = get_use(TypeChecker_Manager_)
        if use_ != None:

            database_ = get_database(use_, TypeChecker_Manager_)
            if database_ != None:

                table_ = get_table(table_name, database_)
                if table_ != None:

                    column_ = get_column(column_name, table_)
                    if column_ != None:

                        if column_.primary_ == None or column_.primary_ == False:

                            try:
                                #success
                                column_number = 0
                                i = 0
                                while i < len(table_.columns):
                                    if table_.columns[i].name == column_.name:
                                        column_number = i
                                        i = len(table_.columns)
                                    i += 1
                                result_AlterTableDropColumn = jsonMode.alterDropColumn(database_.name, table_.name, column_number)
                                if result_AlterTableDropColumn == 0:
                                    table_.columns.pop(column_number)
                                    save_TypeChecker_Manager(TypeChecker_Manager_)
                                    print_success("QUERY", str(column_name) + " column removed from " + str(table_.name) + " table",2)
                                elif result_AlterTableDropColumn == 1:
                                    print_error("UNKNOWN ERROR", "Operation error",2)
                                elif result_AlterTableDropColumn == 2:
                                    print_error("SEMANTIC ERROR", "Database does not exist",2)
                                elif result_AlterTableDropColumn == 3:
                                    print_error("SEMANTIC ERROR", "Table does not exist",2)
                                elif result_AlterTableDropColumn == 4:
                                    print_error("SEMANTIC ERROR", "The key cannot be deleted or the table will be without columns",2)
                                elif result_AlterTableDropColumn == 5:
                                    print_error("SEMANTIC ERROR", "Column out of bounds",2)
                                else:
                                    print_error("UNKNOWN ERROR", "Operation error",2)
                            except Exception as e:
                                print_error("UNKNOWN ERROR", "instruction not executed",2)
                                #print(e)

                        else:
                            print_error("SEMANTIC ERROR", "A column that is primary key cannot be dropped",2)

                    else:
                        print_error("SEMANTIC ERROR", str(column_name) + " column does not exist in " + table_.name + " table",2)

                else:
                    print_error("SEMANTIC ERROR", "Table does not exist",2)

            else:
                print_error("SEMANTIC ERROR", "Database to use does not exist",2)

        else:
            print_warning("RUNTIME ERROR", "Undefined database to use",2)
        
    else:
        print_error("UNKNOWN ERROR", "instruction not executed",2)

def executeAlterIndex(self,AlterIndex):
    database=TCgetDatabase()
    #print(TCcreateFunction('funcion3','fun3codigo3d',False))
    res=TCSearchDatabase(database)
    if res==1:
        return TCAlterIndex(database,AlterIndex.index,AlterIndex.oldname,AlterIndex.newname)
    elif res==2:
        return TCAlterIndex(database,AlterIndex.index,AlterIndex.oldname,AlterIndex.newname)
    elif res==3:
        return TCAlterIndex(database,AlterIndex.index,AlterIndex.oldname,AlterIndex.newname)
    elif res==4:
        return TCAlterIndex(database,AlterIndex.index,AlterIndex.oldname,AlterIndex.newname)
    elif res==5:
        return TCAlterIndex(database,AlterIndex.index,AlterIndex.oldname,AlterIndex.newname)
    else:
        print_error("SEMANTIC ERROR","Mode between 1-5")