import json
import sys, os.path
import os


storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\storageManager')
sys.path.append(storage)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker')
sys.path.append(storage)

from jsonMode import *
from typeChecker.typeChecker import *
tc = TypeChecker()



class Database():
    def __init__(self):
        self.name = None
        self.owner = None
        self.mode = None
        self.replaced = False
        self.ifNotExists = False
        self.responseCode = "0000"
        self.responseMessage = ""

    def compile(self,parent):
        textReturn = "CREATE"
        printDatabase = False
        for hijo in parent.hijos:
            if hijo.nombreNodo == "ORREPLACE":
                textReturn = textReturn + " OR REPLACE DATABASE"
                printDatabase = True
            elif hijo.nombreNodo == "IF_NOT_EXISTS":
                if not printDatabase:
                    textReturn = textReturn + " DATABASE"
                    printDatabase = True
                textReturn = textReturn + " IF NOT EXISTS"
            elif hijo.nombreNodo == "IDENTIFICADOR":
                if not printDatabase:
                    textReturn = textReturn + " DATABASE"
                    printDatabase = True
                textReturn = textReturn + " " + hijo.valor.upper()
            elif hijo.nombreNodo == "OPCIONALES_CREAR_DATABASE":
                textReturn = textReturn + " "+ self.compilarOpcionales(hijo)
        textReturn  = textReturn + ";"
        return textReturn

    def compilarOpcionales(self,parent):
        textReturn = ""
        for i in range(0,len(parent.hijos),2):
            if str(parent.hijos[i].nombreNodo).upper() == "OWNER":
                textReturn  = textReturn + " OWNER "+ parent.hijos[i+1].nombreNodo.upper()
            elif str(parent.hijos[i].nombreNodo).upper() == "MODE":
                textReturn  = textReturn + " MODE "+ str(parent.hijos[i+1].nombreNodo)
        return textReturn


    def execute(self, parent):
        for hijo in parent.hijos:
            if hijo.nombreNodo == "ORREPLACE":
                self.replaced = True
            elif hijo.nombreNodo == "IF_NOT_EXISTS":
                self.ifNotExists = True
            elif hijo.nombreNodo == "IDENTIFICADOR":
                self.name = hijo.valor.upper()
            elif hijo.nombreNodo == "OPCIONALES_CREAR_DATABASE":
                self.procesarOpcionales(hijo)
        
        if self.responseCode == "0000":
            self.addDatabase()
        return {"Code":self.responseCode,"Message":self.responseMessage, "Data" : None}


    def procesarOpcionales(self,parent):
        for i in range(0,len(parent.hijos),2):
            if parent.hijos[i].nombreNodo == "OWNER":
                if self.owner == None:
                    self.owner = parent.hijos[i+1].nombreNodo.upper()
                else:
                    self.responseCode = "42601"
                    self.responseMessage = "Ya se declaró el OWNER anteriormente"
                    return False
            elif parent.hijos[i].nombreNodo == "MODE":
                if self.mode == None:
                    self.mode = parent.hijos[i+1].nombreNodo
                else:
                    self.responseCode = "42601"
                    self.responseMessage = "Ya se declaró el MODE anteriormente"
                    return False
        return True
    
    def addDatabase(self):
        # Modo por default es 1
        if self.mode == None:
            self.mode = 1
        # Se crea si no existe

        if not (self.name.upper() in showDatabases()) : # No existe la base de datos, se crea
            print("Se va a crear la base de datos:")
            if createDatabase(self.name.upper()) == 0:
                self.responseCode="0000"
                self.responseMessage="Se creo la base de datos."
                tc.createDatabase(self.name.upper(), self.owner, self.mode)
        else:
            if not (self.ifNotExists) and self.replaced :
                dropDatabase(self.name.upper())
                createDatabase(self.name.upper())
                self.responseCode="0000"
                tc.replaceDatabase(self.name.upper(), self.owner, self.mode)
                self.responseMessage = "La base de datos fue reemplazada exitosamente"
            else:
                self.responseCode="42P04"
                self.responseMessage = "La base de datos "+self.name+" ya existe"