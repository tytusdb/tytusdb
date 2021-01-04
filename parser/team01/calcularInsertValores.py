import sys 
import ts as TS
import instrucciones as Instruccion
import tempfile
from datetime import datetime
from pprint import pprint

lstResultado = []

contador = 1
x = 0

def inc():
    global x
    x += 1
    return x

def calcularInsertCampos(arbol,ts):
    global lstResultado
    global contador
    contador += 1

    print("--#Iniciando calcularSelect[" + str(contador)+"]"+"[\'\'\'"+str(arbol.etiqueta)+"]")

    if(arbol is not None and arbol.esHoja is not None and arbol.esHoja =='N'):
        if(arbol.etiqueta == 'select_colum_list'):
            ts.operacion_actual = TS.TIPO_SELECT_CAMPOS.COLUMNAS  
        

    if(arbol is not None and arbol.esHoja is not None and arbol.esHoja =='S'):
            #estamos en el subarbol de tablas
        if(arbol.etiqueta == 'table_name_s'):
            ts.operacion_actual = TS.TIPO_SELECT_CAMPOS.TABLAS

    #************************************
    #             ARBOL CON UN SOLO HIJO (UNARIO)
    #************************************
    
    if len(arbol.hijos) == 1:
        id = inc()
        if(arbol.etiqueta == 'value_list1'):
            if(arbol.hijos[0].etiqueta == 'func_NOW'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarValoresInsert(expCampo)   
            elif(arbol.hijos[0].etiqueta == 'func_MD5'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.MD5.name),str(arbol.hijos[0].hijos[0].lexema),str(arbol.hijos[0].hijos[1].lexema),None,None,None)
                ts.agregarValoresInsert(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'value_list'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ID),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarValoresInsert(expCampo)   			

            else:
                calcularInsertCampos(arbol.hijos[0],ts)

        elif(arbol.etiqueta == 'insert_column_list1'):
            if(arbol.hijos[0].etiqueta == 'column_name'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ID),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCamposInsert(expCampo)   			

            else:
                calcularInsertCampos(arbol.hijos[0],ts)
        else:
            calcularInsertCampos(arbol.hijos[0],ts)            

        #************************************
        #             ARBOL CON 2 HIJOS (BINARIO)
        #************************************    
    elif len(arbol.hijos) == 2:
        id = inc()
        if(arbol.etiqueta == 'insert_statement'):

            if(arbol.hijos[0].etiqueta == 'table_name'):
                if(arbol.hijos[0].esHoja == 'S'):
                    temporal = str(arbol.hijos[0].lexema)
                    ts.agregarTablaInsert(temporal)
                else:
                    calcularInsertCampos(arbol.hijos[0],ts)
                    temporal1 = ts.valor_temporal  

            elif(arbol.hijos[0].etiqueta == 'insert_columns_and_source'):
                calcularInsertCampos(arbol.hijos[0],ts)
            else:
                calcularInsertCampos(arbol.hijos[0],ts)



            if(arbol.hijos[1].etiqueta == 'table_name'):
                if(arbol.hijos[1].esHoja == 'S'):
                    temporal = str(arbol.hijos[1].lexema)
                    ts.agregarTablaInsert(temporal)
                else:
                    calcularInsertCampos(arbol.hijos[1],ts)
                    temporal1 = ts.valor_temporal  

            elif(arbol.hijos[1].etiqueta == 'insert_columns_and_source'):
                calcularInsertCampos(arbol.hijos[1],ts)
            else:
                calcularInsertCampos(arbol.hijos[1],ts)

        elif(arbol.etiqueta == 'value_list1'):

            if(arbol.hijos[0].etiqueta == 'value_list'):
                ts.agregarValoresInsert(arbol.hijos[0].lexema)   
            elif(arbol.hijos[0].etiqueta == 'func_MD5'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.MD5.name),str(arbol.hijos[0].hijos[0].lexema),str(arbol.hijos[0].hijos[1].lexema),None,None,None)
                ts.agregaagregarValoresInsertrCampoInsert(expCampo)  
            elif(arbol.hijos[0].etiqueta == 'func_NOW'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarValoresInsert(expCampo)                    			
            else:
                calcularInsertCampos(arbol.hijos[0],ts)

            if(arbol.hijos[1].etiqueta == 'value_list'):
                ts.agregarValoresInsert(arbol.hijos[1].lexema) 
            elif(arbol.hijos[1].etiqueta == 'func_MD5'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.MD5.name),str(arbol.hijos[1].hijos[0].lexema),str(arbol.hijos[1].hijos[1].lexema),None,None,None)
                ts.agregarValoresInsert(expCampo)  
            elif(arbol.hijos[1].etiqueta == 'func_NOW'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarValoresInsert(expCampo)                     
            else:
                calcularInsertCampos(arbol.hijos[1],ts)




        elif(arbol.etiqueta == 'insert_column_list1'):

            if(arbol.hijos[0].etiqueta == 'column_name'):
                ts.agregarCamposInsert(arbol.hijos[0].lexema)   
            else:
                calcularInsertCampos(arbol.hijos[0],ts)

            if(arbol.hijos[1].etiqueta == 'column_name'):
                ts.agregarCamposInsert(arbol.hijos[1].lexema) 
            else:
                calcularInsertCampos(arbol.hijos[1],ts)
                
        else:
            valorRetorno1 = str(calcularInsertCampos(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularInsertCampos(arbol.hijos[1],ts))                           
        return id
