import gramatica as g
from tabla_Simbolos import tablaSimbolos
from Errores import errorReportar
from clasesAbstractas import instruccionAbstracta
from graficarArbol import GraphArbol
import jsonMode

def procesar_instrucciones(instrucciones,tablaSimbolos,listaErrores):
    
    for instrucion in instrucciones:

        if isinstance(instrucion,instruccionAbstracta.InstruccionAbstracta):
            instrucion.ejecutar(tablaSimbolos,listaErrores)
            print("entro")




f =  open("./archivoEntrada.txt")
input = f.read()

miTablaSimbolos = tablaSimbolos.tablaDeSimbolos()
miListaErrores = []   #Será una lista de de objetos: errorReportar
instrucciones = g.parse(input)
#print(len(instrucciones.hijos))
#print(instrucciones)
procesar_instrucciones(instrucciones.hijos,miTablaSimbolos,miListaErrores)

grafica = GraphArbol(instrucciones)
grafica.crearArbol()
#print(jsonMode.update("baseDatos1","estudiante",dict({2:"Eduardooo"}),[str(0)]))

#resultado = jsonMode.extractTable("baseDatos1","estudiante")
print("******************************** ERRORES *******************************************")
for nodoError in miListaErrores:
    print(nodoError.descripcion)
