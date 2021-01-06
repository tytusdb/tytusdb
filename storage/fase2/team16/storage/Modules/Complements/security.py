# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16

from ..handler import Handler
from cryptography.fernet import Fernet
from cryptography.hazmat import backends as backends
from cryptography.hazmat import primitives as primitives
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as mac
import os
import base64 as base
import json
import hashlib
import graph

def encrypt(backup: str, password: str) -> str:
    try:
        criptogram = Fernet(base.urlsafe_b64encode(mac(algorithm=primitives.hashes.SHA256(), length=32, salt=bytes(password, encoding="utf-8"), iterations=50, backend=backends.default_backend()).derive(password.encode("utf-8")))).encrypt(bytes(backup, encoding="utf-8"))
        return criptogram.decode("utf-8")
    except:
        return None

def decrypt(cipherBackup: str, password: str) -> str:
    try:
        original = Fernet(base.urlsafe_b64encode(mac(algorithm=primitives.hashes.SHA256(), length=32, salt=bytes(password, encoding="utf-8"), iterations=50, backend=backends.default_backend()).derive(password.encode("utf-8")))).decrypt(bytes(cipherBackup, encoding="utf-8"))
        return original.decode("utf-8")
    except:
        return None

class Blockchain:
    def __init__(self, dbName:str, tableName: str):
        if not os.path.exists("blockchain"):
            os.makedirs("blockchain")
        Handler.createJson(dbName, tableName, "[]")

    def insert(self, dbName:str, tableName:str, content, pk:list):
        try:
            code = self.hash(content)
            text = json.loads(Handler.readJson(dbName, tableName))
            ID = ""
            for i in pk:
                ID += content[i]
            if len(json.loads(Handler.readJson(dbName, tableName))) == 0:
                new = """{
                    'id': """ + ID + """,
                    'content': """ + content + """,
                    'previous': '',
                    'hash': '""" + code + """',
                    'color': 'green'
                }"""
            else:
                new = """, {
                    'id': """ + ID + """,
                    'content': """ + content + """,
                    'previous': '""" + text[number]['hash'] + """',
                    'hash': """ + code + """,
                    'color': 'green'
                }"""
                text = text[:-1]
            text += new + "]"
            Handler.createJson(dbName, tableName, text)
        except:
            print("Error en la operación")

    def update(self, dbName:str, tableName:str, content, pk:list):
        try:
            key = ""
            code = ""
            for i in pk:
                key += i
            fileJson = json.loads(Handler.readJson(dbName, tableName))
            for value in fileJson:
                if value['id'] == key:
                    for field in content:
                        value['content'][field] = content.get(field)
                    code = self.hash(value['content'])
                    value['hash'] = code
                    color(dbName, tableName)
                    break
            Handler.createJson(dbName, tableName, fileJson)
        except:
            print("Error en la operación")

    def delete(self, dbName:str, tableName:str, pk:list):
        try:
            count = 0
            key = ""
            for i in pk:
                key += i
            fileJson = json.loads(Handler.readJson(dbName, tableName))
            for value in fileJson:
                if value['id'] == key:
                    fileJson.pop(count)
                    color(dbName, tableName)
                    break
        except:
            None

    def color(self, dbName:str, tableName:str):
        try:
            fileJson = json.loads(Handler.readJson(dbName, tableName))
            count = 0
            tmphash = ''
            Next = None
            for i in fileJson:
                if Next:
                    i['color'] = 'red'
                if i['previous'] == tmphash:
                    tmphash = i['hash']
                else:
                    fileJson[count-1]['color'] = 'red'
                    i['color'] = 'red'
                    Next = True
                count += 1
        except:
            None

    def draw(self, dbName:str, tableName:str):
        diag = "digraph graph{\n{rank='same'}\n"
        fileJson = json.loads(Handler.readJson(dbName, tableName))
        first = True
        count = 0
        for i in fileJson:
            if first:
                diag += i['id'] + "[shape='box', style='filled', fillcolor='" + i['color'] + "]\n"
                first = None
            else:
                diag += i['id'] + "[shape='box', style='filled', fillcolor='" + i['color'] + "]\n"
                diag += fileJson[count-1]['id'] + "->" + i['id'] + "\n"
            count += 1
        graph.draw("blockchain/" + dbName + "_" + tableName, diag)



    @staticmethod
    def hash(content):
        tmp = ""
        if type(content) == type({}):
            for field in content:
                tmp += str(content.get(field))
        elif type(content) == type([]):
            for field in content:
                tmp += str(field)
        else:
            return None
        code = bytes(tmp, 'utf-8')
        return hashlib.sha256(code).hexdigest()