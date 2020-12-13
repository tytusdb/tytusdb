from enum import Enum

class TIPO_DE_DATO(Enum) :
    NUMERO = 1
    FLOTANTE=2
    CARACTER=3
    #ir agregando los tipos faltantes para la comprobacion de tipos en las operacioens

class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor) :
        self.id = id
        self.tipo = tipo
        self.valor = valor


class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos

    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        print("a este entra")
        if not id in self.simbolos :
            print('Error1: variable ', id, ' no definida.')
            return("no definida")
        return self.simbolos[id]

    def actualizar(self, simbolo) :
        if not simbolo.id in self.simbolos :
            print('Error2: variable ', simbolo.id, ' no definida.')
        else :
            self.simbolos[simbolo.id] = simbolo

    def mostrar(self,var):
        print(str(var))
        for x in self.simbolos:
            print(x)


    def destruir(self,simbolo):
        print("########################### simbolos>",str(simbolo.id))
        if not simbolo.id in self.simbolos :
            print('Error3: variable ', simbolo.id, ' no definida.')
        else :
            self.simbolos[simbolo.id] = simbolo
            del self.simbolos[simbolo.id]
            print("si lo elimina")