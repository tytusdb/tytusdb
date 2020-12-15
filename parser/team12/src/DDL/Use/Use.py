import json
import sys, os.path
import os

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\storageManager')
sys.path.append(storage)

from jsonMode import *

class Use():
    def __init__(self):
        print("Start")
    
    def execute(self, parent):

        databasesStorage = showDatabases()
        if parent.hijos[0].valor.upper() in databasesStorage : 
            index = databasesStorage.index(parent.hijos[0].valor)

            #Se abre el archivo de configuraciones
            with open('src/Config/Config.json') as file:
                config = json.load(file)
            
            config['databaseIndex'] = index
            with open('src/Config/Config.json',"w") as file:
                json.dump(config,file)

            return {'Code':'0000','Message':'Cambió de base de datos'}
        else:
            return {'Code':'42P12','Message':'La base de datos no existe'}