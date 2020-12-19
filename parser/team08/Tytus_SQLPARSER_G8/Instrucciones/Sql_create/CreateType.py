from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Expresiones.Primitivo import Primitivo
from storageManager.jsonMode import *

class CreateType(Instruccion):
    def __init__(self, id, tipo, listaExpre, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id
        self.listaExpre = listaExpre

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

        lista = []
        if(self.listaExpre):
            print("------VALORES------")
            for x in range(0,len(self.listaExpre)):
                #volver tipo primitivo
                if(type(self.listaExpre[x]) is Primitivo):
                    valor = self.listaExpre[x].ejecutar(tabla,arbol)
                    lista.append(valor)
                    print(valor)
        
        print(lista)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
'''
instruccion = CreateType("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''