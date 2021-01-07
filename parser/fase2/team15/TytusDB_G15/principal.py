import gramatica as g
import ts_index as TSINDEX
import ts as TS
import tc as TC
from expresiones import *
from instrucciones import *
from graphviz import Digraph
from report_ast import *
from report_tc import *
from report_ts import *
from report_errores import *

import datetime
import math
import random
import mpmath
import hashlib
from operator import itemgetter
import base64
import binascii
import re
import hashlib
from prettytable import PrettyTable

from storageManager import jsonMode as j

salida = ""
useCurrentDatabase = ""
pks = []

def toPretty(arr):
    x = PrettyTable()
    x.field_names = arr[0]
    if len(arr) > 1:
        i = 1
        while i < len(arr):
            x.add_row(arr[i])
            i+=1 
    
    return str(x)

def procesar_createTable(instr,ts,tc) :
    global pks
    columns = []
    numC = 0
    i = 0
    if instr.instrucciones != []:
        
        global salida
        for ins in instr.instrucciones:
            if instr.herencia != None:
                columnsH = tc.obtenerColumns(useCurrentDatabase,instr.herencia)
                numC = len(columnsH)
                #ACTUALIZAR NUM TABLA
                '''temp1 = ts.obtener(instr.val,useCurrentDatabase)
                temp2 = TS.Simbolo(temp1.val,temp1.tipo,temp1.valor+numC,temp1.ambito)
                ts.actualizarTableNum(temp2,instr.val,useCurrentDatabase)'''
                if columnsH != []:
                    for col in columnsH:
                        typeC = tc.obtenerReturn(useCurrentDatabase,instr.herencia,col)
                        newType = TC.Tipo(typeC.database,instr.val,typeC.val,typeC.tipo,typeC.tamanio,typeC.referencia,typeC.tablaRef,[])
                        if typeC != False:
                            tc.agregar(newType) 
            if isinstance(ins, Definicion_Columnas): 
                i+=1
                columns.append(i)
                procesar_Definicion(ins,ts,tc,instr.val)
            elif isinstance(ins, LLave_Primaria): 
                procesar_primaria(ins,ts,tc,instr.val)
            elif isinstance(ins, Definicon_Foranea): 
                procesar_Foranea(ins,ts,tc,instr.val)
            elif isinstance(ins, Lista_Parametros): 
                procesar_listaId(ins,ts,tc,instr.val)
            elif isinstance(ins, definicion_constraint): 
                procesar_constraint(ins,ts,tc,instr.val)
    
        

    

    try:
        #print(str(useCurrentDatabase),str(instr.val),int(len(columns)))
        result = j.createTable(str(useCurrentDatabase),str(instr.val),int(len(columns))+numC)
        if result == 0:
            salida = "\nCREATE TABLE"
            temp1 = TS.Simbolo(str(instr.val),'Table',int(len(columns)+numC),str(useCurrentDatabase))
            ts.agregar(temp1)
        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + useCurrentDatabase +"\" does not exist \nSQL state: 3D000"
        elif result == 3 :
            salida = "\nERROR:  relation \"" + str(instr.val) +"\" alredy exists\nSQL state: 42P07"
    except :
        pass

    try:
        #print(pks)
        result = j.alterAddPK(str(useCurrentDatabase),str(instr.val),pks)
        pks = []
        #print(pks)

    except :
        pass

    

            
def procesar_Definicion(instr,ts,tc,tabla) :
    tipo_dato = ""
    tamanio = ""
    if(isinstance(instr.tipo_datos,Etiqueta_tipo)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio = ""
    elif(isinstance(instr.tipo_datos,ExpresionNumero)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio = instr.tipo_datos.val
    elif(isinstance(instr.tipo_datos,Etiqueta_Interval)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio = instr.tipo_datos.ext_time
    elif(isinstance(instr.tipo_datos,ExpresionTiempo)):
        tipo_dato = instr.tipo_datos.operador
        tamanio =  ""
    elif(isinstance(instr.tipo_datos,Expresion_Caracter)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio =  instr.val
    
    if instr.opciones_constraint == None:
        buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.val)
        if buscar == False:
            tipo = TC.Tipo(useCurrentDatabase,tabla,instr.val,tipo_dato,tamanio,"","",[])
            tc.agregar(tipo)
        else:
            nada = 1
            
    else:
        buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.val)
        if buscar == False:
            tipo = TC.Tipo(useCurrentDatabase,tabla,instr.val,tipo_dato,tamanio,"","",[])
            tc.agregar(tipo)
        else:
            nada = 1
            
        for ins in instr.opciones_constraint:
            if isinstance(ins, definicion_constraint): 
                procesar_constraintDefinicion(ins,ts,tc,tabla,instr.val)

        

        
    
def procesar_constraintDefinicion(instr,ts,tc,tabla,id_column):
    #print(tabla,id,instr.val,instr.tipo)
    global pks
    if instr.val == None:
        if instr.tipo == OPCIONES_CONSTRAINT.NOT_NULL:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                nada = 1
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.NOT_NULL)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.NULL:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                nada = 1
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.NULL)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.PRIMARY:
            pk = []
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                nada = 1
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.PRIMARY)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
                pos = tc.getPos(useCurrentDatabase,tabla,id_column)
                pk.append(pos)
                
            pks = pk
                
            


        elif instr.tipo == OPCIONES_CONSTRAINT.FOREIGN:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                nada = 1
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.UNIQUE:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                nada = 1
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.DEFAULT:
            if instr.opciones_constraint != []:
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
                if buscar == False:
                    nada = 1
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.DEFAULT)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.CHECK:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                nada = 1
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.CHECK)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)

    else:
        if instr.tipo == OPCIONES_CONSTRAINT.UNIQUE:
            if instr.opciones_constraint == None:
                temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
                ts.agregar(temp)
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
                if buscar == False:
                    nada = 1
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.CHECK:
            if instr.opciones_constraint != None:
                temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
                ts.agregar(temp)
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
                if buscar == False:
                    nada = 1
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
    

def procesar_listaId(instr,ts,tc,tabla):
    if instr.identificadores != []:
        for ids in instr.identificadores:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.val)
            if buscar == False:
                nada = 1
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                tipo = TC.Tipo(useCurrentDatabase,tabla,ids.val,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,ids.val)

def procesar_primaria(instr,ts,tc,tabla):
    global pks
    pk = []
    for ids in instr.val:
        buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.val)
        if buscar == False:
            nada = 1
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.PRIMARY)
            tipo = TC.Tipo(useCurrentDatabase,tabla,ids.val,buscar.tipo,buscar.tamanio,"","",tempA)
            tc.actualizar(tipo,useCurrentDatabase,tabla,ids.val)
            
            pos = tc.getPos(useCurrentDatabase,tabla,ids.val)
            pk.append(pos)

    pks = pk

def procesar_Foranea(instr,ts,tc,tabla):
    buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.nombre_tabla)
    if buscar == False:
        nada = 1
    else:
        tempA = buscar.listaCons
        tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
        tipo = TC.Tipo(useCurrentDatabase,tabla,instr.nombre_tabla,buscar.tipo,buscar.tamanio,instr.campo_referencia,instr.referencia_tabla,tempA)
        tc.actualizar(tipo,useCurrentDatabase,tabla,instr.nombre_tabla)

def procesar_constraint(instr,ts,tc,tabla):
    if instr.tipo == 'UNIQUE':
        if instr.opciones_constraint != []:
            temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
            ts.agregar(temp)
            for ids in instr.opciones_constraint:
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.val)
                if buscar == False:
                    nada = 1
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,ids.val,buscar.tipo,buscar.tamanio,ids,instr.referencia,tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,ids.val)
                
    elif instr.tipo == 'FOREIGN':
        if instr.opciones_constraint != []:
            temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
            ts.agregar(temp)
            for ids in instr.opciones_constraint:
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.columna)
                if buscar == False:
                    nada = 1
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,instr.columna,buscar.tipo,buscar.tamanio,ids,instr.referencia,tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,instr.columna)

    elif instr.tipo == 'CHECK':
        if instr.opciones_constraint != []:
            temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
            ts.agregar(temp)
            for ids in instr.opciones_constraint:
                if type(ids.exp1) == ExpresionIdentificador:
                    buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.exp1.val)
                    if buscar == False:
                        nada = 1
                    else:
                        tempA = buscar.listaCons
                        tempA.append(OPCIONES_CONSTRAINT.CHECK)
                        tipo = TC.Tipo(useCurrentDatabase,tabla,ids.exp1.val,buscar.tipo,buscar.tamanio,"","",tempA)
                        tc.actualizar(tipo,useCurrentDatabase,tabla,ids.exp1.val)
                else: 
                    buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.exp2.val)
                    if buscar == False:
                        nada = 1
                    else:
                        tempA = buscar.listaCons
                        tempA.append(OPCIONES_CONSTRAINT.CHECK)
                        tipo = TC.Tipo(useCurrentDatabase,tabla,ids.exp2.val,buscar.tipo,buscar.tamanio,"","",tempA)
                        tc.actualizar(tipo,useCurrentDatabase,tabla,ids.exp2.val)
    
def procesar_check(instr,ts,tc):
    nada = 1

def procesar_Expresion_Relacional(instr,ts,tc):
    nada = 1

def procesar_Expresion_Binaria(instr,ts,tc):
    nada = 1

def procesar_Expresion_logica(instr,ts,tc):
    nada = 1
    
def procesar_Expresion_Numerica(instr,ts,tc):
    nada = 1

def procesar_createDatabase(instr,ts,tc) :
    if instr.replace == 1:
        
        result = j.dropDatabase(str(instr.nombre.val))
        global salida
        if result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "

        result1 = j.createDatabase(str(instr.nombre.val))
        if result1 == 0:
            temp1 = TS.Simbolo(instr.nombre.val,'Database',0,"")
            ts.agregar(temp1)
            salida = "\nCREATE DATABASE"
            
        elif result1 == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
    else:
        result1 = j.createDatabase(str(instr.nombre.val))
        if result1 == 0:
            salida = "\nCREATE DATABASE"
            temp1 = TS.Simbolo(instr.nombre.val,'Database',0,"")
            ts.agregar(temp1)
        elif result1 == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result1 == 2 :
            salida = "\nERROR:  database \"" + str(instr.nombre.val) +"\" already exists \nSQL state: 42P04 "

def procesar_showDatabases(instr,ts,tc):
    global salida
    data = []
    dataTables = j.showDatabases()
    data.append(['databases'])
    for databases in dataTables:
        data.append([databases])
    if dataTables == []:
        salida = "\nERROR:  databases does not exist \nSQL state: 3D000"
    else:
        salida = toPretty(data)

def procesar_showTables(instr,ts,tc):
    global salida
    dataT = []
    dataTables = j.showTables(useCurrentDatabase)
    dataT.append(['tables'])
    for tables in dataTables:
        dataT.append([tables])
    if dataTables == []:
        salida = "\nERROR:  Tables does not exist \nSQL state: 3D000"
    else:
        salida = toPretty(dataT)

def procesar_dropDatabase(instr,ts,tc):
    global salida

    result = j.dropDatabase(str(instr.val.val))

    if instr.exists == 0:
        global salida
        if result == 0:
            global salida
            salida = "\nDROP DATABASE"
            ts.deleteDatabase(instr.val.val)
            tc.eliminarDatabase(instr.val.val)
        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + str(instr.val.val) +"\" does not exist \nSQL state: 3D000"
    else:
        if result == 0:
            salida = "\nDROP DATABASE"
        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + str(instr.val.val) +"\" does not exist, skipping DROP DATABASE"

def procesar_useDatabase(instr,ts,tc):
    #print(instr.val.val)
    global salida, useCurrentDatabase
    encontrado = False
    dataTables = j.showDatabases()
    for databases in dataTables:
        if databases == instr.val.val:
            encontrado = True
    
    if encontrado:
        global salida, useCurrentDatabase
        useCurrentDatabase = str(instr.val.val)
        salida = "\nYou are now connected to database  \"" + str(instr.val.val) +"\""
    else: 
        salida = "\nERROR:  database \"" + str(instr.val.val) +"\" does not exist \nSQL state: 3D000"
        useCurrentDatabase = ""
        
def procesar_alterdatabase(instr,ts,tc):
    global salida
    
    if isinstance(instr.tipo_id,ExpresionIdentificador) : 
        global salida
        nada = 1

    elif isinstance(instr.tipo_id, ExpresionComillaSimple) : 
        nada = 1
        
    else:
        result = j.alterDatabase(str(instr.id_tabla),str(instr.tipo_id))
        if result == 0:
            tipo = TC.Tipo(useCurrentDatabase,instr.id_tabla,instr.id_tabla,"",OPCIONES_CONSTRAINT.CHECK,None,None)
            tc.actualizarDatabase(tipo,instr.id_tabla,instr.tipo_id)
            temp1 = ts.obtener(instr.id_tabla,"")
            temp2 = TS.Simbolo(instr.tipo_id,temp1.tipo,temp1.valor,temp1.ambito)
            ts.actualizarDB(temp2,temp1.val)
            ts.actualizarDBTable(temp1.val,temp2.val)
            salida = "\nALTER DATABASE"            

        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + str(instr.id_tabla) +"\" does not exist \nSQL state: 3D000"
        elif result == 3 :
            salida = "\nERROR:  database \"" + str(instr.tipo_id) +"\" alredy exists\nSQL state: 42P04"

def procesar_update(instr,ts,tc):
    global salida
    arrayPK = []
    arrayFilter = []
    arrayColumnasIds = []
    columnas = tc.obtenerColumns(str(useCurrentDatabase),instr.identificador.val)
    iPk = 0
    for ic in columnas:
        get = tc.obtenerReturn(str(useCurrentDatabase),instr.identificador.val,ic)
        if get:
            for icons in get.listaCons:
                if icons == OPCIONES_CONSTRAINT.PRIMARY:
                    arrayPK.append(iPk)

        iPk += 1
    
    #print(arrayPK)
    for ii in instr.lista_update:
        arrayColumnasIds.append(ii.ids.val)

    #print(arrayColumnasIds)

    #WHERE
    columnsTable = tc.obtenerColumns(str(useCurrentDatabase),instr.identificador.val)
    resultArray = j.extractTable(str(useCurrentDatabase),str(instr.identificador.val))
    arrayWhere = resultArray
    arrayWhere.insert(0,columnsTable)   
    #print(resultArray)

    arrayFilter.append(arrayWhere[0])
    arrayupdateNum = []
    i = 1
    coli = 0
    while i < len(arrayWhere):
        arrayTS = []
        arrayTS.append(arrayWhere[0])
        arrayTS.append(arrayWhere[i])
        val = resolver_expresion_logica(instr.expresion.expresion,arrayTS)
        if val == 1:
            arrayFilter.append(arrayWhere[i])
            arrayupdateNum.append(coli)
        i+=1
        coli += 1
    
    #print(arrayupdateNum)

    arrayPosColumna = []
    iiPC = 0
    for iPC in columnas:
        for iPC2 in arrayColumnasIds:
            if iPC == iPC2:
                arrayPosColumna.append(iiPC)
        iiPC += 1

    #print(arrayPosColumna) #POS COLUMN
        
    valores = []
    idic = 1
    for parametros in instr.lista_update:
        if isinstance(parametros.expresion,Funcion_Exclusivas_insert):
            arrTC = []
            salidaR = resolver_expresion_aritmetica(parametros.expresion,arrTC)
            valores.append(salidaR)
        else:
            valores.append(parametros.expresion.val)
        idic += 1

    #print(valores)
    updateDicc = {}
    if len(valores) == len(arrayPosColumna):
        Dicc = 0
        while Dicc < len(valores):
            updateDicc[arrayPosColumna[Dicc]] = valores[Dicc]
            Dicc += 1

        #print(updateDicc)

    resultArraynew = j.extractTable(str(useCurrentDatabase),str(instr.identificador.val))

    llaves = []
    iU = 0
    while iU < len(resultArraynew):
        llavesTemp = []
        for pks in arrayPK:
            for colum in arrayupdateNum:
                if colum == iU:
                    llavesTemp.append(resultArraynew[iU][pks])
        if llavesTemp != []:
            llaves.append(llavesTemp)
        iU += 1
    
    valorReturn = 0
    for llavesPk in llaves:
        valorReturn = j.update(str(useCurrentDatabase),str(instr.identificador.val),updateDicc,llavesPk)

    

    if valorReturn == 0:
        salida = '\nUPDATE'
    elif valorReturn == 1 :
        salida = "\nERROR:  internal_error \nSQL state: XX000 "
    elif valorReturn == 2 :
        salida = "\nERROR:  database \"" + str(useCurrentDatabase) +"\" does not exist \nSQL state: 3D000"
    elif valorReturn == 3 :
        salida = "\nERROR:  table \"" + str(instr.identificador.val) +"\" does not exist \nSQL state: 42P01"
    elif valorReturn == 4 :
        salida = "\nERROR:  PK does not exist \nSQL state: 42P01"
    

def procesar_drop(instr,ts,tc):
    if instr.lista_ids != []:
        for datos in instr.lista_ids:
            #print(datos.val)
            result = j.dropTable(str(useCurrentDatabase),str(datos.val))
            global salida
            if result == 0:
                global salida
                salida = "\nDROP TABLE"
                ts.deleteDatabase(datos.val)
                tc.eliminarTabla(useCurrentDatabase,datos.val)
            elif result == 1 :
                salida = "\nERROR:  internal_error \nSQL state: XX000 "
            elif result == 2 :
                salida = "\nERROR:  database \"" + str(useCurrentDatabase) +"\" does not exist \nSQL state: 3D000"
            elif result == 3 :
                salida = "\nERROR:  table \"" + str(datos.val) +"\" does not exist \nSQL state: 42P01"
        

#Alter table

def procesar_altertable(instr,ts,tc):
    if instr.etiqueta == TIPO_ALTER_TABLE.ADD_CHECK:
        global salida
        if instr.expresionlogica.operador == OPERACION_LOGICA.AND or instr.expresionlogica.operador == OPERACION_LOGICA.OR: 
            nada = 1
        else:
            nada = 1
            if isinstance(instr.expresionlogica.exp1,ExpresionIdentificador):
                nada = 1
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val)
                if buscar == False:
                    nada = 1
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val)
                    
                    salida = "\nALTER TABLE" 

            elif isinstance(instr.expresionlogica.exp2,ExpresionIdentificador):
                nada = 1
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val)
                if buscar == False:
                    nada = 1
                else:
                    salida = "\nALTER TABLE" 
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val)
                    salida = "\nALTER TABLE" 


    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_FOREIGN:
        buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.columnid)
        if buscar == False:
            nada = 1
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
            tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.columnid,buscar.tipo,buscar.tamanio,instr.lista_campos,instr.tocolumnid,tempA)
            tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.columnid)
            salida = "\nALTER TABLE" 

    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_CHECK:
        if instr.expresionlogica.operador == TIPO_LOGICA.AND or instr.expresionlogica.operador == TIPO_LOGICA.OR: 
            nada = 1
            
        else:
            temp = TS.Simbolo(instr.columnid,'CONSTRAINT',0,instr.identificador)
            ts.agregar(temp)
            if type(instr.expresionlogica.exp1) == ExpresionIdentificador:
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val)
                if buscar == False:
                    nada = 1
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val)
                    salida = "\nALTER TABLE" 
            else:
                nada = 1
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val)
                if buscar == False:
                    nada = 1
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val)
                    salida = "\nALTER TABLE" 

    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_UNIQUE:
        nada = 1
        if instr.lista_campos != []:
            temp = TS.Simbolo(instr.columnid,'CONSTRAINT',0,instr.identificador)
            ts.agregar(temp)
            
            for datos in instr.lista_campos:
                nada = 1
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,datos.val)
                if buscar == False:
                    nada = 1
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,datos.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,datos.val)
                    salida = "\nALTER TABLE" 

    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_FOREIGN:
        temp = TS.Simbolo(instr.columnid,'CONSTRAINT',0,instr.identificador)
        ts.agregar(temp)
        buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.tocolumnid)
        if buscar == False:
            nada = 1
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
            tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.tocolumnid,buscar.tipo,buscar.tamanio,instr.lista_ref,instr.lista_campos,tempA)
            tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.tocolumnid)
            salida = "\nALTER TABLE" 
        

        salida = "\nALTER TABLE" 

    elif instr.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN:
        nada = 1
        if instr.lista_campos != []:
            for lista in instr.lista_campos:
                nada = 1

                tipodatoo = TIPO_DE_DATOS.text_ 
                tamanioD = ""
                if lista.tipo.val.upper() == 'TEXT':
                    tipodatoo = TIPO_DE_DATOS.text_ 
                    tamanioD = ""
                elif lista.tipo.val.upper() == 'FLOAT':
                    tipodatoo = TIPO_DE_DATOS.float_ 
                elif lista.tipo.val.upper() == 'INTEGER':
                    tipodatoo = TIPO_DE_DATOS.integer_ 
                    tamanioD = ""
                elif lista.tipo.val.upper() == 'BOOLEAN':
                    tipodatoo = TIPO_DE_DATOS.boolean 
                    tamanioD = ""
                elif lista.tipo.val.upper() == 'SMALLINT':
                    tipodatoo = TIPO_DE_DATOS.smallint_ 
                elif lista.tipo.val.upper() == 'MONEY':
                    tipodatoo = TIPO_DE_DATOS.money 
                elif lista.tipo.val.upper() == 'BIGINT':
                    tipodatoo = TIPO_DE_DATOS.bigint 
                elif lista.tipo.val.upper() == 'REAL':
                    tipodatoo = TIPO_DE_DATOS.real 
                elif lista.tipo.val.upper() == 'DOUBLE':
                    tipodatoo = TIPO_DE_DATOS.double 
                elif lista.tipo.val.upper() == 'INTERVAL':
                    tipodatoo = TIPO_DE_DATOS.interval 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'TIME':
                    tipodatoo = TIPO_DE_DATOS.time 
                elif lista.tipo.val.upper() == 'TIMESTAMP':
                    tipodatoo = TIPO_DE_DATOS.timestamp 
                elif lista.tipo.val.upper() == 'DATE':
                    tipodatoo = TIPO_DE_DATOS.date 
                elif lista.tipo.val.upper() == 'VARYING':
                    tipodatoo = TIPO_DE_DATOS.varying 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'VARCHAR':
                    tipodatoo = TIPO_DE_DATOS.varchar 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'CHAR':
                    tipodatoo = TIPO_DE_DATOS.char 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'CHARACTER':
                    tipodatoo = TIPO_DE_DATOS.character 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'DECIMAL':
                    tipodatoo = TIPO_DE_DATOS.decimal 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'NUMERIC':
                    tipodatoo = TIPO_DE_DATOS.numeric           
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'DOUBLE':
                    tipodatoo = TIPO_DE_DATOS.double_precision

                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,lista.identificador.val)
                if buscar == False:
                    nada = 1
                else:
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,lista.identificador.val,buscar.tipo,tamanioD,buscar.referencia,buscar.tablaRef,buscar.listaCons)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,lista.identificador.val)
                    salida = "\nALTER TABLE"
    
    elif instr.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN_NULL:
        #print(instr.identificador,instr.columnid)
        
        buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.columnid)
        if buscar == False:
            nada = 1
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.NULL)
            tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.columnid,buscar.tipo,buscar.tamanio,"","",tempA)
            tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.columnid)
            salida = "\nALTER TABLE"   

    elif instr.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN_NOT_NULL:
        buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.columnid)
        if buscar == False:
            nada = 1
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.NOT_NULL)
            tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.columnid,buscar.tipo,buscar.tamanio,"","",tempA)
            tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.columnid)
            salida = "\nALTER TABLE"        
    
    elif instr.etiqueta ==  TIPO_ALTER_TABLE.DROP_CONSTRAINT:
        nada = 1
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                nada = 1
                ts.deleteConstraint(datos.val,instr.identificador)
            salida = "\nALTER TABLE" 

    elif instr.etiqueta ==  TIPO_ALTER_TABLE.RENAME_COLUMN:
        # NO EXISTE :(
        nada = 1
        salida = "\nALTER TABLE" 
    
    elif instr.etiqueta == TIPO_ALTER_TABLE.DROP_COLUMN:
        #print('Tabla',instr.identificador)
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                #print('Columna',datos.val)
                
                pos = tc.getPos(useCurrentDatabase,instr.identificador,datos.val)
                nada = 1
                result = j.alterDropColumn(str(useCurrentDatabase),str(instr.identificador),pos)
                
                if result == 0:
                    tc.eliminarID(useCurrentDatabase,instr.identificador,datos.val)
                    temp1 = ts.obtener(instr.identificador,useCurrentDatabase)
                    temp2 = TS.Simbolo(temp1.val,temp1.tipo,temp1.valor-1,temp1.ambito)
                    ts.actualizarDB(temp2,instr.identificador)
                    salida = "\nALTER TABLE"            
                    nada = 1

                elif result == 1 :
                    salida = "\nERROR:  internal_error \nSQL state: XX000 "
                elif result == 2 :
                    salida = "\nERROR:  database \"" + str(useCurrentDatabase) +"\" does not exist \nSQL state: 3D000"
                elif result == 3 :
                    salida = "\nERROR:  relation \"" + str(instr.identificador) +"\" does not exist\nSQL state: 42P01"
                elif result == 4 :
                    salida = "\nERROR:  key cannot be removed\nSQL state: 42P04"
                elif result == 5 :
                    salida = "\nERROR:  column out of bounds\nSQL state: 42P05"

                

    elif instr.etiqueta ==  TIPO_ALTER_TABLE.ADD_COLUMN:
        tipodatoo = TIPO_DE_DATOS.text_ 
        tamanioD = ""
        if instr.lista_campos[0].tipo.val.upper() == 'TEXT':
            tipodatoo = TIPO_DE_DATOS.text_ 
            tamanioD = ""
        elif instr.lista_campos[0].tipo.val.upper() == 'FLOAT':
            tipodatoo = TIPO_DE_DATOS.float_ 
        elif instr.lista_campos[0].tipo.val.upper() == 'INTEGER':
            tipodatoo = TIPO_DE_DATOS.integer_ 
            tamanioD = ""
        elif instr.lista_campos[0].tipo.val.upper() == 'BOOLEAN':
            tipodatoo = TIPO_DE_DATOS.boolean
            tamanioD = ""
        elif instr.lista_campos[0].tipo.val.upper() == 'SMALLINT':
            tipodatoo = TIPO_DE_DATOS.smallint_ 
        elif instr.lista_campos[0].tipo.val.upper() == 'MONEY':
            tipodatoo = TIPO_DE_DATOS.money 
        elif instr.lista_campos[0].tipo.val.upper() == 'BIGINT':
            tipodatoo = TIPO_DE_DATOS.bigint 
        elif instr.lista_campos[0].tipo.val.upper() == 'REAL':
            tipodatoo = TIPO_DE_DATOS.real 
        elif instr.lista_campos[0].tipo.val.upper() == 'DOUBLE':
            tipodatoo = TIPO_DE_DATOS.double 
        elif instr.lista_campos[0].tipo.val.upper() == 'INTERVAL':
            tipodatoo = TIPO_DE_DATOS.interval 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'TIME':
            tipodatoo = TIPO_DE_DATOS.time 
        elif instr.lista_campos[0].tipo.val.upper() == 'TIMESTAMP':
            tipodatoo = TIPO_DE_DATOS.timestamp 
        elif instr.lista_campos[0].tipo.val.upper() == 'DATE':
            tipodatoo = TIPO_DE_DATOS.date 
        elif instr.lista_campos[0].tipo.val.upper() == 'VARYING':
            tipodatoo = TIPO_DE_DATOS.varying 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'VARCHAR':
            tipodatoo = TIPO_DE_DATOS.varchar 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'CHAR':
            tipodatoo = TIPO_DE_DATOS.char 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'CHARACTER':
            tipodatoo = TIPO_DE_DATOS.character 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'DECIMAL':
            tipodatoo = TIPO_DE_DATOS.decimal 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'NUMERIC':
            tipodatoo = TIPO_DE_DATOS.numeric           
            tamanioD = instr.lista_campos[0].par1 
        elif instr.lista_campos[0].tipo.val.upper() == 'DOUBLE':
            tipodatoo = TIPO_DE_DATOS.double_precision
        
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                result = j.alterAddColumn(str(useCurrentDatabase),str(instr.identificador),1)
                if result == 0:
                    buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,datos.identificador.val)
                    if buscar == False:
                        tipo = TC.Tipo(useCurrentDatabase,instr.identificador,datos.identificador.val,tipodatoo,tamanioD,"","",[])
                        tc.agregar(tipo)
                    else:
                        nada = 1
                    
                    temp1 = ts.obtener(instr.identificador,useCurrentDatabase)
                    temp2 = TS.Simbolo(temp1.val,temp1.tipo,temp1.valor+1,temp1.ambito)
                    ts.actualizarDB(temp2,instr.identificador)
                    salida = "\nALTER TABLE"            

                elif result == 1 :
                    salida = "\nERROR:  internal_error \nSQL state: XX000 "
                elif result == 2 :
                    salida = "\nERROR:  database \"" + str(useCurrentDatabase) +"\" does not exist \nSQL state: 3D000"
                elif result == 3 :
                    salida = "\nERROR:  relation \"" + str(instr.tipo_id) +"\" does not exist\nSQL state: 42P01"
                
                
def f_SIGN(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0

#INSERT
def procesar_insert(instr,ts,tc):
    # tabla -> print(instr.val)
    
    global salida
    columns = tc.obtenerColumns(useCurrentDatabase,instr.val)
    numC = len(columns)
    arrayInsert = []
    arrayInserteFinal = []
    arrayParametros = []
    if instr.etiqueta == TIPO_INSERT.CON_PARAMETROS:
        nada = 1
        if instr.lista_parametros != []:
            for parametros in instr.lista_parametros:
                #print(parametros.val)
                typeC = tc.obtenerReturn(useCurrentDatabase,instr.val,parametros.val)
                #print('tc',typeC.val)
                arrayParametros.append(typeC.val)

        if instr.lista_datos != []:
            for parametros in instr.lista_datos:
                if isinstance(parametros,Funcion_Exclusivas_insert):
                    arrTC = []
                    salidaR = resolver_expresion_aritmetica(parametros,arrTC)
                    nada = 1
                    arrayInsert.append(salidaR)
                else:
                    arrayInsert.append(parametros.val)


        arrayNew = []           
        ar = 0
        while ar < len(columns):
            if ar < len(arrayInsert):
                arrayNew.append([arrayParametros[ar],arrayInsert[ar]])
            else:
                arrayNew.append([None,None])
            ar+=1

        
        arrayNone = []
        ii = 0
        jj = 0
        while ii < len(columns):
            iii = 0
            arrPP = []
            while iii < len(arrayNew):
                arrPP.append(arrayNew[iii][0])
                iii+=1
            if columns[ii] in arrPP:
                arrayNone.append(arrayNew[jj][1])
                jj+=1
            else:
                arrayNone.append(None)
            ii+=1

        #print(columns)
        #print(arrayNone)

        if len(arrayNone) == numC:
            i = 0
            while i < numC:
                restricciones = []
                it = 0
                typeC = tc.obtenerReturn(useCurrentDatabase,instr.val,columns[i])

                while it < len(typeC.listaCons):
                    restricciones.append(typeC.listaCons[it])
                    it+=1
                #print(typeC.val,typeC.tamanio,restricciones)

                insertBool = False
                if restricciones != []:
                    for res in restricciones:
                        if res == OPCIONES_CONSTRAINT.CHECK:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.UNIQUE:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.FOREIGN:
                            if arrayNone[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                        if res == OPCIONES_CONSTRAINT.NULL:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.NOT_NULL:
                            if arrayNone[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                        if res == OPCIONES_CONSTRAINT.DEFAULT:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.PRIMARY:
                            if arrayNone[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                else:
                    insertBool = True

                
                if insertBool:
                    arrayInserteFinal.append(arrayNone[i])

                i+=1 
            #print(arrayInserteFinal)

        elif len(arrayInsert) > numC:
            salida = "\nERROR:  INSERT has more expressions than target columns\nSQL state: 42601"
       
    else:
        if instr.lista_datos != []:
            #print(columns)
            #print(numC)
            for parametros in instr.lista_datos:
                if isinstance(parametros,Funcion_Exclusivas_insert):
                    arrTC = []
                    salidaR = resolver_expresion_aritmetica(parametros,arrTC)
                    nada = 1
                    arrayInsert.append(salidaR)
                else:
                    arrayInsert.append(parametros.val)

            

        # LLENAR CAMPOS CON None
        if len(arrayInsert) < numC:
            i = len(arrayInsert)
            while i < numC:
                arrayInsert.append(None)
                i+=1


        if len(arrayInsert) == numC:
            i = 0
            while i < numC:
                restricciones = []
                it = 0
                typeC = tc.obtenerReturn(useCurrentDatabase,instr.val,columns[i])

                while it < len(typeC.listaCons):
                    restricciones.append(typeC.listaCons[it])
                    it+=1
                #print(typeC.val,typeC.tamanio,restricciones)

                insertBool = False
                if restricciones != []:
                    for res in restricciones:
                        if res == OPCIONES_CONSTRAINT.CHECK:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.UNIQUE:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.FOREIGN:
                            if arrayInsert[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                        if res == OPCIONES_CONSTRAINT.NULL:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.NOT_NULL:
                            if arrayInsert[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                        if res == OPCIONES_CONSTRAINT.DEFAULT:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.PRIMARY:
                            if arrayInsert[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                else:
                    insertBool = True

                
                if insertBool:
                    arrayInserteFinal.append(arrayInsert[i])

                i+=1 
            #print(arrayInserteFinal)

        elif len(arrayInsert) > numC:
            salida = "\nERROR:  INSERT has more expressions than target columns\nSQL state: 42601"
            nada = 1


    #FUNCION INSERTAR
    '''print(arrayInserteFinal)
    print(str(useCurrentDatabase),str(instr.val), arrayInserteFinal)'''

    result = j.insert(useCurrentDatabase,instr.val, arrayInserteFinal)
    nada = 1
    if result == 0:
        salida = "\nINSERT 0 1"            
    elif result == 1 :
        salida = "\nERROR:  internal_error \nSQL state: XX000 "
    elif result == 2 :
        salida = "\nERROR:  database \"" + str(useCurrentDatabase) +"\" does not exist \nSQL state: 3D000"
    elif result == 3 :
        salida = "\nERROR:  relation \"" + str(instr.val) +"\" does not exist\nSQL state: 42P01"
    elif result == 4:
        salida = "\nERROR:  duplicate key value violates unique constraint \"" + str(instr.val) + "_pkey\"\nSQL state: 23505"
    elif result == 5:
        salida = "\nERROR:  INSERT has more expressions than target columns\nSQL state: 42601"

    #print(salida)

    


    

#Enum
def procesar_create_type(instr,ts,tc):
    
    nada = 1
    if instr.lista_datos != []:
        for datos in instr.lista_datos:
            nada = 1

#delete
def procesar_delete(instr,ts,tc):
    if instr.etiqueta == TIPO_DELETE.DELETE_NORMAL:
        nada = 1

    elif instr.etiqueta == TIPO_DELETE.DELETE_RETURNING:
        nada = 1
        if instr.returning != []:
            for retornos in instr.returning:
                nada = 1

    elif instr.etiqueta == TIPO_DELETE.DELETE_EXIST:    
        if instr.expresion.operador == OPERACION_RELACIONAL.MAYQUE:
            if instr.expresion.exp1.etiqueta == TIPO_VALOR.IDENTIFICADOR and instr.expresion.exp2.etiqueta ==  TIPO_VALOR.NUMERO:
                nada = 1           

   
    elif instr.etiqueta == TIPO_DELETE.DELETE_EXIST_RETURNING:
        
        nada = 1

        if instr.expresion.operador == OPERACION_RELACIONAL.MAYQUE:
            if instr.expresion.exp1.etiqueta == TIPO_VALOR.IDENTIFICADOR and instr.expresion.exp2.etiqueta ==  TIPO_VALOR.NUMERO:
                nada = 1

        if instr.returning != []:
            for retornos in instr.returning:
                nada = 1

        
    elif instr.etiqueta == TIPO_DELETE.DELETE_CONDIFION:
        nada = 1
    
    elif instr.etiqueta == TIPO_DELETE.DELETE_CONDICION_RETURNING:
        if instr.returning != []:
            for retornos in instr.returning:
                nada = 1

    elif instr.etiqueta == TIPO_DELETE.DELETE_USING:
        nada = 1

    elif instr.etiqueta == TIPO_DELETE.DELETE_USING_returnin:
        if instr.returning != []:
            for retornos in instr.returning:
                nada = 1





def procesar_select_time(instr,ts,tc):
    global salida
    arrayReturn = []
    if instr.etiqueta == SELECT_TIME.EXTRACT:
        if instr.val1.val == 'YEAR':
            year = re.findall('(\d{4})-\d{2}-\d{2}', instr.val2)
            arrayReturn.append(['date_part'])
            arrayReturn.append([year[0]])

        elif instr.val1.val == 'MONTH':
            month = re.findall('\d{4}-(\d{2})-\d{2}', instr.val2)
            arrayReturn.append(['date_part'])
            arrayReturn.append([month[0]])

        elif instr.val1.val == 'DAY':
            day = re.findall('\d{4}-\d{2}-(\d{2})', instr.val2)
            arrayReturn.append(['date_part'])
            arrayReturn.append([day[0]])

        elif instr.val1.val == 'HOUR':
            hora = re.findall('(\d{2}):\d{2}:\d{2}', instr.val2)
            arrayReturn.append(['date_part'])
            arrayReturn.append([hora[0]])

        elif instr.val1.val == 'MINUTE':
            minuto = re.findall('\d{2}:(\d{2}):\d{2}', instr.val2)
            arrayReturn.append(['date_part'])
            arrayReturn.append([minuto[0]])

        elif instr.val1.val == 'SECOND':
            segundo = re.findall('\d{2}:\d{2}:(\d{2})', instr.val2)
            arrayReturn.append(['date_part'])
            arrayReturn.append([segundo[0]])

    elif instr.etiqueta == SELECT_TIME.DATE_PART:
        if instr.val1.upper() == 'HOURS':
            hour = re.findall('(\d+) hours', instr.val2)
            nada = 1 
            arrayReturn.append(['date_part'])
            arrayReturn.append([hour[0]])

        elif instr.val1.upper() == 'MINUTES':
            minutes = re.findall('(\d+) minutes', instr.val2)
            nada = 1
            arrayReturn.append(['date_part'])
            arrayReturn.append([minutes[0]])

        elif instr.val1.upper() == 'SECONDS':
            seconds = re.findall('(\d+) seconds', instr.val2)
            nada = 1
            arrayReturn.append(['date_part'])
            arrayReturn.append([seconds[0]])

    elif instr.etiqueta == SELECT_TIME.NOW:
        current_time = datetime.datetime.now() 
        noww = str(current_time.year)+ '-'+ str(current_time.month)+'-'+str(current_time.day)+' '+ str(current_time.hour)+':'+str(current_time.minute)+':'+str(current_time.second)+'.'+str(current_time.microsecond)
        arrayReturn.append(['now'])
        arrayReturn.append([noww])
    elif instr.etiqueta == SELECT_TIME.CURRENT_TIME:
        current_time = datetime.datetime.now() 
        currentT = str(current_time.hour)+':'+str(current_time.minute)+':'+str(current_time.second)+'.'+str(current_time.microsecond) 
        arrayReturn.append(['current_time'])
        arrayReturn.append([currentT])
    elif instr.etiqueta == SELECT_TIME.CURRENT_DATE:
        current_time = datetime.datetime.now() 
        currentD = str(current_time.year)+ '-'+ str(current_time.month)+'-'+str(current_time.day)
        arrayReturn.append(['current_date'])
        arrayReturn.append([currentD])
    elif instr.etiqueta == SELECT_TIME.TIMESTAMP:
        if instr.val1.upper() == 'NOW':
            current_time = datetime.datetime.now() 
            noww = str(current_time.year)+ '-'+ str(current_time.month)+'-'+str(current_time.day)+' '+ str(current_time.hour)+':'+str(current_time.minute)+':'+str(current_time.second)+'.'+str(current_time.microsecond)
            arrayReturn.append(['now'])
            arrayReturn.append([noww])
    #print(arrayReturn)
    
    salida = toPretty(arrayReturn)

def procesar_select1(instr,ts,tc):
    if instr.etiqueta == OPCIONES_SELECT.GREATEST:
        if instr.lista_extras != []:
            for datos in instr.lista_extras:
                if datos.etiqueta == TIPO_VALOR.DOBLE:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.NUMERO:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.NEGATIVO:
                    nada = 1

    elif instr.etiqueta == OPCIONES_SELECT.LEAST:
        nada = 1
        if instr.lista_extras != []:
            for datos in instr.lista_extras:
                if datos.etiqueta == TIPO_VALOR.DOBLE:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.NUMERO:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.NEGATIVO:
                    nada = 1



def procesar_select_general(instr,ts,tc):
    global salida
    columnsTable = []
    arrayColumns = []
    tables = []
    arrayReturn = []
    #WHERE
    arrayWhere = []
    arrayFilter = []

    array2 = [[],[]]

    
    if  instr.instr1 != None and instr.instr2 == None and instr.instr3 == None and instr.listains == None and instr.listanombres != None:
        global salida
        
        
        if instr.instr1.etiqueta == OPCIONES_SELECT.DISTINCT:
            for datos in instr.instr1.listac:
                nada = 1
        if instr.instr1.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
            for datos in instr.instr1.lista_extras:
                if datos.etiqueta == OPCIONES_SELECT.CASE:
                    for objs in datos.listacase:
                        nada = 1
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                    arrayColumns.append(datos.val)
                    nada = 1

                elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                    nada = 1
                    return datos.val
                else:
                    #print(datos.val) #RESTO DE ETIQUETAS
                    arrayColumns.append(datos.val)
        
        if instr.listanombres != []:
            for datos in instr.listanombres:
                if datos.etiqueta == TIPO_VALOR.DOBLE:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.AS_ID:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 != None:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 == None:
                    nada = 1
                    tables.append(datos.val)

        if '*' in arrayColumns:
            columnsTable = tc.obtenerColumns(useCurrentDatabase,tables[0])
            resultArray = j.extractTable(str(useCurrentDatabase),str(tables[0]))
            arrayReturn.append(columnsTable)
            for filas in resultArray:
                arrayReturn.append(filas)

            salida = toPretty(arrayReturn)
        else:
            columnsTable = tc.obtenerColumns(useCurrentDatabase,tables[0])
            resultArray = j.extractTable(str(useCurrentDatabase),str(tables[0]))
            arrayReturn.append(arrayColumns)
            for filasF in resultArray:
                #print(filasF)
                arrayTemp = []
                for colF in arrayColumns:
                    #print(filasF[columnsTable.index(colF)])
                    arrayTemp.append(filasF[columnsTable.index(colF)])
                    #print(colF)
                arrayReturn.append(arrayTemp)

            salida = toPretty(arrayReturn)

        

        

    

    
    elif instr.instr1 != None and instr.instr2 != None and instr.instr3 == None and instr.listains == None and instr.listanombres != None:
        
        arrayColumnsF = []
        if instr.instr1.etiqueta == OPCIONES_SELECT.DISTINCT:
            for datos in instr.instr1.listac:
                nada = 1
        if instr.instr1.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
            for datos in instr.instr1.lista_extras:
                if datos.etiqueta == OPCIONES_SELECT.CASE:
                    for objs in datos.listacase:
                        nada = 1
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                    #print(datos.val)
                    arrayColumnsF.append(datos.val)

                elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                    nada = 1
                else:
                    columnP = str(datos.val)+"."+str(datos.val1)
                    arrayColumnsF.append(columnP)

        arrayTablas = []
        if instr.listanombres != []:
            for datos in instr.listanombres:
                if datos.etiqueta == TIPO_VALOR.DOBLE:
                    nada = 1
                    #print(datos.val+'.'+datos.val1)
                elif datos.etiqueta == TIPO_VALOR.AS_ID: #TABLA AS T
                    arrayTablas.append([datos.val,datos.val1.val])

                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 != None: #TABLA T
                    arrayTablas.append([datos.val,datos.val1])
                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 == None:
                    nada = 1
                    #print(datos.val)
            #print(arrayTablas)
            #tc.obtenerColumns(useCurrentDatabase,tables[0])
            arrayColumnsMerge = []
            arrC = 0
            while arrC < len(arrayTablas):
                arrayColumnsPrimera = []
                arrayColumnsPrimera = tc.obtenerColumns(useCurrentDatabase,arrayTablas[arrC][0])
                for arrCP in arrayColumnsPrimera:
                    columP = str(arrayTablas[arrC][1])+"."+str(arrCP)
                    arrayColumnsMerge.append(columP)
                arrC +=1

            columnsTable = arrayColumnsMerge
            #print(columnsTable)
            #print(arrayColumnsMerge)


            arrayMerge = [] 
            #arrayMerge.append(columnsTable)
            arrayPrimera = []
            arraySegunda = []   
            temp = []
            iT = 1
            while iT < len(arrayTablas):
                if iT == 1:
                    arrayPrimera = j.extractTable(str(useCurrentDatabase),arrayTablas[0][0])
                    arraySegunda = j.extractTable(str(useCurrentDatabase),arrayTablas[1][0])
                else:
                    arrayMerge = []
                    arrayPrimera = temp
                    arraySegunda = j.extractTable(str(useCurrentDatabase),arrayTablas[iT][0])
                arrP = 0
                while arrP < len(arrayPrimera):
                    
                    arrS = 0
                    while arrS < len(arraySegunda):
                        arrFilas = []
                        arrPP = 0
                        while arrPP < len(arrayPrimera[arrP]):
                            arrFilas.append(arrayPrimera[arrP][arrPP])
                            arrPP +=1
                        arrSS = 0
                        while arrSS < len(arraySegunda[arrS]):
                            arrFilas.append(arraySegunda[arrS][arrSS])
                            arrSS +=1
                        #print(arrayPrimera[arrP],arraySegunda[arrS])
                        arrayMerge.append(arrFilas)
                        arrS+=1
                    arrP +=1
                    
                temp = arrayMerge
                iT +=1

            arrayMerge.insert(0,columnsTable)
            #print(toPretty(arrayMerge))

                    
        if instr.instr2.expwhere != None:
            arrayFilterFilter = []
            arrayFilterFilter.append(arrayMerge[0])
            i = 1
            while i < len(arrayMerge):
                arrayTS = []
                arrayTS.append(arrayMerge[0])
                arrayTS.append(arrayMerge[i])
                val = resolver_expresion_logica(instr.instr2.expwhere.expresion,arrayTS)
                if val == 1:
                    arrayFilterFilter.append(arrayMerge[i])
                i+=1
        
            arrayFilter = arrayFilterFilter

        if '*' in arrayColumnsF:
            for filas in arrayFilter:
                arrayReturn.append(filas)

            salida = toPretty(arrayReturn)
            #print(arrayReturn)

        else:
            for filasF in arrayFilter:
                #print(filasF)
                arrayTemp = []
                for colF in arrayColumnsF:
                    arrayTemp.append(filasF[columnsTable.index(colF)])
                    #print(colF)
                arrayReturn.append(arrayTemp)

            salida = toPretty(arrayReturn)
            #print(arrayReturn)

        '''if instr.instr2.expgb != None:
            print(instr.instr2.expgb.etiqueta)
            for datos in instr.instr2.expgb.expresion:
                print(datos.id)
        if instr.instr2.expob != None:
            print(instr.instr2.expob.etiqueta)
            for datos in instr.instr2.expob.expresion:
                print(datos.val)
        if instr.instr2.exphav != None:
            print(instr.instr2.exphav.etiqueta)
            print(instr.instr2.exphav.expresion)
        if instr.instr2.exporden != None:
            print(instr.instr2.exporden.etiqueta)
            print(instr.instr2.exporden.expresion.id)
        if instr.instr2.explimit != None:
            print(instr.instr2.explimit.etiqueta)
            if instr.instr2.explimit.expresion.etiqueta == TIPO_VALOR.NUMERO:
                print(instr.instr2.explimit.expresion.val)
            else:
                print(instr.instr2.explimit.expresion.val)
        if instr.instr2.expoffset != None:
            print(instr.instr2.expoffset.etiqueta)
            print(instr.instr2.expoffset.expresion.val)
        if instr.instr2.valor != None:
            print(instr.instr2.valor)'''

    elif instr.instr1 == None and instr.instr2 != None and instr.instr3 != None and instr.listains != None and instr.listanombres == None:
        nada = 1
        if instr.instr2.etiqueta == OPCIONES_SELECT.DISTINCT:
            for datos in instr.instr2.listac:
                nada = 1
        if instr.instr2.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
            for datos in instr.instr2.lista_extras:
                if datos.etiqueta == OPCIONES_SELECT.CASE:
                    for objs in datos.listacase:
                        nada = 1
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                    nada = 1
                else:
                    nada = 1

            if instr.instr3[0] == TIPO_VALOR.AS_ID:
                nada = 1
            elif instr.instr3[0] == TIPO_VALOR.DOBLE:
                nada = 1
            else:
                nada = 1

            for objs in instr.listains:
                if objs.instr2 != None:
                    nada = 1
                    if objs.instr2.expwhere != None:
                        nada = 1
                    if objs.instr2.expgb != None:
                        nada = 1
                        for datos in objs.instr2.expgb.expresion:
                            nada = 1
                    if objs.instr2.expob != None:
                        nada = 1
                        for datos in objs.instr2.expob.expresion:
                            nada = 1
                    if objs.instr2.exphav != None:
                        nada = 1
                    if objs.instr2.exporden != None:
                        nada = 1
                    if objs.instr2.explimit != None:
                        nada = 1
                        if objs.instr2.explimit.expresion.etiqueta == TIPO_VALOR.NUMERO:
                            nada = 1
                        else:
                            nada = 1
                    if objs.instr2.expoffset != None:
                        nada = 1
                    if objs.instr2.valor != None:
                        nada = 1
                elif objs.instr2 == None:
                    nada = 1

    elif instr.instr1 != None and instr.instr2 == None and instr.instr3 != None and instr.listains != None and instr.listanombres == None:
        nada = 1
        if instr.instr1.etiqueta == OPCIONES_SELECT.DISTINCT:
            for datos in instr.instr1.listac:
                nada = 1
        if instr.instr1.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
            for datos in instr.instr1.lista_extras:
                if datos.etiqueta == OPCIONES_SELECT.CASE:
                    for objs in datos.listacase:
                        nada = 1
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                    arrayColumns.append(datos.val) # *
                elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                    nada = 1
                else:
                    arrayColumns.append(datos.val) #IDS

        for objs in instr.listains:
            tables.append(objs.val) #tables


        columnsTable = tc.obtenerColumns(useCurrentDatabase,tables[0])
        resultArray = j.extractTable(str(useCurrentDatabase),str(tables[0]))
        arrayWhere = resultArray
        arrayWhere.insert(0,columnsTable)           

        if instr.instr3.expwhere != None:
            arrayFilter.append(arrayWhere[0])
            i = 1
            while i < len(arrayWhere):
                arrayTS = []
                arrayTS.append(arrayWhere[0])
                arrayTS.append(arrayWhere[i])
                val = resolver_expresion_logica(instr.instr3.expwhere.expresion,arrayTS)
                if val == 1:
                    arrayFilter.append(arrayWhere[i])
                i+=1
            
        #print(arrayFilter)

        if '*' in arrayColumns:
            for filas in arrayFilter:
                arrayReturn.append(filas)

            salida = toPretty(arrayReturn)
            nada = 1

        else:
            for filasF in arrayFilter:
                #print(filasF)
                arrayTemp = []
                for colF in arrayColumns:
                    #print(filasF[columnsTable.index(colF)])
                    arrayTemp.append(filasF[columnsTable.index(colF)])
                    #print(colF)
                arrayReturn.append(arrayTemp)

            salida = toPretty(arrayReturn)
            

        if instr.instr3.expgb != None:
            nada = 1
            for datos in instr.instr3.expgb.expresion:
                nada = 1
        if instr.instr3.expob != None:
            nada = 1
            for datos in instr.instr3.expob.expresion:
                nada = 1
        if instr.instr3.exphav != None:
            nada = 1
            nada = 1
        if instr.instr3.exporden != None:
            nada = 1
        if instr.instr3.explimit != None:
            nada = 1
            if instr.instr3.explimit.expresion.etiqueta == TIPO_VALOR.NUMERO:
                nada = 1
            else:
                nada = 1
        if instr.instr3.expoffset != None:
            nada = 1
        if instr.instr3.valor != None:
            nada = 1

    elif instr.instr1 == None and instr.instr2 == None and instr.instr3 == None and instr.listains == None and instr.listanombres != None:
           
        for datos in instr.listanombres:
            #CON IDENTIFICADOR 
            if datos.expresion != None and datos.asterisco != None:
                
                if type(datos.asterisco) == list:
                    array2[0].append(datos.asterisco[1].val)
                else:
                    array2[0].append(datos.asterisco)


                if datos.expresion.operador == OPERACION_ARITMETICA.WIDTH_BUCKET:
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.E_DIV:
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))

                elif datos.expresion.operador == OPERACION_ARITMETICA.GCD:
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.MOD:
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.POWER:
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.TRUNC:
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2:
                    
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2D:
                    
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.SUBSTRING:
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.SUBSTR:
                    
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.GET_BYTE:
                    
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.SET_BYTE:
                    
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.ENCODE:
                    
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.DECODE:
                    
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                else:
                    ts = []
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                
                if datos.asterisco[0] == TIPO_VALOR.AS_ID:
                    nada = 1
                elif datos.asterisco[0] == TIPO_VALOR.DOBLE:
                    nada = 1
                else:
                    nada = 1

            #SIN IDENTIFICADOR
            if datos.expresion != None and datos.asterisco == None:
                
                if datos.expresion.operador == OPERACION_ARITMETICA.WIDTH_BUCKET:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.E_DIV:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.GCD:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.MOD:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.POWER:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.TRUNC:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))

                elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2D:
                    
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.SUBSTRING:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.SUBSTR:
                    
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.GET_BYTE:
                    
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.SET_BYTE:
                    
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.ENCODE:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                elif datos.expresion.operador == CADENA_BINARIA.DECODE:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))
                else:
                    ts = []
                    array2[0].append(datos.expresion.operador)
                    array2[1].append(resolver_expresion_aritmetica(datos.expresion,ts))

        
        arrayReturn = array2

    salida = toPretty(arrayReturn)

def getPosition(ts,id):    
    pos = ts[0].index(id)
    return pos

def f_truncate(number, decimals=0):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor

def f_width_bucket(num,num2,num3,num4):
    if num < num2:
        return 0
    elif num >= num3:
        return num4 + 1
    else:
        if num >= num2 and num < num3:
            i = 0
            j = 0
            while True:
                j += 1
                i += num4+1
                if not i < num:
                    break
            return j


def resolver_expresion_aritmetica(expNum,ts):

    if isinstance(expNum, ExpresionBinaria):
        exp1 = resolver_expresion_aritmetica(expNum.exp1,ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2,ts)      

        if expNum.operador == OPERACION_ARITMETICA.MAS:
            return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS:
            return exp1 - exp2  
        if expNum.operador == OPERACION_ARITMETICA.ASTERISCO:
            return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO:
            return exp1 / exp2   

    elif isinstance(expNum,ExpresionNegativo):
        return expNum.exp * -1
  
    elif isinstance(expNum, ExpresionEntero):
        return expNum.val

    elif isinstance(expNum, ExpresionComillaSimple) :
        return expNum.val

    elif isinstance(expNum, ExpresionIdentificador) :
        pos = getPosition(ts,expNum.val)
        return ts[1][pos]

    elif isinstance(expNum, ExpresionIdentificadorDoble) :
        idd = str(expNum.val) + "." + str(expNum.val1)
        pos = getPosition(ts,idd)
        return ts[1][pos]
        
    elif isinstance(expNum, Expresiondatos):
        exp = resolver_expresion_aritmetica(expNum.exp1,ts)
        exp1 = resolver_expresion_aritmetica(expNum.exp2,ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp3,ts)
        exp3 = resolver_expresion_aritmetica(expNum.exp4,ts)
        if expNum.operador == OPERACION_ARITMETICA.ABS:
            return abs(exp)
        elif expNum.operador == OPERACION_ARITMETICA.CBRT:
            return exp**(1/3)
        elif expNum.operador == OPERACION_ARITMETICA.WIDTH_BUCKET:
            return f_width_bucket(exp,exp1,exp2,exp3)
        elif expNum.operador == OPERACION_ARITMETICA.SIGN:
            return f_SIGN(exp)
        elif expNum.operador == OPERACION_ARITMETICA.LENGTH:
            return len(exp)
        elif expNum.operador == CADENA_BINARIA.LENGTH:
            return len(exp)
        elif expNum.operador == OPERACION_ARITMETICA.CEIL or expNum.operador == OPERACION_ARITMETICA.CEILING:
            return math.ceil(exp)
        elif expNum.operador == OPCIONES_DATOS.SUBSTRING or expNum.operador == OPCIONES_DATOS.SUBSTR:
            expCadena = resolver_expresion_aritmetica(expNum.exp1,ts)
            expInicio = resolver_expresion_aritmetica(expNum.exp2,ts)
            expFin = resolver_expresion_aritmetica(expNum.exp3,ts)            
            return  expCadena[expInicio:expFin]

        elif expNum.operador == CADENA_BINARIA.SUBSTRING or expNum.operador == CADENA_BINARIA.SUBSTR:
            expCadena = resolver_expresion_aritmetica(expNum.exp1,ts)
            expInicio = resolver_expresion_aritmetica(expNum.exp2,ts)
            expFin = resolver_expresion_aritmetica(expNum.exp3,ts)            
            return  expCadena[expInicio:expFin]

        elif expNum.operador == OPCIONES_DATOS.TRIM:
            expCadena = resolver_expresion_aritmetica(expNum.val1,ts)
            return expCadena.strip()
        elif expNum.operador == CADENA_BINARIA.TRIM:
            expCadena = resolver_expresion_aritmetica(expNum.exp1,ts)
            return expCadena.strip()
        elif expNum.operador == OPERACION_ARITMETICA.DEGREES:
            return math.degrees(exp)
        elif expNum.operador == OPERACION_ARITMETICA.E_DIV:
            return exp // exp1
        elif expNum.operador == OPERACION_ARITMETICA.EXP:
            return math.exp(exp)
        elif expNum.operador == OPERACION_ARITMETICA.FACTORIAL:
            return math.factorial(exp)
        elif expNum.operador == OPERACION_ARITMETICA.FLOOR:
            return math.floor(exp)
        elif expNum.operador == OPERACION_ARITMETICA.GCD:
            return math.gcd(exp, exp1)
        elif expNum.operador == OPERACION_ARITMETICA.LN:
            return math.log(exp)
        elif expNum.operador == OPERACION_ARITMETICA.LOG:
            return math.log10(exp)
        elif expNum.operador == OPERACION_ARITMETICA.MOD:
            return exp % exp1
        elif expNum.operador == OPERACION_ARITMETICA.PI:
            return math.pi
        elif expNum.operador == OPERACION_ARITMETICA.POWER:
            return math.pow(exp,exp1)
        elif expNum.operador == OPERACION_ARITMETICA.RADIANS:
            return math.radians(exp)
        elif expNum.operador == OPERACION_ARITMETICA.ROUND:
            return round(exp)
        elif expNum.operador == OPERACION_ARITMETICA.SQRT:
            return math.sqrt(exp)
        elif expNum.operador == OPERACION_ARITMETICA.TRUNC:
            return f_truncate(exp,exp1)
        elif expNum.operador == OPERACION_ARITMETICA.S_TRUNC:
            return math.trunc(exp)
        elif expNum.operador == OPERACION_ARITMETICA.RANDOM:
            return random.random()
        elif expNum.operador == OPERACION_ARITMETICA.ACOS:
            return math.acos(exp)
        elif expNum.operador == OPERACION_ARITMETICA.ASIND:
            valor = math.asin(exp)
            return math.degrees(valor)
        elif expNum.operador == OPERACION_ARITMETICA.ATAN:
            return math.atan(exp)
        elif expNum.operador == OPERACION_ARITMETICA.ATAND:
            return math.degrees(math.atan(exp))
        elif expNum.operador == OPERACION_ARITMETICA.ACOSD:
            return math.acosh(exp)
        elif expNum.operador == OPERACION_ARITMETICA.ATAN:
            return math.atan(exp)
        elif expNum.operador == OPERACION_ARITMETICA.ATAND:
            return math.degrees(math.atan(exp))
        elif expNum.operador == OPERACION_ARITMETICA.ATAN2:
            return math.atan2(exp,exp1)
        elif expNum.operador == OPERACION_ARITMETICA.ATAN2:
            return math.atan2(exp,exp1)
        elif expNum.operador == OPERACION_ARITMETICA.ATAN2D:
            return math.degrees(math.atan2(exp,exp1))
        elif expNum.operador == OPERACION_ARITMETICA.COS:
            return math.cos(exp)
        elif expNum.operador == OPERACION_ARITMETICA.COT:
            return mpmath.cot(exp)
        elif expNum.operador == OPERACION_ARITMETICA.COTD:
            return mpmath.coth(exp)
        elif expNum.operador == OPERACION_ARITMETICA.SIN:
            return mpmath.sin(exp)
        elif expNum.operador == OPERACION_ARITMETICA.SIND:
            valor = mpmath.sin(exp)
            return math.degrees(valor)
        elif expNum.operador == OPERACION_ARITMETICA.TAN:
            return math.tan(exp)
        elif expNum.operador == OPERACION_ARITMETICA.TAND:
            valor = math.degrees(exp)
            return math.tan(exp)
        elif expNum.operador == OPERACION_ARITMETICA.SINH:
            return math.sinh(exp)
        elif expNum.operador == OPERACION_ARITMETICA.ASINH:
            return math.asinh(exp)
        elif expNum.operador == OPERACION_ARITMETICA.COSH:
            return math.cosh(exp)
        elif expNum.operador == OPERACION_ARITMETICA.TANH:
            return math.tanh(exp)
        elif expNum.operador == OPERACION_ARITMETICA.COSD:
            valor = math.cos(exp)
            return math.degrees(valor)
        elif expNum.operador == OPERACION_ARITMETICA.ATANH:
            return math.atanh(exp)
        elif expNum.operador == OPERACION_ARITMETICA.ACOSH:
            valor = math.log(exp + math.sqrt((exp * exp) - 1))
            return valor
        elif expNum.operador == OPERACION_ARITMETICA.ASIN:
            return mpmath.asin(exp)
        elif expNum.operador == CADENA_BINARIA.GET_BYTE:
            string = exp
            posicion = [exp1]

            arr2 = bytes(string,'ascii')

            return (itemgetter(*posicion)(arr2))
        elif expNum.operador == CADENA_BINARIA.SET_BYTE:
            string = exp
            posicion = exp1
            getletra = string[posicion]
            getasii = chr(exp2)
            return string.replace(getletra,getasii)

        elif expNum.operador == CADENA_BINARIA.SHA256:
            return hashlib.sha256(exp.encode()).hexdigest()
        elif expNum.operador == CADENA_BINARIA.ENCODE:
            
            if expNum.exp2 == 'BASE64':
                cadena = exp
                message_bytes = cadena.encode('ascii')
                base = base64.b64encode(message_bytes)
                mensaje_base64 = base.decode('ascii')

                return mensaje_base64
            elif expNum.exp2 == 'HEX':
                hexa = exp.encode("utf-8")
                mensaje_hexa = binascii.hexlify(hexa)

                return mensaje_hexa
            else:
                return exp
        elif expNum.operador == CADENA_BINARIA.DECODE:
        
            if expNum.exp2 == 'BASE64':
                base64_mensaje = exp
                bytes64 = base64_mensaje.encode('ascii')
                mensaje_bbytes = base64.b64decode(bytes64)
                mensaje_de_64 = mensaje_bbytes.decode('ascii')

                return mensaje_de_64

            elif expNum.exp2 == 'HEX':
                hex_string = ("0x"+exp)[2:]

                hex_bytes = bytes.fromhex(hex_string)
                ascii_cadena = hex_bytes.decode("ASCII")
                return ascii_cadena
            else:
                return exp

    elif isinstance(expNum, Funcion_Exclusivas_insert):
        exp = resolver_expresion_aritmetica(expNum.exp1,ts)
        exp1 = resolver_expresion_aritmetica(expNum.exp2,ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp3,ts)
        if expNum.operador == INSERT_EXCLUSIVA.SUBSTRING:
            expCadena = resolver_expresion_aritmetica(expNum.exp1,ts)
            expInicio = resolver_expresion_aritmetica(expNum.exp2,ts)
            expFin = resolver_expresion_aritmetica(expNum.exp3,ts)            
            return  expCadena[expInicio:expFin]

        elif expNum.operador == INSERT_EXCLUSIVA.NOW:
            current_time = datetime.datetime.now() 
            noww = str(current_time.year)+ '-'+ str(current_time.month)+'-'+str(current_time.day)+' '+ str(current_time.hour)+':'+str(current_time.minute)+':'+str(current_time.second)
            return noww

        elif expNum.operador == INSERT_EXCLUSIVA.TRIM:
            expCadena = resolver_expresion_aritmetica(expNum.exp1,ts)
            return expCadena.strip()

        elif expNum.operador == INSERT_EXCLUSIVA.MD5:
            expCadena = resolver_expresion_aritmetica(expNum.exp1,ts)
            hash_obj = hashlib.md5(expCadena.encode())
            md5_to = hash_obj.hexdigest()
            return md5_to

        


        
                


        
        
        
                

def resolver_expresion_relacional(expRel,ts):
    if isinstance(expRel, ExpresionRelacional): 
        exp1 = resolver_expresion_aritmetica(expRel.exp1,ts)
        exp2 = resolver_expresion_aritmetica(expRel.exp2,ts)  
        if expRel.operador == OPERACION_RELACIONAL.MAYQUE:
            return exp1 > exp2
        if expRel.operador == OPERACION_RELACIONAL.MENQUE:
            return exp1 < exp2
        if expRel.operador == OPERACION_RELACIONAL.MAYIGQUE:
            return exp1 >= exp2
        if expRel.operador == OPERACION_RELACIONAL.MENIGQUE:
            return exp1 <= exp2
        if expRel.operador == OPERACION_RELACIONAL.DOBLEIGUAL:
            return exp1 == exp2
        if expRel.operador == OPERACION_RELACIONAL.IGUAL:
            return exp1 == exp2
        if expRel.operador == OPERACION_RELACIONAL.DIFERENTE:
            return exp1 != exp2
        if expRel.operador == OPCION_VERIFICAR.NULL or expRel.operador == OPCION_VERIFICAR.UNKNOWN:
            return exp1 == None
        if expRel.operador == OPCION_VERIFICAR.ISNULL:
            return exp1 == None
        if expRel.operador == OPCION_VERIFICAR.NOTNULL:
            return exp1 != None
        if expRel.operador == OPCION_VERIFICAR.TRUE:
            return exp1 == True
        if expRel.operador == OPCION_VERIFICAR.FALSE:
            return exp1 == False
        if expRel.operador == OPCION_VERIFICAR.N_TRUE:
            return exp1 != True
    else:
        return resolver_expresion_aritmetica(expRel,ts)


def resolver_expresion_logica(expLog,ts):
    
    
    if isinstance(expLog.exp1, ExpresionRelacional) and isinstance(expLog.exp2, ExpresionRelacional):
        
        exp1 = resolver_expresion_relacional(expLog.exp1,ts)
        exp2 = resolver_expresion_relacional(expLog.exp2,ts)
        

        if expLog.operador == OPERACION_LOGICA.AND:
            return exp1 and exp2
            
        if expLog.operador == OPERACION_LOGICA.OR:
            return exp1 or exp2
        
        if expLog.operador ==  OPCION_VERIFICAR.BETWEEN:
            return exp1 and exp2        
        if expLog.operador == OPCION_VERIFICAR.BETWEEN_1:
            return exp1 and exp2
        if expLog.operador == OPCION_VERIFICAR.ISDISTINCT:
            return exp1 and exp2
        if expLog.operador == OPCION_VERIFICAR.NOT_DISTINCT:
            return exp1 and exp2
        if expLog.operador == OPCION_VERIFICAR.LIKE:
            return exp1 and exp2
        if expLog.operador == OPCION_VERIFICAR.NOT_LIKE:
            return exp1 and exp2



    elif isinstance(expLog.exp1, ExpresionLogica) and isinstance(expLog.exp2, ExpresionRelacional):
        exp1 = resolver_expresion_logica(expLog.exp1,ts)
        exp2 = resolver_expresion_relacional(expLog.exp2,ts)
        
        if expLog.operador == OPERACION_LOGICA.AND:
            return exp1 and exp2
            
        elif expLog.operador == OPERACION_LOGICA.OR:
            return exp1 or exp2
       
        elif expLog.operador ==  OPCION_VERIFICAR.BETWEEN:
            
            return exp1 and exp2

        elif expLog.operador == OPCION_VERIFICAR.BETWEEN_1:
            return exp1 and exp2
        elif expLog.operador == OPCION_VERIFICAR.ISDISTINCT:
            return exp1 and exp2
        elif expLog.operador == OPCION_VERIFICAR.NOT_DISTINCT:
            return exp1 and exp2
        elif expLog.operador == OPCION_VERIFICAR.LIKE:
            return exp1 and exp2
        elif expLog.operador == OPCION_VERIFICAR.NOT_LIKE:
            return exp1 and exp2

    else:
        return resolver_expresion_relacional(expLog,ts) 


def procesar_select_uniones(instr,ts,tc):
    #print(instr.etiqueta)
    #print(instr.ins)
    global salida
    
    if instr.etiqueta == OPCIONES_UNIONES.UNION:
        arraySelect1 = procesar_select_for_UNIONES(instr.ins[0],ts,tc)
        arraySelect2 = procesar_select_for_UNIONES(instr.ins[1],ts,tc)
        union_arr = procesar_UNION(arraySelect1,arraySelect2)
        salida = toPretty(union_arr)
        #print(salida)
    elif instr.etiqueta == OPCIONES_UNIONES.UNION_ALL:
        arraySelect1 = procesar_select_for_UNIONES(instr.ins[0],ts,tc)
        arraySelect2 = procesar_select_for_UNIONES(instr.ins[1],ts,tc)
        union_arr = procesar_UNION_ALL(arraySelect1,arraySelect2)
        salida = toPretty(union_arr)
        #print(salida)
    elif instr.etiqueta == OPCIONES_UNIONES.INTERSECT or instr.etiqueta == OPCIONES_UNIONES.INTERSECT_ALL:
        arraySelect1 = procesar_select_for_UNIONES(instr.ins[0],ts,tc)
        arraySelect2 = procesar_select_for_UNIONES(instr.ins[1],ts,tc)
        intersect_arr = procesar_INTERSECT(arraySelect1,arraySelect2)
        salida = toPretty(intersect_arr)
        #print(salida)
    elif instr.etiqueta == OPCIONES_UNIONES.EXCEPTS or instr.etiqueta == OPCIONES_UNIONES.EXCEPTS_ALL:
        arraySelect1 = procesar_select_for_UNIONES(instr.ins[0],ts,tc)
        arraySelect2 = procesar_select_for_UNIONES(instr.ins[1],ts,tc)
        except_arr = procesar_EXCEPT(arraySelect1,arraySelect2)
        salida = toPretty(except_arr)
        #print(salida)

def procesar_UNION(arr1,arr2):
    if len(arr1[0]) != len(arr2[0]):
        return "ERROR:  each UNION query must have the same number of columns\nSQL state: 42601"
    else:
        arrUNION_ALL = []
        i=1
        while i<len(arr1):
            arrUNION_ALL.append(arr1[i])
            i+=1
        j=1
        while j<len(arr2):
            arrUNION_ALL.append(arr2[j])
            j+=1

        arrUNION = []
        
        arrU = 0
        while arrU < len(arrUNION_ALL):
            val = find_ARR(arrUNION_ALL[arrU],arrUNION)
            if val:
                arrUNION.append(arrUNION_ALL[arrU])
            arrU+=1
        arrUNION.insert(0,arr1[0])           
        
        return arrUNION

def procesar_INTERSECT(arr1,arr2):
    if len(arr1[0]) != len(arr2[0]):
        return "ERROR:  each UNION query must have the same number of columns\nSQL state: 42601"
    else:
        arrINTERSECT = []
        i=1
        while i<len(arr1):
            j=1
            while j<len(arr2):
                if arr1[i] == arr2[j]:
                    arrINTERSECT.append(arr1[i])

                j+=1
            i+=1
        arrINTERSECT.insert(0,arr1[0])           
        
        return arrINTERSECT

def procesar_EXCEPT(arr1,arr2):
    if len(arr1[0]) != len(arr2[0]):
        return "ERROR:  each UNION query must have the same number of columns\nSQL state: 42601"
    else:
        arr_INTERSECT = []
        i=1
        while i<len(arr1):
            j=1
            while j<len(arr2):
                if arr1[i] == arr2[j]:
                    arr_INTERSECT.append(arr1[i])

                j+=1
            i+=1
        arr_EXCEPT = []
        arrE = 1
        while arrE < len(arr1):
            val = find_ARR(arr1[arrE],arr_INTERSECT)
            if val:
                arr_EXCEPT.append(arr1[arrE])
            arrE+=1
        
        arr_EXCEPT.insert(0,arr1[0])           
       
        return arr_EXCEPT



def procesar_UNION_ALL(arr1,arr2):
    if len(arr1[0]) != len(arr2[0]):
        return "ERROR:  each UNION query must have the same number of columns\nSQL state: 42601"
    else:
        arrUNION_ALL = []
        i=1
        while i<len(arr1):
            arrUNION_ALL.append(arr1[i])
            i+=1
        j=1
        while j<len(arr2):
            arrUNION_ALL.append(arr2[j])
            j+=1

        
        arrUNION_ALL.insert(0,arr1[0])           
        
        return arrUNION_ALL

def find_ARR(line,arr):
    i=0
    while i < len(arr):
        if arr[i] == line:
            return False
        i+=1
    return True


def procesar_select_for_UNIONES(instr,ts,tc):
    global salida
    columnsTable = []
    arrayColumns = []
    tables = []
    arrayReturn = []
    #WHERE
    arrayWhere = []
    arrayFilter = []
    
    if  instr.instr1 != None and instr.instr2 == None and instr.instr3 == None and instr.listains == None and instr.listanombres != None:
        global salida
        
        if instr.instr1.etiqueta == OPCIONES_SELECT.DISTINCT:
            for datos in instr.instr1.listac:
                nada = 1
        if instr.instr1.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
            for datos in instr.instr1.lista_extras:
                if datos.etiqueta == OPCIONES_SELECT.CASE:
                    for objs in datos.listacase:
                        nada = 1

                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                    arrayColumns.append(datos.val)
                    nada = 1 # * 

                elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                    nada = 1
                    return datos.val
                else:
                    #print(datos.val) #RESTO DE ETIQUETAS
                    arrayColumns.append(datos.val)
        
        if instr.listanombres != []:
            for datos in instr.listanombres:
                if datos.etiqueta == TIPO_VALOR.DOBLE:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.AS_ID:
                    nada = 1
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 != None:
                    nada = 1
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 == None:
                    nada = 1
                    tables.append(datos.val)

        if '*' in arrayColumns:
            columnsTable = tc.obtenerColumns(useCurrentDatabase,tables[0])
            resultArray = j.extractTable(str(useCurrentDatabase),str(tables[0]))
            arrayReturn.append(columnsTable)
            for filas in resultArray:
                arrayReturn.append(filas)

            return arrayReturn
        else:
            columnsTable = tc.obtenerColumns(useCurrentDatabase,tables[0])
            resultArray = j.extractTable(str(useCurrentDatabase),str(tables[0]))
            arrayReturn.append(arrayColumns)
            for filasF in resultArray:
                #print(filasF)
                arrayTemp = []
                for colF in arrayColumns:
                    #print(filasF[columnsTable.index(colF)])
                    arrayTemp.append(filasF[columnsTable.index(colF)])
                    #print(colF)
                arrayReturn.append(arrayTemp)

            return arrayReturn

        

        

    

    
    elif instr.instr1 != None and instr.instr2 != None and instr.instr3 == None and instr.listains == None and instr.listanombres != None:
        
        arrayColumnsF = []
        if instr.instr1.etiqueta == OPCIONES_SELECT.DISTINCT:
            for datos in instr.instr1.listac:
                nada = 1
        if instr.instr1.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
            for datos in instr.instr1.lista_extras:
                if datos.etiqueta == OPCIONES_SELECT.CASE:
                    for objs in datos.listacase:
                        nada = 1 #SOLO ETIQUETAS
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                    #print(datos.val)
                    arrayColumnsF.append(datos.val)

                elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                    nada = 1
                else:
                    columnP = str(datos.val)+"."+str(datos.val1)
                    arrayColumnsF.append(columnP)

        arrayTablas = []
        if instr.listanombres != []:
            for datos in instr.listanombres:
                if datos.etiqueta == TIPO_VALOR.DOBLE:
                    nada = 1
                    #print(datos.val+'.'+datos.val1)
                elif datos.etiqueta == TIPO_VALOR.AS_ID: #TABLA AS T
                    nada = 1
                    arrayTablas.append([datos.val,datos.val1.val])
                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 != None: #TABLA T
                    arrayTablas.append([datos.val,datos.val1])
                elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 == None:
                    nada = 1
                    #print(datos.val)
            #print(arrayTablas)
            #tc.obtenerColumns(useCurrentDatabase,tables[0])
            arrayColumnsPrimera = tc.obtenerColumns(useCurrentDatabase,arrayTablas[0][0])
            arrayColumnsSegunda = tc.obtenerColumns(useCurrentDatabase,arrayTablas[1][0])

            arrayColumnsMerge = []
            arrC = 0
            while arrC < len(arrayTablas):
                if arrC == 0:
                    for arrCP in arrayColumnsPrimera:
                        columP = str(arrayTablas[0][1])+"."+str(arrCP)
                        arrayColumnsMerge.append(columP)
                if arrC == 1:
                    for arrCS in arrayColumnsSegunda:
                        columS = str(arrayTablas[1][1])+"."+str(arrCS)
                        arrayColumnsMerge.append(columS)
                arrC +=1

            columnsTable = arrayColumnsMerge
            #print(arrayColumnsMerge)

            arrayPrimera = j.extractTable(str(useCurrentDatabase),str(arrayTablas[0][0]))
            arraySegunda = j.extractTable(str(useCurrentDatabase),str(arrayTablas[1][0]))
            

            arrayMerge = []
            arrayMerge.append(arrayColumnsMerge)           
            arrP = 0
            while arrP < len(arrayPrimera):
                
                arrS = 0
                while arrS < len(arraySegunda):
                    arrFilas = []
                    arrPP = 0
                    while arrPP < len(arrayPrimera[arrP]):
                        arrFilas.append(arrayPrimera[arrP][arrPP])
                        arrPP +=1
                    arrSS = 0
                    while arrSS < len(arraySegunda[arrS]):
                        arrFilas.append(arraySegunda[arrS][arrSS])
                        arrSS +=1
                    #print(arrayPrimera[arrP],arraySegunda[arrS])
                    arrayMerge.append(arrFilas)
                    arrS+=1
                arrP +=1

            #print(arrayMerge)

                    
        if instr.instr2.expwhere != None:
            arrayFilterFilter = []
            arrayFilterFilter.append(arrayMerge[0])
            i = 1
            while i < len(arrayMerge):
                arrayTS = []
                arrayTS.append(arrayMerge[0])
                arrayTS.append(arrayMerge[i])
                val = resolver_expresion_logica(instr.instr2.expwhere.expresion,arrayTS)
                if val == 1:
                    arrayFilterFilter.append(arrayMerge[i])
                i+=1
        
            arrayFilter = arrayFilterFilter
            #print(instr.instr2.expwhere.expresion)
            #print(instr.instr2.expwhere.etiqueta)
            #print(instr.instr2.expwhere.expresion.etiqueta)

        if '*' in arrayColumnsF:
            for filas in arrayFilter:
                arrayReturn.append(filas)

            return arrayReturn
            

        else:
            for filasF in arrayFilter:
                #print(filasF)
                arrayTemp = []
                for colF in arrayColumnsF:
                    arrayTemp.append(filasF[columnsTable.index(colF)])
                    #print(colF)
                arrayReturn.append(arrayTemp)

            return arrayReturn

    elif instr.instr1 == None and instr.instr2 != None and instr.instr3 != None and instr.listains != None and instr.listanombres == None:
        
        if instr.instr2.etiqueta == OPCIONES_SELECT.DISTINCT:
            for datos in instr.instr2.listac:
                nada = 1
        if instr.instr2.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
            for datos in instr.instr2.lista_extras:
                if datos.etiqueta == OPCIONES_SELECT.CASE:
                    for objs in datos.listacase:
                        nada = 1 #SOLO ETIQUETAS
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                    nada = 1
                else:
                    nada = 1 #RESTO DE ETIQUETAS 

            if instr.instr3[0] == TIPO_VALOR.AS_ID:
                nada = 1
            elif instr.instr3[0] == TIPO_VALOR.DOBLE:
                nada = 1
            else:
                nada = 1   

            for objs in instr.listains:
                if objs.instr2 != None:
                    nada = 1
                    if objs.instr2.expwhere != None:
                        nada = 1
                    if objs.instr2.expgb != None:
                        nada = 1
                        for datos in objs.instr2.expgb.expresion:
                            nada = 1
                    if objs.instr2.expob != None:
                        nada = 1
                        for datos in objs.instr2.expob.expresion:
                            nada = 1
                    if objs.instr2.exphav != None:
                        nada = 1
                        nada = 1
                    if objs.instr2.exporden != None:
                        nada = 1
                        nada = 1
                    if objs.instr2.explimit != None:
                        nada = 1
                        if objs.instr2.explimit.expresion.etiqueta == TIPO_VALOR.NUMERO:
                            nada = 1
                        else:
                            nada = 1
                    if objs.instr2.expoffset != None:
                        nada = 1
                        nada = 1
                    if objs.instr2.valor != None:
                        nada = 1
                elif objs.instr2 == None:
                    nada = 1

    elif instr.instr1 != None and instr.instr2 == None and instr.instr3 != None and instr.listains != None and instr.listanombres == None:
        
        if instr.instr1.etiqueta == OPCIONES_SELECT.DISTINCT:
            for datos in instr.instr1.listac:
                nada = 1
        if instr.instr1.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
            for datos in instr.instr1.lista_extras:
                if datos.etiqueta == OPCIONES_SELECT.CASE:
                    for objs in datos.listacase:
                        nada = 1 #SOLO ETIQUETAS
                    nada = 1
                elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                    arrayColumns.append(datos.val) # *
                elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                    nada = 1
                else:
                    arrayColumns.append(datos.val) #IDS

        for objs in instr.listains:
            tables.append(objs.val) #tables


        columnsTable = tc.obtenerColumns(useCurrentDatabase,tables[0])
        resultArray = j.extractTable(str(useCurrentDatabase),str(tables[0]))
        arrayWhere = resultArray
        arrayWhere.insert(0,columnsTable)           

        if instr.instr3.expwhere != None:
            arrayFilter.append(arrayWhere[0])
            i = 1
            while i < len(arrayWhere):
                arrayTS = []
                arrayTS.append(arrayWhere[0])
                arrayTS.append(arrayWhere[i])
                val = resolver_expresion_logica(instr.instr3.expwhere.expresion,arrayTS)
                if val == 1:
                    arrayFilter.append(arrayWhere[i])
                i+=1
            
        #print(arrayFilter)

        if '*' in arrayColumns:
            for filas in arrayFilter:
                arrayReturn.append(filas)

            return arrayReturn

        else:
            for filasF in arrayFilter:
                #print(filasF)
                arrayTemp = []
                for colF in arrayColumns:
                    #print(filasF[columnsTable.index(colF)])
                    arrayTemp.append(filasF[columnsTable.index(colF)])
                    #print(colF)
                arrayReturn.append(arrayTemp)

            return arrayReturn

        if instr.instr3.expgb != None:
            nada = 1
            for datos in instr.instr3.expgb.expresion:
                nada = 1
        if instr.instr3.expob != None:
            nada = 1
            for datos in instr.instr3.expob.expresion:
                nada = 1
        if instr.instr3.exphav != None:
            nada = 1
        if instr.instr3.exporden != None:
            nada = 1
        if instr.instr3.explimit != None:
            nada = 1
            if instr.instr3.explimit.expresion.etiqueta == TIPO_VALOR.NUMERO:
                nada = 1
            else:
                nada = 1
        if instr.instr3.expoffset != None:
            nada = 1
            nada = 1
        if instr.instr3.valor != None:
            nada = 1


    elif instr.instr1 == None and instr.instr2 == None and instr.instr3 == None and instr.listains == None and instr.listanombres != None:
          
        for datos in instr.listanombres:
            #CON IDENTIFICADOR 
            if datos.expresion != None and datos.asterisco != None:
                
                if type(datos.asterisco) == list:
                    arrayReturn.append([datos.asterisco[1].val])
                    
                else:
                    arrayReturn.append([datos.asterisco])
                    


                if datos.expresion.operador == OPERACION_ARITMETICA.WIDTH_BUCKET:
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.E_DIV:
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])

                elif datos.expresion.operador == OPERACION_ARITMETICA.GCD:
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.MOD:
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.POWER:
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.TRUNC:
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2:
                    
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2D:
                    
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.SUBSTRING:
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.SUBSTR:
                    
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.GET_BYTE:
                    
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.SET_BYTE:
                    
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.ENCODE:
                    
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.DECODE:
                    
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                else:
                    ts = []
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                
                if datos.asterisco[0] == TIPO_VALOR.AS_ID:
                    nada = 1
                elif datos.asterisco[0] == TIPO_VALOR.DOBLE:
                    nada = 1
                else:
                    nada = 1

            #SIN IDENTIFICADOR
            if datos.expresion != None and datos.asterisco == None:
                if datos.expresion.operador == OPERACION_ARITMETICA.WIDTH_BUCKET:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.E_DIV:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.GCD:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.MOD:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.POWER:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.TRUNC:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])

                elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2D:
                    
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.SUBSTRING:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.SUBSTR:
                    
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.GET_BYTE:
                    
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.SET_BYTE:
                    
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.ENCODE:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                elif datos.expresion.operador == CADENA_BINARIA.DECODE:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])
                else:
                    ts = []
                    arrayReturn.append([datos.expresion.operador])
                    arrayReturn.append([resolver_expresion_aritmetica(datos.expresion,ts)])

        return arrayReturn

def procesar_index(instr, ts, tc,tsIndex):
    global salida
    
    buscar = tc.obtenerReturnTabla(useCurrentDatabase,instr.nombre_index)
    if buscar == False:
        salida = "\nERROR:  relation \"" + str(instr.nombre_index) +"\" does not exist\nSQL state: 42P01"
    else:
        #print('---------------- si entra al index ---------------------')
        if instr.etiqueta == INDEX.INDEX:
            columsAr = []
            colums = ""
            if type(instr.lista_index.identificador) == type([]):
                for lista in instr.lista_index.identificador:
                    columsAr.append(lista.val)

            else:
                columsAr.append(instr.lista_index.identificador)
            
            temp = TSINDEX.Simbolo(instr.identificador,'INDEX',instr.nombre_index,columsAr,instr.etiqueta)
            tsIndex.agregar(temp)
            salida = '\nCREATE INDEX'

        
        elif instr.etiqueta == INDEX.INDEX_WHERE:
            #print(instr.identificador)
            #print(instr.nombre_index)
            
            
            temp = TSINDEX.Simbolo(instr.identificador,'INDEX',instr.nombre_index,instr.lista_index.identificador,instr.etiqueta)
            tsIndex.agregar(temp)
            salida = '\nCREATE INDEX'

        elif instr.etiqueta == INDEX.INDEX_INCLUDE:
            #print(instr.identificador)
            #print(instr.nombre_index)

            temp = TSINDEX.Simbolo(instr.identificador,'INDEX',instr.nombre_index,instr.lista_index.identificador,instr.etiqueta)
            tsIndex.agregar(temp)
            salida = '\nCREATE INDEX'

        elif instr.etiqueta == INDEX.INDEX_UNIQUE_WHERE:
            #print(instr.identificador)
            #print(instr.nombre_index)
            
            temp = TSINDEX.Simbolo(instr.identificador,'INDEX',instr.nombre_index,instr.lista_index.identificador,instr.etiqueta)
            tsIndex.agregar(temp)
            salida = '\nCREATE INDEX'

        elif instr.etiqueta == INDEX.INDEX_INCLUDE:
            #print(instr.identificador)
            #print(instr.nombre_index)
            temp = TSINDEX.Simbolo(instr.identificador,'INDEX',instr.nombre_index,instr.lista_index.identificador,instr.etiqueta)
            tsIndex.agregar(temp)
            salida = '\nCREATE INDEX'

        elif instr.etiqueta == INDEX.INDEX_CLASS:
            #print(instr.identificador)
            #print(instr.nombre_index)
            temp = TSINDEX.Simbolo(instr.identificador,'INDEX',instr.nombre_index,instr.lista_index.identificador,instr.etiqueta)
            tsIndex.agregar(temp)
            salida = '\nCREATE INDEX'
    

    
    
    
    
def obtener_indexbody(instr):
    if instr.etiqueta == TIPO_INDEX.USING_HASH:
        nada = 1
    elif instr.etiqueta == TIPO_INDEX.CAMPOS:
        
        for datos in instr.identificador:
            nada = 1
        
    elif instr.etiqueta == TIPO_INDEX.NULLS:
        nada = 1
    elif instr.etiqueta == TIPO_INDEX.STATE:
        nada = 1
        nada = 1
    elif instr.etiqueta == TIPO_INDEX.LOWER:
        nada = 1
    elif instr.etiqueta == TIPO_INDEX.WITH_IDS:
        nada = 1
        nada = 1

def procesar_dropIndex(instr,ts,tc,tsIndex):
    if instr.lista_ids != []:
        for datos in instr.lista_ids:
            result = tsIndex.deleteIndex(datos.val)
            global salida
            if result == 0:
                global salida
                salida = "\nDROP INDEX"
            elif result == 1 :
                salida = "\nERROR:  index  \"" + str(datos.val) +"\" does not exist \nSQL state: 42704"

def procesar_AlterIndex(instr,ts,tc,tsIndex):
    global salida
    arrayList = tsIndex.getIds()
    if arrayList != []:
        bandera1 = False
        bandera2 = False
        if instr.oldName in arrayList:
            bandera1 = True
        else:
            bandera1 = False
            salida = "\nERROR:  relation \"" + str(instr.oldName) +"\" does not exist\nSQL state: 42P01"

        if instr.newName in arrayList:
            bandera2 = False
            salida = "\nERROR:  relation \"" + str(instr.newName) +"\" already exists\nSQL state: 42P07"
        else:
            bandera2 = True
        
        if bandera1 and bandera2:
            tsIndex.actualizarIndex(str(instr.oldName),str(instr.newName))
            salida = "\nALTER INDEX"

def procesar_AlterIndexColumn(instr,ts,tc,tsIndex):
    global salida
    arrayList = tsIndex.getIds()
    if arrayList != []:
        global salida

        bandera1 = False
        if instr.idIndex in arrayList:
            bandera1 = True
        else:
            bandera1 = False
            salida = "\nERROR:  relation \"" + str(instr.idIndex) +"\" does not exist\nSQL state: 42P01"
    
        if bandera1:
            indexId = tsIndex.obtenerIndex(instr.idIndex)
            arrayColumns = tc.obtenerColumns(useCurrentDatabase,indexId.tabla)
            columnaNew = None
            if (isinstance(instr.newColum,ExpresionIdentificador)):
                columnaNew = instr.newColum.val
            elif (isinstance(instr.newColum,ExpresionEntero)):
                numPos = instr.newColum.val - 1
                iPos = 0
                while iPos < len(arrayColumns):
                    if iPos == numPos:
                        columnaNew = arrayColumns[iPos]
                    iPos += 1

            tempcolumnas = indexId.columnas
            itmp = 0
            while itmp < len(tempcolumnas):
                if tempcolumnas[itmp] == instr.oldColumn:
                    tempcolumnas[itmp] = columnaNew
                itmp += 1
            
            newIndex = TSINDEX.Simbolo(indexId.id,indexId.tipo,indexId.tabla,tempcolumnas,indexId.restriccion)
            tsIndex.actualizarINDEXCOLUMN(newIndex,instr.idIndex)
            salida = "\nALTER INDEX"
    

def procesar_instrucciones(instrucciones,ts,tc,tsIndex) :
    try:
        global salida,useCurrentDatabase
        salida = ""
        ## lista de instrucciones recolectadas
        for instr in instrucciones :
            #CREATE DATABASE
            if isinstance(instr,CreateDatabase) : 
                procesar_createDatabase(instr,ts,tc)
            elif isinstance(instr, Create_Table) : 
                if useCurrentDatabase != "":
                    #print(useCurrentDatabase)
                    procesar_createTable(instr,ts,tc)
                else:
                    salida = "\nSELECT DATABASE"
            elif isinstance(instr, ExpresionRelacional) : 
                procesar_Expresion_Relacional(instr,ts,tc)
            elif isinstance(instr, Funcion_Index) :
                procesar_index(instr,ts,tc,tsIndex)
            elif isinstance(instr, Crear_Drop_INDEX) :
                procesar_dropIndex(instr,ts,tc,tsIndex)
            elif isinstance(instr, Create_AlterIndexColumn) :
                procesar_AlterIndexColumn(instr,ts,tc,tsIndex)
            elif isinstance(instr, Create_AlterIndex) :
                procesar_AlterIndex(instr,ts,tc,tsIndex)
            elif isinstance(instr, ExpresionBinaria) : 
                procesar_Expresion_Binaria(instr,ts,tc)
            elif isinstance(instr, ExpresionLogica) : 
                procesar_Expresion_logica(instr,ts,tc)
            elif isinstance(instr, showDatabases) : 
                procesar_showDatabases(instr,ts,tc)
            elif isinstance(instr, dropDatabase) : 
                procesar_dropDatabase(instr,ts,tc)
            elif isinstance(instr, useDatabase) : 
                procesar_useDatabase(instr,ts,tc)
            elif isinstance(instr, Create_Alterdatabase) :
                procesar_alterdatabase(instr,ts,tc)
            elif isinstance(instr, showTables) : 
                if useCurrentDatabase != "":
                    procesar_showTables(instr,ts,tc)
                else:
                    salida = "\nSELECT DATABASE"
            elif isinstance(instr,Create_update) : 
                procesar_update(instr,ts,tc)
            elif isinstance(instr, Crear_Drop) : 
                if useCurrentDatabase != "":
                    procesar_drop(instr,ts,tc)
                else:
                    salida = "\nSELECT DATABASE"
            elif isinstance(instr, Crear_altertable) :
                if useCurrentDatabase != "":
                    procesar_altertable(instr,ts,tc)
                else:
                    salida = "\nSELECT DATABASE"
            elif isinstance(instr, Definicion_Insert) :
                procesar_insert(instr,ts,tc)
            elif isinstance(instr, Create_type) :
                procesar_create_type(instr,ts,tc)
            elif isinstance(instr, Definicion_delete) :
                procesar_delete(instr,ts,tc)

            elif isinstance(instr, Create_select_time) : 
                procesar_select_time(instr,ts,tc)
            elif isinstance(instr,  Create_select_uno) : 
                procesar_select1(instr,ts,tc)
            elif isinstance(instr, Create_select_general) : 
                procesar_select_general(instr,ts,tc)
            elif isinstance(instr, Select_Uniones) : 
                procesar_select_uniones(instr,ts,tc)
        
            #SELECT 
            
            
            else : print('Error: instrucción no válida ' + str(instr[0]))
        return salida 
    except:
        pass

'''f = open("./entrada.txt", "r")
input = f.read()
instrucciones = g.parse(input)

if listaErrores == []:
    instrucciones_Global = instrucciones
    ts_global = TS.TablaDeSimbolos()
    tc_global = TC.TablaDeTipos()
    procesar_instrucciones(instrucciones,ts_global,tc_global)
    typeC = TipeChecker()
    typeC.crearReporte(tc_global)
    typeS = RTablaDeSimbolos()
    typeS.crearReporte(ts_global)
    astt = AST()
    astt.generarAST(instrucciones)
else:
    erroressss = ErrorHTML()
    erroressss.crearReporte()
    listaErrores = []
'''



