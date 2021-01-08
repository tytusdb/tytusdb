from AST.sentence import InsertAll, Insert
from storageManager.TypeChecker_Manager import *
from storageManager.jsonMode import *
from .executeExpression import executeExpression
from .AST.error import *

import sys
sys.path.append("../")
from console import print_error, print_success, print_warning


#def insert(database: str, table: str, register: list) -> int:
#0 -> Successful operation
#1 -> Operation error    
#2 -> Database does not exist
#3 -> Table does not exist
#4 -> Duplicate primary key
#5 -> Columns out of bounds
#anything else -> Operation error

def executeInsertAll(self, InsertAll_):

    # InsertAll : {
    #     table: "table_name",
    #     values: [ { type: ('Entero' | 'Decimal' | 'Cadena' | 'Variable' | 'Regex' | 'All'), value: "" } ]
    #     #values: [ { type: (1       | 2         |  3       |  4         | 5       | 6    ), value: "" } ]
    # }
    
    insertAll: InsertAll = InsertAll_
    table_name = insertAll.table
    values = insertAll.values
    
    check_and_solve_values_ = check_and_solve_values(self, values)
    if check_and_solve_values_ == None:
        
        TypeChecker_Manager_ = get_TypeChecker_Manager()
        if  TypeChecker_Manager_ != None:
        
            use_: str = get_use(TypeChecker_Manager_)
            if use_ != None:
            
                database_ = get_database(use_, TypeChecker_Manager_)
                if database_ != None:
                
                    table_ = get_table(table_name, database_)
                    if table_ != None:
                    
                        if len(table_.columns) == len(values):
                        
                            check_type_ = check_type(table_.columns, values)
                            if check_type_ == None:
                        
                                check_null_ = check_null(table_.columns, values)
                                if check_null_ == None:

                                    check_maxlength_ = check_maxlength(table_.columns, values)
                                    if check_maxlength_ == None:

                                        check_checks_ = check_checks(table_.columns, values)
                                        if check_checks_ == None:
                                        
                                            try:
                                                #success
                                                values_list = []
                                                i = 0
                                                while i < len(values):
                                                    if(values[i] == None):
                                                        values_list.append(None)
                                                    else:
                                                        values_list.append(values[i].value)
                                                    i += 1
                                                replace_default(values_list, table_.columns)
                                                result_insert = insert(database_.name, table_.name, values_list)
                                                if result_insert == 0:
                                                    print_success("QUERY", "Insert in " + str(table_.name) + " table, done successfully",2)
                                                elif result_insert == 1:
                                                    print_error("UNKNOWN ERROR", "Operation error",2)
                                                elif result_insert == 2:
                                                    print_error("SEMANTIC ERROR", "Database does not exist",2)
                                                elif result_insert == 3:
                                                    print_error("SEMANTIC ERROR", "Table does not exist",2)
                                                elif result_insert == 4:
                                                    print_error("SEMANTIC ERROR", "Duplicate primary key",2)
                                                elif result_insert == 5:
                                                    print_error("SEMANTIC ERROR", "Columns out of bounds",2)
                                                else:
                                                    print_error("UNKNOWN ERROR", "Operation error",2)
                                            except Exception as e:
                                                print_error("UNKNOWN ERROR", "instruction not executed",2)
                                                #print(e)

                                        else:
                                            print_error("SEMANTIC ERROR", check_checks_,2)

                                    else:
                                        print_error("SEMANTIC ERROR", check_maxlength_,2)

                                else:
                                    print_error("SEMANTIC ERROR", check_null_,2)

                            else:
                                print_error("SEMANTIC ERROR", check_type_,2)
                        
                        else:
                            print_error("SEMANTIC ERROR", "Wrong arguments submitted for table. " + str(len(table_.columns)) + " required and " + str(len(values)) + " received",2)

                    else:
                        print_error("SEMANTIC ERROR", "Table does not exist",2)

                else:
                    print_error("SEMANTIC ERROR", "Database to use does not exist",2)

            else:
                print_warning("RUNTIME ERROR", "Undefined database to use",2)
        
        else:
            print_error("UNKNOWN ERROR", "instruction not executed",2)

    else:
        print_error("SEMANTIC ERROR", check_and_solve_values_,2)


def executeInsert(self, Insert_):

    # Insert : {
    #     table: "table_name",
    #     columns: [ "column_name", "column_name" ],
    #     values: [ { type: ('Entero' | 'Decimal' | 'Cadena' | 'Variable' | 'Regex' | 'All'), value: "" } ]
    #     #values: [ { type: (1       | 2         |  3       |  4         | 5       | 6    ), value: "" } ]
    # }
    
    insert: Insert = Insert_
    table_name = insert.table
    columns = insert.columns
    values = insert.values

    if len(columns) == len(values):

        TypeChecker_Manager_ = get_TypeChecker_Manager()
        if  TypeChecker_Manager_ != None:
        
            use_: str = get_use(TypeChecker_Manager_)
            if use_ != None:
            
                database_ = get_database(use_, TypeChecker_Manager_)
                if database_ != None:
                
                    table_ = get_table(table_name, database_)
                    if table_ != None:
                        
                            if len(table_.columns) >= len(values):
                            
                                table_columns_names = []
                                i = 0
                                while i < len(table_.columns):
                                    table_columns_names.append(table_.columns[i].name)
                                    i += 1

                                i = 0
                                columns_exist = True
                                columns_exist_error = 0
                                while i < len(columns) and columns_exist == True:
                                    if not(columns[i] in table_columns_names) == True:
                                        columns_exist = False
                                        columns_exist_error = i
                                    i += 1

                                if columns_exist == True:     
                                    new_list_of_values = []
                                    i = 0
                                    while i < len(table_columns_names):
                                        if (table_columns_names[i] in columns) == True:
                                            j = 0
                                            while j < len(columns):
                                                if table_columns_names[i] == columns[j]:
                                                    new_list_of_values.append(values[j])
                                                    j = len(columns) 
                                                j += 1
                                        else:
                                            new_list_of_values.append(None)                                        
                                        i += 1
                                    new_InsertAll = InsertAll(table_name, new_list_of_values)
                                    executeInsertAll(self, new_InsertAll)

                                else:
                                    print_error("SEMANTIC ERROR", str(columns[columns_exist_error]) + " column in which you want to insert does not exist",2) 
                        
                            else:
                                print_error("SEMANTIC ERROR", "Number of arguments sent is greater than the number of columns in the table",2)

                    else:
                        print_error("SEMANTIC ERROR", "Table does not exist",2)

                else:
                    print_error("SEMANTIC ERROR", "Database to use does not exist",2)

            else:
                print_warning("RUNTIME ERROR", "Undefined database to use",2)
        
        else:
            print_error("UNKNOWN ERROR", "instruction not executed",2)
    
    else:
        print_error("SEMANTIC ERROR", "number of columns and values ​​are not the same size",2)


def check_and_solve_values(self, values_):

    return_ = None

    i = 0
    while i < len(values_):
        
        if values_[i] != None:
    
            result_executeExpression = executeExpression(self, values_[i])

            if( isinstance(result_executeExpression, Error) ):
                return_ = result_executeExpression.detail
        
            else:
                values_[i].type = result_executeExpression.type
                values_[i].value = result_executeExpression.value
        
        i += 1

    return return_


type_int = ["SMALLINT", "INTEGER", "BIGINT", "REAL"]
type_float = ["DECIMAL", "NUMERIC", "DOUBLE PRECISION", "PRECISION", "MONEY"]
type_char = ["CHARACTER", "CHAR", "TEXT"]
type_string = ["TEXT"]
type_bool = ["BOOLEAN"]
# | TIMESTAMP
# | DATE
# | TIME 
# | INTERVAL
# | TIME WITHOUT TIME ZONE
# | TIME WITH TIME ZONE
# | INTERVAL INT
# | TIMESTAMP WITH TIME ZONE
# | ID


def check_type(columns_, values_) -> str:

    return_ = None

    i = 0
    while i < len(columns_):
        
        if values_[i] != None:

            column_type = ((str(columns_[i].type_)).upper())  
            if ( column_type in type_int ) == True:
                if values_[i].type != 1 and values_[i].type!=4:
                    return_ = "Argument " + str((i+1)) + " of wrong type. It should be a " + str(column_type) + " type."
                    i = len(columns_)
        
            elif ( column_type in type_float ) == True:
                if values_[i].type != 2 and values_[i].type!=4:
                    return_ = "Argument " + str((i+1)) + " of wrong type. It should be a " + str(column_type) + " type."
                    i = len(columns_)
        
            elif ( column_type in type_char ) == True:
                if values_[i].type != 3 and values_[i].type!=4:
                    return_ = "Argument " + str((i+1)) + " of wrong type. It should be a " + str(column_type) + " type."
                    i = len(columns_)
        
            elif ( column_type in type_string ) == True:
                if values_[i].type != 3 and values_[i].type!=4:
                    return_ = "Argument " + str((i+1)) + " of wrong type. It should be a " + str(column_type) + " type."
                    i = len(columns_)

            elif ( column_type in type_bool ) == True:
                if values_[i].type != 1 and values_[i].type!=4:
                    return_ = "Argument " + str((i+1)) + " of wrong type. It should be a " + str(column_type) + " type."
                    i = len(columns_)
                else:
                    if (not(str(values_[i].value)=="0" or str(values_[i].value=="1"))) == True:
                        return_ = "Argument " + str((i+1)) + " of wrong type. It should be a " + str(column_type) + " type."
                        i = len(columns_)
        
        i += 1

    return return_


def check_null(columns_, values_) -> str:

    return_ = None

    i = 0
    while i < len(columns_):

        if columns_[i].null_ != None:
            if columns_[i].null_ == False:
                if values_[i] == None:
                    return_ = "Argument " + str((i+1)) + " is null and the column does not allow null values."
                    i = len(columns_)

        i += 1

    return return_


def check_maxlength(columns_, values_) -> str:

    return_ = None

    i = 0
    while i < len(columns_):

        if values_[i] != None:

            if columns_[i].maxlength_ != None:
                if ( columns_[i].maxlength_ < len(str(values_[i].value)) ) == True:
                    return_ = "Argument " + str((i+1)) + " exceeds the maximum length allowed by the column."
                    i = len(columns_)

        i += 1

    return return_


def check_checks(columns_, values_) -> str:

    return_ = None
    error_encontrado = False

    i = 0
    while i < len(columns_) and error_encontrado == False:

        if values_[i] != None:

            value = str(values_[i].value)
            j = 0
            while j < len(columns_[i].checks) and error_encontrado == False:

                check_operation = columns_[i].checks[j].operation
                check_value = columns_[i].checks[j].value

                if str(check_operation) == "<":
                    if not(str(value) < str(check_value)):
                        return_ = "Argument " + str((i+1)) + " must be " + str(check_operation) + " to "
                        is_int_or_float_ = is_int_or_float(check_value)
                        if is_int_or_float_== True:
                            return_ += str(check_value) + "."
                        else:
                            return_ += "\"" + str(check_value) + "\"."
                        error_encontrado = True
                elif str(check_operation) == ">":
                    if not(str(value) > str(check_value)):
                        return_ = "Argument " + str((i+1)) + " must be " + str(check_operation) + " to "
                        is_int_or_float_ = is_int_or_float(check_value)
                        if is_int_or_float_== True:
                            return_ += str(check_value) + "."
                        else:
                            return_ += "\"" + str(check_value) + "\"."
                        error_encontrado = True
                elif str(check_operation) == "<=":
                    if not(str(value) <= str(check_value)):
                        return_ = "Argument " + str((i+1)) + " must be " + str(check_operation) + " to "
                        is_int_or_float_ = is_int_or_float(check_value)
                        if is_int_or_float_== True:
                            return_ += str(check_value) + "."
                        else:
                            return_ += "\"" + str(check_value) + "\"."
                        error_encontrado = True
                elif str(check_operation) == ">=":
                    if not(str(value) >= str(check_value)):
                        return_ = "Argument " + str((i+1)) + " must be " + str(check_operation) + " to "
                        is_int_or_float_ = is_int_or_float(check_value)
                        if is_int_or_float_== True:
                            return_ += str(check_value) + "."
                        else:
                            return_ += "\"" + str(check_value) + "\"."
                        error_encontrado = True
                elif str(check_operation) == "==":
                    if not(str(value) == str(check_value)):
                        return_ = "Argument " + str((i+1)) + " must be " + str(check_operation) + " to "
                        is_int_or_float_ = is_int_or_float(check_value)
                        if is_int_or_float_== True:
                            return_ += str(check_value) + "."
                        else:
                            return_ += "\"" + str(check_value) + "\"."
                        error_encontrado = True
                elif str(check_operation) == "!=":
                    if not(str(value) != str(check_value)):
                        return_ = "Argument " + str((i+1)) + " must be " + str(check_operation) + " to "
                        is_int_or_float_ = is_int_or_float(check_value)
                        if is_int_or_float_== True:
                            return_ += str(check_value) + "."
                        else:
                            return_ += "\"" + str(check_value) + "\"."
                        error_encontrado = True
            
                j += 1

        i += 1

    return return_


def replace_default(values_, columns_):

    return_ = None

    if len(values_) == len(columns_):
        i = 0
        while i < len(values_):

            if values_[i] == None:
                values_[i] = columns_[i].default_

            i += 1