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

    def verifyFirstBlock(self, hashActual):
        if self.firstHash == hashActual:
            return True
        return False

    def insertBlock(self, tupla, nameJson):
        id_hash = self.generate_hash(tupla)
        newBlock = Block(self.idChain, tupla, self.previous, id_hash)
        self.blocks_list.append(newBlock)

        file = self.load_json(nameJson)
        file.write(json.dumps([j.getBlock() for j in self.blocks_list]))
        file.close()

        # only for the first
        if self.idChain == 1:
            self.firstHash = id_hash

        self.idChain += 1
        self.previous = id_hash

    def graphBlockchain(self, nombreImagen):
        graph = 'digraph G{\n'
        graph += 'rankdir=LR;\n'
        graph += "node[shape = \"box\"]\n"
        graph += self.__graficar()
        graph += '}'
        direccion = self.pathImageGraph()
        file = open(f"{direccion}\\{nombreImagen}.dot", "w")
        file.write(graph)
        file.close()
        os.system(f'dot -Tpng {direccion}\\{nombreImagen}.dot -o {direccion}\\{nombreImagen}.png')

    def __graficar(self):
        graph = ""
        bandera = True
        for i in range(len(self.blocks_list)):
            info = self.blocks_list[i].getInfoGraph()
            nodo = 'node' + str(self.blocks_list[i].getIdBlock())
            color = "green"

            # If is not the first, verify the previous hash
            if not (i == 0):
                hashAnterior = self.blocks_list[i-1].getIdHash()
                brokeChain = self.blocks_list[i].verifyBlock(str(hashAnterior))

            # If is the first, verify the actual hash, because the first always has previous in 0
            else:
                hashActual = self.blocks_list[i].getIdHash()
                brokeChain = self.verifyFirstBlock(hashActual)

            if not brokeChain:
                self.checkerChain = False
                bandera = False

            if bandera is False:
                color = "red"

            # If is not the last to put the next pointer
            if not (i == (len(self.blocks_list) - 1)):
                nextId = self.blocks_list[i + 1].getIdBlock()
                nextNodo = 'node' + str(nextId)
                graph += nodo + f'[label="{info}", color="{color}", penwidth=3]\n'
                graph += nodo + '->' + nextNodo + '\n'

            # If is the Last not put the next pointer
            else:
                graph += nodo + f'[label="{info}", color="{color}", penwidth=3]\n'

            # If is not the First to the Back pointer
            if not (i == 0):
                nodoAnterior = "node" + str(self.blocks_list[i-1].getIdBlock())
                if color == "green":
                    graph += nodo + '->' + nodoAnterior + "\n"
                graph += nodoAnterior + f"[color={color}]"
        return graph

    def updateBlock(self, oldTuple, newTuple, nameJson):
        # Cambiando valores de la lista y generando nuevo hash
        file = open(os.getcwd() + "\\DataJsonBC\\" + nameJson + ".json", "r")
        JSblock_list = json.loads(file.read())
        file.close()

        newHash = self.generate_hash(newTuple)

        # Recorriendo y actualizando JSON
        for blockJS in JSblock_list:
            if oldTuple == blockJS[1]:
                blockJS[1] = newTuple
                blockJS[3] = newHash

        # recorriendo y actualizando Block list
        for block in self.blocks_list:
            if oldTuple == block.getData():
                block.setData(newTuple)
                block.setIdHash(newHash)

        file = open(os.getcwd() + "\\DataJsonBC\\" + nameJson + ".json", "w+")
        file.write(json.dumps(JSblock_list))
        file.close()

    # ------------------------------------------------------- FILES ----------------------------------------------------
    def load_json(self, nombre):
        if os.path.isdir(os.getcwd() + "\\DataJsonBC"):
            file = open(os.getcwd() + "\\DataJsonBC\\" + nombre + ".json", "+w")
            return file
        os.makedirs(os.getcwd() + "\\DataJsonBC")
        file = open(os.getcwd() + "\\DataJsonBC\\" + nombre + ".json", "+w")
        return file

    def pathImageGraph(self):
        if not os.path.isdir(os.getcwd() + "\\ImageBlockChain"):
            os.makedirs(os.getcwd() + "\\ImageBlockChain")
        direccion = os.getcwd() + "\\ImageBlockChain"
        return direccion

    def removeFilesBlock(self, nameJson):
        if os.path.isdir(os.getcwd() + "\\DataJsonBC"):
            if os.path.isfile(os.getcwd() + "\\DataJsonBC\\" + nameJson + ".json"):
                os.remove(os.getcwd() + "\\DataJsonBC\\" + nameJson + ".json")
                

        
