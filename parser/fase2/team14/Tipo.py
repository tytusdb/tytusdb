import sys


class Tipo():

    def __init__(self, tipo=None, valor=None, size=0, decimales=0):
        'Obtener el valor de la Instrruccion'
        self.valor = valor
        self.tipo = tipo
        self.size = size
        self.decimales = decimales

    def devString(self):
        cad: str = str(self.tipo)
        if self.size > 0:
            cad += '(' + str(self.size)

        if self.decimales > 0:
            cad += ',' + str(self.decimales)

        if self.size > 0 or self.decimales > 0:
            cad += ')'

        return cad

    def tipoInt(self):
        'devueleve el tipo indicado de tipo int'
        if self.valor <= 32767 and self.valor >= -32768:
            self.tipo = 'smallint'
        elif self.valor <= 2147483647 and self.valor >= -2147483648:
            self.tipo = 'integer'
        elif self.valor <= 9223372036854775807 and self.valor >= -9223372036854775808:
            self.tipo = 'bigint'

    def tipoDecimal(self):
        'devueleve el tipo indicado de tipo decimal'
        decimales = str(self.valor).split('.')
        if len(decimales[1]) <= 6:
            self.tipo = 'real'
        elif len(decimales[1]) <= 15:
            if self.valor >= -92233720368547758.08 and self.valor <= 92233720368547758.07:
                self.tipo = 'money'
            self.tipo = 'double'
        else:
            self.tipo = 'decimal'

    def getTipo(self):

        if self.tipo == 'int':
            return self.tipoInt()
        elif self.tipo == 'decimal':
            return self.tipoDecimal()
        else:
            return self.tipo

    def comparetipo(self, tipocolumn, tipovalor):
        'comparo los tipos de la columna con el del valor'
        tipovalor.tipo = tipovalor.tipo.lower()
        tipocolumn.tipo = tipocolumn.tipo.lower()
        if tipocolumn.tipo == 'int':
            tipocolumn.tipo = 'integer'

        if tipovalor.tipo in ('decimal', 'numeric', 'double', 'real', 'money'):
            tipovalor.size = tipovalor.size - 1

        if tipocolumn.size >= tipovalor.size or tipocolumn.size == -1:
            if tipocolumn.tipo == 'decimal' or tipocolumn.tipo == 'numeric':
                if tipovalor.tipo == 'decimal' or tipovalor.tipo == 'numeric' or tipovalor.tipo == 'bigint' or tipovalor.tipo == 'smallint' or tipovalor.tipo == 'integer' or tipovalor.tipo == 'money' or tipovalor.tipo == 'double' or tipovalor.tipo == 'real':
                    return True
            elif tipocolumn.tipo == 'double':
                if tipovalor.tipo == 'double' or tipovalor.tipo == 'bigint' or tipovalor.tipo == 'smallint' or tipovalor.tipo == 'integer' or tipovalor.tipo == 'money' or tipovalor.tipo == 'real':
                    return True
            elif tipocolumn.tipo == 'money':
                if tipovalor.tipo == 'bigint' or tipovalor.tipo == 'smallint' or tipovalor.tipo == 'integer' or tipovalor.tipo == 'money' or tipovalor.tipo == 'real':
                    return True
            elif tipocolumn.tipo == 'real':
                if tipovalor.tipo == 'bigint' or tipovalor.tipo == 'smallint' or tipovalor.tipo == 'integer' or tipovalor.tipo == 'real':
                    return True
            elif tipocolumn.tipo == 'bigint':
                if tipovalor.tipo == 'bigint' or tipovalor.tipo == 'smallint' or tipovalor.tipo == 'integer':
                    return True
            elif tipocolumn.tipo == 'integer':
                if tipovalor.tipo == 'smallint' or tipovalor.tipo == 'integer':
                    return True
            elif tipocolumn.tipo == 'smallint':
                if tipovalor.tipo == 'smallint':
                    return True
            elif tipocolumn.tipo in ('varchar', 'char', 'character varyng', 'text', 'character'):
                if tipovalor.tipo in ('varchar', 'char', 'character varyng', 'text', 'character'):
                    return True
            elif tipocolumn.tipo == 'timestamp without time zone':
                if tipovalor.tipo in ('date', 'timestamp without time zone'):
                    return True
            elif tipocolumn.tipo == 'date':
                if tipovalor.tipo in ('date', 'timestamp without time zone'):
                    return True
            elif tipocolumn.tipo == 'time without time zone':
                if tipovalor.tipo in ('time without time zone', 'timestamp without time zone'):
                    return True
            elif tipocolumn.tipo == 'boolean':
                if tipovalor.tipo == 'boolean':
                    return True