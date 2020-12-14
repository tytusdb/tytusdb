import gramaticaAscendente as g
#import gramaticaAscendente as gr
import re
import reportes as h
import TablaDeSimbolos as TS
from queries import *
import math as mt
import random as rand

from expresiones import *
from math import *
import storageManager.jsonMode as store
import reportes as h
from expresiones import * 
import numpy as geek

# ---------------------------------------------------------------------------------------------------------------------
#                                QUERY SHOW DATABASE
# ---------------------------------------------------------------------------------------------------------------------

def procesar_showdb(query,ts):
    print("entra a Show BD")
    print("entra al print con: ",query.variable)
    h.textosalida+="TYTUS>> Bases de datos existentes\n"
    print(store.showDatabases())
    #llamo al metodo de EDD

# ---------------------------------------------------------------------------------------------------------------------
#                                QUERY SELECT
# ---------------------------------------------------------------------------------------------------------------------

def procesar_select(query,ts):
    print("entra select")
    if query.tipo==1:
        print("entra al select de TIPO 1")
        print(query.operacion)
        if isinstance(query.operacion,list):
            if len(query.operacion)==1:
                print("entra al if de tamaño 1")
                if isinstance(query.operacion[0], ExpresionFuncionBasica): 
                    print(procesar_operacion_basica(query.operacion[0], ts))
                    h.textosalida+="TYTUS>>"  + str(procesar_operacion_basica(query.operacion[0],ts)) +"\n"
                elif isinstance(query.operacion[0],Asignacion):
                    print("entra al select de asignaciones")
                    h.textosalida+="TYTUS>>"  + str(procesar_asignacion(query.operacion[0], ts))  +"\n"
            else:
                print("--------SELECT TIPO 2-------------")
                print("en este select se obtienen todos los campos de la lista de tablas")
                print("obtener tablas: ",procesar_select2_obtenerTablas(query,ts))
        else:
            print("no es array")
            print("entra al if de tamaño 1")
            if isinstance(query.operacion, ExpresionFuncionBasica): 
                print(procesar_operacion_basica(query.operacion, ts))
                h.textosalida+="TYTUS>>"  + str(procesar_operacion_basica(query.operacion,ts)) +"\n"
            elif isinstance(query.operacion,Asignacion):
                print("entra al select de asignaciones")
                h.textosalida+="TYTUS>>"  + str(procesar_asignacion(query.operacion, ts))  +"\n"
    
def procesar_select_Tipo2(query,ts):
    print("************************ENTRO AL 2DO SELECT*********************")
    print(query)
            
def procesar_insertBD(query,ts):
    print("entra a insert")
    print("entra al print con: ",query.idTable, query.listRegistros)
    h.textosalida+="TYTUS>> Insertando registro de una tabla"

def procesar_updateinBD(query,ts):
    print("entro a update")
    print("entro al print con: ",query.idTable,query.asignaciones,query.listcond)
    h.textosalida+="TYTUS>> Actualizando datos en la tabla"

def procesar_select2_obtenerTablas(query,ts):
    print("Entra al else del select")
    tablas=""
    for x in range(len(query.operacion)) :
        if isinstance(query.operacion[x], ExpresionFuncionBasica): 
            print("entra a la opcion funcionBasica del else")
            tablas+=query.operacion[x].id.id+" ; "
        elif isinstance(query.operacion[x],Asignacion):
            print("entra a la opcion select del else")

        elif isinstance(query.operacion[x],ExpresionIdentificador):
            print("entra a la opcion de identificador del lse")
            tablas+=query.operacion[x].id+" ; "
        if x==len(query.operacion)-1:
            print(tablas)
            return tablas

# ---------------------------------------------------------------------------------------------------------------------
#                                OPERACIONES BASICAS
# ---------------------------------------------------------------------------------------------------------------------


def procesar_operacion_basica(query,ts):
    print("entra a operacion basica")
    print(query.id)
    if isinstance(query.id,ExpresionABS): return resolver_expresion_aritmetica(query.id, ts)
    elif isinstance(query.id,ExpresionCBRT): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCEIL): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCEILING): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionDEGREES): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionDIV): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionEXP): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionFACTORIAL): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionFLOOR): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionGCD): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionLN): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionLOG): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionMOD): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionPI): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionPOWER): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionRADIANS): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionROUND): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionSIGN): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionSQRT): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionTRUNC): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionRANDOM): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionWIDTHBUCKET): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionACOS): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionACOSD): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionASIN): return resolver_expresion_aritmetica(query.id,ts)  
    elif isinstance(query.id,ExpresionASIND): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionATAN): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionATAND): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionATAN2): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionATAN2D): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCOS): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCOSD): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCOT): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCOTD): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionSIN): return resolver_expresion_aritmetica(query.id,ts)  
    elif isinstance(query.id,ExpresionSIND): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionTAN): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionTAND): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionSINH): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCOSH): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionTANH): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionASINH): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionACOSH): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionATANH): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionIdentificador): return resolver_expresion_aritmetica(query.id,ts)
    else:
        print("error en operaciones basicas")


# ---------------------------------------------------------------------------------------------------------------------
#                               PROCESAR ASIGNACIONES
# ---------------------------------------------------------------------------------------------------------------------
def procesar_asignacion(query, ts) :  
    print("entra a procesar asignacion")
    print(query.campo)
    print(query.alias)
    if isinstance(query.campo,Asignacion):
        print("***-------aun hay instancias por baja----------------")
        print(query.campo)
        print(query.alias)
        procesar_asignacion(query.campo,ts)
        procesar_asignacion(query.alias,ts)
    elif isinstance(query.campo,ExpresionIdentificador):
        print("-------------estos datos se asignan--------------")
        print(query.campo.id)
        print(query.alias.id)
        return guardar_asignacion(query.campo.id,query.alias.id,ts)
    elif isinstance(query.campo, ExpresionFuncionBasica): 
        print("entra a procesar asignacion de expresion basica")
        print(procesar_operacion_basica(query.operacion, ts))
            #h.textosalida+="TYTUS>>"  + str(procesar_operacion_basica(query.operacion,ts)) +"\n"
    elif isinstance(query.campo,ExpresionDIV):
        print("-------------estos datos se asignan con operacion div--------------")
        exp1= resolver_expresion_aritmetica(query.campo.exp1, ts)
        exp2= resolver_expresion_aritmetica(query.campo.exp2, ts)
        resultado=exp1//exp2
        return guardar_asignacion(resultado,query.alias.id,ts)
    elif isinstance(query.campo,ExpresionGCD):
        exp1= resolver_expresion_aritmetica(query.campo.exp1, ts)
        exp2= resolver_expresion_aritmetica(query.campo.exp2, ts)
        resultado=mt.gcd(exp1,exp2)
        return guardar_asignacion(resultado,query.alias.id,ts)
    elif isinstance(query.campo,ExpresionMOD):
        exp1= resolver_expresion_aritmetica(query.campo.exp1, ts)
        exp2= resolver_expresion_aritmetica(query.campo.exp2, ts)
        resultado=mt.fmod(exp1,exp2)
        return guardar_asignacion(resultado,query.alias.id,ts)
    elif isinstance(query.campo,ExpresionPOWER):
        exp1= resolver_expresion_aritmetica(query.campo.exp1, ts)
        exp2= resolver_expresion_aritmetica(query.campo.exp2, ts)
        resultado=mt.pow(exp1,exp2)
        return guardar_asignacion(resultado,query.alias.id,ts)
    elif isinstance(query.campo,ExpresionWIDTHBUCKET):
        exp1= resolver_expresion_aritmetica(query.campo.exp1, ts)
        exp2= resolver_expresion_aritmetica(query.campo.exp2, ts)
        exp3= resolver_expresion_aritmetica(query.campo.exp3, ts)
        exp4= resolver_expresion_aritmetica(query.campo.exp4, ts)
        resultado=0
        return guardar_asignacion(resultado,query.alias.id,ts)
    elif isinstance(query.campo,ExpresionATAN2):
        exp1= resolver_expresion_aritmetica(query.campo.exp1, ts)
        exp2= resolver_expresion_aritmetica(query.campo.exp2, ts)
        resultado=mt.atan2(exp1,exp2)
        return guardar_asignacion(resultado,query.alias.id,ts)
    elif isinstance(query.campo,ExpresionATAN2D):
        exp1= resolver_expresion_aritmetica(query.campo.exp1, ts)
        exp2= resolver_expresion_aritmetica(query.campo.exp2, ts)
        resultado=mt.degrees(mt.atan2(exp1,exp2))
        return guardar_asignacion(resultado,query.alias.id,ts)
    elif isinstance(query, ExpresionNumero) :
        print(query.id)
    elif isinstance(query, ExpresionIdentificador) :
        return ts.obtener(query.id).valor
    elif isinstance(query,ExpresionCadenas):
        print(query.id)
    else :
        print("-------------estos datos se asignan con operacion--------------")
        print(query.campo.exp)
        print(query.alias.id)
        return guardar_asignacion(resolver_expresion_aritmetica(query.campo,ts),query.alias.id,ts)
        


    
    


 # ---------------------------------------------------------------------------------------------------------------------
#                               PARA ALMACENAR LAS ASIGNACIONES
# ---------------------------------------------------------------------------------------------------------------------
   
    
def guardar_asignacion(valor, variable,ts):  
    if ts.obtener2(variable)==0:
        simbolo = TS.Simbolo(variable, 1, valor)      # inicializamos con 0 como valor por defecto
        ts.agregar(simbolo)
        print("se creo una nueva variable")
        return "se creo una nueva variable: "+str(variable)
    else:
        simbolo = TS.Simbolo(variable, 1, valor)
        ts.actualizar(simbolo)
        print("la variable ya existia, se actualizo")
        return "se actualizo variable: "+str(variable)


# ---------------------------------------------------------------------------------------------------------------------
#                                Expresiones aritmeticas
# ---------------------------------------------------------------------------------------------------------------------

def resolver_expresion_aritmetica(expNum, ts) :
    try:
        if isinstance(expNum, ExpresionNegativo) :
            return expNum.id * -1
        elif isinstance(expNum,ExpresionABS):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return abs(exp)
        elif isinstance(expNum,ExpresionCBRT):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return exp**(1/3)
        elif isinstance(expNum,ExpresionCEIL):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.ceil(exp)
        elif isinstance(expNum,ExpresionCEILING):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.ceil(exp)
        elif isinstance(expNum,ExpresionDEGREES):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.degrees(exp)
        elif isinstance(expNum,ExpresionDIV):
            exp1= resolver_expresion_aritmetica(expNum.exp1, ts)
            exp2= resolver_expresion_aritmetica(expNum.exp2, ts)
            return exp1//exp2
        elif isinstance(expNum,ExpresionEXP):
            exp1= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.exp(exp1)
        elif isinstance(expNum,ExpresionFACTORIAL):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.factorial(exp)
        elif isinstance(expNum,ExpresionFLOOR):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.floor(exp)
        elif isinstance(expNum,ExpresionGCD):
            exp1= resolver_expresion_aritmetica(expNum.exp1, ts)
            exp2= resolver_expresion_aritmetica(expNum.exp2, ts)
            return mt.gcd(exp1,exp2)
        elif isinstance(expNum,ExpresionLN):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.log(exp) #este devuelve el logaritmo natural
        elif isinstance(expNum,ExpresionLOG):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.log10(exp) #este devuelve el logaritmo base 10
        elif isinstance(expNum,ExpresionMOD):
            exp1= resolver_expresion_aritmetica(expNum.exp1, ts)
            exp2= resolver_expresion_aritmetica(expNum.exp2, ts)
            return mt.fmod(exp1,exp2)
        elif isinstance(expNum,ExpresionPI):
            return mt.pi
        elif isinstance(expNum,ExpresionPOWER):
            exp1= resolver_expresion_aritmetica(expNum.exp1, ts)
            exp2= resolver_expresion_aritmetica(expNum.exp2, ts)
            return mt.pow(exp1,exp2)
        elif isinstance(expNum,ExpresionRADIANS):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.radians(exp)   
        elif isinstance(expNum,ExpresionROUND):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return round(exp)
        elif isinstance(expNum,ExpresionSIGN):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return geek.sign(exp)
        elif isinstance(expNum,ExpresionSQRT):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.sqrt(exp)
        elif isinstance(expNum,ExpresionTRUNC):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.trunc(exp)
        elif isinstance(expNum,ExpresionRANDOM):
            return rand.random()
        elif isinstance(expNum,ExpresionWIDTHBUCKET):
            exp1= resolver_expresion_aritmetica(expNum.exp1, ts)
            exp2= resolver_expresion_aritmetica(expNum.exp2, ts)
            exp3= resolver_expresion_aritmetica(expNum.exp3, ts)
            exp4= resolver_expresion_aritmetica(expNum.exp4, ts)
            return 0
        elif isinstance(expNum,ExpresionACOS):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.acos(exp)
        elif isinstance(expNum,ExpresionACOSD):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.degrees(mt.acos(exp))
        elif isinstance(expNum,ExpresionASIN):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.asin(exp)
        elif isinstance(expNum,ExpresionASIND):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.degrees(mt.asin(exp))
        elif isinstance(expNum,ExpresionATAN):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.atan(exp)
        elif isinstance(expNum,ExpresionATAND):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.degrees(mt.asin(exp))
        elif isinstance(expNum,ExpresionATAN2):
            exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
            exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
            return mt.atan2(exp1,exp2)
        elif isinstance(expNum,ExpresionATAN2D):
            exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
            exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
            return mt.degrees(mt.atan2(exp1,exp2))
        elif isinstance(expNum,ExpresionCOS):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.cos(exp)
        elif isinstance(expNum,ExpresionCOSD):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.degrees(mt.asin(exp))
        elif isinstance(expNum,ExpresionCOT):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return 1/mt.tan(exp)
        elif isinstance(expNum,ExpresionCOTD):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.degrees(1/mt.tan(exp))
        elif isinstance(expNum,ExpresionSIN):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.sin(exp)
        elif isinstance(expNum,ExpresionSIND):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.degrees(mt.sin(exp))
        elif isinstance(expNum,ExpresionTAN):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.tan(exp)
        elif isinstance(expNum,ExpresionTAND):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.degrees(mt.tan(exp))
        elif isinstance(expNum,ExpresionSINH):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.sinh(exp)
        elif isinstance(expNum,ExpresionCOSH):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.cosh(exp)
        elif isinstance(expNum,ExpresionTANH):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.tanh(exp)
        elif isinstance(expNum,ExpresionASINH):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.asinh(exp)
        elif isinstance(expNum,ExpresionACOSH):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.acosh(exp)
        elif isinstance(expNum,ExpresionATANH):
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            return mt.atanh(exp)
        elif isinstance(expNum, ExpresionNumero) :
            return expNum.id
        elif isinstance(expNum, ExpresionIdentificador) :
            return ts.obtener(expNum.id).valor
        elif isinstance(expNum,ExpresionCadenas):
            return expNum.id
        else:
            print("error de operacion aritmetica")
            #h.errores+=  "<tr><td>"+str(exp1)+"|"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>error de operacion</td></tr>\n"
    except ValueError as F:
        return ("Se genero un error: "+str(F))
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
def drop_table(query,ts):
    print("voy a imprimir los valores del drop :v")
    print("aqui viene el id de la tabla a dropear:",query.id)
    h.textosalida+="TYTUS>> Eliminaré la tabla"+query.id

def alter_table(query,ts):
    print("voy a imprimir los valores del alter :v")
    print("aqui viene el id de la tabla a cambiar:",query.id)
    h.textosalida+="TYTUS>> Alteraré la tabla"+query.id
    temp = query.querys.tipo
    if(temp.upper()=="ADD"):
        print("VIENE UN ADD, POR TANTO SE AGREGA ALGO A LA TABLA")
        print("SE AGREGARÁ UNA: ", query.querys.contenido.tipo)
        print("DE NOMBRE: ",query.querys.contenido.id1)
        print("DE TIPO: ", query.querys.contenido.tipo2)
    elif(temp.upper()=="DROP"):
        print("VIENE UN DROP, ALGO DE LA TABLA VA A EXPLOTAR, F")
        print("LO QUE EXPLOTARA SERA: ", query.querys.contenido.tipo)
        print("CON EL ID: ", query.querys.contenido.id)
    elif(temp.upper()=="ALTER"):
        print("VIENE UN ALTER DENTRO DE OTRO ALTER")
        print("DE TIPO: ", query.querys.contenido.tipo)
        print("CON EL ID: ", query.querys.contenido.id)
        print("PARA ASIGNAR: ", query.querys.contenido.tipoAsignar)


        

    

# ---------------------------------------------------------------------------------------------------------------------
#                                 EJECUCION DE LOS QUERIES PRINCIPALES
# ---------------------------------------------------------------------------------------------------------------------
def procesar_queries(queries, ts) :
    ## lista de instrucciones recolectadas
    for query in queries :
        if isinstance(query, ShowDatabases) : procesar_showdb(query, ts)
        elif isinstance(query, Select) : procesar_select(query, ts)
        
        elif isinstance(query, Select2) : procesar_select_Tipo2(query, ts)
        elif isinstance(query, InsertinDataBases) : procesar_insertBD(query,ts)
        elif isinstance(query, UpdateinDataBase) : procesar_updateinBD(query,ts)
        elif isinstance(query, DeleteinDataBases) : procesar_deleteinBD(query, ts)
        elif isinstance(query, CreateTable) : procesar_createTale(query,ts)
        #elif
        #elif isinstance(query, ShowDatabases) : procesar_showdb(query, ts)
        elif isinstance(query,DropTable): drop_table(query,ts)
        elif isinstance(query,AlterTable): alter_table(query,ts)
        else : 
            print('Error: instrucción no válida')
            h.errores+=  "<tr><td>"+str(query)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>La consulta no es valida.</td></tr>\n"  



def ejecucionAscendente(input):
    #print("El resultado de la creacion de tabla es: %d",store.createTable("db5", "table1", 5))
    #print(store.showTables)
    #print(store.showTables("db2"))
    #print("--------------------------------Archivo original---------------------------------------")
    #print(input)
    print("--------------------------------Archivo Ejecucion---------------------------------------")
    prueba =g.parse(input)
    ts_global=TS.TablaDeSimbolos()
    h.todo=prueba
    print(prueba)
    procesar_queries(prueba,ts_global)
    h.textosalida+="--------------------FIN EJECUCION ASCENDENTE--------------------\n"
    return h.textosalida

# ---------------------------------REPORTE GRAMATICAL -------------------------------------------
def genenerarReporteGramaticalAscendente(ruta):
    h.reporteGramatical(ruta)

def genenerarReporteErroresAscendente(ruta):
    h.reporteErrores(ruta)

def generarReporteSimbolos(ruta):
    print(ruta)
    val=""
    print("++++++++++++++++")
    print(ruta)
    ts_global=TS.TablaDeSimbolos()
    for x in ts_global.simbolos:
        print(x)
        print(ts_global.obtener(x).id)
        print(ts_global.obtener(x).valor)
        val+="<tr><td>"+str(ts_global.obtener(x).id)+"</td><td>"+str(ts_global.obtener(x).valor)+"</td></tr>\n"
    #construyo el archivo html
    print("manda los datos")
    h.reporteSimbolos(ruta,val)
