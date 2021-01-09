from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
import collections
from storageManager.jsonMode import *

class AlterIndex(Instruccion):

    def __init__(self, nombreIndice, id1, id2, if_exists, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.nombreIndice = nombreIndice
        self.id1 = id1
        self.id2 = id2
        self.if_exists = if_exists    

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTablas = arbol.devolverTablas()
            objetoIndice = None
            objetoTabla = None
            for t in objetoTablas:
                for i in t.lista_de_indices:
                    if i.nombre == self.nombreIndice:
                        objetoIndice = i
                        objetoTabla = t
            if objetoIndice == None:
                error = Excepcion('42P01',"Semántico","El indice «"+self.nombreIndice+"» no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            else:
                listaColumnas = []
                for t in objetoTabla.lista_de_campos:
                    listaColumnas.append(t.nombre)
                
                if (self.id1 in listaColumnas and self.id2 in listaColumnas):
                    for l in objetoIndice.lRestricciones:
                        if self.id1 in l:
                            nuevo = l.replace(self.id1, self.id2)
                            objetoIndice.lRestricciones.remove(l)
                            objetoIndice.lRestricciones.append(nuevo)
                        arbol.consola.append("Consulta devuelta correctamente.")
                else:
                    error = Excepcion('42701',"Semántico",f"Las columnas {self.id1} y {self.id2} no existen en la tabla.",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        else:
            error = Excepcion("100","Semantico","No ha seleccionado ninguna Base de Datos.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
    
    def analizar(self, tabla, arbol):
        pass
    
    def traducir(self, tabla, arbol):
        cadena = "\"ALTER INDEX "
        cadena += self.nombreIndice
        cadena += " ALTER COLUMN "
        cadena += self.id1 + " "
        cadena += self.id2 + ";\""
        
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
