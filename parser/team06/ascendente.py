import gramaticaAscendente as g
import gramaticaAscendenteTree as gt
import astMethod
#import gramaticaAscendente as gr
import re
import reportes as h
import TablaDeSimbolos as TS
from queries import *
import math as mt
import random as rand

from expresiones import *
import math
import storageManager.jsonMode as store
import reportes as h
from expresiones import * 
import numpy as geek
import datetime
from datetime import date
import tkinter
from tkinter import messagebox
baseActual = ""

# ---------------------------------------------------------------------------------------------------------------------
#                                QUERY SHOW DATABASE
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------- 
#                                             QUERIES
# ----------------------------------------------------------------------------------------------------------------

def procesar_showdb(query,ts):
    h.textosalida+="TYTUS>> "+str(store.showDatabases())+"\n"
    #llamo al metodo de EDD

def procesar_useBD(query,ts):
    h.bd_enuso = query.bd_id
# ---------------------------------------------------------------------------------------------------------------- 

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
                    if procesar_operacion_basica(query.operacion[0],ts)==None:
                        h.textosalida+="TYTUS>> La tabla consultada no existe\n"
                    else:
                        h.textosalida+="TYTUS>>"  + str(procesar_operacion_basica(query.operacion[0],ts)) +"\n"
                elif isinstance(query.operacion[0],Asignacion):
                    print("entra al select de asignaciones")
                    h.textosalida+="TYTUS>>"  + str(procesar_asignacion(query.operacion[0], ts))  +"\n"
            else:
                print("--------SELECT TIPO 2-------------")
                print("en este select se obtienen todos los campos de la lista de tablas")
                print("obtener tablas: ",procesar_select2_obtenerTablas(query.operacion,ts))
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
    print(query.operacion1)
    print(query.operacion2)
    if isinstance(query.operacion2, list) and len(query.operacion2)==1:
        print("viene solo 1 tabla")
        print("+++++++++++TABLA+++++++++++")
        print(query.operacion2[0])
        if isinstance(query.operacion2[0],Asignacion):
            print(procesar_asignacion(query.operacion2[0],ts))
            print("LAS TABLAS SERAN: ",str(procesar_asignacion(query.operacion2[0],ts)))
            print("LAS COLUMNAS SERAN: ",procesar_select2_obtenerColumnas(query.operacion1,ts))
        else:
            if procesar_operacion_basica(query.operacion2[0],ts)==None:
                h.textosalida+="TYTUS>> La tabla consultada no existe\n"
            else:
                print("LAS TABLAS SERAN: ",str(procesar_operacion_basica(query.operacion2[0],ts)))
                print("LAS COLUMNAS SERAN: ",procesar_select2_obtenerColumnas(query.operacion1,ts))
       
    else:
        print("vienen mas tablas*******************************")
        print("LAS TABLAS SERAN: ",procesar_select2_obtenerTablas(query.operacion2,ts))
        print("LAS COLUMNAS SERAN: ",procesar_select2_obtenerColumnas(query.operacion1,ts))
    
    


def procesar_select2_obtenerColumnas(query,ts):
    print("Entra a OBTENER COLUMNAS")
    print(query)
    columnas=[]
    if isinstance(query,list):
        for x in range(len(query)) :
            if isinstance(query[x], ExpresionFuncionBasica): 
                #print("entra a la opcion funcionBasica del else")
                columnas.append(query[x].id.id)
            elif isinstance(query[x],Asignacion):
                print("entra a la opcion de la lista//////////////////////////////////////////")
                columnas.append(procesar_asignacion(query[x],ts))
            elif isinstance(query[x],ExpresionIdentificador):
                #print("entra a la opcion de identificador del lse")
                columnas.append(query[x].id)
            if x==len(query)-1:
                #print(columnas)
                return columnas 
    else:
        if isinstance(query, ExpresionFuncionBasica): 
            print("entra a la opcion funcionBasica del else2//////////////////////////////////////////")
            columnas.append(query.id.id)
        elif isinstance(query,Asignacion):
            print("entra a la opcion solitaria//////////////////////////////////////////")
            print(query)
            print(procesar_asignacion(query,ts))
            columnas.append(procesar_asignacion(query,ts))
            print("aca ya retorno el valor del return ", procesar_asignacion(query,ts) )
            print("aca ya retorno el valor del return ", columnas )
        elif isinstance(query,ExpresionIdentificador):
            print("entra a la opcion de identificador del lse2//////////////////////////////////////////")
            print(query.id)
            columnas.append(query.id)
        print("asfasfasfasdf++++++++++++++++ ",columnas)
        return columnas 

               


def procesar_retorno_lista_valores(query,ts):
    valores=[]
    for x in range(len(query)) :
        if isinstance(query[x], ExpresionFuncionBasica): 
            #print("entra a la opcion funcionBasica del else")
            valores.append(query[x].id.id)
        elif isinstance(query[x],ExpresionIdentificador):
            #print("entra a la opcion de identificador del lse")
            valores.append(query[x].id)
        elif isinstance(query[x],ExpresionNumero):
            #print("entra a la opcion de identificador del lse")
            valores.append(query[x].id)
        elif isinstance(query[x],ExpresionCadenas):
            #print("entra a la opcion de identificador del lse")
            valores.append(query[x].id)
        if x==len(query)-1:
            #print(columnas)
            return valores 

def procesar_select_Tipo3(query,ts):
    print("si llega al metodo de select 3")
    print(query.operacion1)
    print(query.operacion2)
    if isinstance(query.operacion1, list) and len(query.operacion1)==1:
        print("viene solo 1 tabla")
        print("+++++++++++TABLA+++++++++++")
        a=procesar_operacion_basica(query.operacion1[0],ts)
        b=procesar_where(query.operacion2,ts,1,procesar_operacion_basica(query.operacion1[0],ts))
        print("LAS TABLAS SERAN: ",a)
        print("EL OBJETO WHERE: ",b)
    else:
        if isinstance(query.operacion1,Asignacion):
            print("vienen mas tablas*******************************2")
            print(query.operacion1)
            print(query.operacion2)
            print([query.operacion1])
            a=procesar_select2_obtenerTablas([query.operacion1],ts)
            b=procesar_where(query.operacion2,ts,1,procesar_select2_obtenerTablas([query.operacion1],ts))
            print("LAS TABLAS SERAN: ",a)
            print("LAS COLUMNAS SERAN: todas")
            print("EL WHERE SERA: ",b)
        else:
            print("vienen mas tablas*******************************")
            print(query.operacion1)
            print(query.operacion2)
            a=procesar_select2_obtenerTablas(query.operacion1,ts)
            b=procesar_where(query.operacion2,ts,1,procesar_select2_obtenerTablas(query.operacion1,ts))
            print("LAS TABLAS SERAN: ",a)
            print("LAS COLUMNAS SERAN: todas")
            print("EL WHERE SERA: ",b)
            
            


def procesar_select_Tipo4(query,ts):
    print("ya entro al select TIPO 4")
    print(query.operacion1)
    print(query.operacion2)
    print(query.operacion3)
    a=procesar_select2_obtenerTablas(query.operacion2,ts) #tablas
    b=procesar_select2_obtenerColumnas(query.operacion1,ts) #columnas
    c=procesar_where(query.operacion3,ts,b,a)
    print("-------------RESULTADO SELECT 4------------------")
    print("LAS TABLAS SERAN: ",a)
    print("Las columnas seran: ",b)
    print("La sentencia Where sera ",c)
    



def procesar_select_Tipo5(query,ts):
    print("llega al select 5")
    if query.operacion1=='*':
        print("trae asterisco saca todas las columnas")
        a=procesar_select2_obtenerTablas(query.operacion2,ts) #tablas    
        c=procesar_where(query.operacion3,ts,"todo",a)
        d=procesar_extras(query.operacion4,ts,c)
        print("-------------RESULTADO SELECT 5 * ------------------")
        print("LAS TABLAS SERAN: ",a)
        print("las columas seran: Todas")
        print("La sentencia Where sera ",c)
    else:
        print("trae una lista de columnas")
        a=procesar_select2_obtenerTablas(query.operacion2,ts) #tablas
        b=procesar_select2_obtenerColumnas(query.operacion1,ts) #columnas
        c=procesar_where(query.operacion3,ts,b,a)
        d=procesar_extras(query.operacion4,ts,c)
        print("-------------RESULTADO SELECT 5------------------")
        print("LAS TABLAS SERAN: ",a)
        print("EL OBJETO WHERE: ",b)
        print("La sentencia Where sera ",c)
        

def procesar_extras(query,ts,donde):
    print("entro a procesar los extras")
    print(query)
    print(donde)
    for x in range(0,len(query)):
        if isinstance(query[x],ExpresionLimit):
            print("trae una limitante")
        elif isinstance(query[x],ExpresionLimitOffset):
            print("trae una limitante con offset")
        elif isinstance(query[x],ExpresionGroup):
            print("trae para agrupar")
        elif isinstance(query[x],ExpresionHaving):
            print("trae condicion adicional")
        elif isinstance(query[x],ExpresionOrder):
            print("trae expresion de ordenamiento")
    
    return 1



def procesar_where(query,ts,campos,tablas):
    print("entra a procesar el where con lo que traiga")
    print("campos: ", campos)
    print("tablas: ",tablas)
    print(query.condiciones)
    return operar_where(query.condiciones,ts)


def operar_where(query,ts):
    print("entra a operar where")
    if isinstance(query,ExpresionRelacional):
        print("trae relacional")
        print(query.exp1)
        print(query.operador)
        print(query.exp2)
        a=operar_where(query.exp1,ts)
        b=operar_where(query.exp2,ts)
        if query.operador == OPERACION_RELACIONAL.IGUAL_IGUAL:
            print("compara si ",a," == ",b)
            return "compara si ",a," == ",b
        elif query.operador == OPERACION_RELACIONAL.NO_IGUAL:
            print("compara si ",a," != ",b)
            return "compara si ",a," != ",b
        elif query.operador == OPERACION_RELACIONAL.MAYOR_IGUAL:
            print("compara si ",a," >= ",b)
            return "compara si ",a," >= ",b
        elif query.operador == OPERACION_RELACIONAL.MENOR_IGUAL:
            print("compara si ",a," <= ",b)
            return "compara si ",a," <= ",b
        elif query.operador == OPERACION_RELACIONAL.MAYOR:
            print("compara si ",a," > ",b)
            return "compara si ",a," > ",b
        elif query.operador == OPERACION_RELACIONAL.MENOR:
            print("compara si ",a," < ",b)
            return "compara si ",a," < ",b
        elif query.operador == OPERACION_RELACIONAL.DIFERENTE:
            print("compara si ",a," != ",b)
            return "compara si ",a," != ",b
    elif isinstance(query,ExpresionLogica):
        print("trae logica")
        print(query.exp1)
        print(query.operador)
        print(query.exp2)
        operar_where(query.exp2,ts)
        a=operar_where(query.exp1,ts)
        b=operar_where(query.exp2,ts)
        if query.operador == OPERACION_LOGICA.AND:
            print("compara si ",a," AND ",b)
            return "compara si ",a," AND ",b
        elif query.operador == OPERACION_LOGICA.OR:
            print("compara si ",a," OR ",b)
            return "compara si ",a," OR ",b
    elif isinstance(query, ExpresionBetween) :
        print("trae una expresion de  between")
        print(query.valor1) 
        a=operar_where(query.valor1,ts)
        b=operar_where(query.valor2,ts)
        print("compara datos que esten entre ",a,"  y  ",b)
    elif isinstance(query, ExpresionNotBetween) :
        print("trae una expresion de not between")
        a=operar_where(query.valor1,ts)
        b=operar_where(query.valor2,ts)
        print("compara datos que NO esten entre ",a,"  y  ",b)
    elif isinstance(query, ExpresionBetweenSymmetric) :
        print("trae una expresion de between symmetric")
        a=operar_where(query.valor1,ts)
        b=operar_where(query.valor2,ts)
        print("compara datos que esten entre algo symmetric ",a,"  y  ",b)
    elif isinstance(query, ExpresionNotBetweenSymmetric) :
        print("trae una expresion de not between symmetric")
        a=operar_where(query.valor1,ts)
        b=operar_where(query.valor2,ts)
        print("compara datos que NO esten entre algo symmetric ",a,"  y  ",b)
    elif isinstance(query, ExpresionIsDistinct) :
        print("trae una expresion de is distinct")
        a=operar_where(query.valor1,ts)
        b=operar_where(query.valor2,ts)
        print("compara datos sean distintos de ",a,"  y  ",b)
    elif isinstance(query, ExpresionIsNotDistinct) :
        print("trae una expresion de is not distinct")
        a=operar_where(query.valor1,ts)
        b=operar_where(query.valor2,ts)
        print("compara datos NO sean distintos de ",a,"  y  ",b)
    elif isinstance(query, ExpresionNumero) :
        print("retorna el NUMERO: ",query.id)
        return query.id
    elif isinstance(query, ExpresionIdentificador) :
        if ts.obtener(query.id)=="no definida":
            return None
        else:
            print("retorna el ID: ",ts.obtener(query.id).valor)
            return ts.obtener(query.id).valor
    elif isinstance(query,ExpresionCadenas):
        print("retorna la CADENA: ",query.id)
        return query.id
    elif isinstance(query, ExpresionNegativo) :
        print("NEGATIVO")
        print("EXP_NUM:",query.id)
        return query.id * -1

def procesar_createdb(query,ts):
    if ts.verificacionCrearBD(query.variable)==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        store.createDatabase(query.variable)
        ts.printBD()
        return "se creo una nueva bd: "+str(query.variable)
    elif ts.verificacionCrearBD(query.variable)==1:
        print(str(query.variable),"es el nombre de una BD puede ser que quiera crear una tabla o columna")
        return str(query.variable)+"es el nombre de una BD puede ser que quiera crear una tabla o columna"

def procesar_create_if_db(query,ts):
    if ts.verificacionCrearBD(query.variable)==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        store.createDatabase(query.variable)
        ts.printBD()
        return "se creo una nueva bd: "+str(query.variable)
    elif ts.verificacionCrearBD(query.variable)==1:
        print(str(query.variable),"es el nombre de una BD puede ser que quiera crear una tabla o columna")
        return str(query.variable)+"es el nombre de una BD puede ser que quiera crear una tabla o columna"      
    #llamo al metodo de EDD

def procesar_create_replace_db(query,ts):
    if ts.verificacionCrearBD(query.variable)==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        store.createDatabase(query.variable)
        ts.printBD()
        return "se creo una nueva bd: "+str(query.variable)
    elif ts.verificacionCrearBD(query.variable)==1:
        print(str(query.variable),"es el nombre de una BD puede ser que quiera crear una tabla o columna")
        return str(query.variable)+"es el nombre de una BD puede ser que quiera crear una tabla o columna"      
    #llamo al metodo de EDD

def procesar_create_replace_if_db(query,ts):
    if ts.verificacionCrearBD(query.variable)==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        store.createDatabase(query.variable)
        ts.printBD()
        return "se creo una nueva bd: "+str(query.variable)
    elif ts.verificacionCrearBD(query.variable)==1:
        print(str(query.variable),"es el nombre de una BD puede ser que quiera crear una tabla o columna")
        return str(query.variable)+"es el nombre de una BD puede ser que quiera crear una tabla o columna"      
    #llamo al metodo de EDD
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_createwithparametersdb(query,ts):
    for q in query.parametros:   
        if isinstance(q, ExpresionOwner) :
            print("ID:",query.variable)
            print("OWNER:",q.owner)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        elif isinstance(q, ExpresionMode) :
            print("ID:",query.variable)
            print("MODE:",q.mode)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        else:
            print("TIPO INCORRECTO DE QUERY:",query)

def procesar_createwithparameters_if_db(query,ts):
    for q in query.parametros:   
        if isinstance(q, ExpresionOwner) :
            print("IF:",query.iff)
            print("ID:",query.variable)
            print("OWNER:",q.owner)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        elif isinstance(q, ExpresionMode) :
            print("IF:",query.iff)
            print("ID:",query.variable)
            print("MODE:",q.mode)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        else:
            print("TIPO INCORRECTO DE QUERY:",query)

def procesar_createwithparameters_replace_db(query,ts):
    for q in query.parametros:   
        if isinstance(q, ExpresionOwner) :
            print("REPLACE:",query.replacee)
            print("ID:",query.variable)
            print("OWNER:",q.owner)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        elif isinstance(q, ExpresionMode) :
            print("REPLACE:",query.replacee)
            print("ID:",query.variable)
            print("MODE:",q.mode)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        else:
            print("TIPO INCORRECTO DE QUERY:",query)

def procesar_createwithparameters_replace_if_db(query,ts):
    for q in query.parametros:   
        if isinstance(q, ExpresionOwner) :
            print("REPLACE:",query.replacee)
            print("IF:",query.iff)
            print("ID:",query.variable)
            print("OWNER:",q.owner)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        elif isinstance(q, ExpresionMode) :
            print("REPLACE:",query.replacee)
            print("IF:",query.iff)
            print("ID:",query.variable)
            print("MODE:",q.mode)
            print("FINAL:",resolver_expresion_aritmetica(q.final,ts))
        else:
            print("TIPO INCORRECTO DE QUERY:",query)
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_alterdb(query,ts):
    if ts.verificacionAlterBD(query.id_original)==1:
        ts.actualizarAlterBD(query.id_original,query.id_alter)
        #store.alterDatabase(query.id_original, id_alter)
        ts.printBD()
        print("se creo actualizo la bd")
        return "se creo actualizo la bd: "+str(query.id_original) + "por" +str(query.id_alter)
    elif ts.verificacionAlterBD(query.id_original)==0:
        print(str(query.id_original),"No se encontro ninguna base de datos con ese nombre")
        return "No se encontro ninguna base de datos con ese nombre"
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_alterwithparametersdb(query,ts):
    print(query.id_original)
    print(query.owner)
    print(query.id_alter)
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_dropdb(query,ts):
    if ts.destruirBD(query.id)==1:
        #store.dropDatabase(query.id)
        return "ELIMINADA BD:"+str(query.id)
    elif ts.destruirBD(query.id)==0:
        print(str(query.id),"No se encontro ninguna base de datos con ese nombre")
        return "No se encontro ninguna base de datos con ese nombre"

def procesar_dropifdb(query,ts):
    if ts.destruirBD(query.id)==1:
        #store.dropDatabase(query.id)
        ts.printBD()
        return "ELIMINADA BD:"+str(query.id)
    elif ts.destruirBD(query.id)==0:
        print(str(query.id),"No se encontro ninguna base de datos con ese nombre")
        return "No se encontro ninguna base de datos con ese nombre"
# ---------------------------------------------------------------------------------------------------------------- 
#                                             QUERIES
# ----------------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------------- 
#                                             EXPRESIONES
# ----------------------------------------------------------------------------------------------------------------

# --------------------------------------EXPRESION ARITMETICA-----------------------------------------------------------
def resolver_expresion_aritmetica(expNum, ts) :
    try:
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
                        #22012	division_by_zero
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

    #--------------------------------------------------------------------------------------------------------------------------        
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

    #--------------------------------------------------------------------------------------------------------------------------        
        elif isinstance(expNum,ExpresionABS):
            print(expNum)
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            print("dddddddddddddddddddddd")
            print(exp)
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
            print("llega al identificador++++")
            if ts.obtener(expNum.id)=="no definida":
                print("no esta definida")
                return "no se encontro la variable: "+str(expNum.id)
            else:
                print("esta definida")
                return ts.obtener(expNum.id).valor
        elif isinstance(expNum,ExpresionCadenas):
            return expNum.id
        elif isinstance(expNum, ExpresionNegativo) :
            print("EXP_NUM:",expNum.id)
            return expNum.id * -1
        elif isinstance(expNum,ExpresionGREATEST):
            print("entro al greatest +++++++++++++++")
            print(expNum.exp)
            exp= procesar_retorno_lista_valores(expNum.exp, ts)
            print(exp)
            return max(exp)
        elif isinstance(expNum,ExpresionLEAST):
            print("entro al least +++++++++++++++")
            print(expNum.exp)
            exp= procesar_retorno_lista_valores(expNum.exp, ts)
            return min(exp)
        elif isinstance(expNum,ExpresionNOW):
            today=date.today()
            return str(today.strftime("%Y-%m-%d"))
        else:
            print("error de operacion aritmetica")
            #h.errores+=  "<tr><td>"+str(exp1)+"|"+str(exp2)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>error de operacion</td></tr>\n"
    except ValueError as F:
        return ("Se genero un error: "+str(F))


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
    print("entra al print con: ",query.idTable)
    h.textosalida+="TYTUS>> Insertando registro de una tabla\n"
    if query.listidCol == None: 
        for i in query.listRegistros:
            if isinstance(i,ExpresionNOW):
                print("dato: ", str(date.today().strftime("%Y-%m-%d")))
            else:
                print("dato: ",i.id)
            
    elif query.listidCol != None:
        tamlistid = len(query.listidCol)
        tamlistreg = len(query.listRegistros)
        contcol = 0 
        while contcol < tamlistid:
            col = ts.obtenerColumna(query.idTable,'BD1',)
            print("nombre columna: ",col.nombre)
            contcol=contcol+1


def procesar_updateinBD(query,ts):
    print("entro a update")
    print("entro al print con: ",query.idTable,query.asignaciones,query.listcond)
    h.textosalida+="TYTUS>> Actualizando datos en la tabla\n"
    print("Valores que se asignaran")
    for i in query.asignaciones:
        print("id: ",i.id," valor: ",i.expNumerica.id)

    print("Condicion de where")
    for x in query.listcond:
        print("id: ",x.id," valor: ",x.expNumerica.id)


def procesar_select2_obtenerTablas(query,ts):
    print("Entra al else del select")
    #print(query)
    tablas=[]
    for x in range(len(query)) :
        if isinstance(query[x], ExpresionFuncionBasica): 
            #print("entra a la opcion funcionBasica del else")
            tablas.append(query[x].id.id)
        elif isinstance(query[x],Asignacion):
            print("entra a la opcion select del else")
            print(procesar_asignacion(query[x],ts))
            tablas.append(procesar_asignacion(query[x].campo,ts))
            tablas.append(procesar_asignacion(query[x].alias,ts))
        elif isinstance(query[x],ExpresionIdentificador):
            #print("entra a la opcion de identificador del lse")
            tablas.append(query[x].id)
        if x==len(query)-1:
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
    elif isinstance(query.id,ExpresionGREATEST): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionLEAST): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionNOW): return resolver_expresion_aritmetica(query.id,ts)

    elif isinstance(query.id,ExpresionIdentificador): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCadenas): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionAritmetica): return resolver_expresion_aritmetica(query.id,ts)
    
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
    elif isinstance(query.campo,ExpresionAritmetica):
        return guardar_asignacion(resolver_expresion_aritmetica(query.campo,ts),query.alias.id,ts)
    else :
        print("-------------estos datos se asignan con operacion--------------")
        print(query.campo.exp)
        print(query.alias.id)
        return guardar_asignacion(resolver_expresion_aritmetica(query.campo,ts),query.alias.id,ts)
        


    
    


 # ---------------------------------------------------------------------------------------------------------------------
#                               PARA ALMACENAR LAS ASIGNACIONES
# ---------------------------------------------------------------------------------------------------------------------
   
    
def guardar_asignacion(valor, variable,ts):  
    print("entro a guardar la variable")
    print(variable)
    print(valor)
    if ts.obtener2(variable)==0:
        print("no se ha creado la variable")
        print(variable)
        print(valor)
        if (isinstance(valor, str) and valor.find("error")>0):
            print("entra al if con error")
            return valor
        else:
            print("se agregara la variable")
            simbolo = TS.Simbolo(None,variable,None,None,None,None,None,None,None,None,None,None,None,None,None,None, valor,None)      # inicializamos con 0 como valor por defecto
            ts.agregar(simbolo)
            print("se creo una nueva variable")
            print(variable)
            return variable
    else:
        if isinstance(valor, str) and valor.find("error")>0:
            return valor
        else:
            simbolo = TS.Simbolo(None,variable,None,None,None,None,None,None,None,None,None,None,None,None,None,None, valor,None)
            ts.actualizar(simbolo)
            print("la variable ya existia, se actualizo")
            print(variable)
            return variable


# ---------------------------------------------------------------------------------------------------------------------
#                                Expresiones aritmeticas
# ---------------------------------------------------------------------------------------------------------------------


def procesar_deleteinBD(query,ts):
    print("entra a delete from")
    print("entra al print con: ",query.idTable)
    h.textosalida+="TYTUS>> Eliminando registro de una tabla\n"
    for i in query.condColumna:
        print("id: ",i.id," valor: ",i.expNumerica.id)
    #llamada de funcion

def procesar_createTale(query,ts):
    print("entra a Create table")
    print("entra al print con: ",query.idTable)
    idtab = query.idTable
    h.textosalida+="TYTUS>>Creando tabla\n"
    cantcol = 0

    if ts.validarTabla(query.idTable,'BD1') == 0:
        simbolo = TS.Simbolo(None,query.idTable,None,None,'BD1',None,None,None,None,None,None,None,None,None,None,None,None,None)
        ts.agregarnuevTablaBD(simbolo)
        print("--> Se creo nueva tabla con id: "+query.idTable)
        #return "Se creo Tabla con id: "+str(query.idTable)
    else:
        print("--> Ya existe una tabla con el mismo nombre en BD")
        return "Ya existe una Tabla con id: "+str(query.idTable)

    for i in query.listColumn:
        print("---------------------------")
    # -------------------------------------------------------------------------------------------------------------- 
        if i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.COLUMNASINRESTRICCION:
            print("Crea Columna: ",i.objAtributo.idColumna)
            print("Tipo de dato: ",i.objAtributo.TipoColumna.id)
            idcol=i.objAtributo.idColumna
            idtipo=i.objAtributo.TipoColumna.id
            cantcol=cantcol+1
           
            if idtipo=="CHARACTER" or idtipo=="VARING" or idtipo=="VARCHAR" or idtipo=="CHAR":
                idtamcad = i.objAtributo.TipoColumna.longitud 
                if ts.verificarcolumnaBD(idcol,'BD1',idtab) == 0:
                    simbolo = TS.Simbolo(cantcol,idcol,idtipo,idtamcad,'BD1',idtab,1,0,0,None,None,0,None,0,None,None,None,None)
                    ts.agregarnuevaColumna(simbolo)
                    print("Se creo nueva columna :",idcol," a tabla: ",idtab)
                else:
                    print("columna: ",idcol," ya existe en tabla: ",idtab)
                   
            else:
                idtamcad = i.objAtributo.TipoColumna.longitud
                if ts.verificarcolumnaBD(idcol,'BD1',idtab) == 0:
                    simbolo = TS.Simbolo(cantcol,idcol,idtipo,None,'BD1',idtab,1,0,0,None,None,0,None,0,None,None,None,None)
                    ts.agregarnuevaColumna(simbolo)
                    print("Se creo nueva columna :",idcol," a tabla: ",idtab)
                else:
                    print("columna: ",idcol," ya existe en tabla: ",idtab)
            ts.printcontsimbolos()
    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.COLUMNACONRESTRICCION:
            print("Crea Columna: ",i.objAtributo.idColumna)
            print("Tipo de dato: ",i.objAtributo.TipoColumna.id)
            idcol=i.objAtributo.idColumna
            idtipo = i.objAtributo.TipoColumna.id
            
            #varibales temporales
            pk = 0
            df = None
            obl = 1
            idconsuniq = None
            unq = 0
            idconscheck = None
            chk = 0
            condchk = None

            cantcol=cantcol+1
            for res in i.objAtributo.RestriccionesCol:
                if res.typeR == OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY:
                    print("Restriccion: PRIMARY KEY")
                    pk = 1

                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.DEFAULT:
                    print("REstriccion: DEFAULT ")
                    print("Dato Default: ",res.objrestriccion.valor)
                    df = res.objrestriccion.valor

                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.NULL:
                    print("Restriccion: NULL")
                    obl = 1

                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.NOT_NULL:
                    print("Restriccion: NOT NULL")
                    obl = 0

                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.UNIQUE_CONSTAINT:
                    print("Restriccion: CONSTRAINT UNIQUE")
                    print("Id contraint: ",res.objrestriccion.idUnique)
                    unq = 1
                    idconsuniq = res.objrestriccion.idUnique

                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.UNIQUE_COLUMNA:
                    print("Restriccion: UNIQUE")
                    unq = 1

                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.CHECK_SIMPLE:
                    print("Restriccion: CHECK")
                    print("Valor de check: ",res.objrestriccion.condCheck.exp1.id,res.objrestriccion.condCheck.operador,res.objrestriccion.condCheck.exp2.id)
                    chk = 1

                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.CHECK_CONSTRAINT:
                    print("Restriccion: CONSTRAINT CHECK")
                    print("Id contraint: ",res.objrestriccion.idConstraint)
                    print("Valor de check: ",res.objrestriccion.condCheck.exp1.id,res.objrestriccion.condCheck.operador,res.objrestriccion.condCheck.exp2.id)
                    chk = 1
                    idconscheck = res.objrestriccion.idConstraint
                    condchk = res.objrestriccion.condCheck

                else:
                    print("No se encontro ninguna restriccion")
        

            if idtipo=="CHARACTER" or idtipo=="VARING" or idtipo=="VARCHAR" or idtipo=="CHAR":
                idtamcad = i.objAtributo.TipoColumna.longitud 
                if ts.verificarcolumnaBD(idcol,'BD1',idtab) == 0:
                    simbolo = TS.Simbolo(cantcol,idcol,idtipo,idtamcad,'BD1',idtab,obl,pk,0,None,None,unq,idconsuniq,chk,condchk,idconscheck,None,df)
                    ts.agregarnuevaColumna(simbolo)
                    print("Se creo nueva columna :",idcol," a tabla: ",idtab)
                else:
                    print("columna: ",idcol," ya existe en tabla: ",idtab)
                   
            else:
                idtamcad = i.objAtributo.TipoColumna.longitud
                if ts.verificarcolumnaBD(idcol,'BD1',idtab) == 0:
                    simbolo = TS.Simbolo(cantcol,idcol,idtipo,None,'BD1',idtab,obl,pk,0,None,None,unq,idconsuniq,chk,condchk,idconscheck,None,df)
                    ts.agregarnuevaColumna(simbolo)
                    print("Se creo nueva columna :",idcol," a tabla: ",idtab)
                else:
                    print("columna: ",idcol," ya existe en tabla: ",idtab)
            ts.printcontsimbolos()

    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.UNIQUE_ATRIBUTO:
            print("Declaracion de varias columnas UNIQUE")
            print("Lista de columnas: ")
            
            for lc in i.objAtributo.listColumn:
                print("id: ",lc.id)
                if ts.verificarcolumnaBD(idcol,'BD1',idtab) == 0:
                    print("La columna especificada no existe, no se creo restriccion unique")
                    return
                else:
                    ts.actualizauniqueColumna(lc.id,'BD1',idtab)
            ts.printcontsimbolos()

    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.CHECK_CONSTRAINT:
            print("Declaracion de constraint check")
            print("Id constraint: ", i.objAtributo.idConstraint)
            print("Condicion check: ",i.objAtributo.condCheck.exp1.id, i.objAtributo.condCheck.operador, i.objAtributo.condCheck.exp2.id)
            if ts.verificarcolumnaBD(i.objAtributo.condCheck.exp1.id,'BD1',idtab) == 1:
                ts.actualizarcheckColumna(i.objAtributo.condCheck.exp1.id,'BD1',idtab,i.objAtributo.idConstraint,i.objAtributo.condCheck)
            else:
                print("La columna especificada no existe")
            ts.printcontsimbolos()

    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.CHECK_SIMPLE:
            print("Delaracion de check")
            print("Condicion check: ",i.objAtributo.condCheck.exp1.id, i.objAtributo.condCheck.operador, i.objAtributo.condCheck.exp2.id)
            if ts.verificarcolumnaBD(i.objAtributo.condCheck.exp1.id,'BD1',idtab) == 1:
                ts.actualizarcheckColumna(i.objAtributo.condCheck.exp1.id,'BD1',idtab,None,i.objAtributo.condCheck)
            else:
                print("La columna especificada no existe")
            ts.printcontsimbolos()
    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY:
            print("Declaracion de una o varias PRIMARY KEY")
            print("Lista de columnas: ")
            for lc in i.objAtributo.listColumn:
                print("id: ",lc.id)
                if ts.verificarcolumnaBD(lc.id,'BD1',idtab) == 1:
                    ts.actualizapkcolumna(lc.id,'BD1',idtab)
                    print("se actualizo llave primaria en: ",lc.id)
                else:
                    print("La columna especificada no existe, no se creo llave primaria")
            ts.printcontsimbolos()

    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.FOREIGN_KEY:
            print("Declaracion de FOREIGN KEY")
            print("Lista de ID FOREING KEY")
            contidfor = len(i.objAtributo.idForanea)
            contidref = len(i.objAtributo.idLlaveF)
            conttemp = 0
            while conttemp < contidfor:
                if ts.verificarcolumnaBD(i.objAtributo.idLlaveF[conttemp].id,'BD1',i.objAtributo.idTable) == 1:
                    if ts.verificarcolumnaBD(i.objAtributo.idForanea[conttemp].id,'BD1',idtab)==1:
                        ts.actualizafkcolumna(i.objAtributo.idForanea[conttemp].id,'BD1',idtab,i.objAtributo.idLlaveF[conttemp],i.objAtributo.idTable)
                    else:
                        print("la columna especificada no existe para crear llave foranea")
                else:
                    print("la columna referenciada en la tabla no existe")
                conttemp = conttemp+1
            ts.printcontsimbolos()
    # -------------------------------------------------------------------------------------------------------------- 
        else:
            print("No se encontraron columnas a crear")

    #print("Cantidad de columnas ------> ",cantcol)
    #Llamada a metodo crear Tabla
    #store.createTable("bd1",query.idTable,cantcol)



def procesar_inheritsBD(query, ts):
    print("entra a Inherits")
    print("Crea tabla con id: ",query.idTable)
    print("Hereda atributos de tabla: ",query.idtableHereda)
    h.textosalida+="TYTUS>>Creando tabla Inherits\n"

    for i in query.listColumn:
        print("---------------------------")
    #-------------------------------------------------------------------------------------------------------------- 
        if i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.COLUMNASINRESTRICCION:
            print("Crea Columna: ",i.objAtributo.idColumna)
            print("Tipo de dato: ",i.objAtributo.TipoColumna.id)
    


def drop_table(query,ts):
    print("voy a imprimir los valores del drop :v")
    print("aqui viene el id de la tabla a dropear:",query.id)
    h.textosalida+="TYTUS>> Eliminaré la tabla"+query.id+"\n"

def alter_table(query,ts):
    print("voy a imprimir los valores del alter :v")
    print("aqui viene el id de la tabla a cambiar:",query.id)
    h.textosalida+="TYTUS>> Alteraré la tabla"+query.id+"\n"
    temp = query.querys.tipo #TIPO DE OBJETO
    if(temp.upper()=="ADD"):
        contenido = query.querys.contenido #AQUI ESTA EL CONTENIDO DEL ADD - contAdd
        if contenido.tipo.upper()=="COLUMN":
            print("SE AGREGARA UNA COLUMNA")
            #METODO PARA ALTERAR LA COLUMNA
            #alterAddColumn(baseActual,contenido.id1,anyxd)
        elif contenido.tipo.upper()=="CHECK":
            print("SE AGREGARA UN CHECK")
        elif contenido.tipo.upper()=="FOREIGN":
            print("SE AGREGARA UNA LLAVE FORANEA")
        elif contenido.tipo.upper()=="PRIMARY":
            print("SE AGREGARA UNA LLAVE PRIMARIA")
        elif contenido.tipo.upper()=="CONSTRAINT":
            print("SE VIENE UN CONSTRAINT")
            if contenido.tipo2.upper()=="FOREIGN":
                print("Y DENTRO VIENE UNA LLAVE FORANEA")
            elif contenido.tipo2.upper()=="PRIMARY":
                print("Y DENTRO VIENE UNA LLAVE PRIMARIA")
            elif contenido.tipo2.upper()=="UNIQUE":
                print("Y DENTRO VIENE UN UNIQUE")
        #print("VIENE UN ADD, POR TANTO SE AGREGA ALGO A LA TABLA")
        #print("SE AGREGARÁ UNA: ", query.querys.contenido.tipo)
        #print("DE NOMBRE: ",query.querys.contenido.id1)
        #print("DE TIPO: ", query.querys.contenido.tipo2)
    elif(temp.upper()=="DROP"):
        print("VIENE UN DROP, ALGO DE LA TABLA VA A EXPLOTAR, F")
        contenido = query.querys.contenido #AQUI ESTA EL CONTENIDO DEL DROP - contDrop
        if contenido.tipo.upper() == "COLUMN":
            print("DROPEARÉ UNA COLUMNA: ",contenido.id)
        else:
            print("DROPEARÉ UNA CONSTRAINT: ",contenido.id)
        #print("LO QUE EXPLOTARA SERA: ", query.querys.contenido.tipo)
        #print("CON EL ID: ", query.querys.contenido.id)
    elif(temp.upper()=="ALTER"):
        print("VIENE UN ALTER DENTRO DE OTRO ALTER")
        #print("DE TIPO: ", query.querys.contenido.tipo)
        #print("CON EL ID: ", query.querys.contenido.id)
        #print("PARA ASIGNAR: ", query.querys.contenido.tipoAsignar)


        

    

# ---------------------------------------------------------------------------------------------------------------------
#                                 EJECUCION DE LOS QUERIES PRINCIPALES
# ---------------------------------------------------------------------------------------------------------------------
def procesar_queries(queries, ts) :
    ## lista de instrucciones recolectadas
    print(queries)
    for query in queries :
        if isinstance(query, ShowDatabases) : procesar_showdb(query, ts)
        elif isinstance(query, Select) : procesar_select(query, ts)
        elif isinstance(query, Select2) : procesar_select_Tipo2(query, ts)
        elif isinstance(query, Select3) : procesar_select_Tipo3(query, ts)
        elif isinstance(query, Select4) : procesar_select_Tipo4(query, ts)
        elif isinstance(query, Select5) : procesar_select_Tipo5(query, ts)
        elif isinstance(query, CreateDatabases) : procesar_createdb(query, ts)
        elif isinstance(query, Create_IF_Databases) : procesar_create_if_db(query, ts)
        elif isinstance(query, Create_Replace_Databases) : procesar_create_replace_db(query, ts)
        elif isinstance(query, Create_Replace_IF_Databases) : procesar_create_replace_if_db(query, ts)
        elif isinstance(query, CreateDatabaseswithParameters) : procesar_createwithparametersdb(query, ts)
        elif isinstance(query, Create_Databases_IFwithParameters) : procesar_createwithparameters_if_db(query, ts)
        elif isinstance(query, Create_Replace_DatabaseswithParameters) : procesar_createwithparameters_replace_db(query, ts)
        elif isinstance(query, Create_Replace_IF_Databases) : procesar_createwithparameters_replace_if_db(query, ts)
        elif isinstance(query, AlterDB) : procesar_alterdb(query, ts)
        elif isinstance(query, AlterOwner) : procesar_alterwithparametersdb(query, ts)
        elif isinstance(query, DropDB) : procesar_dropdb(query, ts)
        elif isinstance(query, DropDBIF) : procesar_dropifdb(query, ts)
        elif isinstance(query, ExpresionAritmetica) : resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionNegativo) : resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionInvocacion) : resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionNumero) : resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionIdentificador) : resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionCadenas) : resolver_expresion_aritmetica(query, ts)
        elif isinstance(query, ExpresionNOT) : resolver_expresion_logica(query, ts)
        elif isinstance(query, ExpresionBIT) : resolver_expresion_bit(query, ts)
        elif isinstance(query, ExpresionRelacional) : resolver_expresion_relacional(query, ts)
        elif isinstance(query, InsertinDataBases) : procesar_insertBD(query,ts)
        elif isinstance(query, UpdateinDataBase) : procesar_updateinBD(query,ts)
        elif isinstance(query, DeleteinDataBases) : procesar_deleteinBD(query, ts)
        elif isinstance(query, CreateTable) : procesar_createTale(query,ts)
        elif isinstance(query, InheritsBD) : procesar_inheritsBD(query,ts)
        elif isinstance(query,DropTable): drop_table(query,ts)
        elif isinstance(query,AlterTable): alter_table(query,ts)
        elif isinstance(query,UseDatabases): procesar_useBD(query,ts)
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
    arbol =gt.parse(input)
    ts_global=TS.TablaDeSimbolos()
    h.todo=prueba
    procesar_queries(prueba,ts_global)
    h.textosalida+="--------------------FIN EJECUCION ASCENDENTE--------------------\n"
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
    print("++++++++++++++++")
    print(ruta)
    ts_global=TS.TablaDeSimbolos()
    for simbolo in  ts_global.simbolos:
        val+="<tr><td>"+str(ts_global.simbolos[simbolo].id)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].nombre)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].tipo)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].tamanoCadena)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].BD)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].tabla)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].obligatorio)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].pk)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].FK)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].referenciaTablaFK)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].referenciaCampoFK)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].unique)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].idUnique)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].check)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].condicionCheck)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].idCheck)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].valor)+"</td>"
        val+="<td>"+str(ts_global.simbolos[simbolo].default)+"</td>"    
        val+="</tr>\n"
    #construyo el archivo html
    print("manda los datos")
    print("///////////////////////////////////////////////////////////////////////////////////")
    ts_global.printcontsimbolos()
    h.reporteSimbolos(ruta,val)

def generarASTReport():
    if gt.gramaticaAscendenteTree.tree.root == None:
        box_tilte ="AST Error"
        box_msg = "No hay entrada que analizar o hay un error en la misma"
        messagebox.showerror(box_tilte,box_msg)
    else:
        astMethod.astFile("ast", gt.gramaticaAscendenteTree.tree.root)
# ---------------------------------------------------------------------------------------------------------------------
#                                 REPORTE GRAMATICAL
# ---------------------------------------------------------------------------------------------------------------------


def validaTipoDato(tipo, valor, tam):
    if tipo == 'INTEGER':
        if -2147483648 < valor and valor > 2147483648:
            return True
        else:
            print("El valor ingresado supera la longitud permitida para INTEGER")
            return False
    elif tipo == 'SMALLINT':
        if -2147483648 < valor and valor > 2147483648:
            return True
        else:
            print("El valor ingresado supera la lingitud permitida para SMALLINT")
            return False
    elif tipo == 'BIGINT':
        if -9223372036854775808 < valor and valor > 9223372036854775807:
            return True
        else:
            print("El valor ingresado supera la longitud permitida para BIGING")
            return False
    elif tipo == "DECIMAL":
        temp = str(valor)
        num = temp.split(".")
        entero = len(num[0])
        decimal = len(num[1])
        if(131072 < entero and 16383 < decimal):
            return True
        else:
            print("El valor ingresado no cumple como Decimal")
            return False
    elif tipo == "NUMERIC":
        temp = str(valor)
        num = temp.split(".")
        entero = len(num[0])
        decimal = len(num[1])
        if(131072 < entero and 16383 < decimal):
            return True
        else:
            print("El valor ingresado no cumple como NUMERIC")
            return False
    elif tipo == "REAL":
        temp = str(valor)
        num = temp.split(".")
        decimal = len(num[1])
        if(6 <= decimal):
            return True
        else:
            print("El valor ingresado tiene mas de 6 decimales")
            return False
    elif tipo == "DOUBLE":
        temp = str(valor)
        num = temp.split(".")
        decimal = len(num[1])
        if(15 <= decimal):
            return True
        else:
            print("El valor ingresado tiene mas de 15 decimales")
            return False
    elif tipo == "MONEY":
        if -92233720368547758.08 < valor and valor > +92233720368547758.07:
            return True
        else:
            print("El valor ingresado supera la longitud permitida para BIGING")
            return False
    elif tipo == "VARING":
        if type(valor) is str :
            tamcad = len(valor)
            if tamcad > 0 and tamcad <= tam:
                return True
            else:
                print("La cadena ingresada supera el limite del CHARETECTER VARING definido")
                return False
        else:
            print("El valor ingresado no es una cadena")
            return False
    elif tipo == "VARCHAR":
        if type(valor) is str :
            tamcad = len(valor)
            if tamcad > 0 and tamcad <= tam:
                return True
            else:
                print("La cadena ingresada supera el limite del VARCHAR definido")
                return False
        else:
            print("El valor ingresado no es una cadena")
    elif tipo == "CHARACTER":
        if type(valor) is str :
            tamcad = len(valor)
            if tamcad > 0 and tamcad <= tam:
                return True
            else:
                print("La cadena ingresada supera el limite del CHARETECTER definido")
                return False
        else:
            print("El valor ingresado no es una cadena")
    elif tipo == "CHAR":
        if type(valor) is str :
            tamcad = len(valor)
            if tamcad > 0 and tamcad <= tam:
                return True
            else:
                print("La cadena ingresada supera el limite del CHAR definido")
                return False
        else:
            print("El valor ingresado no es una cadena")
    elif tipo == "TIMESTAMP":
        date_format = '%Y-%m-%d %H:%M:%S'
        try:
            if datetime.datetime.strptime(valor,date_format):
                return True
        except:
            print("La fecha y hora ingresada es invalida")
            return False
    elif tipo == "TIME":
        date_format = '%H:%M:%S'
        try:
            if datetime.datetime.strptime(valor,date_format):
                return True
        except:
            print("La hora ingresada es invalida")
            return False
    elif tipo == "DATE":
        date_format = '%Y-%m-%d'
        try:
            if datetime.datetime.strptime(valor,date_format):
                return True
        except:
            print("La fecha ingresada es invalida")
            return False