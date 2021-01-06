import json
import hashlib
import os
import pickle
import re
import shutil

class Block:
    def __init__(self, numberBlock, data, previousHash, idHash):
        self._idBlock = numberBlock
        self._data = data
        self._previousHash = previousHash
        self._idHash = idHash
        self._checker = True

    def getIdBlock(self):
        return self._idBlock

    def getData(self):
        return self._data

    def getPreviousHash(self):
        return self._previousHash

    def getIdHash(self):
        return self._idHash

    def getChecker(self):
        return self._checker

    def setData(self, data):
        self._data = data

    def setIdHash(self, idHash):
        self._idHash = idHash

    def setChecker(self, boolInfo):
        self._checker = boolInfo

    def getBlock(self):
        return [self._idBlock, self._data, self._previousHash, self._idHash]

    def getInfoGraph(self):
        info = "Bloque: " + str(self._idBlock) + "\\nData: " + str(self._data) + "\\nHash Bloque: " + str(self._idHash)\
               + "\\nHash Ant.: " + str(self._previousHash)
        return info

    def verifyBlock(self, hashAnteriorBA):
        if hashAnteriorBA == self._previousHash:
            return True
        # self._checker = False
        return False


class Blockchain:
    def __init__(self):
        self.idChain = 1
        self.previous = 0
        self.blocks_list = []
        self.firstHash = ""
        self.checkerChain = True
        
        
    def generate_hash(self, data):
        pattern = r'[0-9a-zA-Z]+'
        objectStr = pickle.dumps(data)
        while True:
            id_hash = hashlib.sha256(objectStr).hexdigest()
            if re.match(pattern, id_hash):
                return id_hash
        
