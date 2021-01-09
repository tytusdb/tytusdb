from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Expresiones.Primitivo import Primitivo
from sql.Instrucciones.Expresiones.Enum import Enum
from sql.storageManager.jsonMode import *

class CreateType(Instruccion):
    def __init__(self, id, tipo, listaExpre, strGram,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = id
        self.listaExpre = listaExpre

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        enum1 = Enum(self.valor, None, self.linea, self.columna)
        lista = []
        if(self.listaExpre):
            #print("------VALORES------")
            for x in range(0,len(self.listaExpre)):
                #volver tipo primitivo
                if(type(self.listaExpre[x]) is Primitivo):
                    valor = self.listaExpre[x].ejecutar(tabla,arbol)
                    lista.append(valor)
                    #print(valor)
        
        #print(lista)
        enum1.listaValores = lista
        arbol.lEnum.append(enum1)
        #print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
        arbol.consola.append("Consulta devuelta correctamente.")

