from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
class ShowDatabases(Instruccion):
    def __init__(self, id, tipo, strGram ,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        listaBD = showDatabases()
        arbol.lRepDin.append(self.strGram)
        lista = []
        columna = ['Database']
        iteracion = 1  
        #arbol.consola.append("Show Databases:")      
        for bd in listaBD:
            if self.valor:
                # Para ver que contenga el string 
                if self.valor in str(bd):
                    lista.append([f"{iteracion}. {bd}"])
                    #arbol.consola.append(f"\t{iteracion}. {bd}")
                    iteracion += 1
            else:
                lista.append([f"{iteracion}. {bd}"])
                #arbol.consola.append(f"\t{iteracion}. {bd}")
                iteracion += 1
            #aqui se van a agregar las bases de datos
            if(arbol.existeBd(bd) == 0):
                nueva = BaseDeDatos(bd)
                arbol.setListaBd(nueva)
            
        #arbol.consola.append("\n")
        print(lista)
        arbol.getMensajeTabla(columna,lista)
        #print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

    def analizar(self, tabla, arbol):
        print("analizar")

    def traducir(self, tabla, arbol):

        cadena = "\"show databases"
        if( self.valor != None):
            cadena += " like "
            cadena += "\'"+self.valor+"\'"
        
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
instruccion = ShowDatabases("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''