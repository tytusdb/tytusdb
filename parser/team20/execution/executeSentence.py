from .AST.sentence import *
from .executeCreate import executeCreateDatabase, executeShowDatabases
def executeSentence(self, sentence):
    if isinstance(sentence, CreateDatabase):
        if(executeCreateDatabase(self,sentence)==0):
            print("Base de datos "+sentence.name+" creada")
        elif(executeCreateDatabase(self,sentence)==2):
            print("Base de datos "+sentence.name+" ya existe")
        else:
            print("ERROR: Base de datos "+sentence.name+" ya existe")
    elif isinstance(sentence, ShowDatabases):
        executeShowDatabases(self)
    #Resto de sentencias posibles
    