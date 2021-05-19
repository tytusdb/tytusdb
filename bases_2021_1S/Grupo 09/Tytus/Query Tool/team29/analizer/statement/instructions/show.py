from team29.analizer.reports import Nodo
# from storage.storageManager import jsonMode
from team29.analizer.abstract.instruction import Instruction
import json
import requests

class showDataBases(Instruction):
    def __init__(self, like, row, column):
        Instruction.__init__(self, row, column)
        if like != None:
            self.like = like[1 : len(like) - 1]
        else:
            self.like = None

    def execute(self, environment):
        lista = []
        resp = requests.get('http://127.0.0.1:9998/DB/showDatabase')
        json1 = json.loads(resp.text)
        bases = json1['DataBase']
        if self.like != None:
            for l in bases:
                if self.like in l:
                    lista.append(l)
        else:
            resp = requests.get('http://127.0.0.1:9998/DB/showDatabase')
            json1 = json.loads(resp.text)
            lista = json1['DataBase']
        if len(lista) == 0:
            return "No hay bases de datos"
        return lista

    def dot(self):
        new = Nodo.Nodo("SHOW_DATABASES")
        if self.like != None:
            l = Nodo.Nodo("LIKE")
            ls = Nodo.Nodo(self.like)
            new.addNode(l)
            l.addNode(ls)

        return new
