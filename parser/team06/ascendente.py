import gramaticaAscendente as g
#import gramaticaAscendente as gr
import re
import reportes as h
import TablaDeSimbolos as TS
from queries import *
from expresiones import *
from math import *
import storageManager.jsonMode as store
import reportes as h


def procesar_showdb(query,ts):
    print("entra a Show BD")
    print("entra al print con: ",query.variable)
    h.textosalida+="TYTUS>> Bases de datos existentes\n"
    print(store.showDatabases())
    #llamo al metodo de EDD

def procesar_insertBD(query,ts):
    print("entra a insert")
    print("entra al print con: ",query.idTable, query.listRegistros)
    h.textosalida+="TYTUS>> Insertando registro de una tabla"

def procesar_updateinBD(query,ts):
    print("entro a update")
    print("entro al print con: ",query.idTable,query.asignaciones,query.listcond)
    h.textosalida+="TYTUS>> Actualizando datos en la tabla"

def procesar_deleteinBD(query,ts):
    print("entra a delete from")
    print("entra al print con: ",query.idTable)
    h.textosalida+="TYTUS>> Eliminando registro de una tabla"
    #llamada de funcion

def procesar_createTale(query,ts):
    print("entra a Create table")
    print("entra al print con: ",query.idTable)
    print(query.listColumn)
    #print("cantidad de columnas: ",len(query.listColumn))
    for i in query.listColumn:
        print(i.idColumna,i.TipoColumna)
        if i.RestriccionesCol != None:
            for res in i.RestriccionesCol:
                print(res.typeR)
                print(res.objrestriccion.valor)
                if res.typeR == OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY:
                    print("columna con restriccion llave primaria")
                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.DEFAULT:
                    print("columna con un valor por default")
                    print("valor: ",res.objrestriccion.valor) #<---- correccion
                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.NULL:
                    print("columna que puede ser nulo")
                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.NOT_NULL:
                    print("columna que no debe ser nulo")
                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.UNIQUE_CONSTAINT:
                    print("columna que debe ser unico definicon con constraint")
                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.UNIQUE_COLUMNA:
                    print("columna que debe ser unico")
                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.CHECK_SIMPLE:
                    print("Columna con restriccion check")
                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.CHECK_CONSTRAINT:
                    print("Columna con restricion check definido con constraint")
    h.textosalida+="TYTUS>>Creando tabla"



# ---------------------------------------------------------------------------------------------------------------------
#                                 EJECUCION DE LOS QUERIES PRINCIPALES
# ---------------------------------------------------------------------------------------------------------------------
def procesar_queries(queries, ts) :
    ## lista de instrucciones recolectadas
    for query in queries :
        if isinstance(query, ShowDatabases) : procesar_showdb(query, ts)
        elif isinstance(query, InsertinDataBases) : procesar_insertBD(query,ts)
        elif isinstance(query, UpdateinDataBase) : procesar_updateinBD(query,ts)
        elif isinstance(query, DeleteinDataBases) : procesar_deleteinBD(query, ts)
        elif isinstance(query, CreateTable) : procesar_createTale(query,ts)
        #elif
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
