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

def calcularSelectCampos(arbol,ts):
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
        if(arbol.etiqueta == 'select_column_list'):
            if(arbol.hijos[0].etiqueta == 'function_tipo_ID'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ID.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   
            elif(arbol.hijos[0].etiqueta == 'function_tipo_NOW'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_CURRENT_DATE'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_DATE.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_CURRENT_TIME'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_TIME.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)  
            elif(arbol.hijos[0].etiqueta == 'function_tipo_OPMULT'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_ASTERISCO.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'DISTINCT_column_name_select'):
                expCampo = TS.ExpresionCampo(str(TS.TIPO_SELECT_CONDICION.DISTINCT.name),str(arbol.hijos[0].hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)                                 			
            else:
                calcularSelectCampos(arbol.hijos[0],ts)
        # elif(arbol.hijos[0].etiqueta == 'table_name_s'):
        #     ts.agregarTablaSelect(arbol.hijos[0].lexema)   
        # if(arbol.etiqueta == 'column_func_name_select'):
        #     if(arbol.hijos[0].etiqueta == 'function_tipo_ID'):
        #         calcularSelectCampos(arbol.hijos[0],ts)         
        return id
    

        #************************************
        #             ARBOL CON 2 HIJOS (BINARIO)
        #************************************    
    elif len(arbol.hijos) == 2:
        id = inc()
        if(arbol.etiqueta == 'SELECT_FROM'):

            if(arbol.hijos[0].etiqueta == 'table_name_s'):
                ts.agregarTablaSelect(arbol.hijos[0].lexema)   
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ID'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ID.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_NOW'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_CURRENT_DATE'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_DATE.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_CURRENT_TIME'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_TIME.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_OPMULT'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_ASTERISCO.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'DISTINCT_column_name_select'):
                expCampo = TS.ExpresionCampo(str(TS.TIPO_SELECT_CONDICION.DISTINCT.name),str(arbol.hijos[0].hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   
            elif(arbol.hijos[0].etiqueta == 'column_name_func'):
                if(arbol.hijos[0].hijos[0].etiqueta == 'select_function_element_ID' and arbol.hijos[0].hijos[1].etiqueta == 'column_select_punto'):
                    expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_PUNTO.name),str(arbol.hijos[0].hijos[0].lexema),arbol.hijos[0].hijos[1].hijos[0].lexema,None,None,None)
                ts.agregarCampoSelect(expCampo)     
            elif(arbol.hijos[0].etiqueta == 'function_tipo_RANDOM'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.RANDOM.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)                                			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ABS'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ABS.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)    


            else:
                calcularSelectCampos(arbol.hijos[0],ts)

            if(arbol.hijos[1].etiqueta == 'table_name_s'):
                ts.agregarTablaSelect(arbol.hijos[1].lexema)   
            elif(arbol.hijos[1].etiqueta == 'function_tipo_ID'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ID.name),str(arbol.hijos[1].lexema),None,None,None,None)                        
                ts.agregarCampoSelect(expCampo) 			
            elif(arbol.hijos[1].etiqueta == 'function_tipo_NOW'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[1].etiqueta == 'function_tipo_CURRENT_DATE'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_DATE.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[1].etiqueta == 'function_tipo_CURRENT_TIME'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_TIME.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)
            elif(arbol.hijos[1].etiqueta == 'function_tipo_OPMULT'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_ASTERISCO.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[1].etiqueta == 'DISTINCT_column_name_select'):
                expCampo = TS.ExpresionCampo(str(TS.TIPO_SELECT_CONDICION.DISTINCT.name),str(arbol.hijos[1].hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)                     			
            elif(arbol.hijos[1].etiqueta == 'column_name_func'):
                if(arbol.hijos[1].hijos[0].etiqueta == 'select_function_element_ID' and arbol.hijos[1].hijos[1].etiqueta == 'column_select_punto'):
                    expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_PUNTO.name),str(arbol.hijos[1].hijos[0].lexema),arbol.hijos[1].hijos[1].hijos[0].lexema,None,None,None)
                ts.agregarCampoSelect(expCampo)                   
            elif(arbol.hijos[1].etiqueta == 'function_tipo_RANDOM'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.RANDOM.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)                   
            else:
                calcularSelectCampos(arbol.hijos[1],ts)


        elif(arbol.etiqueta == 'select_column_list'):
            if(arbol.hijos[0].etiqueta == 'function_tipo_ID'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ID.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)  
            elif(arbol.hijos[0].etiqueta == 'function_tipo_NOW'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_CURRENT_DATE'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_DATE.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_CURRENT_TIME'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_TIME.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)
            elif(arbol.hijos[0].etiqueta == 'function_tipo_OPMULT'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_ASTERISCO.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[0].etiqueta == 'DISTINCT_column_name_select'):
                expCampo = TS.ExpresionCampo(str(TS.TIPO_SELECT_CONDICION.DISTINCT.name),str(arbol.hijos[0].hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)     
            elif(arbol.hijos[0].etiqueta == 'column_name_func'):
                if(arbol.hijos[0].hijos[0].etiqueta == 'select_function_element_ID' and arbol.hijos[0].hijos[1].etiqueta == 'column_select_punto'):
                    expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_PUNTO.name),str(arbol.hijos[0].hijos[0].lexema),arbol.hijos[0].hijos[1].hijos[0].lexema,None,None,None)
                ts.agregarCampoSelect(expCampo)  
            elif(arbol.hijos[0].etiqueta == 'function_tipo_RANDOM'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.RANDOM.name),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)                                                                     			
            else:
                calcularSelectCampos(arbol.hijos[0],ts)

            if(arbol.hijos[1].etiqueta == 'function_tipo_ID'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ID.name),str(arbol.hijos[1].lexema),None,None,None,None)                        
                ts.agregarCampoSelect(expCampo) 
            elif(arbol.hijos[1].etiqueta == 'function_tipo_NOW'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[1].etiqueta == 'function_tipo_CURRENT_DATE'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_DATE.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[1].etiqueta == 'function_tipo_CURRENT_TIME'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_TIME.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)      
            elif(arbol.hijos[1].etiqueta == 'function_tipo_OPMULT'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_ASTERISCO.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   			
            elif(arbol.hijos[1].etiqueta == 'DISTINCT_column_name_select'):
                expCampo = TS.ExpresionCampo(str(TS.TIPO_SELECT_CONDICION.DISTINCT.name),str(arbol.hijos[1].hijos[0].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)  
            elif(arbol.hijos[1].etiqueta == 'column_name_func'):
                if(arbol.hijos[1].hijos[0].etiqueta == 'select_function_element_ID' and arbol.hijos[1].hijos[1].etiqueta == 'column_select_punto'):
                    expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_PUNTO.name),str(arbol.hijos[1].hijos[0].lexema),arbol.hijos[1].hijos[1].hijos[0].lexema,None,None,None)
                ts.agregarCampoSelect(expCampo) 
            elif(arbol.hijos[1].etiqueta == 'function_tipo_RANDOM'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.RANDOM.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)   
                
                                            			
            else:
                calcularSelectCampos(arbol.hijos[1],ts)

        elif(arbol.etiqueta == 'column_name_select_AS_value_expression'):
                expCampo = TS.ExpresionCampo('AS',str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.agregarCampoSelect(expCampo)  


        elif(arbol.etiqueta == 'column_func_name_select'):
            if(arbol.hijos[0].etiqueta[14:]=='EXTRACT'):
                if(arbol.hijos[1].etiqueta =='column_datefuntion_select_from_timestamp'):
                    tipoExpExtract = arbol.hijos[1].hijos[0].lexema
                    valorExpExtract = arbol.hijos[1].hijos[1].lexema
                    expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.EXTRACT.name),tipoExpExtract,valorExpExtract,None,None,None)
                    ts.agregarCampoSelect(expCampo)
            else:
                expCampo = TS.ExpresionCampo(str(arbol.hijos[0].etiqueta[14:]),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarCampoSelect(expCampo)

        else:
            valorRetorno1 = str(calcularSelectCampos(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularSelectCampos(arbol.hijos[1],ts))                           
        return id
