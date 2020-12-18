import gramatica as g
from tabla_Simbolos import tablaSimbolos
from Errores import errorReportar
from clasesAbstractas import instruccionAbstracta
from graficarArbol import GraphArbol

def procesar_instrucciones(instrucciones,tablaSimbolos,listaErrores):
    
    for instrucion in instrucciones:

        if isinstance(instrucciones,instruccionAbstracta.InstruccionAbstracta):
            instrucion.ejecutar(tablaSimbolos,listaErrores)
            print("entro")




f =  open("./archivoEntrada.txt")
input = f.read()

miTablaSimbolos = tablaSimbolos.tablaDeSimbolos()
miListaErrores = []   #Será una lista de de objetos: errorReportar
instrucciones = g.parse(input)
print(len(instrucciones.hijos))
print(instrucciones)
procesar_instrucciones(instrucciones.hijos,miTablaSimbolos,miListaErrores)

grafica = GraphArbol(instrucciones)
grafica.crearArbol()