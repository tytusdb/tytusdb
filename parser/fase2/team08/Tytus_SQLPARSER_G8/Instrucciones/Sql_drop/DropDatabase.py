from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
class DropDatabase(Instruccion):
    def __init__(self, id, tipo, existe, opcion, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.id = id
        self.opcion = opcion
        self.existe = existe

        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bandera = False
        listaBD = showDatabases()
        for bd in listaBD:
            if bd == self.id:
                bandera = True
                break

        #LA BD se encontro
        if self.existe and bandera:
            print(f"La Base de Datos: {self.id} ha sido eliminada")
            arbol.consola.append(f"Se encontro la base de datos: {self.id} ha sido eliminada")
            dropDatabase(self.id)
            arbol.eliminarBD(self.id)
        elif self.existe and not bandera:
            arbol.consola.append(f"La Base de datos: {self.id} no existe")
        elif not self.existe and bandera:
            arbol.consola.append(f"La Base de Datos: {self.id} ha sido eliminada")
            dropDatabase(self.id)
            arbol.eliminarBD(self.id)
        elif not self.existe and not bandera:
            error = Exception("XX000", "Semantico", "Error Base de Datos no existe", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            
    
    def analizar(self, tabla, arbol):
        print("analizar")

    def traducir(self, tabla, arbol):
        cadena = "\"drop database "
        
        if( self.existe == True):
            cadena += "if exists "
        
        if( self.id != None):
            cadena += self.id
        
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
instruccion = Use("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''