import sys 
import ts as TS
import instrucciones as Instruccion
import tempfile
import calcularSelectCampos as selectcampos 
import calcularSelectGrupos as selectgrupos
import calcularSelectWhere as selectwhere
import calcularInsertValores as insertvalores
import calcularDelete as calculardeletevalores
from datetime import datetime
from pprint import pprint

lstResultado = []

contador = 1
x = 0

def inc():
    global x
    x += 1
    return x

def calcularUpdate(arbol,ts):
    global lstResultado
    global contador
    contador += 1

    print("--#Iniciando calcularSelect[" + str(contador)+"]"+"[\'\'\'"+str(arbol.etiqueta)+"]")

    if(arbol is not None and arbol.esHoja is not None and arbol.esHoja =='N'):
        if(arbol.etiqueta == 'set_clause'):
            ts.operacion_actual = 'set_clause'  
        

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
                calcularUpdate(arbol.hijos[0],ts)

        elif(arbol.etiqueta == 'insert_column_list1'):
            if(arbol.hijos[0].etiqueta == 'column_name'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ID),str(arbol.hijos[0].lexema),None,None,None,None)
                ts.agregarCamposInsert(expCampo)   			

            else:
                calcularUpdate(arbol.hijos[0],ts)
        else:
            calcularUpdate(arbol.hijos[0],ts)            

        #************************************
        #             ARBOL CON 2 HIJOS (BINARIO)
        #************************************    
    elif len(arbol.hijos) == 2:
        id = inc()
        if(arbol.etiqueta == 'set_clause'):

            if(arbol.hijos[0].etiqueta == 'column_name'):
                if(arbol.hijos[0].esHoja == 'S'):
                    temporal1 = str(arbol.hijos[0].lexema)
                    #ts.agregarTablaInsert(temporal)
                else:
                    calcularUpdate(arbol.hijos[0],ts)
                    temporal1 = ts.valor_temporal  
            elif(arbol.hijos[0].etiqueta == 'function_tipo_TRUE'):
                if(arbol.hijos[0].esHoja == 'S'):
                    temporal1 = str(arbol.hijos[0].lexema)
                    #ts.agregarTablaInsert(temporal)
                else:
                    calcularUpdate(arbol.hijos[0],ts)
                    temporal1 = ts.valor_temporal                     


            if(arbol.hijos[1].etiqueta == 'function_tipo_ENTERO'):
                if(arbol.hijos[1].esHoja == 'S'):
                    temporal2 = str(arbol.hijos[1].lexema)
                    #ts.agregarTablaInsert(temporal)
                else:
                    calcularUpdate(arbol.hijos[1],ts)
                    temporal2 = ts.valor_temporal  

            elif(arbol.hijos[1].etiqueta == 'function_tipo_TRUE'):
                if(arbol.hijos[1].esHoja == 'S'):
                    temporal2 = str(arbol.hijos[1].lexema)
                    #ts.agregarTablaInsert(temporal)
                else:
                    calcularUpdate(arbol.hijos[1],ts)
                    temporal2 = ts.valor_temporal  

            elif(arbol.hijos[1].etiqueta == 'function_tipo_FALSE'):
                if(arbol.hijos[1].esHoja == 'S'):
                    temporal2 = str(arbol.hijos[1].lexema)
                    #ts.agregarTablaInsert(temporal)
                else:
                    calcularUpdate(arbol.hijos[1],ts)
                    temporal2 = ts.valor_temporal                     


            if(arbol.hijos[1].etiqueta == 'column_func_name_select'):
                if(arbol.hijos[1].esHoja == 'S'):
                    temporal2 = str(arbol.hijos[1].lexema)
                    #ts.agregarTablaInsert(temporal)
                else:
                    calcularUpdate(arbol.hijos[1],ts)
                    temporal2 = ts.valor_temporal  
                expCampo = TS.ExpresionCampo("set",temporal1, '=',temporal2.expresion1,temporal2.expresion2,None)
                ts.agregarCampoUpdate(expCampo) 
                return 1 



            expCampo = TS.ExpresionCampo("set",temporal1, '=',temporal2,None,None)
            ts.agregarCampoUpdate(expCampo)  
            

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
                calcularUpdate(arbol.hijos[0],ts)

            if(arbol.hijos[1].etiqueta == 'value_list'):
                ts.agregarValoresInsert(arbol.hijos[1].lexema) 
            elif(arbol.hijos[1].etiqueta == 'func_MD5'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.MD5.name),str(arbol.hijos[1].hijos[0].lexema),str(arbol.hijos[1].hijos[1].lexema),None,None,None)
                ts.agregarValoresInsert(expCampo)  
            elif(arbol.hijos[1].etiqueta == 'func_NOW'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.hijos[1].lexema),None,None,None,None)
                ts.agregarValoresInsert(expCampo)                     
            else:
                calcularUpdate(arbol.hijos[1],ts)


        elif(arbol.etiqueta == 'insert_column_list1'):

            if(arbol.hijos[0].etiqueta == 'column_name'):
                ts.agregarCamposInsert(arbol.hijos[0].lexema)   
            else:
                calcularUpdate(arbol.hijos[0],ts)

            if(arbol.hijos[1].etiqueta == 'column_name'):
                ts.agregarCamposInsert(arbol.hijos[1].lexema) 
            else:
                calcularUpdate(arbol.hijos[1],ts)


        elif(arbol.etiqueta == 'column_func_name_select'):

            if(arbol.hijos[0].etiqueta == 'function_tipo_SIN'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SIN.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1
            elif(arbol.hijos[0].etiqueta == 'function_tipo_COS'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.COS.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1
            elif(arbol.hijos[0].etiqueta == 'function_tipo_SIND'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SIND.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                
            elif(arbol.hijos[0].etiqueta == 'function_tipo_TAN'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.TAN.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                    
            elif(arbol.hijos[0].etiqueta == 'function_tipo_TAND'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.TAND.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ABS'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ABS.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                    
            elif(arbol.hijos[0].etiqueta == 'function_tipo_CBRT'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CBRT.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1      
            elif(arbol.hijos[0].etiqueta == 'function_tipo_CEIL'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CEIL.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                      
            elif(arbol.hijos[0].etiqueta == 'function_tipo_CEILING'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CEILING.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1            
            elif(arbol.hijos[0].etiqueta == 'function_tipo_DEGREES'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.DEGREES.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                    
            elif(arbol.hijos[0].etiqueta == 'function_tipo_DIV'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.DIV.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                            
            elif(arbol.hijos[0].etiqueta == 'function_tipo_EXP'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.EXP.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                            
            elif(arbol.hijos[0].etiqueta == 'function_tipo_factorial'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.FACTORIAL.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1   
            elif(arbol.hijos[0].etiqueta == 'function_tipo_FLOOR'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.FLOOR.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
            elif(arbol.hijos[0].etiqueta == 'function_tipo_gcd'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.GCD.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_LN'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.LN.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_LOG'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.LOG.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_MOD'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.MOD.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_PI'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.PI.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_POWER'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.POWER.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_RADIANS'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.RADIANS.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ROUND'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ROUND.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_SIGN'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SIGN.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_SQRT'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SQRT.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_TRUNC'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.TRUNC.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_RANDOM'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.RANDOM.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ACOS'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ACOS.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ASIN'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ASIN.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ASIND'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ASIND.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ATAN'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ATAN.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ATAND'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ATAND.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ATAN2'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ATAN2.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ATAN2D'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ATAN2D.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    


            elif(arbol.hijos[0].etiqueta == 'function_tipo_COSD'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.COSD.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_COT'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.COT.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_COTd'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.COTD.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_sinh'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SINH.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_COSH'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.COSH.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_TANH'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.TANH.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_asinh'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ASINH.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ACOSH'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ACOSH.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			
            elif(arbol.hijos[0].etiqueta == 'function_tipo_ATANH'):
                expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ATANH.name),str(arbol.hijos[0].lexema),str(arbol.hijos[1].lexema),None,None,None)
                ts.valor_temporal = expCampo
                return 1                                                    
			                
            # if(arbol.hijos[0].etiqueta == 'column_name'):
            #     ts.agregarCamposInsert(arbol.hijos[0].lexema)   
            # else:
            #     calcularUpdate(arbol.hijos[0],ts)

            # if(arbol.hijos[1].etiqueta == 'column_name'):
            #     ts.agregarCamposInsert(arbol.hijos[1].lexema) 
            # else:
            #     calcularUpdate(arbol.hijos[1],ts)

              

        else:
            valorRetorno1 = str(calcularUpdate(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularUpdate(arbol.hijos[1],ts))                           
        return id

    elif len(arbol.hijos) == 3:
        id = inc()
        if(arbol.hijos[0].etiqueta == 'table_name'):
            if(arbol.hijos[0].esHoja == 'S'):
                temporal = str(arbol.hijos[0].lexema)
                ts.agregarTablaInsert(temporal)
            else:
                calcularUpdate(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal

        elif(arbol.hijos[0].etiqueta == 'set_clause'):
            if(arbol.hijos[0].esHoja == 'S'):
                temporal = str(arbol.hijos[0].lexema)
                ts.agregarCampoSelect(temporal)
            else:
                calcularUpdate(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal


        if(arbol.hijos[0].etiqueta == 'set_clause_list'):
            if(arbol.hijos[0].esHoja == 'S'):
                temporal = str(arbol.hijos[0].lexema)
                ts.agregarTablaInsert(temporal)
            else:
                calcularUpdate(arbol.hijos[1],ts)
                temporal1 = ts.valor_temporal                   

        elif(arbol.hijos[0].etiqueta =='WHERE_CONDITION'):
            selectwhere.calcularSelectWhere(arbol.hijos[0],ts)


        if(arbol.hijos[1].etiqueta == 'table_name'):
            if(arbol.hijos[1].esHoja == 'S'):
                temporal = str(arbol.hijos[1].lexema)
                ts.agregarTablaInsert(temporal)
            else:
                calcularUpdate(arbol.hijos[1],ts)
                temporal1 = ts.valor_temporal

        elif(arbol.hijos[1].etiqueta == 'set_clause'):
            if(arbol.hijos[1].esHoja == 'S'):
                temporal = str(arbol.hijos[1].lexema)
                ts.agregarCampoSelect(temporal)
            else:
                calcularUpdate(arbol.hijos[1],ts)
                #temporal1 = ts.valor_temporal

        if(arbol.hijos[1].etiqueta == 'set_clause_list'):
            if(arbol.hijos[1].esHoja == 'S'):
                temporal = str(arbol.hijos[1].lexema)
                ts.agregarTablaInsert(temporal)
            else:
                calcularUpdate(arbol.hijos[1],ts)
                temporal1 = ts.valor_temporal


        elif(arbol.hijos[1].etiqueta =='WHERE_CONDITION'):
            selectwhere.calcularSelectWhere(arbol.hijos[1],ts)




        if(arbol.hijos[2].etiqueta =='table_name'):
            selectcampos.calcularSelectCampos(arbol.hijos[2],ts)


        elif(arbol.hijos[2].etiqueta == 'set_clause'):
            if(arbol.hijos[2].esHoja == 'S'):
                temporal = str(arbol.hijos[2].lexema)
                ts.agregarCampoSelect(temporal)
            else:
                calcularUpdate(arbol.hijos[2],ts)
                temporal1 = ts.valor_temporal

        if(arbol.hijos[2].etiqueta == 'set_clause_list'):
            if(arbol.hijos[2].esHoja == 'S'):
                temporal = str(arbol.hijos[2].lexema)
                ts.agregarTablaInsert(temporal)
            else:
                calcularUpdate(arbol.hijos[2],ts)
                temporal1 = ts.valor_temporal                

        elif(arbol.hijos[2].etiqueta =='WHERE_CONDITION'):
            selectwhere.calcularSelectWhere(arbol.hijos[2],ts)


        return id
