from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.Excepcion import Excepcion
from storageManager.jsonMode import *
class AlterDatabase(Instruccion):
    def __init__(self, id, tipo, opcion, id2, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.nombreAntiguo = id
        self.nombreNuevo = id2
        self.opcion = opcion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #aqui vamos a renombrar el alter
        res = alterDatabase(self.nombreAntiguo, self.nombreNuevo)
        if( res == 1):
            Excepcion(3,"Semántico","No se pudo renombrar la base de datos",self.linea,self.columna)
        elif(res == 2):
            error = Excepcion("100","Semantico","La bd no existe.",self.linea,self.columna)
        elif(res == 3):
            error = Excepcion("100","Semantico","La bd nueva ya existe.",self.linea,self.columna)
        else:
            if(len(arbol.listaBd)==0):
                #aqui vamos a renombrar en memoria
                Instruccion = ShowDatabases(None, None, self.linea, self.columna)
                Instruccion.ejecutar(tabla,arbol)
                '''
                import os

                archivo = "/home/decodigo/Documentos/python/archivos/archivo.txt"
                nombre_nuevo = "/home/decodigo/Documentos/python/archivos/archivo_renombrado.txt"

                os.rename(archivo, nombre_nuevo)
                '''
                arbol.consola.append(f"La base de datos se cambio: {self.nombreNuevo} correctamente.")
            else:
                #aqui vamos a renombrar en memoria
                arbol.renombrarBd(self.nombreAntiguo,self.nombreNuevo)
                arbol.consola.append(f"La base de datos se cambio: {self.nombreNuevo} correctamente.")

    
    def analizar(self, tabla, arbol):
        print("analizar")

    def traducir(self, tabla, arbol):
        cadena = "\"alter database " + self.nombreAntiguo
        cadena += " rename to " + self.nombreNuevo
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
'''
instruccion = AlterDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''