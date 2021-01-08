import json
import sys, os.path
import os

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\storageManager')
sys.path.append(storage)


from jsonMode import *

class Use():
    def __init__(self):
        self.databaseName = None

    def compile(self, parent):
        return "USE " + parent.hijos[0].valor.upper()+";"

    
    def execute(self, parent):

        databasesStorage = showDatabases()
        if parent.hijos[0].valor.upper() in databasesStorage : 
            #Se abre el archivo de configuraciones
            with open('src/Config/Config.json') as file:
                config = json.load(file)
            config['databaseIndex'] = parent.hijos[0].valor.upper()
            with open('src/Config/Config.json',"w") as file:
                json.dump(config,file)

            return {'Code':'0000','Message':'Cambio de base de datos'}
        else:
            return {'Code':'42P12','Message':'La base de datos no existe'}