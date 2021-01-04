from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.Expresiones.Enum import Enum
from storageManager.jsonMode import *

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

    def analizar(self, tabla, arbol):
        print("analizar")

    def traducir(self, tabla, arbol):

        cadena = "\"create type " + self.valor + " "
        cadena += "as enum "
        cadena += "( "

        if(self.listaExpre):
            #print("------VALORES------")
            for x in range(0,len(self.listaExpre)):
                if(x > 0):
                    cadena += ","
                    #volver tipo primitivo
                if(type(self.listaExpre[x]) is Primitivo):
                    retorno = self.listaExpre[x].traducir(tabla,arbol)
                    cadena  += " "+ retorno.temporalAnterior.replace("\"", "\'")

        
        cadena += ")"
        cadena += ";\""
        arbol.addComen("Asignar cadena")
        temporal1 = tabla.getTemporal()
        arbol.addc3d(f"{temporal1} = { cadena }")

        arbol.addComen("Entrar al ambito")
        temporal2 = tabla.getTemporal()
        arbol.addc3d(f"{temporal2} = P+2")
        temporal3 = tabla.getTemporal()
        arbol.addComen("parametro 1")
        arbol.addc3d(f"{temporal3} = { temporal2}+1")
        arbol.addComen("Asignacion de parametros")
        arbol.addc3d(f"Pila[{temporal3}] = {temporal1}")

        arbol.addComen("Llamada de funcion")
        arbol.addc3d(f"P = P+2")
        arbol.addc3d(f"funcionintermedia()")
        
        arbol.addComen("obtener resultado")
        temporalX = tabla.getTemporal()
        arbol.addc3d(f"{temporalX} = P+2")
        temporalR = tabla.getTemporal()
        arbol.addc3d(f"{temporalR} = Pila[{ temporalX }]")

        arbol.addComen("Salida de funcion")
        arbol.addc3d(f"P = P-2")