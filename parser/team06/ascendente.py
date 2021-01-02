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
import hashlib as ha

#jossie
from storageManager import jsonMode as j
import pandas as pd
import time

from decimal import Decimal, getcontext
getcontext().prec = 8


# ---------------------------------------------------------------------------------------------------------------------
#                                QUERY SHOW DATABASE
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------- 
#                                             QUERIES
# ----------------------------------------------------------------------------------------------------------------

def procesar_showdb(query,ts):
    verificacion =  ts.verificacionShowBD()
    if verificacion == 0:
        h.textosalida+="TYTUS>> " + " No hay BD que mostrar "+"\n"
    else:
        h.textosalida+="TYTUS>> "+str(verificacion)+"\n"
    #llamo al metodo de EDD

def procesar_useBD(query,ts):
    verificacion =  ts.verificacionUseBD(query.bd_id)
    if verificacion==1:
        h.bd_enuso = query.bd_id
        h.textosalida+="TYTUS>> " + " Se esta utilizando la BD "+str(h.bd_enuso)+"\n"
        return "se usa la bd: "+str(h.bd_enuso)
    elif verificacion==0:
        h.textosalida+="TYTUS>> " + "BD "+ str(query.bd_id) + " no existente, no se puede usar "+"\n"
        return "Esta BD no existe "+str(query.bd_id)+"\n"
        
# ---------------------------------------------------------------------------------------------------------------- 

# ---------------------------------------------------------------------------------------------------------------------
#                                QUERY SELECT
# ---------------------------------------------------------------------------------------------------------------------
def procesar_select(query,ts):
    print("entra select")
    if query.tipo==1:
        print("entra al select de TIPO 1")
        print(query.operacion)
        if query.bandera==2:
            if isinstance(query.operacion,list):
                if len(query.operacion)==1:
                    print("entra al if de tamaño 1")
                    if isinstance(query.operacion[0], ExpresionFuncionBasica): 
                        if procesar_operacion_basica(query.operacion[0],ts)==None:
                            h.textosalida+="TYTUS>> La tabla consultada no existe\n"
                        else:
                            a=str(procesar_operacion_basica(query.operacion[0],ts))
                            print("---------------------------------------------RESULTADO SELECT 1A-------------------------------------------------")
                            print(a)
                            b=a.split(" ")
                            print(b[-1])
                            print(h.bd_enuso)
                            print("saca el valor")
                            c=ts.obtenerSelect1A(b[-1],h.bd_enuso)
                            print("resultado+++++++++++++++++++++: ")
                            
                            print(str(c))
                            h.textosalida+="TYTUS>>El resultado de su consulta es \n"
                            h.textosalida+=str(c)+"\n"
                    elif isinstance(query.operacion[0],Asignacion):
                        print("entra al select de asignaciones")
                        a=str(procesar_asignacion(query.operacion[0], ts))
                        print("---------------------------------------------RESULTADO SELECT 1B-------------------------------------------------")
                        print(a)
                        h.textosalida+="TYTUS>>"  + a  +"\n"
                else:
                    print("--------SELECT TIPO 2-------------")
                    print("en este select se obtienen todos los campos de la lista de tablas")
                    a=procesar_select2_obtenerTablas(query.operacion,ts)
                    print("---------------------------------------------RESULTADO SELECT 2D--------------------------------------------------")
                    print("LAS TABLAS SERAN: ",a)
                    print("LAS COLUMNAS SERAN: todas")
                    
                    h.textosalida+="TYTUS>>Se ha ejecutado su consulta\n"
            else:
                print("no es array")
                print("entra al if de tamaño 1")
                if isinstance(query.operacion, ExpresionFuncionBasica): 
                    print(procesar_operacion_basica(query.operacion, ts))
                    h.textosalida+="TYTUS>>"  + str(procesar_operacion_basica(query.operacion,ts)) +"\n"
                elif isinstance(query.operacion,Asignacion):
                    print("entra al select de asignaciones")
                    h.textosalida+="TYTUS>>"  + str(procesar_asignacion(query.operacion, ts))  +"\n"
        elif query.bandera==1:
            print("--------SELECT TIPO 2-------------")
            print("en este select se obtienen todos los campos de la lista de columnas")
            a=procesar_select2_obtenerColumnas(query.operacion,ts)
            print("---------------------------------------------RESULTADO SELECT 2E--------------------------------------------------")
            print("LAS COLUMNAS SERAN: ",a)
            print("NO TIENE TABLAS")
            
            try:
                b=ts.obtenerSelect2E(a)
                if b==0:
                    h.textosalida+="TYTUS>>Se ha ejecutado su consulta:\n"+str(a)+"\n"
                else:
                    h.textosalida+="TYTUS>>Se ha ejecutado su consulta:\n"+str(b)+"\n"
            except:
                h.textosalida+="TYTUS>>Se ha ejecutado su consulta:\n"+str(a)+"\n"

        
    
def procesar_select_Tipo2(query,ts):
    print("************************ENTRO AL 2DO SELECT*********************")
    print(query.operacion1)
    print(query.operacion2)
    if isinstance(query.operacion2, list) and len(query.operacion2)==1:
        print("viene solo 1 tabla")
        print("+++++++++++TABLA+++++++++++")
        print(query.operacion2[0])
        if isinstance(query.operacion2[0],Asignacion):
            a=str(procesar_asignacion(query.operacion2[0],ts))
            b=procesar_select2_obtenerColumnas(query.operacion1,ts)
            print("---------------------------------------------RESULTADO SELECT 2A--------------------------------------------------")
            print("LAS TABLAS SERAN: ",a)
            print("LAS COLUMNAS SERAN: ",b)
            h.textosalida+="TYTUS>>Se ha ejecutado su consulta\n"
        else:
            if procesar_operacion_basica(query.operacion2[0],ts)==None:
                h.textosalida+="TYTUS>> La tabla consultada no existe\n"
            else:
                a=str(procesar_operacion_basica(query.operacion2[0],ts))
                b=procesar_select2_obtenerColumnas(query.operacion1,ts)
                print("---------------------------------------------RESULTADO SELECT 2B--------------------------------------------------")
                print("LAS TABLAS SERAN: ",a)
                print("LAS COLUMNAS SERAN: ",b)
                c=a.split(" ")
                print(c[-1])
                print(h.bd_enuso)
                print("saca el valor")
                d=ts.obtenerSelect2B(c[-1],h.bd_enuso,b)
                print("resultado+++++++++++++++++++++: ")
                print(d)
                h.textosalida+="TYTUS>>El resultado de su consulta es \n"
                h.textosalida+=str(d)+"\n"

                
       
    else:
        print("vienen mas tablas*******************************")
        a=procesar_select2_obtenerTablas(query.operacion2,ts)
        b=procesar_select2_obtenerColumnas(query.operacion1,ts)
        print(query.operacion1)
        print(query.operacion2)
        print("---------------------------------------------RESULTADO SELECT 2C--------------------------------------------------")
        print("LAS TABLAS SERAN: ",a)
        print("LAS COLUMNAS SERAN: ",b)
        h.textosalida+="TYTUS>>Se ha ejecutado su consulta\n"
    
    


def procesar_select2_obtenerColumnas(query,ts):
    print("Entra a OBTENER COLUMNAS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(query)
    columnas=[]
    if isinstance(query,list):
        for x in range(len(query)) :
            if x==0:
                print("++++++++++++++++++++++++++++++++entraA: ",x,"+++++++++++++++++++++++++++++++")
                print(query[x])
                if isinstance(query[0],Asignacion):
                    print("trae una asignacionA")
                    columnas.append(procesar_asignacion(query[x],ts))
                if isinstance(query[0],ExpresionFuncionBasica):
                    print("trae una funcion basicaA")
                    print(query[0].id)

                    if isinstance(query[0].id,ExpresionLlamame):
                        print("trae una expresion llamameA")
                        columnas.append(query[x].id.id+"-"+(query[x].id.id1))
                    if isinstance(query[0].id,ExpresionIdentificador):
                        print("trae una expresion identificadorA")
                        columnas.append(query[x].id.id)
                        
                    else:
                        print("trae otra cosaA")
                        print(query[0].id)
                        a=procesar_operacion_basica(query[0],ts)
                        print("subio el valor de: ",a)
                        columnas.append(a)
                        #return a
                if isinstance(query[0],ExpresionLlamame):
                    print("trae una expresion llamameB")
                    columnas.append(query[0].id+"-"+(query[x].id1))
               
            else:
                print("++++++++++++++++++++++++++++++++entraB: ",x,"+++++++++++++++++++++++++++++++")
                print(query[x])
                if isinstance(query[x], ExpresionFuncionBasica): 
                    #print("entra a la opcion funcionBasica del else")
                    columnas.append(query[x].id)
                elif isinstance(query[x],Asignacion):
                    print("entra a la opcion de la lista//////////////////////////////////////////")
                    columnas.append(procesar_asignacion(query[x],ts))
                elif isinstance(query[x],ExpresionIdentificador):
                    #print("entra a la opcion de identificador del lse")
                    columnas.append(query[x].id)
                elif isinstance(query[x],ExpresionLlamame):
                    #print("entra a la opcion de identificador del lse")
                    columnas.append(query[x].id+"-"+(query[x].id1))
                else: 
                    print("trae otra cosaB")
                    print(query[x])
                    a=resolver_expresion_aritmetica(query[x],ts)
                    print("subio el valor deB: ",a)
                    columnas.append(a)

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
        
        print("---------------------------------------------RESULTADO SELECT 3A --------------------------------------------------")
        print("LAS TABLAS SERAN: ",a)
        
        c=a.split(" ")
        print(c[-1])
        print(h.bd_enuso)
        print("saca el valor+++++")
        d=ts.obtenerSelect1A(c[-1],h.bd_enuso)
        print("resultado+++++++++++++++++++++3A: ")
        print(d)
        b=procesar_where(query.operacion2,ts,d,procesar_operacion_basica(query.operacion1[0],ts))
        print("EL OBJETO WHERE: \n",b)
        h.textosalida+="TYTUS>>Se ha ejecutado su consulta\n"+str(b)+"\n"
        
    else:
        if isinstance(query.operacion1,Asignacion):
            print("vienen mas tablas*******************************2")
            print(query.operacion1)
            print(query.operacion2)
            print([query.operacion1])
            a=procesar_select2_obtenerTablas([query.operacion1],ts)
            
            print("---------------------------------------------RESULTADO SELECT 3B--------------------------------------------------")
            print("LAS TABLAS SERAN: ",a)
            print("LAS COLUMNAS SERAN: todas")
            b=procesar_where(query.operacion2,ts,1,procesar_select2_obtenerTablas([query.operacion1],ts))
            print("EL WHERE SERA: ",b)
            h.textosalida+="TYTUS>>Se ha ejecutado su consulta\n"
        else:
            print("vienen mas tablas*******************************")
            print(query.operacion1)
            print(query.operacion2)
            a=procesar_select2_obtenerTablas(query.operacion1,ts)
           
            print("---------------------------------------------RESULTADO SELECT 3C--------------------------------------------------")
            print("LAS TABLAS SERAN: ",a)
            print("LAS COLUMNAS SERAN: todas")
            b=procesar_where(query.operacion2,ts,1,procesar_select2_obtenerTablas(query.operacion1,ts))
            print("EL WHERE SERA: ",b)
            h.textosalida+="TYTUS>>Se ha ejecutado su consulta\n"
            
            


def procesar_select_Tipo4(query,ts):
    print("ya entro al select TIPO 4")
    print(query.operacion1)
    print(query.operacion2)
    print(query.operacion3)
    a=procesar_select2_obtenerTablas(query.operacion2,ts) #tablas
    b=procesar_select2_obtenerColumnas(query.operacion1,ts) #columnas
    print("---------------------------------------------RESULTADO SELECT 4--------------------------------------------------")
    print("LAS TABLAS SERAN: ",a)
    print("Las columnas seran: ",b)
    print("saca el valor++++++++++++++++++++++++++++++")
    d=ts.obtenerSelect4(a,h.bd_enuso,b)
    print("resultado+++++++++++++++++++++4: ")
    print(d)
    c=procesar_where(query.operacion3,ts,d,a)
    print("La sentencia Where sera \n",c)
    h.textosalida+="TYTUS>>Se ha ejecutado su consulta\n"+str(c)+"\n"
    



def procesar_select_Tipo5(query,ts):
    print("llega al select 5")
    if query.operacion1=='*':
        print("trae asterisco saca todas las columnas")
        a=procesar_select2_obtenerTablas(query.operacion2,ts) #tablas    
        
        print("--------------------------------RESULTADO SELECT 5 * --------------------------------")
        print("LAS TABLAS SERAN: ",a)
        print("las columas seran: Todas")
        c=procesar_where(query.operacion3,ts,"todo",a)
        d=procesar_extras(query.operacion4,ts,c)
        print("La sentencia Where sera ",c)
        h.textosalida+="TYTUS>>Se ha ejecutado su consulta\n"
    else:
        print("trae una lista de columnas")
        a=procesar_select2_obtenerTablas(query.operacion2,ts) #tablas
        b=procesar_select2_obtenerColumnas(query.operacion1,ts) #columnas
        
        print("---------------------------------------------RESULTADO SELECT 5--------------------------------------------------")
        print("LAS TABLAS SERAN: ",a)
        print("LAS COLUMNAS SERAN: ",b)
        print("saca el valor++++++++++++++++++++++++++++++")
        d=ts.obtenerSelect4(a,h.bd_enuso,b)
        print("resultado+++++++++++++++++++++4: ")
        print(d)
        c=procesar_where(query.operacion3,ts,d,a)
        print("La sentencia Where sera \n",c)
        e=procesar_extras(query.operacion4,ts,c)
        print("el resultado despues de filtros es: \n",e)
        h.textosalida+="TYTUS>>Se ha ejecutado su consulta\n"+str(e)+"\n"

        

        

def procesar_extras(query,ts,donde):
    print("entro a procesar los extras")
    print(query)
    print(donde)
    filtro=donde
    for x in range(0,len(query)):
        if isinstance(query[x],ExpresionLimit):
            print("trae una limitante")
            a=desglosar_extras(query[x].valor1,ts)
            print("El limite a mostrar sera: ",a)
            filtro=filtro.head(a)
        elif isinstance(query[x],ExpresionLimitOffset):
            print("trae una limitante con offset")
            print(query[x])
            a=desglosar_extras(query[x].valor1,ts)
            b=desglosar_extras(query[x].valor2,ts)
            print("El limite a mostrar sera de",a, "  a ",b)
            filtro=filtro[b:]
            filtro=filtro.head(a)
        elif isinstance(query[x],ExpresionGroup):
            print("trae para agrupar")
            print(query[x])
        elif isinstance(query[x],ExpresionHaving):
            print("trae condicion adicional")
            print(query[x])
        elif isinstance(query[x],ExpresionOrder):
            print("trae expresion de ordenamiento")
            campoOdenamiento=desglosar_extras(query[x].valor1,ts)
            print(campoOdenamiento)
            print(query[x].valor2)
            if query[x].valor2=="ASC":
                filtro=filtro.sort_values(by=[campoOdenamiento], ascending=True)
            elif query[x].valor2=="DESC":
                filtro=filtro.sort_values(by=[campoOdenamiento], ascending=False)

    return filtro

def desglosar_extras(query,ts):
    print("entro a desglosar el ordenamiento=======")
    print(query)
    if isinstance(query,list):
        if isinstance(query[0],ExpresionFuncionBasica):
            print("entra a funcion basica")
            print(query[0].id)
            return desglosar_extras(query[0].id,ts)
        elif isinstance(query,ExpresionNumero):
            return query.id
        elif isinstance(query,ExpresionIdentificador):
            print("entra a identificadorA")
            print(query.id)
            return query.id
    else:
        if isinstance(query,ExpresionFuncionBasica):
            print("entra a funcion basica")
            print(query.id)
            return desglosar_extras(query.id,ts)
        elif isinstance(query,ExpresionNumero):
            return query.id
        elif isinstance(query,ExpresionIdentificador):
            print("entra a identificadorB")
            print(query.id)
            return query.id
        


def procesar_where(query,ts,campos,tablas):
    print("entra a procesar el where con lo que traiga++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("campos: ", campos)
    print("tablas: ",tablas)
    print(query.condiciones)
    return operar_where(query.condiciones,ts,campos)


def operar_where(query,ts,campos):
    print("entra a operar where")
    if isinstance(query,ExpresionRelacional):
        print("trae relacional")
        print(query.exp1)
        print(query.operador)
        print(query.exp2)
        a=operar_where(query.exp1,ts,campos)
        b=operar_where(query.exp2,ts,campos)
        if query.operador == OPERACION_RELACIONAL.IGUAL_IGUAL:
            print("compara si ",a," == ",b)
            filtro=campos.loc[campos[a]==b]
            print("el filtro sera******************\n",filtro)
            #"compara si ",a," == ",b
            return filtro
        elif query.operador == OPERACION_RELACIONAL.NO_IGUAL:
            print("compara si ",a," != ",b)
            filtro=campos.loc[campos[a]!=b]
            print("el filtro sera******************\n",filtro)
            #"compara si ",a," != ",b
            return filtro
        elif query.operador == OPERACION_RELACIONAL.MAYOR_IGUAL:
            print("compara si ",a," >= ",b)
            filtro=campos.loc[campos[a]>=b]
            print("el filtro sera******************\n",filtro)
            # "compara si ",a," >= ",b
            return filtro
        elif query.operador == OPERACION_RELACIONAL.MENOR_IGUAL:
            print("compara si ",a," <= ",b)
            filtro=campos.loc[campos[a]<=b]
            print("el filtro sera******************\n",filtro)
            #"compara si ",a," <= ",b
            return filtro
        elif query.operador == OPERACION_RELACIONAL.MAYOR:
            print("compara si ",a," > ",b)
            filtro=campos.loc[campos[a]>b]
            print("el filtro sera******************\n",filtro)
            #"compara si ",a," > ",b
            return filtro
        elif query.operador == OPERACION_RELACIONAL.MENOR:
            print("compara si ",a," < ",b)
            filtro=campos.loc[campos[a]<b]
            print("el filtro sera******************\n",filtro)
            #"compara si ",a," < ",b
            return filtro
        elif query.operador == OPERACION_RELACIONAL.DIFERENTE:
            print("compara si ",a," != ",b)
            filtro=campos.loc[campos[a]!=b]
            print("el filtro sera******************\n",filtro)
            # "compara si ",a," != ",b
            return filtro
    elif isinstance(query,ExpresionLogica):
        print("trae logica")
        print(query.exp1)
        print(query.operador)
        print(query.exp2)
        operar_where(query.exp2,ts,campos)
        a=operar_where(query.exp1,ts,campos)
        b=operar_where(query.exp2,ts,campos)
        if query.operador == OPERACION_LOGICA.AND:
            print("compara si ",a," AND ",b)
            #filtro=pd.where(a and b, 'True','False')
            #print("El filtro and sera\n",filtro)
            return filtro
        elif query.operador == OPERACION_LOGICA.OR:
            print("compara si ",a," OR ",b)
            return "compara si ",a," OR ",b
    elif isinstance(query, ExpresionBetween) :
        print("trae una expresion de  between")
        print(query.valor1) 
        a=operar_where(query.valor1,ts,campos)
        b=operar_where(query.valor2,ts,campos)
        print("compara datos que esten entre ",a,"  y  ",b)
    elif isinstance(query, ExpresionNotBetween) :
        print("trae una expresion de not between")
        a=operar_where(query.valor1,ts,campos)
        b=operar_where(query.valor2,ts,campos)
        print("compara datos que NO esten entre ",a,"  y  ",b)
    elif isinstance(query, ExpresionBetweenSymmetric) :
        print("trae una expresion de between symmetric")
        a=operar_where(query.valor1,ts,campos)
        b=operar_where(query.valor2,ts,campos)
        print("compara datos que esten entre algo symmetric ",a,"  y  ",b)
    elif isinstance(query, ExpresionNotBetweenSymmetric) :
        print("trae una expresion de not between symmetric")
        a=operar_where(query.valor1,ts,campos)
        b=operar_where(query.valor2,ts,campos)
        print("compara datos que NO esten entre algo symmetric ",a,"  y  ",b)
    elif isinstance(query, ExpresionIsDistinct) :
        print("trae una expresion de is distinct")
        a=operar_where(query.valor1,ts,campos)
        b=operar_where(query.valor2,ts,campos)
        print("compara datos sean distintos de ",a,"  y  ",b)
    elif isinstance(query, ExpresionIsNotDistinct) :
        print("trae una expresion de is not distinct")
        a=operar_where(query.valor1,ts,campos)
        b=operar_where(query.valor2,ts,campos)
        print("compara datos NO sean distintos de ",a,"  y  ",b)
    elif isinstance(query, ExpresionNumero) :
        print("retorna el NUMERO: ",query.id)
        return query.id
    elif isinstance(query, ExpresionIdentificador) :
        if ts.obtener(query.id)=="no definida":
            return None
        else:
            print("retorna el ID: ",ts.obtener(query.id).nombre)
            return (str(ts.obtener(query.id).nombre)+str(ts.obtener(query.id).BD)+str(ts.obtener(query.id).tabla))
    elif isinstance(query,ExpresionCadenas):
        print("retorna la CADENA: ",query.id)
        return query.id
    elif isinstance(query, ExpresionNegativo) :
        print("NEGATIVO")
        print("EXP_NUM:",query.id)
        return query.id * -1
    elif isinstance(query, ExpresionNegativo) :
        print("NEGATIVO")
        print("EXP_NUM:",query.id)
        return query.id * -1
    elif isinstance(query, ExpresionNotIn) :
        print("TRAE UN NOT IN")
        print("ID: ",query.valor1)
        print("select: ", query.valor2)
        procesar_queries(query.valor2,ts)
        return 0
def procesar_createdb(query,ts):
    verificacion =  ts.verificacionCrearBD(query.variable)
    if verificacion==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        h.textosalida+="TYTUS>> "+"Se creo la BD "+ str(query.variable) +" en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la BD " +str(query.variable) +" en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return "se creo una nueva bd: "+str(query.variable)
    elif verificacion==1:
        h.textosalida+="TYTUS>> "+str(query.variable)+" es una BD ya en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la " +str(query.variable) +" BD en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return str(query.variable)+ "es el nombre de una BD puede ser que quiera crear una tabla o columna"+"\n"
        
def procesar_create_if_db(query,ts):
    verificacion =  ts.verificacionCrearBD(query.variable)
    if verificacion==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        h.textosalida+="TYTUS>> "+"Se creo la BD "+ str(query.variable) +" en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la BD " +str(query.variable) +" en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return "se creo una nueva bd: "+str(query.variable)
    elif verificacion==1:
        h.textosalida+="TYTUS>> "+str(query.variable)+" es una BD ya en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la " +str(query.variable) +" BD en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return str(query.variable)+ "es el nombre de una BD puede ser que quiera crear una tabla o columna"+"\n" 
    #llamo al metodo de EDD

def procesar_create_replace_db(query,ts):
    verificacion =  ts.verificacionCrearBD(query.variable)
    if verificacion==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        h.textosalida+="TYTUS>> "+"Se creo la BD "+ str(query.variable) +" en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la BD " +str(query.variable) +" en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return "se creo una nueva bd: "+str(query.variable)
    elif verificacion==1:
        h.textosalida+="TYTUS>> "+str(query.variable)+" es una BD ya en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la " +str(query.variable) +" BD en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return str(query.variable)+ "es el nombre de una BD puede ser que quiera crear una tabla o columna"+"\n"

def procesar_create_replace_if_db(query,ts):
    verificacion =  ts.verificacionCrearBD(query.variable)
    if verificacion==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        h.textosalida+="TYTUS>> "+"Se creo la BD "+ str(query.variable) +" en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la BD " +str(query.variable) +" en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return "se creo una nueva bd: "+str(query.variable)
    elif verificacion==1:
        h.textosalida+="TYTUS>> "+str(query.variable)+" es una BD ya en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la " +str(query.variable) +" BD en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return str(query.variable)+ "es el nombre de una BD puede ser que quiera crear una tabla o columna"+"\n"
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_createwithparametersdb(query,ts):
    verificacion =  ts.verificacionCrearBD(query.variable)
    if verificacion==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        h.textosalida+="TYTUS>> "+"Se creo la BD "+ str(query.variable) +" en memoria dinamica"+"\n"
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
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la BD " +str(query.variable) +" en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return "se creo una nueva bd: "+str(query.variable)
    elif verificacion==1:
        h.textosalida+="TYTUS>> "+str(query.variable)+" es una BD ya en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la " +str(query.variable) +" BD en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return str(query.variable)+ "es el nombre de una BD puede ser que quiera crear una tabla o columna"+"\n"


def procesar_createwithparameters_if_db(query,ts):
    verificacion =  ts.verificacionCrearBD(query.variable)
    if verificacion==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        h.textosalida+="TYTUS>> "+"Se creo la BD "+ str(query.variable) +" en memoria dinamica"+"\n"
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
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la BD " +str(query.variable) +" en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return "se creo una nueva bd: "+str(query.variable)
    elif verificacion==1:
        h.textosalida+="TYTUS>> "+str(query.variable)+" es una BD ya en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la " +str(query.variable) +" BD en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return str(query.variable)+ "es el nombre de una BD puede ser que quiera crear una tabla o columna"+"\n"


def procesar_createwithparameters_replace_db(query,ts):
    verificacion =  ts.verificacionCrearBD(query.variable)
    if verificacion==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        h.textosalida+="TYTUS>> "+"Se creo la BD "+ str(query.variable) +" en memoria dinamica"+"\n"
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
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la BD " +str(query.variable) +" en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return "se creo una nueva bd: "+str(query.variable)
    elif verificacion==1:
        h.textosalida+="TYTUS>> "+str(query.variable)+" es una BD ya en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la " +str(query.variable) +" BD en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return str(query.variable)+ "es el nombre de una BD puede ser que quiera crear una tabla o columna"+"\n"


def procesar_createwithparameters_replace_if_db(query,ts):
    verificacion =  ts.verificacionCrearBD(query.variable)
    if verificacion==0:
        base_datos = TS.Simbolo(None,query.variable,None,None, None, None, 0,0,0,None,None,0,None,0,None,None,None,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregarCrearBD(base_datos)
        h.textosalida+="TYTUS>> "+"Se creo la BD "+ str(query.variable) +" en memoria dinamica"+"\n"
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
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la BD " +str(query.variable) +" en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return "se creo una nueva bd: "+str(query.variable)
    elif verificacion==1:
        h.textosalida+="TYTUS>> "+str(query.variable)+" es una BD ya en memoria dinamica"+"\n"
        if store.createDatabase(query.variable) == 0:
            h.textosalida+="TYTUS>> "+"Se creo la " +str(query.variable) +" BD en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.variable) + " ya existe en memoria estatica"+"\n"
        elif store.createDatabase(query.variable) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        return str(query.variable)+ "es el nombre de una BD puede ser que quiera crear una tabla o columna"+"\n"

# ---------------------------------------------------------------------------------------------------------------- 
def procesar_alterdb(query,ts):
    verificacion =  ts.verificacionAlterBD(query.id_original)
    verificacion2 =  ts.verificacionAlterBD_2(query.id_alter)
    if verificacion==1:
        if verificacion2 == 0:
            ts.actualizarAlterBD(query.id_original,query.id_alter)
            if store.alterDatabase(query.id_original,query.id_alter) == 0:
                h.textosalida+="TYTUS>> "+"se actualizo la bd: "+str(query.id_original) + " por " +str(query.id_alter) + "en memoria estatica"+"\n"
            elif store.alterDatabase(query.id_original,query.id_alter) == 3:
                h.textosalida+="TYTUS>> "+"La BD "+ str(query.id_alter) + " ya existe en memoria estatica, elija otro nombre para reemplazar "+ str(query.id_original) +"\n"
            elif store.alterDatabase(query.id_original,query.id_alter) == 2:
                h.textosalida+="TYTUS>> "+"La BD "+ str(query.id_original) + " no existe en memoria estatica"+"\n"
            elif store.alterDatabase(query.id_original,query.id_alter) == 1:
                h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
            else:
                print("ERROR\n")
            h.textosalida+="TYTUS>> "+"se actualizo la bd: "+str(query.id_original) + " por " +str(query.id_alter) + "\n"
            return "se actualizo la bd: "+str(query.id_original) + "por" +str(query.id_alter)
        elif verificacion2 == 1:
            h.textosalida+="TYTUS>> " + "La BD "+str(query.id_alter)+" ya existe en memoria dinamica, elija otro nombre por favor" + "\n"
    elif verificacion==0:
        h.textosalida+="TYTUS>> " +str(query.id_original) + " No se encontro ninguna base de datos con ese nombre" + "\n"
        return "No se encontro ninguna base de datos con ese nombre"
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_alterwithparametersdb(query,ts):
    print("ID:",query.id_original)
    print("OWNER:",query.owner)
    print("USER:",query.id_alter)
# ---------------------------------------------------------------------------------------------------------------- 
def procesar_dropdb(query,ts):
    if ts.destruirBD(query.id)==1:
        if store.dropDatabase(query.id) == 0:
            h.textosalida+="TYTUS>> "+"Se elimino la BD " +str(query.id) +" en memoria estatica"+"\n"
        elif store.dropDatabase(query.id) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.id) + " no existe"+"\n"
        elif store.dropDatabase(query.id) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        h.textosalida+="TYTUS>> "+ "ELIMINADA BD:"+str(query.id) + "\n"
        return "ELIMINADA BD:"+str(query.id)
    elif ts.destruirBD(query.id)==0:
        h.textosalida+="TYTUS>> "+str(query.id)+" No se encontro ninguna base de datos con ese nombre"+"\n"
        return "No se encontro ninguna base de datos con ese nombre"

def procesar_dropifdb(query,ts):
    if ts.destruirBD(query.id)==1:
        if store.dropDatabase(query.id) == 0:
            h.textosalida+="TYTUS>> "+"Se elimino la BD " +str(query.id) +" en memoria estatica"+"\n"
        elif store.dropDatabase(query.id) == 2:
            h.textosalida+="TYTUS>> "+"La BD "+ str(query.id) + " no existe"+"\n"
        elif store.dropDatabase(query.id) == 1:
            h.textosalida+="TYTUS>> "+"Error 22000 data_exception"+"\n"
        else:
            print("ERROR\n")
        h.textosalida+="TYTUS>> "+ "ELIMINADA BD:"+str(query.id) + "\n"
        return "ELIMINADA BD:"+str(query.id)
    elif ts.destruirBD(query.id)==0:
        h.textosalida+="TYTUS>> "+str(query.id)+" No se encontro ninguna base de datos con ese nombre"+"\n"
        return "No se encontro ninguna base de datos con ese nombre"
# ---------------------------------------------------------------------------------------------------------------- 
#                                             QUERIES
# ----------------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------------- 
#                                             EXPRESIONES
# ----------------------------------------------------------------------------------------------------------------

# --------------------------------------EXPRESION ARITMETICA-----------------------------------------------------------
def resolver_expresion_aritmetica(expNum, ts) :
    print("entra a expresion aritmetica")
    print(expNum)
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
            print("entro al acos")
            exp= resolver_expresion_aritmetica(expNum.exp, ts)
            print("entro al acos")
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


        elif isinstance(expNum,ExpresionLENGTH):
            exp= resolver_expresion_aritmetica(expNum.exp1, ts)
            return len(exp)
        elif isinstance(expNum,ExpresionSUBSTR):
            ex= resolver_expresion_aritmetica(expNum.exp1, ts)
            ex1= resolver_expresion_aritmetica(expNum.exp2, ts)
            ex2= resolver_expresion_aritmetica(expNum.exp3, ts)
            return ex[ex1:ex2]
        elif isinstance(expNum,ExpresionSUBSTRINGA):
            ex= resolver_expresion_aritmetica(expNum.exp1, ts)
            ex1= resolver_expresion_aritmetica(expNum.exp2, ts)
            ex2= resolver_expresion_aritmetica(expNum.exp3, ts)
            return ex[ex1:ex2]
        elif isinstance(expNum,ExpresionSUBSTRINGB):
            ex= resolver_expresion_aritmetica(expNum.exp1, ts)
            ex1= resolver_expresion_aritmetica(expNum.exp2, ts)
            return ex[ex1:]
        elif isinstance(expNum,ExpresionSUBSTRINGC):
            ex= resolver_expresion_aritmetica(expNum.exp1, ts)
            ex1= resolver_expresion_aritmetica(expNum.exp2, ts)
            return ex[:ex1]
        elif isinstance(expNum,ExpresionSHA256):
            exp= resolver_expresion_aritmetica(expNum.exp1, ts)
            print(exp)
            return str(ha.sha256(exp.encode()))
        elif isinstance(expNum,ExpresionMD5):
            exp= resolver_expresion_aritmetica(expNum.exp1, ts)
            return str(ha.md5(exp.encode()))
        elif isinstance(expNum,ExpresionTRIM):
            ex= resolver_expresion_aritmetica(expNum.exp1, ts)
            ex1= resolver_expresion_aritmetica(expNum.exp2, ts)
            ex2= resolver_expresion_aritmetica(expNum.exp3, ts)
            print(ex)
            print(ex1)
            print(ex2)
            if ex=="1":
                res=ex2.lstrip(ex1)
                print(res)
                return res
            elif ex=="2":
                res=ex2.rstrip(ex1)
                return res
            elif ex=="3":
                res=ex2.strip(ex1)
                return res
        elif isinstance(expNum,ExpresionCurrentTime):
            print(datetime.datetime.now().strftime("%H:%M:%S"))
            return str(datetime.datetime.now().strftime("%H:%M:%S"))
        elif isinstance(expNum,ExpresionCurrentDate):
            print(datetime.datetime.now().strftime("%Y-%m-%d"))
            return str(datetime.datetime.now().strftime("%Y-%m-%d"))
        elif isinstance(expNum,ExpresionEXTRACT):
            print("entro al extract")
            ex1= resolver_expresion_aritmetica(expNum.exp1, ts)
            print(ex1)
            ex2= resolver_expresion_aritmetica(expNum.exp2, ts)
            print(ex2)
            ex3=time.strptime(ex2,"%Y-%m-%d %H:%M:%S")
            print(str(ex3))
            if ex1=="1":
                res=ex3.tm_year
                print(str(res))
                return str(res)
            elif ex1=="2":
                res=ex3.tm_mon
                print(str(res))
                return str(res)
            elif ex1=="3":
                res=ex3.tm_mday
                print(str(res))
                return str(res)
            elif ex1=="4":
                res=ex3.tm_hour
                print(str(res))
                return str(res)
            elif ex1=="5":
                res=ex3.tm_min
                print(str(res))
                return str(res)
            elif ex1=="6":
                res=ex3.tm_sec
                print(str(res))
                return str(res)
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
    #h.textosalida+="TYTUS>> Insertando registro de una tabla\n"
    numdatocolumna = 0
    if query.listidCol == None: #solo cuando no se especifica las columnas al ingresar un dato
        tamlistreg = len(query.listRegistros)
        contcol = 1
        while contcol <= tamlistreg:
            col = ts.obtenersinNombreColumna(query.idTable,h.bd_enuso,contcol-1)
            if col == 0:
                print("ERROR: La tabla especificada no se encuentra creada")
                return
            else:
                if col.tipo.upper() == 'VARCHAR' or col.tipo.upper() == 'CHARACTER' or col.tipo.upper() == 'VARYING' or col.tipo.upper() == 'CHAR':
                    if validaTipoDato(col.tipo,str(query.listRegistros[contcol-1].id),col.tamanoCadena) == True:
                        #ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)
                        if col.pk == 1 or col.unique == 1: #columna es llave primaria
                            temp = 0
                            if col.valor != None:
                                sizeregcol = len(col.valor)
                                while temp < sizeregcol:
                                    if col.valor[temp] == query.listRegistros[contcol-1].id:
                                        if col.valor == None:
                                            correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                            print("Error: valor invalido para la columna")
                                            return

                                        else:
                                            correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                            print("Error: valor invalido para la columna")
                                            return
                                    temp=temp+1

                            ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)

                        else:
                            ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)
                    else:
                        if col.valor == None:
                            correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                            print("Error: valor invalido para la columna")
                            return

                        else:
                            correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                            print("Error: valor invalido para la columna")
                            return

                elif col.check == 1: #validacion de dato si cumple con restriccion check
                    exp1=ExpresionNumero(query.listRegistros[contcol-1].id)
                    #print("-------",col.condicionCheck)
                    #print(col.condicionCheck.exp1)
                    #print(col.condicionCheck.exp2)
                    #print(col.condicionCheck.exp2.exp1)
                    #print(col.condicionCheck.exp2.exp1.exp1.id)
                    #print(col.condicionCheck.exp2.exp1.exp2.id)
                    #print(col.condicionCheck.exp2.exp1.operador)
                    #validarCheck(col.condicionCheck,exp1,None,ts)
                    #return
                    if validaTipoDato(col.tipo.upper(),query.listRegistros[contcol-1].id,col.tamanoCadena) == True:
                        #print("valido check")
                        tp = col.tipo.upper()
                        if tp=='SMALLINT' or tp=='INTEGER' or tp=='BIGINT' or tp=='DECIMAL' or tp=='NUMERIC' or tp=='REAL' or tp=='DOUBLE' or tp=='MONEY':
                            exp1=ExpresionNumero(query.listRegistros[contcol-1].id)
                            exp2= None
                            if isinstance(col.condicionCheck.exp2,ExpresionIdentificador):
                                coltemp = ts.obtenerconNombreColumna(col.condicionCheck.exp2.id,h.bd_enuso,query.idTable)
                                tamtemp = len(coltemp.valor)
                                valtemp = coltemp.valor[tamtemp-1]
                                exp2=ExpresionNumero(valtemp)
                                
                            else:
                                exp2=col.condicionCheck
                            if validarCheck(exp2,exp1,col.condicionCheck.operador,ts) == 1:
                                if col.pk == 1 or col.unique == 1: #columna es llave primaria
                                    temp = 0
                                    if col.valor != None:
                                        sizeregcol = len(col.valor)
                                        while temp < sizeregcol:
                                            if col.valor[temp] == query.listRegistros[contcol-1].id:
                                                if col.valor == None:
                                                    correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                                    print("Error: valor invalido para la columna")
                                                    return

                                                else:
                                                    correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                                    print("Error: valor invalido para la columna")
                                                    return
                                            temp=temp+1

                                    ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)

                                else:
                                    ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)
                            else:
                                if col.valor == None:
                                    correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                    print("Error: valor invalido para la columna")
                                    return

                                else:
                                    correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                    print("Error: valor invalido para la columna")
                                    return
                        else:
                            exp1=ExpresionCadenas(query.listRegistros[contcol-1].id)
                            exp2= None
                            if isinstance(col.condicionCheck.exp2,ExpresionIdentificador):
                                coltemp = ts.obtenerconNombreColumna(col.condicionCheck.exp2.id,h.bd_enuso,query.idTable)
                                tamtemp = len(coltemp.valor)
                                valtemp = coltemp.valor[tamtemp-1]
                                exp2=ExpresionCadenas(valtemp)
                            else:
                                exp2=col.condicionCheck
                            if validarCheck(exp2,exp1,col.condicionCheck.operador,ts)==1:
                                if col.pk == 1 or col.unique == 1: #columna es llave primaria
                                    temp = 0
                                    if col.valor != None:
                                        sizeregcol = len(col.valor)
                                        while temp < sizeregcol:
                                            if col.valor[temp] == query.listRegistros[contcol-1].id:
                                                if col.valor == None:
                                                    correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                                    print("Error: valor invalido para la columna")
                                                    return

                                                else:
                                                    correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                                    print("Error: valor invalido para la columna")
                                                    return
                                            temp=temp+1

                                    ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)

                                else:
                                    ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)
                            else:
                                if col.valor == None:
                                    correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                    print("Error: valor invalido para la columna")
                                    return

                                else:
                                    correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                    print("Error: valor invalido para la columna")
                                    return
                    else:
                        if col.valor == None:
                            correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                            print("Error: valor invalido para la columna")
                            return

                        else:
                            correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                            print("Error: valor invalido para la columna")
                            return


                elif isinstance(query.listRegistros[contcol-1], ExpresionNOW) and col.tipo.upper() == 'DATE':
                    #ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,str(date.today().strftime("%Y-%m-%d")))
                    if col.pk == 1 or col.unique == 1: #columna es llave primaria
                        temp = 0
                        if col.valor != None:
                            sizeregcol = len(col.valor)
                            while temp < sizeregcol:
                                if col.valor[temp] == query.listRegistros[contcol-1].id:
                                    if col.valor == None:
                                        correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                        print("Error: valor invalido para la columna")
                                        return

                                    else:
                                        correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                        print("Error: valor invalido para la columna")
                                        return
                                temp=temp+1

                        ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,str(date.today().strftime("%Y-%m-%d")))

                    else:
                        ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,str(date.today().strftime("%Y-%m-%d")))
                else:
                    if validaTipoDato(col.tipo.upper(),query.listRegistros[contcol-1].id,col.tamanoCadena) == True:
                        if col.tipo.upper()=="MONEY":
                            datotemp = convertiraMoney(query.listRegistros[contcol-1].id)
                        elif col.tipo.upper()=="DECIMAL" and col.tamanoCadena != None:
                            y = query.listRegistros[contcol-1].id
                            exact = col.tamanoCadena.split(",")
                            form = "{0:."+str(exact[1])+"f}"
                            numero = form.format(y)
                            datotemp = numero
                        else:
                            datotemp = query.listRegistros[contcol-1].id
                        if col.pk == 1 or col.unique == 1: #columna es llave primaria
                            temp = 0
                            if col.valor != None:
                                sizeregcol = len(col.valor)
                                while temp < sizeregcol:
                                    if col.valor[temp] == datotemp:
                                        if col.valor == None:
                                            correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                            print("Error: valor invalido para la columna")
                                            return

                                        else:
                                            correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                                            print("Error: valor invalido para la columna")
                                            return
                                    temp=temp+1

                            ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,datotemp)

                        else:
                            ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,datotemp)

                    else:
                        if col.valor == None:
                            correccionTamanoValoresColumna(0,tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                            print("Error: valor invalido para la columna")
                            return

                        else:
                            correccionTamanoValoresColumna(len(col.valor),tamlistreg,query.listRegistros,h.bd_enuso,query.idTable,ts,2)
                            print("Error: valor invalido para la columna")
                            return
                        

            contcol=contcol+1
            
    elif query.listidCol != None:  #cuando se especifica la columna a la que se le ingresara un dato
        
        numdatocolumna = ts.numerodeDatosenColumna(query.listidCol[0].id,h.bd_enuso,query.idTable)
        tamlistid = len(query.listidCol)
        tamlistreg = len(query.listRegistros)
        contcol = 1 
        while contcol <= tamlistid:
            col = ts.obtenerconNombreColumna(query.listidCol[contcol-1].id,h.bd_enuso,query.idTable)
            if col == 0:
                print("ERROR: La tabla especificada no se encuentra creada")
                return
            else:
                if col.tipo.upper() == 'VARCHAR' or col.tipo.upper() == 'CHARACTER' or col.tipo.upper() == 'VARYING' or col.tipo.upper() == 'CHAR':
                    if validaTipoDato(col.tipo,str(query.listRegistros[contcol-1].id),col.tamanoCadena) == True:
                        if col.pk == 1 or col.unique == 1: #columna es llave primaria
                            temp = 0
                            if col.valor != None:
                                sizeregcol = len(col.valor)
                                while temp < sizeregcol:
                                    if col.valor[temp] == query.listRegistros[contcol-1].id:
                                        if col.valor == None:
                                            correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                            print("Error: valor invalido para la columna")
                                            return

                                        else:
                                            correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                            print("Error: valor invalido para la columna")
                                            return

                            ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)

                        else:
                            ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)

                    else:
                        if col.valor == None:
                            correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                            print("Error: valor invalido para la columna")
                            return

                        else:
                            correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                            print("Error: valor invalido para la columna")
                            return

                elif col.check == 1:
                    if validaTipoDato(col.tipo.upper(),query.listRegistros[contcol-1].id,col.tamanoCadena) == True:
                        print("valido check")
                        tp = col.tipo.upper()
                        if tp=='SMALLINT' or tp=='INTEGER' or tp=='BIGINT' or tp=='DECIMAL' or tp=='NUMERIC' or tp=='REAL' or tp=='DOUBLE' or tp=='MONEY':
                            exp1=ExpresionNumero(query.listRegistros[contcol-1].id)
                            exp2= None
                            if isinstance(col.condicionCheck.exp2,ExpresionIdentificador):
                                coltemp = ts.obtenerconNombreColumna(col.condicionCheck.exp2.id,h.bd_enuso,query.idTable)
                                tamtemp = len(coltemp.valor)
                                valtemp = coltemp.valor[tamtemp-1]
                                exp2=ExpresionNumero(valtemp)
                            else:
                                exp2=col.condicionCheck
                            if validarCheck(exp2,exp1,col.condicionCheck.operador,ts) == 1:
                                if col.pk == 1 or col.unique == 1: # se verifica que la llave primaria no sea repetida
                                    temp = 0
                                    if col.valor != None:
                                        sizeregcol = len(col.valor)
                                        while temp < sizeregcol:
                                            if col.valor[temp] == query.listRegistros[contcol-1].id:
                                                print("llave primaria a insertar repetida")
                                                if col.valor == None:
                                                    correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                                    print("Error: valor invalido para la columna")
                                                    return

                                                else:
                                                    correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                                    print("Error: valor invalido para la columna")
                                                    return
                                                
                                            temp= temp+1

                                    ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)

                                else:
                                    ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)
                            else:
                                if col.valor == None:
                                    correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                    print("Error: valor invalido para la columna")
                                    return

                                else:
                                    correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                    print("Error: valor invalido para la columna")
                                    return

                        else:
                            exp1=ExpresionCadenas(query.listRegistros[contcol-1].id)
                            exp2= None
                            if isinstance(col.condicionCheck.exp2,ExpresionIdentificador):
                                coltemp = ts.obtenerconNombreColumna(col.condicionCheck.exp2.id,h.bd_enuso,query.idTable)
                                tamtemp = len(coltemp.valor)
                                valtemp = coltemp.valor[tamtemp-1]
                                exp2=ExpresionCadenas(valtemp)
                            else:
                                exp2=col.condicionCheck

                            if validarCheck(exp2,exp1,col.condicionCheck.operador,ts)==1:
                                if col.pk == 1 or col.unique == 1: # se verifica que la llave primaria no sea repetida
                                    temp = 0
                                    if col.valor != None:
                                        sizeregcol = len(col.valor)
                                        while temp < sizeregcol:
                                            if col.valor[temp] == query.listRegistros[contcol-1].id:
                                                print("llave primaria a insertar repetida")
                                                if col.valor == None:
                                                    correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                                    print("Error: valor invalido para la columna")
                                                    return

                                                else:
                                                    correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                                    print("Error: valor invalido para la columna")
                                                    return
                                                
                                            temp= temp+1

                                    ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)

                                else:
                                    ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,query.listRegistros[contcol-1].id)
                            else:
                                if col.valor == None:
                                    correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                    print("Error: valor invalido para la columna")
                                    return

                                else:
                                    correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                    print("Error: valor invalido para la columna")
                                    return
                    else:
                        if col.valor == None:
                            correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                            print("Error: valor invalido para la columna")
                            return

                        else:
                            correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                            print("Error: valor invalido para la columna")
                            return

                elif isinstance(query.listRegistros[contcol-1], ExpresionNOW) and col.tipo.upper() == 'DATE':
                    if col.pk == 1 or col.unique == 1:#se verifica que la llave primaria no sea repetida
                        temp = 0
                        if col.valor != None:
                            sizeregcol = len(col.valor)
                            while temp < sizeregcol:
                                if col.valor[temp] == query.listRegistros[contcol-1].id:
                                    print("llave primaria a insertar repetida")
                                    if col.valor == None:
                                        correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                        print("Error: valor invalido para la columna")
                                        return

                                    else:
                                        correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                        print("Error: valor invalido para la columna")
                                        return

                        ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,str(date.today().strftime("%Y-%m-%d")))

                    else:
                        ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,str(date.today().strftime("%Y-%m-%d")))
                    
                else:
                    if validaTipoDato(col.tipo.upper(),query.listRegistros[contcol-1].id,col.tamanoCadena) == True:
                        datotemp = None
                        if col.tipo.upper()=="MONEY":
                            datotemp = convertiraMoney(query.listRegistros[contcol-1].id)
                        else:
                            datotemp = query.listRegistros[contcol-1].id

                        if col.pk == 1 or col.unique == 1: # se verifica que la llave primaria no sea repetida
                            temp = 0
                            if col.valor != None:
                                sizeregcol = len(col.valor)
                                while temp < sizeregcol:
                                    if col.valor[temp] == datotemp:
                                        print("llave primaria a insertar repetida")
                                        if col.valor == None:
                                            correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                            print("Error: valor invalido para la columna")
                                            return

                                        else:
                                            correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                                            print("Error: valor invalido para la columna")
                                            return
                                        
                                    temp= temp+1

                            ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,datotemp)

                        else:
                            ts.actualizarValorColumna(col.nombre,col.BD,col.tabla,datotemp)

                    else:
                        if col.valor == None:
                            correccionTamanoValoresColumna(0,tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                            print("Error: valor invalido para la columna")
                            return

                        else:
                            correccionTamanoValoresColumna(len(col.valor),tamlistid,query.listidCol,h.bd_enuso,query.idTable,ts,1)
                            print("Error: valor invalido para la columna")
                            return
                        

            contcol=contcol+1
        ValidandoDefault(numdatocolumna+1,h.bd_enuso,query.idTable,ts)
    insertTablaStorage(query.idTable,ts)

    
def insertTablaStorage(tabla,ts):
    cont = 0
    listdatos = None
    numcol = ts.numerodeColumnas(h.bd_enuso,tabla)
    while cont < numcol:
        col = ts.obtenersinNombreColumna(tabla,h.bd_enuso,cont)
        temp = len(col.valor)
        if listdatos == None:
            listdatos = [col.valor[temp-1]]
        else:
            listdatos.append(col.valor[temp-1])
        cont=cont+1
    print(listdatos)
    h.textosalida+="TYTUS>> "+"\n"
    h.textosalida+="TYTUS>> "+"\n"
    h.textosalida +="TYTUS>> Se inserto datos a la tabla: "+str(tabla)+"\n"
    h.textosalida +="TYTUS>> Datos isertados: "+str(listdatos)+"\n"



#se utiliza cuando se produce un error y anteriormente se ingresaron datos, recalcula la cantidad de valores
def correccionTamanoValoresColumna(tamValores,tamlistid,listidcol,BD,tabla,ts,forma):
    #forma = 1 ---> con parametros id
    #forma = 2 ---> sin parametros id
    if tamValores != 0: #con valores en la columna
        contt=1
        while contt <= tamlistid:
            if forma == 1:
                col2 = ts.obtenerconNombreColumna(listidcol[contt-1].id,BD,tabla)
            elif forma == 2:
                col2 = ts.obtenersinNombreColumna(tabla,BD,contt-1)

            if len(col2.valor) != tamValores:
                col2.valor.pop()
            contt=contt+1
        return
    else: #sin valores en la columna
        sizeValores = None
        contt = 1
        while contt <= tamlistid:
            if forma == 1:
                col2 = ts.obtenerconNombreColumna(listidcol[contt-1].id,BD,tabla)
            elif forma == 2:
                col2 = ts.obtenersinNombreColumna(tabla,BD,contt-1)
            if len(col2.valor) != sizeValores:
                col2.valor.pop()
            contt=contt+1
        return



def ValidandoDefault(tamValores,BD,tabla,ts):
    cantColumnas = ts.numerodeColumnas(h.bd_enuso,tabla)
    cont=1
    while cont <= cantColumnas:
        col = ts.obtenersinNombreColumna(tabla,BD,cont-1)
        if col.valor != None:  
            if len(col.valor) < tamValores:
                ts.actualizandoDefaultColumna(col.nombre,BD,tabla)
        else:
             if 0 < tamValores:
                ts.actualizandoDefaultColumna(col.nombre,BD,tabla)
        cont = cont+1


def validarCheck(exp1,exp2,operador,ts):
    print(exp1)
    result1 = None
    result2 = None
    if isinstance(exp1, ExpresionRelacional):
        if isinstance(exp1.exp1, ExpresionIdentificador) and isinstance(exp1.exp2, ExpresionRelacional):
            cond1 = ExpresionRelacional(exp2,exp1.exp2.exp1.exp1,exp1.operador)
            result1 = resolver_expresion_relacional(cond1,ts)
            print("Resultado1: ",result1)

            if isinstance(exp1.exp2, ExpresionRelacional):
                cond2 = ExpresionRelacional(exp2,exp1.exp2.exp2,exp1.exp2.operador)
                result2 = resolver_expresion_relacional(cond2,ts)
                print("REesultado2: ",result2)
            return result1 and result2
        elif isinstance(exp1.exp1, ExpresionIdentificador) and isinstance(exp1.exp2, ExpresionNumero):
            cond = ExpresionRelacional(exp2,exp1.exp2,exp1.operador)
            return resolver_expresion_relacional(cond,ts)
    elif isinstance(exp1,ExpresionNumero):
        cond1 = ExpresionRelacional(exp2,exp1,operador)
        return resolver_expresion_relacional(cond1,ts)
        
    #    print("se valido check")
    #    return 1
    #else:
    #    print("dato no valido para check")
    #    return 0

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
    print("Entra al else del select-------------------------------------------------------------------------------------------")
    print(query)
    print(len(query))
    tablas=[]
    for x in range(0,len(query)) :
        print("***********************************************Itera: ",x,"******************************************************")
        if isinstance(query[x], ExpresionFuncionBasica): 
            print("***********************************************BASICA******************************************************")
            a=query[x]
            print(a)
            tablas.append(query[x].id.id)
        elif isinstance(query[x],Asignacion):
            print("***********************************************ASIGNACION******************************************************")
            #print(procesar_asignacion(query[x],ts))
            a=query[x]
            print(a.campo)
            print(a.alias)
            b=procesar_asignacion(query[x],ts)
            tablas.append(b)
            #tablas.append(procesar_asignacion(query[x].campo,ts))
            #tablas.append(procesar_asignacion(query[x].alias,ts))
        elif isinstance(query[x],ExpresionIdentificador):
            print("***********************************************IDENTIFICADOR******************************************************")
            a=query[x]
            print(a)
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
    elif isinstance(query.id,ExpresionLlamame):
        print("trae una expresion llamameO")
        return (query.id.id+"-"+query.id.id1)
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

    elif isinstance(query.id,ExpresionLENGTH): 
        print("pasa opr lenght de operaciones basicas")
        return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionTRIM): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionSUBSTR): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionSUBSTRINGA): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionSUBSTRINGB): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionSUBSTRINGC): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionSHA256): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionMD5): return resolver_expresion_aritmetica(query.id,ts)

    elif isinstance(query.id,ExpresionCurrentTime): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCurrentDate): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionEXTRACT): return resolver_expresion_aritmetica(query.id,ts)
    
    

    elif isinstance(query.id,ExpresionIdentificador): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionCadenas): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.id,ExpresionAritmetica): return resolver_expresion_aritmetica(query.id,ts)
    elif isinstance(query.campo,ExpresionLlamame): print("777777777 LLEGO A LLAMAME 77777777777777777777777")
    
    
    else:
        print("error en operaciones basicas")


# ---------------------------------------------------------------------------------------------------------------------
#                               PROCESAR ASIGNACIONES
# ---------------------------------------------------------------------------------------------------------------------
def procesar_asignacion(query, ts) :  
    print("entra a procesar asignacion")
    print(query)
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
    elif isinstance(query.campo,ExpresionLlamame):
        print("777777777 LLEGO A LLAMAME 77777777777777777777777")
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
            simbolo = TS.Simbolo(None,variable,None,None,None,None,None,None,None,None,None,None,None,None,None,None, valor,None,None,None)      # inicializamos con 0 como valor por defecto
            ts.agregar(simbolo)
            print("se creo una nueva variable")
            print(variable)
            return variable
    else:
        if isinstance(valor, str) and valor.find("error")>0:
            return valor
        else:
            simbolo = TS.Simbolo(None,variable,None,None,None,None,None,None,None,None,None,None,None,None,None,None, valor,None,None,None)
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
    h.textosalida+="TYTUS>>\n"
    h.textosalida+="TYTUS>> Eliminando registro de una tabla\n"
    
    if isinstance(query.condColumna,operacionDelete):
        print(query.condColumna.exp1)
        print(query.condColumna.exp2)
        if isinstance(query.condColumna.exp1,ExpresionIdentificador) and isinstance(query.condColumna.exp2,ExpresionNumero):
            print("condicion simple")
            numcolumnas = ts.numerodeColumnas(h.bd_enuso,query.idTable)
            cont=0
            while cont < numcolumnas:
                col = ts.obtenersinNombreColumna(query.idTable,h.bd_enuso,cont)
                if col.nombre == query.condColumna.exp1.id:
                    temp = len(col.valor)
                    contval = 0
                    while contval < temp:
                        if col.valor == None:
                            print("Tabla vacia")
                            return
                        else:
                            if col.valor[contval] == query.condColumna.exp2.id:
                                ts.eliminarRegistroTabla(h.bd_enuso,query.idTable,contval)
                                h.textosalida+="TYTUS>> Registro eliminado en la tabla "+query.idTable+" que cumple la condicion de la columna"+str(query.condColumna.exp2.id)+"\n"
                                h.textosalida+="TYTUS>>\n"
                                return
                        contval=contval+1     
        elif isinstance(query.condColumna.exp1,ExpresionIdentificador) and isinstance(query.condColumna.exp2,operacionDelete):
            print("condicion con and")
            numcolumnas = ts.numerodeColumnas(h.bd_enuso,query.idTable)
            id1 = query.condColumna.exp1.id
            id2 = query.condColumna.exp2.exp1.exp2.id
            val1 = query.condColumna.exp2.exp1.exp1.id
            val2 = query.condColumna.exp2.exp2.id

            col1= ts.obtenerconNombreColumna(id1,h.bd_enuso,query.idTable)
            col2= ts.obtenerconNombreColumna(id2,h.bd_enuso,query.idTable)
            if col1 != None and col2 != None:
                temp1 = len(col1.valor)
                contval = 0
                while contval < temp1:
                    if col1.valor == None:
                        print("Tabla vacia")
                    else:
                        if col1.valor[contval] == val1 and col2.valor[contval] == val2:
                            ts.eliminarRegistroTabla(h.bd_enuso,query.idTable,contval)
                            h.textosalida+="TYTUS>> Registro eliminado tabla "+query.idTable+" con condiciones en las columnas "+str(id1)+" y "+str(id2)+"\n"
                            h.textosalida+="TYTUS>>\n"
                            return
                    contval=contval+1 

        
    else:
        print("Se eliminara el registro que cumple la siguiente condicion")
        print(query.condColumna.exp1.id," ",query.condColumna.operador,query.condColumna.exp2.id)
    #llamada de funcion

def procesar_createTale(query,ts):
    print("entra a Create table")
    print("entra al print con: ",query.idTable)
    idtab = query.idTable
    h.textosalida+="TYTUS>>Creando tabla\n"
    cantcol = 0

    if ts.validarTabla(query.idTable,h.bd_enuso) == 0:
        simbolo = TS.Simbolo(None,query.idTable,None,None,h.bd_enuso,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)
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
            
           
            if idtipo.upper() =="CHARACTER" or idtipo.upper() =="VARYING" or idtipo.upper()=="VARCHAR" or idtipo.upper()=="CHAR":
                idtamcad = i.objAtributo.TipoColumna.longitud
                #print(idtamcad) 
                if ts.verificarcolumnaBD(idcol,h.bd_enuso,idtab) == 0:
                    simbolo = TS.Simbolo(cantcol,idcol,idtipo,idtamcad,h.bd_enuso,idtab,1,0,0,None,None,0,None,0,None,None,None,None,None,None)
                    ts.agregarnuevaColumna(simbolo)
                    print("Se creo nueva columna :",idcol," a tabla: ",idtab)
                else:
                    print("columna: ",idcol," ya existe en tabla: ",idtab)

            elif idtipo.upper() == "DECIMAL" and i.objAtributo.TipoColumna.longitud != None:
                print("exactitud: ",i.objAtributo.TipoColumna.longitud)     
                idtamcad = i.objAtributo.TipoColumna.longitud
                if ts.verificarcolumnaBD(idcol,h.bd_enuso,idtab) == 0:
                    simbolo = TS.Simbolo(cantcol,idcol,idtipo,idtamcad,h.bd_enuso,idtab,1,0,0,None,None,0,None,0,None,None,None,None,None,None)
                    ts.agregarnuevaColumna(simbolo)
                    print("Se creo nueva columna :",idcol," a tabla: ",idtab)
                else:
                    print("columna: ",idcol," ya existe en tabla: ",idtab)

            else:
                if ts.verificarcolumnaBD(idcol,h.bd_enuso,idtab) == 0:
                    simbolo = TS.Simbolo(cantcol,idcol,idtipo,None,h.bd_enuso,idtab,1,0,0,None,None,0,None,0,None,None,None,None,None,None)
                    ts.agregarnuevaColumna(simbolo)
                    print("Se creo nueva columna :",idcol," a tabla: ",idtab)
                else:
                    print("columna: ",idcol," ya existe en tabla: ",idtab)
                    
            cantcol=cantcol+1
            #ts.printcontsimbolos()
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

            
            for res in i.objAtributo.RestriccionesCol:
                if res.typeR == OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY:
                    print("Restriccion: PRIMARY KEY")
                    pk = 1

                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.DEFAULT:
                    print("REstriccion: DEFAULT ")
                    print("Dato Default: ",res.objrestriccion.valor.id)
                    df = res.objrestriccion.valor.id

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
                    #print("Valor de check: ",res.objrestriccion.condCheck.exp1.id,res.objrestriccion.condCheck.operador,res.objrestriccion.condCheck.exp2.id)
                    chk = 1
                    condchk = res.objrestriccion.condCheck
                    #print(res.objrestriccion.condCheck)

                elif res.typeR == OPERACION_RESTRICCION_COLUMNA.CHECK_CONSTRAINT:
                    print("Restriccion: CONSTRAINT CHECK")
                    print("Id contraint: ",res.objrestriccion.idConstraint)
                    print("Valor de check: ",res.objrestriccion.condCheck.exp1.id,res.objrestriccion.condCheck.operador,res.objrestriccion.condCheck.exp2.id)
                    chk = 1
                    idconscheck = res.objrestriccion.idConstraint
                    condchk = res.objrestriccion.condCheck

                else:
                    print("No se encontro ninguna restriccion")
        

            if idtipo.upper()=="CHARACTER" or idtipo.upper()=="VARYING" or idtipo.upper()=="VARCHAR" or idtipo.upper()=="CHAR":
                idtamcad = i.objAtributo.TipoColumna.longitud 
                if ts.verificarcolumnaBD(idcol,h.bd_enuso,idtab) == 0:
                    simbolo = TS.Simbolo(cantcol,idcol,idtipo,idtamcad,h.bd_enuso,idtab,obl,pk,0,None,None,unq,idconsuniq,chk,condchk,idconscheck,None,df,None,None)
                    ts.agregarnuevaColumna(simbolo)
                    print("Se creo nueva columna :",idcol," a tabla: ",idtab)
                else:
                    print("columna: ",idcol," ya existe en tabla: ",idtab)
                   
            else:
                idtamcad = i.objAtributo.TipoColumna.longitud
                if ts.verificarcolumnaBD(idcol,h.bd_enuso,idtab) == 0:
                    simbolo = TS.Simbolo(cantcol,idcol,idtipo,None,h.bd_enuso,idtab,obl,pk,0,None,None,unq,idconsuniq,chk,condchk,idconscheck,None,df,None,None)
                    ts.agregarnuevaColumna(simbolo)
                    print("Se creo nueva columna :",idcol," a tabla: ",idtab)
                else:
                    print("columna: ",idcol," ya existe en tabla: ",idtab)

            cantcol=cantcol+1
            #ts.printcontsimbolos()

    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.UNIQUE_ATRIBUTO:
            print("Declaracion de varias columnas UNIQUE")
            print("Lista de columnas: ")
            
            for lc in i.objAtributo.listColumn:
                print("id: ",lc.id)
                if ts.verificarcolumnaBD(idcol,h.bd_enuso,idtab) == 0:
                    print("La columna especificada no existe, no se creo restriccion unique")
                    h.errores+=  "<tr><td>N/A</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>La columna especificada no existe, no se creo restriccion unique</td></tr>\n"
                    return
                else:
                    ts.actualizauniqueColumna(lc.id,h.bd_enuso,idtab)
            #ts.printcontsimbolos()

    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.CHECK_CONSTRAINT:
            print("Declaracion de constraint check")
            print("Id constraint: ", i.objAtributo.idConstraint)
            print("Condicion check: ",i.objAtributo.condCheck.exp1.id, i.objAtributo.condCheck.operador, i.objAtributo.condCheck.exp2.id)
            if ts.verificarcolumnaBD(i.objAtributo.condCheck.exp1.id,h.bd_enuso,idtab) == 1:
                ts.actualizarcheckColumna(i.objAtributo.condCheck.exp1.id,h.bd_enuso,idtab,i.objAtributo.idConstraint,i.objAtributo.condCheck)
            else:
                print("La columna especificada no existe")
            #ts.printcontsimbolos()
                h.errores+=  "<tr><td>N/A</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>La columna especificada no existe</td></tr>\n"
            #ts.printcontsimbolos()

    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.CHECK_SIMPLE:
            print("Delaracion de check")
            print("Condicion check: ",i.objAtributo.condCheck.exp1.id, i.objAtributo.condCheck.operador, i.objAtributo.condCheck.exp2.id)
            if ts.verificarcolumnaBD(i.objAtributo.condCheck.exp1.id,h.bd_enuso,idtab) == 1:
                ts.actualizarcheckColumna(i.objAtributo.condCheck.exp1.id,h.bd_enuso,idtab,None,i.objAtributo.condCheck)
            else:
                print("La columna especificada no existe")
                h.errores+=  "<tr><td>N/A</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>La columna especificada no existe</td></tr>\n"
            #ts.printcontsimbolos()
    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY:
            print("Declaracion de una o varias PRIMARY KEY")
            print("Lista de columnas: ")
            for lc in i.objAtributo.listColumn:
                print("id: ",lc.id)
                if ts.verificarcolumnaBD(lc.id,h.bd_enuso,idtab) == 1:
                    ts.actualizapkcolumna(lc.id,h.bd_enuso,idtab)
                    print("se actualizo llave primaria en: ",lc.id)
                else:
                    print("La columna especificada no existe, no se creo llave primaria")
                    h.errores+=  "<tr><td>N/A</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>La columna especificada no existe, no se creo llave primaria</td></tr>\n"

            #ts.printcontsimbolos()

    # -------------------------------------------------------------------------------------------------------------- 
        elif i.TypeAtrib == OPERACION_RESTRICCION_COLUMNA.FOREIGN_KEY:
            print("Declaracion de FOREIGN KEY")
            print("Lista de ID FOREING KEY")
            contidfor = len(i.objAtributo.idForanea)
            contidref = len(i.objAtributo.idLlaveF)
            conttemp = 0
            while conttemp < contidfor:
                if ts.verificarcolumnaBD(i.objAtributo.idLlaveF[conttemp].id,h.bd_enuso,i.objAtributo.idTable) == 1:
                    if ts.verificarcolumnaBD(i.objAtributo.idForanea[conttemp].id,h.bd_enuso,idtab)==1:
                        ts.actualizafkcolumna(i.objAtributo.idForanea[conttemp].id,h.bd_enuso,idtab,i.objAtributo.idLlaveF[conttemp],i.objAtributo.idTable)
                    else:
                        print("la columna especificada no existe para crear llave foranea")
                        h.errores+=  "<tr><td>N/A</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>la columna especificada no existe para crear llave foranea</td></tr>\n"
                else:
                    print("la columna referenciada en la tabla no existe")
                    h.errores+=  "<tr><td>N/A</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>la columna referenciada en la tabla no existe</td></tr>\n"
                conttemp = conttemp+1
            #ts.printcontsimbolos()
    # -------------------------------------------------------------------------------------------------------------- 
        else:
            print("No se encontraron columnas a crear")
            h.errores+=  "<tr><td>N/A</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>No se encontraron columnas a crear</td></tr>\n"

    print("----------se creara en storage------------")
    print("Base de datos: ",h.bd_enuso)
    print("Tabla: ",query.idTable)
    print("Cantidad de columnas: ",cantcol)
    h.textosalida+="TYTUS>> "+"\n"
    h.textosalida+="TYTUS>> "+"\n"
    h.textosalida+="TYTUS>> Se creo Tabla:        "+str(query.idTable)+"\n"
    h.textosalida+="TYTUS>> Base de datos usada:  "+str(h.bd_enuso)+"\n"
    h.textosalida+="TYTUS>> Cantidad de columnas: "+str(cantcol)+"\n"
    print(ts.columnasPrimaria(h.bd_enuso,query.idTable))
    #store.createDatabase(h.bd_enuso)
    #store.createTable(h.bd_enuso,query.idTable,cantcol+1)



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
    #print("voy a imprimir los valores del drop :v")
    #print("aqui viene el id de la tabla a dropear:",query.id)
    #h.textosalida+="TYTUS>> Eliminaré la tabla"+query.id+"\n"
    nombreTab = query.id
    xd = ts.obtenerColumnas(nombreTab,h.bd_enuso)
    print("TOTAL DE COLUMNAS")
    print(len(xd))
    for x in range(0,len(xd)):
        ts.destruirColumna(xd[x],h.bd_enuso,nombreTab)
        print (xd[x])
    xdd = ts.destruirTabla(nombreTab,h.bd_enuso)


def alter_table(query,ts):
    print("voy a imprimir los valores del alter :v")
    print("aqui viene el id de la tabla a cambiar:",query.id)
    h.textosalida+="TYTUS>> Alteraré la tabla"+query.id+"\n"
    temp = query.querys.tipo #TIPO DE OBJETO
    if(temp.upper()=="ADD"):
        contenido = query.querys.contenido #AQUI ESTA EL CONTENIDO DEL ADD - contAdd
        tablatemp = query.id #AQUI ESTA EL NOMBRE DE LA TABLA A ALTERAR
        if contenido.tipo.upper()=="COLUMN":
            print("ESTA ES MI TABLA-->: ",tablatemp)
            columnaNew = contenido.id1
            print("SE AGREGARA UNA COLUMNA")
            #la cadena a buscar sería query.id + baseactual
            #por el momento tengo quemada la BD1 al final del nombre de la tabla
            #resNum = ts.verificarcolumnaBD(columnaNew,"BD1",tablatemp)
            res = ts.verificarcolumnaBDAT(columnaNew,h.bd_enuso,tablatemp)
            if res!=0:
                print("ENCONTRE LA #$%& COLUMNA :V, YA ESTABA CREADA")
                """x = res.valor
                if x!=None:
                    #NO PUEDO CAMBIAR EL TIPO PORQUE YA HAY VALORES ASOCIADOS A LA COLUMNA
                    print("NO PUEDO CAMBIAR EL TIPO DE LA COLUMNA PORQUE YA TIENE VALORES ASOCIADOS")
                else:
                    #PUEDO CAMBIAR EL TIPO PORQUE NO HAY VALORES TODAVÍA
                    if contenido.tipo2.id.upper()=='VARCHAR': #VIENE UN VARCHAR
                        print("ESTE ES EL TAMAÑO QUE TRAE-->: ",contenido.tipo2.longitud)
                        res.tipo = contenido.tipo2.id
                        res.tamanoCadena = contenido.tipo2.logitud
                        ts.printcontsimbolos()
                    else:
                        #VIENE OTRO TIPO QUE NO SE VARCHAR
                        res.tipo = contenido.tipo2.id
                        ts.printcontsimbolos()"""
                #CODIGO ALTER TYPE ------------------------------------------
                
                #TERMINA CODIGO ALTER TYPE ----------------------------------
            else:#NO ESTA CREADA LA COLUMNA
                print("NO ENCONTRE LA $#%& columna")
                tempTab = ts.obtener2(tablatemp+h.bd_enuso)
                if tempTab == 0:
                    print("NO EXISSTE LA TABLA, NO PUEDO CREAR LA COLUMNA, F!!")
                else:
                    print("EXISTE LA TABLA, PUEDO CREAR LA COLUMNAAAA")
                    #debo contar que id le toca
# id, nombre, tipo, tamanoCadena, BD, tabla, obligatorio, pk, FK, referenciaTablaFK, referenciaCampoFK, unique, idUnique, check, condicionCheck, idCheck,valor,default)
                    if contenido.tipo2.id.upper()=="VARCHAR":
                        print("ES UN VARCHARRRRRRRRRRRRRRRRR")
                        print(contenido.tipo2.id)
                        print(contenido.id1)
                        print(contenido.tipo2.longitud)
                        print(tablatemp)
                        idNueva = ts.numerodeColumnas(h.bd_enuso,tablatemp)
                        print("AQUI VIENE ID NUEVA ---::>> ",idNueva)
                        ahora = TS.Simbolo(idNueva,contenido.id1,contenido.tipo2.id,contenido.tipo2.longitud,h.bd_enuso,tablatemp,0,0,None,None,None,None,None,None,None,None,None,None,None,None)
                        print("xd")
                        ts.agregarnuevaColumna(ahora)
                        ts.printcontsimbolos()
                    else:
                        print("POR ACÁ CREO")
                        idNueva = ts.numerodeColumnas(h.bd_enuso,tablatemp)
                        ahora = TS.Simbolo(idNueva,contenido.id1,contenido.tipo2.id,None,h.bd_enuso,tablatemp,0,0,None,None,None,None,None,None,None,None,None,None,None,None)
                        ts.agregarnuevaColumna(ahora)
                        ts.printcontsimbolos()              
            #METODO PARA ALTERAR LA COLUMNA
            #h.bde_nuso
            #alterAddColumn(baseActual,contenido.id1,anyxd)
        elif contenido.tipo.upper()=="CHECK":
            print("SE AGREGARA UN CHECK")
            operacion = contenido.operacion
            id1byron = contenido.operacion.exp1.id
            print("exp1: ",id1byron)
            id2byron = contenido.operacion.exp2.id
            print("exp2: ",id2byron)
            ans = ts.actualizarcheckColumna(id1byron,h.bd_enuso,tablatemp,None,operacion)
            ans = ts.actualizarcheckColumna(id2byron,h.bd_enuso,tablatemp,None,operacion)
            '''if not id1byron.isnumeric():
                ans = ts.actualizarcheckColumna(id1byron,h.bd_enuso,tablatemp,None,operacion)
            else:
                ans = ts.actualizarcheckColumna(id2byron,h.bd_enuso,tablatemp,None,operacion)
            '''
        
        elif contenido.tipo.upper()=="FOREIGN":
            #print("SE AGREGARA UNA LLAVE FORANEA")
            #nombre,BD,tabla,idrefcolumna,idreftabla
            #print(query.querys.contenido.id1)
            contenidox = query.querys.contenido
            tabla = query.id
            #print("nuevamente jejeje: ",contenidox.id1)
            #print("nuevamente jejeje: ",contenidox.id2)
            #print(query.id)
            res = ts.actualizafkcolumna(contenidox.id1,h.bd_enuso,tabla,contenidox.id2,None)
        elif contenido.tipo.upper()=="PRIMARY":
            #print("SE AGREGARA UNA LLAVE PRIMARIA")
            contenidox = query.querys.contenido
            tabla = query.id
            res = ts.actualizapkcolumna(contenidox.id1,h.bd_enuso,tabla)
        elif contenido.tipo.upper()=="CONSTRAINT":
            print("SE VIENE UN CONSTRAINT")
            if contenido.tipo2.upper()=="FOREIGN":
                print("Y DENTRO VIENE UNA LLAVE FORANEA")
                contenidox = query.querys.contenido
                tabla = query.id
                idConstraint = contenidox.id1
                print(tabla)
                print(idConstraint)
                print(contenidox.id3)
                print(contenidox.id4)
                res = ts.actualizafkcolumnaAT(contenidox.id2,h.bd_enuso,tabla,contenidox.id3,contenidox.id4,idConstraint)
            elif contenido.tipo2.upper()=="PRIMARY":
                print("Y DENTRO VIENE UNA LLAVE PRIMARIA")
                contenidox = query.querys.contenido
                tabla = query.id
                idConstraint = contenidox.id1
                nombre = contenidox.id2
                print(tabla)
                print(idConstraint)
                print(nombre)
                res = ts.actualizapkcolumnaAT(nombre,h.bd_enuso,tabla,idConstraint)
            elif contenido.tipo2.upper()=="UNIQUE":
                print("Y DENTRO VIENE UN UNIQUE")
                contenidox = query.querys.contenido
                tabla = query.id
                idConstraint = contenidox.id1
                nombre = contenidox.operacion
                print(tabla)
                print(idConstraint)
                print(nombre)
                rs = ts.actualizauniqueColumnaAT(nombre,h.bd_enuso,tabla,idConstraint)
        #print("VIENE UN ADD, POR TANTO SE AGREGA ALGO A LA TABLA")
        #print("SE AGREGARÁ UNA: ", query.querys.contenido.tipo)
        #print("DE NOMBRE: ",query.querys.contenido.id1)
        #print("DE TIPO: ", query.querys.contenido.tipo2)
    elif(temp.upper()=="DROP"):
        print("VIENE UN DROP, ALGO DE LA TABLA VA A EXPLOTAR, F")
        contenido = query.querys.contenido #AQUI ESTA EL CONTENIDO DEL DROP - contDrop
        if contenido.tipo.upper() == "COLUMN":
            print("DROPEARÉ UNA COLUMNA: ",contenido.id)
            contenidox = query.querys.contenido
            nombreTab = query.id
            nombreCol = contenidox.id
            print(nombreTab)
            print(nombreCol)
            print(nombreCol+h.bd_enuso+nombreTab)
            #simbTemp = ts.obtener2(nombreCol+h.bd_enuso+nombreTab)
            xd = ts.destruirColumna(nombreCol,h.bd_enuso,nombreTab)
            #AQUI VA EL CODIGO DE LA REASIGNACIÓN DE IDS A LAS TABLAS RESTANTES
            xd = ts.obtenerColumnas(nombreTab,h.bd_enuso)
            print("TOTAL DE COLUMNAS")
            print(len(xd))
            for x in range(0,len(xd)):
                tempCambioid = ts.verificarcolumnaBDAT(xd[x],h.bd_enuso,nombreTab)
                print("ESTA ES LA COLUMNA QUE ESTOY USANDO AHORITA --> ",tempCambioid.nombre)
                print("ESTE ES EL ID ANTERIOR--> ",tempCambioid.id)
                tempCambioid.id = x
                print("ESTE ES EL NUEVO ID ----> ",tempCambioid.id)
            '''
            nombreTab = query.id
            xd = ts.obtenerColumnas(nombreTab,h.bd_enuso)
            print("TOTAL DE COLUMNAS")
            print(len(xd))
            for x in range(0,len(xd)):
            ts.destruirColumna(xd[x],h.bd_enuso,nombreTab)
            print (xd[x])
            xdd = ts.destruirTabla(nombreTab,h.bd_enuso)
            '''
        else:
            print("DROPEARÉ UNA CONSTRAINT: ",contenido.id)
            print("LO QUE EXPLOTARA SERA: ", contenido.tipo)
            idConstraint = contenido.id
            tabla = query.id
            print(idConstraint)
            print(tabla)
            xd = ts.destruirConstraint(idConstraint,h.bd_enuso,tabla)

    elif(temp.upper()=="ALTER"):
        print("VIENE UN ALTER DENTRO DE OTRO ALTER")
        contenido = query.querys.contenido
        if contenido.tipo.upper()=="SET":
            print("ES UN SET")
            print(contenido.tipoAsignar)
            if contenido.tipoAsignar.upper()=="NOT":
                print("ES UN NOT NULL")
                #nuevotipo = contenido.tipoAsignar.id
                tabla = query.id
                res = ts.verificarcolumnaBDAT(contenido.id,h.bd_enuso,tabla)
                if res!=0:
                    print("ENCONTRE LA COLUMNA")
                    if res.valor!=None:
                        print("YA HAY VALORES ASIGNADOS, NO SE PUEDE CAMBIAR EL TIPO AHORA")
                    else:
                        print("NO HAY VALORES, SE PUEDE CAMBIAR EL TIPO")
                        res.obligatorio = 0
            else:
                print("VAMOS A SETEAR EL VALOR DE LA COLUMNA A NULL")
                res = ts.verificarcolumnaBDAT(contenido.id,h.bd_enuso,tabla)
                if res!=0:
                    print("ENCONTRE LA COLUMNA")
                    if res.valor!=None:
                        print("YA HAY VALORES ASIGNADOS, NO SE PUEDE CAMBIAR EL TIPO AHORA")
                    else:
                        print("NO HAY VALORES, SE PUEDE CAMBIAR EL TIPO")
                        res.obligatorio = 1
        elif contenido.tipo.upper()=="TYPE":
            print("SE LE ASIGNARA UN VALOR DIFERENTE A NULL Y NOT NULL, ESTE ES : ", contenido.tipoAsignar.id)
            nuevotipo = contenido.tipoAsignar.id
            tabla = query.id
            res = ts.verificarcolumnaBDAT(contenido.id,h.bd_enuso,tabla)
            if res !=0:
                print("encontre la columna")
                if res.valor!=None:
                    print("YA HAY VALORES ASIGNADOS, NO SE PUEDE CAMBIAR EL TIPO AHORA")
                else:
                    print("NO HAY VALORES, PUEDO CAMBIAR EL TIPO")
                    if nuevotipo.upper()=="VARCHAR":
                            longitud = contenido.tipoAsignar.longitud
                            res.tipo = nuevotipo
                            res.tamanoCadena = longitud
                    else:
                            res.tipo = nuevotipo
            else:
                print("NO SE ENCONTRÓ LA TABLA, F")
                

            #print("ESTE ES EL TIPO NUEVO-->: ",contenido.tipo2.id)
                #if contenido.tipo2.id.upper()=='VARCHAR': #VIENE UN VARCHAR
                #    print("ESTE ES EL TAMAÑO QUE TRAE-->: ",contenido.tipo2.longitud)
                #    res.tipo = contenido.tipo2.id
                #    res.tamanoCadena = contenido.tipo2.logitud
                #    ts.printcontsimbolos()
                #else:#VIENE OTRO TIPO QUE NO SE VARCHAR
                #    res.tipo = contenido.tipo2.id
                #    ts.printcontsimbolos()


        

    

# ---------------------------------------------------------------------------------------------------------------------
#                                 EJECUCION DE LOS QUERIES PRINCIPALES
# ---------------------------------------------------------------------------------------------------------------------
def procesar_queries(queries, ts) :
    ## lista de instrucciones recolectadas
    
    print("Entra a procesar queries",queries)
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
        elif isinstance(query, Create_Replace_Databases_IFwithParameters) : procesar_createwithparameters_replace_if_db(query, ts)
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
        elif isinstance(query, Tipo) : procesar_tipo(query, ts)
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
        val+="<td>"+str(ts_global.simbolos[simbolo].idConstraintFK)+"</td>"
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
    if tipo.upper() == 'INTEGER':
        try:
            if -2147483648 < valor and valor < 2147483648:
                return True
            else:
                print("El valor ingresado supera la longitud permitida para INTEGER")
                return False
        except:
            print("El dato no es valido para tipo INTEGER")
            return False

    elif tipo.upper() == 'SMALLINT':
        try:
            if -2147483648 < valor and valor < 2147483648:
                return True
            else:
                print("El valor ingresado supera la lingitud permitida para SMALLINT")
                return False
        except:
            print("El dato no se valido para tipo SMALLINT")
            return False

    elif tipo.upper() == 'BIGINT':
        try:
            if -9223372036854775808 < valor and valor < 9223372036854775807:
                return True
            else:
                print("El valor ingresado supera la longitud permitida para BIGING")
                return False
        except:
            print("El dato no es valido para tipo BEGINT")
            return False

    elif tipo.upper() == "DECIMAL":
        try:
            if tam != None:
                exact = tam.split(",")
                form = "{0:."+str(exact[1])+"f}"
                numero = form.format(valor)
                temp = str(numero)
                num = temp.split(".")
                entero = len(num[0])
                decimal = len(num[1])
            
                if int(exact[0]) >= entero and int(exact[1]) >= decimal:
                    return True
                else:
                    print("El valor ingresado no cumple como Decimal")
                    return False
            else:
                if type(valor) is int:
                    numero = float(valor)
                    temp = str(numero)
                    num = temp.split(".")
                    entero = len(num[0])
                    dec = len(num[1])
            
                    if 131072 > entero and 16383 > dec:
                        return True
                    else:
                        print("El valor ingresado no cumple como Decimal")
                        return False
                elif type(valor) is float:
                    temp = str(valor)
                    num = temp.split(".")
                    entero = len(num[0])
                    dec = len(num[1])
            
                    if 131072 > entero and 16383 > dec:
                        return True
                    else:
                        print("El valor ingresado no cumple como Decimal")
                        return False

        except:
            print("El dato no es valido para tipo DECIMAL")
            return False

    elif tipo.upper() == "NUMERIC":
        try:
            temp = str(valor)
            num = temp.split(".")
            entero = len(num[0])
            decimal = len(num[1])
            if(131072 > entero and 16383 > decimal):
                return True
            else:
                print("El valor ingresado no cumple como NUMERIC")
                return False
        except:
            print("El dato no es valido para tipo NUMERIC")
            return False

    elif tipo.upper() == "REAL":
        try:
            temp = str(valor)
            num = temp.split(".")
            decimal = len(num[1])
            if decimal <= 6:
                return True
            else:
                print("El valor ingresado tiene mas de 6 decimales")
                return False
        except:
            print("El dato no es valido para tipo REAL")
            return False

    elif tipo.upper() == "DOUBLE":
        try:
            temp = str(valor)
            num = temp.split(".")
            decimal = len(num[1])
            if(decimal <= 15):
                return True
            else:
                print("El valor ingresado tiene mas de 15 decimales")
                return False
        except:
            print("El dato no es valido para tipo DOUBLE")
            return False

    elif tipo.upper() == "MONEY":
        try:
            if type(valor) is str:
                x = valor.replace(',','')
                "{:0,.2f}".format(float(x))
                return True
            elif type(valor) is int:
                y = float(valor)
                "{:0,.2f}".format(float(y))
                return True
            elif type(valor) is float:
                "{:0,.2f}".format(float(valor))
                return True

        except:
            print("El dato no es valido para tipo MONEY")
            return False

    elif tipo.upper() == "VARYING":
        try:
            if type(valor) is str :
                tamcad = len(valor)
                if tamcad > 0 and tamcad <= tam:
                    return True
                else:
                    print("La cadena ingresada supera el limite del CHARETECTER VARYING definido")
                    return False
            else:
                print("El valor ingresado no es una cadena")
                return False
        except:
            print("El dato no es valido para tipo CHARACTER VARING")

    elif tipo.upper() == "VARCHAR":
        try:
            if type(valor) is str :
                tamcad = len(valor)
                if tamcad > 0 and tamcad <= tam:
                    return True
                else:
                    print("La cadena ingresada supera el limite del VARCHAR definido")
                    return False
            else:
                print("El valor ingresado no es una cadena")
        except:
            print("El dato no es valido para tipo VARCHAR")

    elif tipo.upper() == "CHARACTER":
        try:
            if type(valor) is str :
                tamcad = len(valor)
                if tamcad > 0 and tamcad <= tam:
                    return True
                else:
                    print("La cadena ingresada supera el limite del CHARETECTER definido")
                    return False
            else:
                print("El valor ingresado no es una cadena")
        except:
            print("El dato no es valido para tipo CHARACTER")

    elif tipo.upper() == "CHAR":
        try:
            if type(valor) is str :
                tamcad = len(valor)
                if tamcad > 0 and tamcad <= tam:
                    return True
                else:
                    print("La cadena ingresada supera el limite del CHAR definido")
                    return False
            else:
                print("El valor ingresado no es una cadena")
        except:
            print("El dato no es valido para tipo CHAR")

    elif tipo.upper() == "TEXT":
        try:
            if type(valor) is str:
                return True
        except:
            print("El valor ingresado no es valido para tipo TEXT")

    elif tipo.upper() == "TIMESTAMP":
        date_format = '%Y-%m-%d %H:%M:%S'
        try:
            if datetime.datetime.strptime(valor,date_format):
                return True
        except:
            print("La fecha y hora ingresada es invalida")
            return False

    elif tipo.upper() == "TIME":
        date_format = '%H:%M:%S'
        try:
            if datetime.datetime.strptime(valor,date_format):
                return True
        except:
            print("La hora ingresada es invalida")
            return False

    elif tipo.upper() == "DATE":
        date_format = '%Y-%m-%d'
        try:
            if datetime.datetime.strptime(valor,date_format):
                return True
        except:
            print("La fecha ingresada es invalida")
            return False

    elif tipo.upper() == "BOOLEAN":
        try:
            if valor.upper() == 'TRUE' or valor.upper() == 'FALSE':
                return True
            return False
        except:
            print("El valor booleando no es valido")
            return False


def convertiraMoney(valor):
    try:
        if type(valor) is str:
            x = valor.replace(',','')
            respuesta = "{:0,.2f}".format(float(x))
            return respuesta
        elif type(valor) is int:
            y = float(valor)
            respuesta = "{:0,.2f}".format(float(y))
            return respuesta
        elif type(valor) is float:
            respuesta = "{:0,.2f}".format(float(valor))
            return respuesta

    except:
        print("El dato no es valido para tipo MONEY")
        return False



def procesar_tipo(query,ts):
    
    try:
        print("llega al metodo del type")
        print(query.operacion1.id)
        print(query.operacion2)
        a=procesar_retorno_lista_valores(query.operacion2,ts)
        print(a)
        simbolo = TS.Simbolo(None,query.operacion1.id,None,None,h.bd_enuso,None,None,None,None,None,None,None,None,None,None,None, a,None,None,None)      # inicializamos con 0 como valor por defecto
        ts.agregar(simbolo)
        h.textosalida+="TYTUS>> se creo el TYPE:  "+query.operacion1.id+"\n"
    except:
        h.errores+=  "<tr><td>"+str(query.operacion1.id)+ "</td><td>N/A</td><td>N/A</td><td>SEMANTICO</td><td>Se genero un error en la creacion</td></tr>\n"  
        h.textosalida+="TYTUS>> Se genero un error en la creacion del type\n"
