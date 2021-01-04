import os
import json

class GuardarTabla():
    def __init__(self):
        self.path = 'tablasimbolos/'
        self.dataPath = self.path + 'tabla'

    def guardarDic(self,diccionario):
        self.initCheck()
        self.write(self.dataPath,diccionario)

    def initCheck(self):
        if not os.path.exists('tablasimbolos'):
            os.makedirs('tablasimbolos')
        if not os.path.exists('tablasimbolos/tabla'):
            data = {}
            with open('tablasimbolos/tabla', 'w') as file:
                json.dump(data, file)

    def read(self,path):
        with open(path) as file:
            return json.load(file)    

    def write(self,path, data):
        with open(path, 'w') as file:
            json.dump(data, file)

    def dropAll(self):
        self.initCheck()
        data = {}
        with open('tablasimbolos/tabla', 'w') as file:
            json.dump(data, file)