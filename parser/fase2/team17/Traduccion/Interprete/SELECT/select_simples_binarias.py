from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.simbolo import Simbolo
import hashlib
import datetime


class Select_simples_binarias(NodoArbol):

    def __init__(self, exp, tipo, line, coliumn, substart_=None, subend_=None):
        super().__init__(line, coliumn)
        self.exp = exp
        self.tipo = tipo
        self.substart = substart_
        self.subend = subend_

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero

        if self.tipo == "LENGTH":
            retorno: Valor = Valor(TIPO.NUMERIC, len(expresion.data))
            return retorno
        elif self.tipo == "SUBSTRING" or self.tipo == "SUBSTR":
            substring = expresion.data[self.substart.data: self.subend.data]
            retorno: Valor = Valor(TIPO.CADENA, substring)
            return retorno
        elif self.tipo == "TRIM":
            retorno: Valor = Valor(TIPO.CADENA, expresion.data.strip())
            return retorno
        elif self.tipo == "MD5":
            result = hashlib.md5(expresion.data.encode())
            res = result.hexdigest()
            retorno: Valor = Valor(TIPO.CADENA, res)
            return retorno
        elif self.tipo == "SHA256":
            result = hashlib.sha256(expresion.data.encode())
            res = result.hexdigest()
            retorno: Valor = Valor(TIPO.CADENA, res)
            return retorno
        elif self.tipo == "GET_BYTE":
            result = bytes(expresion.data, "utf-8")
            if len(result) > self.substart.data:
                retorno: Valor = Valor(TIPO.NUMERIC, result[self.substart.data])
                return retorno
        elif self.tipo == "SET_BYTE":
            result = bytes(expresion.data, "utf-8")
            res = result[self.substart.data]
            res2 = bytes(res)
            retorno: Valor = Valor(TIPO.NUMERIC, res2)
            return retorno
        elif self.tipo == "CONVERT":
            date_time_obj = datetime.datetime.strptime(expresion.data, '%d/%m/%y %H:%M:%S')
            retorno: Valor = Valor(TIPO.DATE, date_time_obj)
            return retorno
        elif self.tipo == "ENCODE":
            retorno: Valor = Valor(TIPO.CADENA, expresion.data.encode("UTF-8", "escape"))
            return retorno
        elif self.tipo == "DECODE":
            retorno: Valor = Valor(TIPO.CADENA, expresion.data.decode('base64'))
            return retorno


