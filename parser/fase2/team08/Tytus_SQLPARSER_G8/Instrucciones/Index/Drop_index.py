from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
import numpy as np
import pandas as pd
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.PL.Llamada import Llamada
from Instrucciones.Excepcion import Excepcion

class Drop_index(Instruccion):
    def __init__(self, id_index, id_tabla, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.QUERY),linea,columna,strGram)
        self.id_index = id_index
        self.id_tabla = id_tabla

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        objetoTabla = arbol.devolviendoTablaDeBase(self.id_tabla)

        if objetoTabla !=None:
            bandera =False
            for indi in objetoTabla.lista_de_indices:
                if indi.nombre == self.id_index:
                    objetoTabla.lista_de_indices.remove(indi)
                    bandera= True
                    arbol.consola.append(f"Se borro el Index: {self.id_index} correctamente.")
                    break
            if not bandera:
                error = Excepcion('42704',"Semántico","No existe el indice «"+ self.id_tabla +"».",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        else:
            error = Excepcion('42704',"Semántico","La Tabla: «"+ self.id_tabla +"» no existe.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error


    def buscarColumna(self, nombre, listacolumnas):
        for i in range(0, len(listacolumnas)):
            if listacolumnas[i] == nombre:
                return True

        return False


    def analizar(self, tabla, arbol):
        super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        cadena = f"\"DROP INDEX {self.id_index} ON {self.id_tabla} ;\""
        
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