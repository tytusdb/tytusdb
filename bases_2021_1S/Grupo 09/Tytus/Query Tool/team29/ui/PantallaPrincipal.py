from sys import path
from os.path import dirname as dir
import webbrowser
import os
path.append(dir(path[0]))
from team29.analizer import interpreter
from team29.analizer import variables

class Pantalla:
    usetable = ""
    
    def __init__(self):
        self.lexicalErrors = list()
        self.syntacticErrors = list()
        self.semanticErrors = list()
        self.postgreSQL = list()
        self.ts = list()
        # self.inicializarScreen()

    def parse(self, input):
        result = interpreter.parser(input)
        if len(result["lexical"]) + len(result["syntax"]) == 0:
            return [0, variables.graph, variables.bnfgrammar, variables.usetable]
        else:
            self.lexicalErrors = result["lexical"]
            self.syntacticErrors = result["syntax"]
            return [1, self.lexicalErrors, self.syntacticErrors, variables.graph, variables.bnfgrammar, variables.usetable]

    def analize(self, entrada):
        result = interpreter.execution(entrada)
        self.lexicalErrors = result["lexical"]
        self.syntacticErrors = result["syntax"]
        self.semanticErrors = result["semantic"]
        self.postgreSQL = result["postgres"]
        self.ts = result["symbols"]
        self.indexes = result["indexes"]
        error = False
        if (
            len(self.lexicalErrors)
            + len(self.syntacticErrors)
            + len(self.semanticErrors)
            + len(self.postgreSQL)
            > 0
        ):
            error = True		
        querys = result["querys"]
        messages = result["messages"]
        return [error, self.lexicalErrors, self.syntacticErrors, self.semanticErrors, self.postgreSQL, self.ts, self.indexes, variables.graph, variables.bnfgrammar, querys, messages, variables.usetable]