from Cilindro import Cilindro, Registro

class Indice:
    def __init__(self, pkey, ruta):
        self.indx = [None]*30
        self.intervalo = 30
        self.pkey = pkey
        self.ruta = ruta

    def insert(self, registro):
        val = []
        for key in self.pkey:
            val.append(registro[key])
        if type(val[0]) is int:
            i = self._hashn(val[0])
        else:
            i = self._hashl(val[0])
        if self.indx[i] == None:
            self.indx[i] = Cilindro("CS"+str(i), self.pkey, i, self.ruta)
        return self.indx[i].insert(registro)

    def _hashl(self, key):
        fst = ord(key[0].upper())
        return (fst - 65) % self.intervalo

    def _hashn(self, key):
        return (key // 30) % self.intervalo

    def update(self, register, val):
        if type(val[0]) is int:
            i = self._hashn(val[0])
        else:
            i = self._hashl(val[0])
        return self.indx[i].update(register, val)

    def delete(self, val): #probar borrar overflow
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


i = Indice([1], "c")

s = 0
d = "a"
#while s < 90:
 #   print(i.insert([ d,s]))
  #  s += 10

i.insert([1, 'Guatemala',    'Guatemala',    'GTM'])
i.insert([2, 'Cuilapa',      'Santa Rosa',   'GTM'])
i.insert([3, 'San Salvador', 'San Salvador', 'SLV'])
i.insert([5, 'Peten', 'Yucatan', 'aaa'])
i.insert([4, 'San Miguel',   'San Miguel',   'SLV'])
f = i.readAll()
for x in f:
    print(x)

print()
print(i.update({2:"ahora", 3:"nunca"}, ["Peten"]))
print(i.delete(['Guatemala']))
print(i.extractRow(['San Salvador']))
print()
f = i.readAll()
for x in f:
    print(x)
""""
f = i.readAll()
for x in f:
    print(x)
print()
r = i.readRange(1, "g","s")
for x in r:
    print(x)
print()
f = i.indx[0].readAll()
for x in f:
    print(x)
print()
#f = i.indx[2].readAll()
#for x in f:
  #  print(x)
  """

i.insert([1, 'Guatemala',    'Guatemala',    'GTM'])
i.insert([2, 'Cuilapa',      'Santa Rosa',   'GTM'])
i.insert([3, 'San Salvador', 'San Salvador', 'SLV'])
i.insert([4, 'San Miguel',   'San Miguel',   'SLV'])