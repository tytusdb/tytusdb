from sys import path
from os.path import dirname as dir
import webbrowser
import os
path.append(dir(path[0]))

from Parser.analizer import interpreter 


class Pantalla2:
    def __init__(self):
        self.lexicalErrors = list()
        self.syntacticErrors = list()
        self.semanticErrors = list()
        self.postgreSQL = list()
        self.ts = list()
    
    def MetodoParser(self, texto):
        #DECLARAR RETORNO
        salida = "";
        # EJECUTAR PARSER
        result = interpreter.execution(texto)
        self.lexicalErrors = result["lexical"]
        self.syntacticErrors = result["syntax"]
        self.semanticErrors = result["semantic"]
        self.postgreSQL = result["postgres"]
        self.ts = result["symbols"]
        self.indexes = result["indexes"]
        if (
            len(self.lexicalErrors)
            + len(self.syntacticErrors)
            + len(self.semanticErrors)
            + len(self.postgreSQL)
            > 0
        ):
            if len(self.postgreSQL) > 0:
                i = 0
                salida +=  "================================================== \n"
                salida +=  "                       TYTUS ERROR \n"
                salida +=  "================================================== \n"
                while i < len(self.postgreSQL):
                    salida +=  ">> " + str(self.postgreSQL[i]) + "\n"

                    i += 1
        
        querys = result["querys"]
        messages = result["messages"]
        if len(messages) > 0:
            i = 0
            salida +=  "==================================================\n"
            salida +=  "                       TYTUS \n"
            salida +=  "================================================== \n"

            while i < len(messages):
                salida +=  ">> " + str(messages[i]) + "\n"
                i += 1
            while i < len(querys):
                salida +=  ">> " + str(querys[i]) + "\n"
                i += 1
            
        return {'salida': salida, 'query': querys }
