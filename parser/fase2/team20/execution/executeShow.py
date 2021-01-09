from .storageManager.jsonMode import showDatabases
from console import print_success, print_table 
from prettytable import PrettyTable
def executeShowDatabases(self):
    #self.intermediate.memory.append(self)
    x = PrettyTable()
    dbs = showDatabases()
    #self.messages.append("Databases:")
    x.field_names = ["Databases"]
    for db in dbs:
        x.add_row([db])
        #self.messages.append("\t"+db)
    x.align = "r"
    x.border = True
    x.padding_width = 7
    print_success("QUERY","Query carried out successfully",2)
    print_table("QUERY TABLE",x.get_string(),2)
    print(x) #show databases;