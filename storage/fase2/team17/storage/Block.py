# File:     Block
# License:  Released under MIT License
# Notice:   Copyright (c) 2020 TytusDB Team

import datetime
import hashlib

class Block:

    def __init__(self, prevHash, data, timeM):
        self.prevHash = prevHash
        self.data = data
        self.timeM = timeM
        self.hash = self.getHash()

    @staticmethod
    def iniBlock():
        return Block("0","0",datetime.datetime.now())

    def getHash(self):
        leHeader = (str(self.prevHash) + str(self.data) + str(self.timeM)).encode()
        leInterno = hashlib.sha256(leHeader).hexdigest().encode()
        leExterno = hashlib.sha256(leInterno).hexdigest()
        return leExterno