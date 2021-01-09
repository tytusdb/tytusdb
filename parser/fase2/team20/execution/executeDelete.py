from .AST.sentence import Delete
from .AST.expression import Relational, Logical
from .executeExpression import executeExpression
from storageManager.TypeChecker_Manager import *
from .storageManager.jsonMode import *
from .AST.error import *

import sys
sys.path.append("../")
from console import print_error, print_success


#def delete(database: str, table: str, columns: list) -> int:
#0 -> Successful operation
#1 -> Operation error    
#2 -> Database does not exist
#3 -> Table does not exist
#4 -> Primary key does not exist
#anything else -> Operation error

def executeDelete(self, Delete_):

    # Delete : {
    #     table: "table_name",
    #     expression: expression
    # }

    # expression : { (Relational | Logical}

    # Relational : {
    #     value1: Value,
    #     value2: Value,
    #     type: ("=" | "!=" | "<>" | ">" | "<" | ">=" | "<=")
    # }
    
    # Logical : {
    #     value1: (Logical | Relational),
    #     value2: (Logical | Relational),
    #     type: ("AND" | "OR")
    # }

    delete_: Delete = Delete_
    table_name = delete_.table
    expression_ = delete_.expression

    relational_ = get_first_relational(self, expression_)
    if relational_ != None:
        
        TypeChecker_Manager_ = get_TypeChecker_Manager()
        if  TypeChecker_Manager_ != None:
        
            use_: str = get_use(TypeChecker_Manager_)
            if use_ != None:
            
                database_ = get_database(use_, TypeChecker_Manager_)
                if database_ != None:
                
                    table_ = get_table(table_name, database_)
                    if table_ != None:
                    
                        result1 = executeExpression(self, relational_.value1)
                        result2 = executeExpression(self, relational_.value2)
                        result_type = relational_.type

                        column_ = get_column(str(result1.value), table_)
                        if column_ != None:

                            #----------------------------------------------------------------------
                            column_number_to_compare = 0
                            i = 0
                            while i < len(table_.columns):
                                if table_.columns[i].name == column_.name:
                                    column_number_to_compare = i
                                    i = len(table_.columns)
                                i += 1                            

                            table_records = extractTable(database_.name, table_.name)
                            table_record_to_delete = []
                            i = 0
                            while i < len(table_records):
                                if(result_type == '='):
                                    if str(table_records[i][column_number_to_compare]) == str(result2.value):
                                        table_record_to_delete.append(table_records[i])
                                elif(result_type == '!=' or result_type == '<>'):
                                    if str(table_records[i][column_number_to_compare]) != str(result2.value):
                                        table_record_to_delete.append(table_records[i])
                                elif(result_type == '>'):
                                    if str(table_records[i][column_number_to_compare]) > str(result2.value):
                                        table_record_to_delete.append(table_records[i])
                                elif(result_type == '<'):
                                    if str(table_records[i][column_number_to_compare]) < str(result2.value):
                                        table_record_to_delete.append(table_records[i])
                                elif(result_type == '>='):
                                    if str(table_records[i][column_number_to_compare]) >= str(result2.value):
                                        table_record_to_delete.append(table_records[i])
                                elif(result_type == '<='):
                                    if str(table_records[i][column_number_to_compare]) <= str(result2.value):
                                        table_record_to_delete.append(table_records[i])
                                i += 1   

                            columns_with_primary_keys = []
                            i = 0
                            while i < len(table_.columns):
                                if table_.columns[i].primary_ != None and table_.columns[i].primary_ == True:
                                    columns_with_primary_keys.append(i)
                                i += 1

                            table_record_to_delete_only_with_primary_keys = []
                            i = 0
                            while i < len(table_record_to_delete):
                                primary_keys = []
                                j = 0
                                while j < len(columns_with_primary_keys):
                                    primary_keys.append(table_record_to_delete[i][(columns_with_primary_keys[j])])
                                    j += 1
                                table_record_to_delete_only_with_primary_keys.append(primary_keys)
                                i += 1

                            number_of_rows_removed = 0
                            i = 0
                            while i < len(table_record_to_delete_only_with_primary_keys):
                                try:
                                    #success
                                    result_delete = delete(database_.name, table_.name, table_record_to_delete_only_with_primary_keys[i])
                                    if result_delete == 0:
                                        #print_success("QUERY", "Delete row in " + str(table_.name) + " table, done successfully")
                                        number_of_rows_removed += 1
                                    elif result_delete == 1:
                                        #print_error("UNKNOWN ERROR", "Operation error")
                                        a = 0
                                    elif result_delete == 2:
                                        #print_error("SEMANTIC ERROR", "Database does not exist")
                                        a = 0
                                    elif result_delete == 3:
                                        #print_error("SEMANTIC ERROR", "Table does not exist")
                                        a = 0
                                    elif result_delete == 4:
                                        #print_error("SEMANTIC ERROR", "Primary key does not exist")
                                        a = 0
                                    else:
                                        #print_error("UNKNOWN ERROR", "Operation error")
                                        a = 0
                                except Exception as e:
                                    #print_error("UNKNOWN ERROR", "instruction not executed")
                                    a = 0
                                    #print(e)
                                i += 1
                            print_success("QUERY",str(number_of_rows_removed) + " rows removed successfully",2)
                            #----------------------------------------------------------------------

                        else:
                            print_error("SEMANTIC ERROR", str(relational_.value1) + " column does not exist in " + table_.name + " table",2)

                    else:
                        print_error("SEMANTIC ERROR", "Table does not exist",2)

                else:
                    print_error("SEMANTIC ERROR", "Database to use does not exist",2)

            else:
                print_warning("RUNTIME ERROR", "Undefined database to use",2)
        
        else:
            print_error("UNKNOWN ERROR", "instruction not executed",2)

    else:
        print_error("UNKNOWN ERROR", "instruction not executed",2)


def get_first_relational(self, expression_) -> Relational:

    relational_: Relational = None

    current_expression = expression_
    while isinstance(current_expression, Logical) == True:
        current_expression = current_expression.value1
    
    relational_ = current_expression

    return relational_