from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.storageManager.jsonMode import *
from sql.Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
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
'''
instruccion = ShowDatabases("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''