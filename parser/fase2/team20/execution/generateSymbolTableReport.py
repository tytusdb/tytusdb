from storageManager.TypeChecker_Manager import *
from prettytable import PrettyTable

import sys
sys.path.append("../")
from console import print_error

def printSymbolTable(self):

    x = PrettyTable(["Number", "Name", "Type", "Environment"])

    try:
        TypeChecker_Manager_ = get_TypeChecker_Manager()
        #Databases
        Databases = TypeChecker_Manager_.databases
        i = 0
        a = 1
        while i < len(Databases):        
            x.add_row([a, str(Databases[i].name), "Database", "Global"])
            a += 1
            #Tables
            Tables = Databases[i].tables
            j = 0
            while j < len(Tables):        
                x.add_row([a, str(Tables[j].name), "Table", "Local"])
                a += 1
                #Columns
                Columns = Tables[j].columns
                k = 0
                while k < len(Columns):        
                    x.add_row([a, str(Columns[k].name), "Column type " + str(Columns[k].type_), "Local"])
                    a += 1
                    k += 1
                j += 1
            i += 1
    except Exception as e:
        print_error("Unknown Error", "Incorrectly generated Symbol Table")
        #print(e)

    print_ = x.get_string(title="Symbol Table")

    return print_