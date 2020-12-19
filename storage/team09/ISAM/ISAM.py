<<<<<<< HEAD
from Cilindro import Cilindro
import BinWriter as bin
import os

class Indice:
    def __init__(self, pkey, ruta):
        self.indx = [None]*30
        self.intervalo = 30
        self.pkey = pkey
        self.ruta = ruta
        self.readI()

    def readI(self):
        if os.path.exists(self.ruta+"/indx.b"):
            data = bin.read(self.ruta+"/indx.b")
            i = 0
            for d in data:
                if type(d) is str:
                    self.indx[i] = Cilindro(d, self.pkey, i, self.ruta)
                elif type(d) is list:
                    self.pkey = d
                elif d is None:
                    self.indx[i] = None
                i+=1

    def writeI(self):
        data=[]
        for x in self.indx:
            if x != None:
                data.append(x.nombre)
            else:
                data.append(None)
        data.append(self.pkey)
        bin.write(data, self.ruta+"/indx.b")

    def insert(self, registro):
        val = []
        try:
            for key in self.pkey:
                val.append(registro[key])
            if type(val[0]) is int:
                i = self._hashn(val[0])
            else:
                i = self._hashl(val[0])
            if self.indx[i] == None:
                self.indx[i] = Cilindro("CS"+str(i), self.pkey, i, self.ruta)
                bin.write([None]*30, self.ruta +"/"+ "CS"+str(i)+".b")
                self.writeI()
            return self.indx[i].insert(registro)
        except:
            return 1

    def _hashl(self, key):
        fst = ord(key[0].upper())
        return (fst - 65) % self.intervalo
=======
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
            self.indx[i] = Cilindro("CS"+str(i))
        return self.indx[i].insert(registro)

    def _hashl(self, key):
        fst = ord(key[0].upper())
        return (fst - 65) // self.intervalo
>>>>>>> main

    def _hashn(self, key):
        return (key // 30) % self.intervalo

    def update(self, register, val):
<<<<<<< HEAD
        try:
            if type(val[0]) is int:
                i = self._hashn(val[0])
            else:
                i = self._hashl(val[0])
            return self.indx[i].update(register, val)
        except:
            return 1

    def delete(self, val): #probar borrar overflow
        try:
            if type(val[0]) is int:
                i = self._hashn(val[0])
            else:
                i = self._hashl(val[0])
            return self.indx[i].delete(val)
        except:
            return 1

    def extractRow(self, val):
        try:
            if type(val[0]) is int:
                i = self._hashn(val[0])
            else:
                i = self._hashl(val[0])
            return self.indx[i].extractRow(val)
        except:
            return 1

    def readAll(self):
        data=[]
        try:
            for cil in self.indx:
                if cil == None:
                    continue
                data.extend(cil.readAll())
            return data
        except:
            return None

    def readRange(self, columnNumber ,lower, upper):
        data = []
        try:
            for cil in self.indx:
                if cil == None:
                    continue
                data.extend(cil.readRange(columnNumber, lower, upper))
            return data
        except:
            return None

    #actualiza todos los registros a su version mas reciente y reescribe el indice a su version mas reciente
    def refreshMem(self):
        for x in self.indx:
            if x != None:
                x.indx = bin.read(self.ruta +"/"+ x.nombre + ".b")
        self.writeI()


=======
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
        for cil in self.indx:
            if not cil == None:
                return cil.readAll()

    def readRange(self, upper, lower):
        pass
>>>>>>> main
