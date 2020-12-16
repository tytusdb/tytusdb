from Cilindro import Cilindro, Registro

class Indice:
    def __init__(self, pkey):
        self.indx = [None]*30
        self.intervalo = 30
        self.pkey = pkey

    def insert(self, registro):
        val = []
        for key in self.pkey:
            val.append(registro[key])
        if type(val[0]) is int:
            i = self._hashn(val[0])
        else:
            i = self._hashl(val[0])
        if self.indx[i] == None:
            self.indx[i] = Cilindro("CS"+str(i), self.pkey, i)
        return self.indx[i].insert(registro)

    def _hashl(self, key):
        fst = ord(key[0].upper())
        return (fst - 65) // self.intervalo

    def _hashn(self, key):
        return (key // 30) % self.intervalo

    def update(self, register, val):
        if type(val[0]) is int:
            i = self._hashn(val[0])
        else:
            i = self._hashl(val[0])
        return self.indx[i].update(register, val)

    def delete(self, val):
        if type(val[0]) is int:
            i = self._hashn(val[0])
        else:
            i = self._hashl(val[0])
        return self.indx[i].delete(val)

    def extractRow(self, val):
        if type(val[0]) is int:
            i = self._hashn(val[0])
        else:
            i = self._hashl(val[0])
        return self.indx[i].extractRow(val)

    def readAll(self):
        data=[]
        for cil in self.indx:
            if cil == None:
                continue
            data.extend(cil.readAll())
        return data

    def readRange(self, columnNumber ,lower, upper):
        data = []
        for cil in self.indx:
            if cil == None:
                continue
            data.extend(cil.readRange(columnNumber, lower, upper))
        return data
