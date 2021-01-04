# Functions to call in intermediate code
from .executeShow import executeShowDatabases
import os, json
class IntermediateFunctions:
    memory = []
    
    def showDatabases(self):
        executeShowDatabases(self.memory[0])
        self.memory.pop(0)
    def writeMemory(self, item):
        IntermediateFunctions.memoryCheck(self)
        # write item memory into json file
    def loadMemory(self):
        IntermediateFunctions.memoryCheck(self)
        # load memory from json to memory = []
    def memoryCheck(self):
        if not os.path.exists('memory'):
            os.makedirs('memory')
        if not os.path.exists('memory/memory'):
            data = {}
            with open('memory/memory', 'w') as file:
                json.dump(data, file)