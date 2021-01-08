# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Andree Avalos
class Estructura:
    def __init__(self, columnas):
        self.columnas = columnas
        self.registros = {}
        self.pks = None
        self.auto = 0
    
    def setPK(self, columns: list):
        if self.pks:
            return 4
        for num in columns:
            if self.columnas<num: 
                return 5

        self.pks = columns

        if self.registros:
            temp = self.registros
            self.registros = {}
            for tupla in temp.values():
                if self.insert(tupla)!=0:
                    self.registros = temp
                    self.pks = None
                    return 1
        return 0

    def delPK(self):
        if not self.pks:
            return 4
        self.pks = None
        return 0
    
    def insert(self, register:list):
        if len(register)!=self.columnas: return 5
        result = str(self.auto)
        if self.pks:
            temp = []
            for pk in self.pks:
                temp.append(register[pk])
            result = self.concatenar(temp)
            if result in self.registros:
                return 4
        else:
            while True:
                if not str(self.auto) in self.registros:
                    break
                self.auto +=1
                result = str(self.auto)
        self.registros[result] = register
        return 0

    def concatenar(self,lista):
        contador = 0
        salida = ""
        for i in lista:
            if contador == 0: salida = str(i)
            else: salida += "|" + str(i) 
            contador += 1
        return salida
    
    def update(self, register:dict, primarias):
        result = self.concatenar(primarias)
        if not result in self.registros: return 4
        tupla = self.registros[result]
        for dato in register:
            if int(dato)>len(tupla):
                continue
            tupla[int(dato)] = register[dato]
        self.registros[result] = tupla
        return 0 

    def delete(self, llaves):
        result = self.concatenar(llaves)
        if not result in self.registros: return 4
        self.registros.pop(result)
        return 0 

    def truncate(self):
        self.registros = {}
        return 0

    def add(self, valor):
        self.columnas += 1
        for valores in self.registros.values():
            valores.append(valor)
        return 0

    def drop(self, columna):
        temp = self.registros
        if columna in self.pks: return 4
        if self.columnas <= 0: return 4
        for registro in self.registros.values():
            if len(registro)-1 < columna:
                self.registros = temp
                return 5
            registro.pop(columna)
        self.columnas-=1
        return 0
            

    def extractT(self):
        return [tupla for tupla in self.registros.values()]
    
    def extractRT(self,column:int, lower, upper):
        lower = str(lower)
        upper = str(upper)
        lower = int(lower) if lower.isnumeric() else lower
        upper = int(upper) if upper.isnumeric() else upper

        if column > self.columnas: return 1
        temp = []
        for valores in self.registros.values():
            if lower<= valores[column] and valores[column] <= upper:
                temp.append(valores)
        return temp

    def extractR(self, primarias):
        result = self.concatenar(primarias)
        if not result in self.registros: return []
        return self.registros[result]
    

