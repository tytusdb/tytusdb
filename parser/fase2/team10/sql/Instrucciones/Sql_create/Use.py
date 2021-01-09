from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Excepcion import Excepcion
from sql.storageManager.jsonMode import *
from sql.Instrucciones.Tablas.BaseDeDatos import BaseDeDatos

class Use(Instruccion):
    def __init__(self, id, strGram ,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #SE OBTIENE LA LISTA DE BD
        arbol.lRepDin.append(self.strGram)
        lb=showDatabases()
        #SE RECORRE LA BD PARA VERIFICAR QUE NO EXISTA
        for bd in lb:
            if bd== self.valor:
                #SI SE ENCUENTRA LA BD SE TERMINA EL RECORRIDO
                arbol.setBaseDatos(self.valor)
                #llenar la base de datos
                if(arbol.existeBd(self.valor) == 0):
                    nueva = BaseDeDatos(self.valor)
                    arbol.setListaBd(nueva)
                    arbol.llenarTablas(nueva)
                arbol.consola.append(f"Se selecciono la BD: {self.valor} correctamente.")
                return
        error = Excepcion("100","Semantico",f"No existe la BD: {self.valor}",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append(error.toString())
        #print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))


    def analizar(self, tabla, arbol):
        print("hola")

    def traducir(self, tabla, arbol):
        cadena = "\""+"use "
        cadena += self.valor + ";\""
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