# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16

from ..handler import Handler
from cryptography.fernet import Fernet
from cryptography.hazmat import primitives
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as mac
import base64 as base
import hashlib
from .graph import *

handler = Handler()
mode = 'security'


def encrypt(backup: str, password: str) -> str:
    try:
        crypt = Fernet(_generateKey(password)).encrypt(bytes(backup, encoding="utf-8"))
        return crypt.decode("utf-8")
    except:
        return None


def decrypt(cipherBackup: str, password: str) -> str:
    try:
        crypt = Fernet(_generateKey(password)).decrypt(bytes(cipherBackup, encoding="utf-8"))
        return crypt.decode("utf-8")
    except:
        return None


def _generateKey(password: str):
    tmp = mac(algorithm=primitives.hashes.SHA256(), length=32, salt=bytes(password, encoding="utf-8"), iterations=50,
              backend=backends.default_backend()).derive(password.encode("utf-8"))
    return base.urlsafe_b64encode(tmp)


class Blockchain:
    def __init__(self, database: str, table: str):
        self.database = database
        self.table = table
        self.current = ""
        self.previous = '0000000000000000000000000000000000000000000000000000000000000000'
        self.blocks = []
        self.number = 1
        self.rape = False
        handler.modeinstance(mode)
        handler.writeJSON(database, table, [])

    def destruction(self):
        handler.delete('./data/security/' + self.database + "_" + self.table + ".json")
        handler.clean(mode)
        return None

    def insert(self, register: list):
        try:
            self.current = self.hash(register)
            blocks = handler.readJSON(self.database, self.table)
            color = 'red' if self.rape else 'green'
            newblock = {
                'id': self.number,
                'content': register,
                'previous': self.previous,
                'hash': self.current,
                'color': color
            }
            self.number += 1
            self.previous = self.current
            blocks.append(newblock)
            handler.writeJSON(self.database, self.table, blocks)
        except:
            print("Error en la operación")

    def update(self, register: dict, row: list):
        try:
            rape = False
            blocks = handler.readJSON(self.database, self.table)
            for block in blocks:
                if row == block['content']:
                    for value in register:
                        block['content'][value] = register.get(value)
                    block['hash'] = self.hash(block['content'])
                    block['color'] = 'red'
                    rape = True
                if rape:
                    self.rape = True
                    block['color'] = 'red'
            handler.writeJSON(self.database, self.table, blocks)
            if rape:
                print("          Ruptura de seguridad")
        except:
            print("Error en la operación")

    def delete(self, row: list):
        try:
            rape = False
            blocks = handler.readJSON(self.database, self.table)
            for block in blocks:
                if row == block['content']:
                    block['content'] = []
                    block['hash'] = self.hash(block['content'])
                    block['color'] = 'red'
                    rape = True
                if rape:
                    self.rape = True
                    block['color'] = 'red'
            handler.writeJSON(self.database, self.table, blocks)
            if rape:
                print("          Ruptura de seguridad")
        except:
            print("Error en la operación")

    def draw(self, blocks=None):
        if not blocks:
            blocks = handler.readJSON(self.database, self.table)
        diag = "digraph G{\n{rank=\"same\"}\n"
        first = True
        count = 0
        for block in blocks:
            if first:
                diag += str(block['id']) + "[shape=\"box\", style=\"filled\", fillcolor=\" " + block['color'] + "\"]\n"
                first = None
            else:
                diag += str(block['id']) + "[shape=\"box\", style=\"filled\", fillcolor=\" " + block['color'] + "\"]\n"
                diag += str(blocks[count - 1]['id']) + "->" + str(block['id']) + "\n"
            count += 1
        diag += "}"
        generate(self.database + "_" + self.table, diag)

    @staticmethod
    def hash(register: list):
        tmp = ""
        for x in register:
            tmp += str(x)
        code = bytes(tmp, 'utf-8')
        return hashlib.sha256(code).hexdigest()
