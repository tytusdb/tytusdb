import gramaticaAscendente as g
#import gramaticaAscendente as gr
import re
import reportes as h
import TablaDeSimbolos as TS
from queries import *
from math import *
import storageManager.jsonMode as store
import reportes as h


def procesar_showdb(query,ts):
    print("entra a Show BD")
    print("entra al print con: ",query.variable)
    h.textosalida+="TYTUS>> Bases de datos existentes\n"
    print(store.showDatabases())
    #llamo al metodo de EDD




# ---------------------------------------------------------------------------------------------------------------------
#                                 EJECUCION DE LOS QUERIES PRINCIPALES
# ---------------------------------------------------------------------------------------------------------------------
def procesar_queries(queries, ts) :
    ## lista de instrucciones recolectadas
    for query in queries :
        if isinstance(query, ShowDatabases) : procesar_showdb(query, ts)
        #elif isinstance(query, ShowDatabases) : procesar_showdb(query, ts)
        else : 
            print('Error: instrucción no válida')
            h.errores+=  "<tr><td>"+str(query)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>La consulta no es valida.</td></tr>\n"  



def ejecucionAscendente(input):

    #print("--------------------------------Archivo original---------------------------------------")
    #print(input)
    print("--------------------------------Archivo Ejecucion---------------------------------------")
    prueba =g.parse(input)
    ts_global=TS.TablaDeSimbolos()
    h.todo=prueba
    print(prueba)
    procesar_queries(prueba,ts_global)

    return h.textosalida

# ---------------------------------REPORTE GRAMATICAL -------------------------------------------
def genenerarReporteGramaticalAscendente(ruta):
    h.reporteGramatical(ruta)

def genenerarReporteErroresAscendente(ruta):
    h.reporteErrores(ruta)

def generarReporteSimbolos(ruta):
    print(ruta)
    val=""
    ts_global=TS.TablaDeSimbolos()
    for x in ts_global.simbolos:
        val+="<tr><td>"+str(x)+"</td><td>"+str(ts_global.obtener(x).valor)+"</td><td>"+ts_global.obtener(x).tipo+"</td></tr>\n"
    #construyo el archivo html
    print("manda los datos")
    h.reporteSimbolos(ruta,val)
