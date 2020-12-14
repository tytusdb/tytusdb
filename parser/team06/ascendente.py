import gramaticaAscendente as g
#import gramaticaAscendente as gr
import re
import reportes as h
import TablaDeSimbolos as TS
from queries import *
from expresiones import *
import math
import storageManager.jsonMode as store
import reportes as h

# ---------------------------------------------------------------------------------------------------------------- 
#                                             QUERIES
# ----------------------------------------------------------------------------------------------------------------

def procesar_showdb(query,ts):
    h.textosalida+="TYTUS>> Bases de datos existentes\n"
    print(store.showDatabases())
    #llamo al metodo de EDD
# ---------------------------------------------------------------------------------------------------------------- 

def procesar_createdb(query,ts):
    h.textosalida+="TYTUS>> Bases de datos existentes\n"
    if store.createDatabase(query.variable) == 0: 
        print("SE CREO LA BASE DE DATOS "+str(query.variable)+" ")
    elif store.createDatabase(query.variable) == 2:
        print("LA BASE DE DATOS "+str(query.variable)+" YA EXISTE")
    elif store.createDatabase(query.variable) == 1:
        print("ERROR :(")
        
    #llamo al metodo de EDD
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_createwithparametersdb(query,ts):
    for q in query.parametros:   
        if isinstance(q, ExpresionOwner) :
            print(query.variable)
            print("OWNER:",q.owner)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        elif isinstance(q, ExpresionMode) :
            print(query.variable)
            print("MODE:",q.mode)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        else:
            print("TIPO INCORRECTO DE QUERY:",query)
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_alterdb(query,ts):
    if store.alterDatabase(query.id_original,query.id_alter) == 0: 
        print("LA BASE DE DATOS "+str(query.id_original)+" HA SIDO ALTERADA")
# ---------------------------------------------------------------------------------------------------------------- 
    elif store.alterDatabase(query.id_original,query.id_alter)  == 3:
        print("LA BASE DE DATOS "+str(query.id_alter)+" YA EXISTE")
# ---------------------------------------------------------------------------------------------------------------- 
    elif store.alterDatabase(query.id_original,query.id_alter)  == 2:
        print("LA BASE DE DATOS "+str(query.id_original)+" NO EXISTE")
# ---------------------------------------------------------------------------------------------------------------- 
    elif store.alterDatabase(query.id_original,query.id_alter)  == 1:
        print("ERROR :(")
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_alterwithparametersdb(query,ts):
    print(query.id_original)
    print(query.owner)
    print(query.id_alter)
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_dropdb(query,ts):
    if store.dropDatabase(query.id) == 0: 
        print("LA BASE DE DATOS "+str(query.id)+" HA SIDO ELIMINADA")
# ---------------------------------------------------------------------------------------------------------------- 
    elif store.dropDatabase(query.id)  == 2:
        print("LA BASE DE DATOS "+str(query.id)+" NO EXISTE")
# ---------------------------------------------------------------------------------------------------------------- 
    elif store.dropDatabase(query.id)  == 1:
        print("ERROR :(")
# ---------------------------------------------------------------------------------------------------------------- 
#                                             QUERIES
# ----------------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------------- 
#                                             EXPRESIONES
# ----------------------------------------------------------------------------------------------------------------

# --------------------------------------EXPRESION ARITMETICA-----------------------------------------------------------
def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionAritmetica) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        #---------------------------------OPERACION MAS-----------------------------------------------------------------------        
        if expNum.operador == OPERACION_ARITMETICA.MAS : 
            if  isinstance(exp1,int)  and isinstance(exp2,int):
                print("RESULTADO:",exp1+exp2)
                return exp1 + exp2
            elif  isinstance(exp1,int)  and isinstance(exp2,float): 
                print("RESULTADO:",exp1 + exp2)
                return exp1 + exp2
            elif  isinstance(exp1,float)  and isinstance(exp2,float): 
                print("RESULTADO:",exp1 + exp2)
                return exp1 + exp2
            elif  isinstance(exp1,float)  and isinstance(exp2,int): 
                print("RESULTADO:",exp1 + exp2)
                return exp1 + exp2
            elif  isinstance(exp1,str)  and isinstance(exp2,str): 
                print("RESULTADO:",exp1 + exp2)
                return exp1 + exp2
            else: 
                print("error: no se pueden operar distintos tipos")
                h.errores+=  "<tr><td>"+str(exp1)+"+"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                return 0
        #---------------------------------OPERACION MENOS-----------------------------------------------------------------------        
        elif expNum.operador == OPERACION_ARITMETICA.MENOS : 
            if  isinstance(exp1,int)  and isinstance(exp2,int):
                print("RESULTADO:",exp1-exp2)
                return exp1 - exp2
            elif  isinstance(exp1,float)  and isinstance(exp2,int):
                print("RESULTADO:",exp1-exp2)
                return exp1 - exp2
            elif  isinstance(exp1,float)  and isinstance(exp2,float):
                print("RESULTADO:",exp1-exp2)
                return exp1 - exp2
            elif  isinstance(exp1,int)  and isinstance(exp2,float):
                print("RESULTADO:",exp1-exp2)
                return exp1 - exp2
            else: 
                print("error: no se pueden operar distintos tipos")
                h.errores+=  "<tr><td>"+str(exp1)+"-"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                return 0
        #---------------------------------OPERACION POR-----------------------------------------------------------------------        
        elif expNum.operador == OPERACION_ARITMETICA.POR : 
            if  isinstance(exp1,int)  and isinstance(exp2,int):
                print("RESULTADO:",exp1 * exp2)
                return exp1 * exp2
            elif  isinstance(exp1,float)  and isinstance(exp2,int):
                print("RESULTADO:",exp1 * exp2)
                return exp1 * exp2
            elif  isinstance(exp1,float)  and isinstance(exp2,float):
                print("RESULTADO:",exp1 * exp2)
                return exp1 * exp2
            elif  isinstance(exp1,int)  and isinstance(exp2,float):
                print("RESULTADO:",exp1 * exp2)
                return exp1 * exp2
            else: 
                print("error: no se pueden operar distintos tipos")
                h.errores+=  "<tr><td>"+str(exp1)+"*"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                return 0
        #---------------------------------OPERACION DIVISION-----------------------------------------------------------------------        
        elif expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : 
            if  isinstance(exp1,int)  and isinstance(exp2,int):
                print("DIVIDENDO:",exp1)
                print("DIVISOR:",exp2)  
                if exp2==0 :
                    print("error: divido por 0 da infinito")
                    h.errores+=  "<tr><td>"+str(exp1)+"/"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                    return 0 
                return exp1/exp2

            elif  isinstance(exp1,float)  and isinstance(exp2,int):
                print("DIVIDENDO:",exp1)
                print("DIVISOR:",exp2)   
                if exp2 == 0 :
                    print("error: divido por 0 da infinito")
                    h.errores+=  "<tr><td>"+str(exp1)+"/"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                    return 0  
                return exp1 / exp2

            elif  isinstance(exp1,float)  and isinstance(exp2,float):
                print("DIVIDENDO:",exp1)
                print("DIVISOR:",exp2)   
                if exp2 == 0.0 :
                    print("error: divido por 0.0 da infinito")
                    h.errores+=  "<tr><td>"+str(exp1)+"/"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                    return 0  
                return exp1 / exp2

            elif  isinstance(exp1,int)  and isinstance(exp2,float):
                print("DIVIDENDO:",exp1)
                print("DIVISOR:",exp2)   
                if exp2 == 0.0 :
                    print("error: divido por 0.0 da infinito")
                    h.errores+=  "<tr><td>"+str(exp1)+"/"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                    return 0  
                return exp1 / exp2
            else: 
                print("error: no se pueden operar distintos tipos")
                h.errores+=  "<tr><td>"+str(exp1)+"/"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                return 0
        #---------------------------------OPERACION MODULO-----------------------------------------------------------------------        
        elif expNum.operador == OPERACION_ARITMETICA.MODULO : 
            if  isinstance(exp1,int)  and isinstance(exp2,int):
                print("NUMERO:",exp1)
                print("MODULO:",exp2) 
                if exp2==0 :
                    print("error: divido modular por 0 da infinito")
                    h.errores+=  "<tr><td>"+str(exp1)+"%"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                    return 0 
                return exp1 % exp2

            elif  isinstance(exp1,float)  and isinstance(exp2,int):
                print("NUMERO:",exp1)
                print("MODULO:",exp2)
                if exp2==0 :
                    print("error: divido modular por 0 da infinito")
                    h.errores+=  "<tr><td>"+str(exp1)+"%"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                    return 0  
                return exp1 % exp2

            elif  isinstance(exp1,float)  and isinstance(exp2,float):
                print("NUMERO:",exp1)
                print("MODULO:",exp2)
                if exp2==0.0 :
                    print("error: divido modular por 0.0 da infinito")
                    h.errores+=  "<tr><td>"+str(exp1)+"%"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                    return 0  
                return exp1 % exp2

            elif  isinstance(exp1,int)  and isinstance(exp2,float):
                print("NUMERO:",exp1)
                print("MODULO:",exp2)
                if exp2==0.0 :
                    print("error: divido modular por 0.0 da infinito")
                    h.errores+=  "<tr><td>"+str(exp1)+"%"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                    return 0  
                return exp1 % exp2

            else: 
                print("error: no se pueden operar distintos tipos")
                h.errores+=  "<tr><td>"+str(exp1)+"%"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                return 0
        #---------------------------------OPERACION POTENCIA-----------------------------------------------------------------------        
        elif expNum.operador == OPERACION_ARITMETICA.POTENCIA : 
            if  isinstance(exp1,int)  and isinstance(exp2,int):
                print("RESULTADO:",math.pow(exp1,exp2))  
                return math.pow(exp1,exp2)
            elif  isinstance(exp1,float)  and isinstance(exp2,int):
                return math.pow(exp1,exp2)
            elif  isinstance(exp1,float)  and isinstance(exp2,float):
                return math.pow(exp1,exp2)
            elif  isinstance(exp1,int)  and isinstance(exp2,float):
                return math.pow(exp1,exp2)
            else: 
                print("error: no se pueden operar distintos tipos")
                h.errores+=  "<tr><td>"+str(exp1)+"^"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>no se pueden operar distintos tipos</td></tr>\n"
                return 0
#--------------------------------------------------------------------------------------------------------------------------        
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
#--------------------------------------------------------------------------------------------------------------------------          
    elif isinstance(expNum, ExpresionNegativo) :
        print("NEGATIVO")
        print("EXP_NUM:",expNum.exp)
        return expNum.exp * -1
#--------------------------------------------------------------------------------------------------------------------------        
    elif isinstance(expNum, ExpresionIdentificador) :
        return ts.obtener(expNum.id).valor
#--------------------------------------------------------------------------------------------------------------------------        
    elif isinstance(expNum, ExpresionInvocacion) :
        resultado = "" 
        #r1 = ts.obtener(expNum.id).valor 
        #r2 = ts.obtener(expNum.id1).valor
        r1 = expNum.id
        r2 = expNum.id1
        resultado = r1 + "." + r2
        print(resultado)
        return resultado
#--------------------------------------------------------------------------------------------------------------------------        
    elif isinstance(expNum,ExpresionCadenas):
        print("CADENA:",expNum.val)
        return expNum.val
#--------------------------------------------------------------------------------------------------------------------------        
    else:
        h.errores+=  "<tr><td>"+str(exp1)+"|"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>error de operacion</td></tr>\n"

# ------------------------------------------------EXPRESION LOGICA---------------------------------------------------------------------

def resolver_expresion_logica(expLog, ts) :
    if isinstance(expLog,ExpresionLogica):
        exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
        print("EXP1:",exp1)
        exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
        print("EXP2:",exp2)
        #---------------------------------OPERACION AND-----------------------------------------------------------------------        
        if expLog.operador == OPERACION_LOGICA.AND : 
            return exp1 and exp2
        #---------------------------------OPERACION OR-----------------------------------------------------------------------                
        elif expLog.operador == OPERACION_LOGICA.OR : 
            return exp1 or exp2
#---------------------------------OPERACION NOT-----------------------------------------------------------------------                     
    elif isinstance(expLog,ExpresionNOT):
        exp = resolver_expresion_aritmetica(expLog.exp, ts)
        print("EXP:",exp)
        pivote=not exp
        print("PIVOTE",pivote)
        if pivote==True: 
            print("TRUE")
            return 1
        else:
            print("FALSE") 
            return 0

# ------------------------------------------------EXPRESION BIT---------------------------------------------------------------------

def resolver_expresion_bit(expBit, ts) :
    print("ENTRO")
    if isinstance(expBit,ExpresionBIT):
        exp1 = resolver_expresion_aritmetica(expBit.exp1, ts)
        print("EXP1:",exp1)
        exp2 = resolver_expresion_aritmetica(expBit.exp2, ts)
        print("EXP2:",exp2)
        #---------------------------------OPERACION LEFT SHIFT-----------------------------------------------------------------------        
        if expBit.operador == OPERACION_BIT.DESPLAZAMIENTO_IZQUIERDA :
            print("RESULTADO:",exp1<<exp2) 
            return exp1 << exp2
        #---------------------------------OPERACION RIGHT SHIFT-----------------------------------------------------------------------                
        elif expBit.operador == OPERACION_BIT.DESPLAZAMIENTO_DERECHA :
            print("RESULTADO:",exp1>>exp2)  
            return exp1 >> exp2

# ------------------------------------------------EXPRESION RELACIONAL---------------------------------------------------------------------

def resolver_expresion_relacional(expRel, ts) :
    print("ENTRO")
    if isinstance(expRel,ExpresionRelacional):
        exp1 = resolver_expresion_aritmetica(expRel.exp1, ts)
        print("EXP1:",exp1)
        exp2 = resolver_expresion_aritmetica(expRel.exp2, ts)
        print("EXP2:",exp2)
        #---------------------------------OPERACION IGUAL_IGUAL-----------------------------------------------------------------------        
        if expRel.operador == OPERACION_RELACIONAL.IGUAL_IGUAL :
            print("RESULTADO:",exp1==exp2) 
            return exp1 == exp2
        #---------------------------------OPERACION DIFERENTE-----------------------------------------------------------------------                
        if expRel.operador == OPERACION_RELACIONAL.DIFERENTE :
            print("RESULTADO:",exp1!=exp2) 
            return exp1 != exp2
        #---------------------------------OPERACION NO IGUAL-----------------------------------------------------------------------                
        if expRel.operador == OPERACION_RELACIONAL.NO_IGUAL :
            print("RESULTADO:",exp1!=exp2) 
            return exp1 != exp2
        #---------------------------------OPERACION MAYOR IGUAL-----------------------------------------------------------------------                
        if expRel.operador == OPERACION_RELACIONAL.MAYOR_IGUAL :
            print("RESULTADO:",exp1>=exp2) 
            return exp1 >= exp2
        #---------------------------------OPERACION MAYOR-----------------------------------------------------------------------                
        if expRel.operador == OPERACION_RELACIONAL.MAYOR :
            print("RESULTADO:",exp1>exp2) 
            return exp1 > exp2
        #---------------------------------OPERACION MENOR IGUAL-----------------------------------------------------------------------                
        if expRel.operador == OPERACION_RELACIONAL.MENOR_IGUAL :
            print("RESULTADO:",exp1<=exp2) 
            return exp1 <= exp2
        #---------------------------------OPERACION RIGHT SHIFT-----------------------------------------------------------------------                
        if expRel.operador == OPERACION_RELACIONAL.MENOR :
            print("RESULTADO:",exp1<exp2) 
            return exp1 < exp2                                    
# --------------------------------------------------------------------------------------------------------------------- 
#                                             EXPRESIONES
# ---------------------------------------------------------------------------------------------------------------------
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
    print(queries)
    for query in queries :
        if isinstance(query, ShowDatabases) : 
            procesar_showdb(query, ts)
        elif isinstance(query, CreateDatabases) : 
            procesar_createdb(query, ts)
        elif isinstance(query, CreateDatabaseswithParameters) :
            procesar_createwithparametersdb(query, ts)
        elif isinstance(query, AlterDB) :
            procesar_alterdb(query, ts)
        elif isinstance(query, AlterOwner) :
            procesar_alterwithparametersdb(query, ts)
        elif isinstance(query, DropDB) :
            procesar_dropdb(query, ts)
        elif isinstance(query, DropDBIF) :
            procesar_dropdb(query, ts)
        elif isinstance(query, ExpresionAritmetica) : 
            resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionNegativo) : 
            resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionInvocacion) : 
            resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionNumero) : 
            resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionIdentificador) : 
            resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionCadenas) : 
            resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionNOT) : 
            resolver_expresion_logica(query, ts)
        elif isinstance(query, ExpresionBIT) : 
            resolver_expresion_bit(query, ts)
        elif isinstance(query, ExpresionRelacional) : 
            resolver_expresion_relacional(query, ts)
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

    print("--------------------------------Archivo Ejecucion---------------------------------------")
    prueba =g.parse(input)
    ts_global=TS.TablaDeSimbolos()
    h.todo=prueba
    procesar_queries(prueba,ts_global)

    return h.textosalida

# ---------------------------------------------------------------------------------------------------------------------
#                                 EJECUCION DE LOS QUERIES PRINCIPALES
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
#                                 REPORTE GRAMATICAL
# ---------------------------------------------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------------------------------------
#                                 REPORTE GRAMATICAL
# ---------------------------------------------------------------------------------------------------------------------