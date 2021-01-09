import re
import os
import json
import shutil
import pickle
import hashlib
class block:
    def __init__(self,number_block,data,previus_Hash,id_Hash):
        self._idBlock = number_block
        self._data = data
        self._previousHash = previus_Hash
        self._idHash = id_Hash
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

    def verify_block(self,hash_anterior):
        if hash_anterior == self._previousHash:
            return True
        return False
    def get_data(self):
        data = "Block: " + str(self._idBlock) + "\\nData: " + str(self._data) + "\\nHash Block: " + str(self._idHash) \
               + "\\nHash Ant.: " + str(self._previousHash)
        return data
class blockchain:
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
    def insertBlock(self, tupla, nameJson):
        id_hash = self.generate_hash(tupla)
        newBlock = Block(self.idChain, tupla, self.previous, id_hash)
        self.blocks_list.append(newBlock)
        file = self.load_json(nameJson)
        file.write(json.dumps([j.getBlock() for j in self.blocks_list]))
        file.close()
        if self.idChain == 1:
            self.firstHash = id_hash
        self.idChain += 1
        self.previous = id_hash
    def verifyFirstBlock(self, hashActual):
        if self.firstHash == hashActual:
            return True
        return False
    def updateBlock(self, oldTuple, newTuple, nameJson):
       #cambiar datos y actualizar hash, recorrer los blocks y comparar
        file = open(os.getcwd() + "\\DataJsonBC\\" + nameJson + ".json", "r")
        JSblock_list = json.loads(file.read())
        file.close()
        newHash = self.generate_hash(newTuple)
        for blockJS in JSblock_list:
            if oldTuple == blockJS[1]:
                blockJS[1] = newTuple
                blockJS[3] = newHash
        for block in self.blocks_list:
            if oldTuple == block.getData():
                block.setData(newTuple)
                block.setIdHash(newHash)
        file = open(os.getcwd() + "\\DataJsonBC\\" + nameJson + ".json", "w+")
        file.write(json.dumps(JSblock_list))
        file.close()

    def load_json(self, nombre):
        if os.path.isdir(os.getcwd() + "\\DataJsonBC"):
            file = open(os.getcwd() + "\\DataJsonBC\\" + nombre + ".json", "+w")
            return file
        os.makedirs(os.getcwd() + "\\DataJsonBC")
        file = open(os.getcwd() + "\\DataJsonBC\\" + nombre + ".json", "+w")
        return file

    def removeFilesBlock(self, nameJson):
        if os.path.isdir(os.getcwd() + "\\DataJsonBC"):
            if os.path.isfile(os.getcwd() + "\\DataJsonBC\\" + nameJson + ".json"):
                os.remove(os.getcwd() + "\\DataJsonBC\\" + nameJson + ".json")

