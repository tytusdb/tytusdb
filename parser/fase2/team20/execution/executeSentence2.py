from .AST.sentence import *
from .AST.expression import *
from .AST.error import * 
import sys
sys.path.append("../")
from console import *



def executeSentence2(self, sentence):
    if isinstance(sentence, CreateDatabase):
        h=0                   
    elif isinstance(sentence, ShowDatabases):
        h=0
    elif isinstance(sentence, DropDatabase):
        h=0
    elif isinstance(sentence,Use):
        h=0
    elif isinstance(sentence,CreateTable):
        h=0
    elif isinstance(sentence, CreateType):
        h=0
    elif isinstance(sentence, InsertAll):
        h=0
    elif isinstance(sentence, Insert):
        h=0
    elif isinstance(sentence, Delete):
        h=0
    elif isinstance(sentence,Select):
        print(sentence.columns)
        #print(sentence.columns[0].function)
        #print(sentence.columns[0].expression)
        print(sentence.tables)
        print(sentence.options)
    elif isinstance(sentence,DropTable):
        h=0
    elif isinstance(sentence,AlterDatabaseRename):
        archivo = open("C3D.py", 'a')
        archivo.write("\n")
        archivo.write("ICreateDatabase("+sentence.name+","+sentence.ifNotExistsFlag+","+sentence.OrReplace+","+sentence.OwnerMode+")") 
        archivo.close()
    elif isinstance(sentence,Update):
        h=0
    elif isinstance(sentence,AlterTableDropConstraint):
        archivo = open("C3D.py", 'a')
        archivo.write("\n")
        archivo.write("ICreateDatabase("+sentence.name+","+sentence.ifNotExistsFlag+","+sentence.OrReplace+","+sentence.OwnerMode+")") 
        archivo.close()
    elif isinstance(sentence,AlterTableAlterColumnType):
        h=0
    elif isinstance(sentence, AlterTableAddColumn):
        h=0
    elif isinstance(sentence, AlterTableDropColumn):
        archivo = open("C3D.py", 'a')
        archivo.write("\n")
        archivo.write("ICreateDatabase("+sentence.name+","+sentence.ifNotExistsFlag+","+sentence.OrReplace+","+sentence.OwnerMode+")") 
        archivo.close()
