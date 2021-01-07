from . import BinWriter as bi
import os

class Cilindro:
    def __init__(self, nombre, pkeys, ikey, ruta):
        self.indx = [None]*30
        self.longi = 30
        self.nombre = nombre
        self.ruta = ruta+"/"+nombre+".b"
        self.icode = ikey
        self.pkeys = pkeys
        self.seguiente = ikey + 1
        self.readD()
    #hashea numeros
    def _hashn(self, key):
        return key % 30
    #hashea letras
    def _hashl(self, key):
        multi = 1
        hashvalue = 0
        for ch in key:
            hashvalue += multi * ord(ch)
            multi += 1
        return hashvalue % 30

    def _rehash(self, val, i):
        return (val+i)**2 % 30
    #crea una llave primaria en base a la cantidad de llaves entregada
    def _createKey(self, values):
        key = ""
        for k in values:
            key += str(k)+"-"
        if key[-1] == "-":
            key = key[:-1]
        try:
            r = int(key)
            return r
        except:
            return key
    #hashea un llave primaria en base a su tipo de dato
    def hash(self, val):
        if type(val) is int:
            i = self._hashn(val)
        else:
            i = self._hashl(val)
        return i

    #añade una tupla a la DB
    def insert(self, registro):
        try:
            key=[]
            for k in self.pkeys:
                key.append(registro[k])
            keyval = self._createKey(key)
            val = self.hash(keyval)
            i=0
            while i<3:
                if self.indx[val] is None :
                    self.indx[val] = Registro(registro)
                    self.writeD()
                    return 0
                else:
                    ke = []
                    for k in self.pkeys:
                        ke.append(self.indx[val].valores[k])
                    if self._createKey(ke) == keyval:
                        return 4
                    val = self._rehash(val, i)
                i+=1
            else:
                self.indx.append(Registro(registro))
                self.writeD()
                self.longi +=1
                return 0
        except:
            return 1
    #acutaliza los valores de una tupla escpecificada
    def update(self, register, key):
        try:
            keyval = self._createKey(key)
            val = self.hash(keyval)
            i = 0
            while i < 3:
                ke = []
                for k in self.pkeys:
                    ke.append(self.indx[val].valores[k])
                if self._createKey(ke) == keyval:
                    r =  self.indx[val].update(register)
                    if r == 0: self.writeD()
                    return r
                val = self._rehash(val, i)
                i += 1
            else:
                if self.longi > 30:
                    for v in range(30, self.longi):
                        ke = []
                        for k in self.pkeys:
                            ke.append(self.indx[v].valores[k])
                        if self._createKey(ke) == keyval:
                            r = self.indx[v].update(register)
                            if r == 0: self.writeD()
                            return r
                    else:
                        return 4
                else: return 4

        except:
            return 1
    #elimina una tupla segun sea especificado
    def delete(self, key):
        try:
            keyval = self._createKey(key)
            val = self.hash(keyval)
            i = 0
            while i < 3:
                ke = []
                for k in self.pkeys:
                    ke.append(self.indx[val].valores[k])
                if self._createKey(ke) == keyval:
                    self.indx[val] = None
                    self.writeD()
                    return 0
                val = self._rehash(val, i)
                i += 1
            else:
                if self.longi > 30:
                    for v in range(30, self.longi):
                        ke = []
                        for k in self.pkeys:
                            ke.append(self.indx[v].valores[k])
                        if self._createKey(ke) == keyval:
                            self.indx.pop(v)
                            self.longi -= 1
                            self.writeD()
                            return 0
                    else:
                        return 4
                else: return 4
        except:
            return 1
#devuelve una tupla segun el valor solicitado
    def extractRow(self, key):
        try:
            keyval = self._createKey(key)
            val = self.hash(keyval)
            i = 0
            while i < 3:
                ke = []
                for k in self.pkeys:
                    ke.append(self.indx[val].valores[k])
                if self._createKey(ke) == keyval:
                    return self.indx[val].valores
                val = self._rehash(val, i)
                i += 1
            else:
                if self.longi > 30:
                    for v in range(30, self.longi):
                        ke = []
                        for k in self.pkeys:
                            ke.append(self.indx[v].valores[k])
                        if self._createKey(ke) == keyval:
                            return self.indx[v].valores
                    else:
                        return []
                else: return []
        except:
            return []
    #retorna todos los valores
    def readAll(self):
        data = []
        for x in self.indx:
            if x is None:
                continue
            data.append(x.valores)

        return data
    #retorna todos los valores dentro del rango especificado
    def readRange(self, columnNumber, lower, upper):
        data=[]
        flag = (type(lower) is str) and (type(upper) is str)
        if(flag):
            lower = lower.upper()
            upper = upper.upper()
        for x in self.indx:
            if x is None:
                continue
            v = x.valores[columnNumber]
            try:
                if (type(v) is str) and flag:
                    a, b = len(lower), len(upper)
                    li = (a, b)[a > b]
                    v = v.upper()[:li]
                if (v >= lower) and (v <= upper):
                    data.append(x.valores)
            except:
                data.append(None)
        return data

    #escribe en los archivos acutalizados
    def writeD(self):
        bi.write(self.indx, self.ruta)
    #lee los archivos almacenados
    def readD(self):
        if os.path.exists(self.ruta):
            self.indx =  bi.read(self.ruta)


class Registro:
    def __init__(self, valores):
        self.valores = valores

    def update(self, register):
        for k in register:
            try:
                self.valores[k] = register[k]
            except:
                return 1
        return 0

    def alterAddColumn(self):
        try:
            self.valores.append(None)
            return 0
        except:
            return 1

    def alterDropColumn(self, ind: int):
        try:
            self.valores.pop(ind)
            return 0
        except:
            return 1
