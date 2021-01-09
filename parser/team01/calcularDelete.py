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
    

def calcularDelete(arbol,ts):
    global lstResultado
    global contador
    contador += 1

    print("--#Iniciando calcularSelect[" + str(contador)+"]"+"[\'\'\'"+str(arbol.etiqueta)+"]")

    if(arbol is not None and arbol.esHoja is not None and arbol.esHoja =='N'):
        if(arbol.etiqueta == 'select_colum_list'):
            ts.operacion_actual = TS.TIPO_SELECT_CAMPOS.COLUMNAS  
        

    if(arbol is not None and arbol.esHoja is not None and arbol.esHoja =='S'):
            #estamos en el subarbol de tablas
        if(arbol.etiqueta == 'table_name_d'):
            ts.operacion_actual = TS.TIPO_SELECT_CAMPOS.TABLAS
    #region
    if len(arbol.hijos) == 1:
        id = inc()
        #arbol.hijos[0].etiquetaPadre = arbol.etiqueta
        if(arbol.etiqueta =='in_value_list'):
            if(arbol.hijos[0].esHoja == 'S'):
                ts.valor_temporal = arbol.hijos[0].lexema
            else:
                calcularDelete(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal
        else:              
            valorRetorno = str(calcularDelete(arbol.hijos[0],ts))

        if(arbol.etiqueta == 'WHERE_CONDITION'):
            if(hasattr(ts, 'TIPO_SELECT_CONDICION') and ts.TIPO_SELECT_CONDICION == TS.TIPO_SELECT_CONDICION.COMPARACION) :
                if(len(ts.lstcondiciones) == 0) :
                    ts.agregarCondicionDelete(ts.valor_temporal)         
        return id


    elif len(arbol.hijos) == 2:
        id = inc()
        if(arbol.etiqueta == 'delete_statement'):

            if(arbol.hijos[0].etiqueta == 'table_name_d'):
                if(arbol.hijos[0].esHoja == 'S'):
                    temporal = str(arbol.hijos[0].lexema)
                    ts.agregarTablaDelete(temporal)
                else:
                    calcularDelete(arbol.hijos[0],ts)
                    temporal1 = ts.valor_temporal  

            elif(arbol.hijos[0].etiqueta == 'insert_columns_and_source'):
                calcularDelete(arbol.hijos[0],ts)
            else:
                calcularDelete(arbol.hijos[0],ts)



            if(arbol.hijos[1].etiqueta == 'table_name_d'):
                if(arbol.hijos[1].esHoja == 'S'):
                    temporal = str(arbol.hijos[1].lexema)
                    ts.agregarTablaDelete(temporal)
                else:
                    calcularDelete(arbol.hijos[1],ts)
                    temporal1 = ts.valor_temporal  

            elif(arbol.hijos[1].etiqueta == 'insert_columns_and_source'):
                calcularDelete(arbol.hijos[1],ts)
            else:
                calcularDelete(arbol.hijos[1],ts)

        elif(arbol.etiqueta == 'in_value_list'):

            # str(calcularDelete(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = str(arbol.hijos[0].lexema)
            else:
                calcularDelete(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal             

            # str(calcularDelete(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal.valor
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = str(arbol.hijos[1].lexema)
            else:
                calcularDelete(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal             


            ts.valor_temporal = temporal1+','+temporal2
        else:
            valorRetorno1 = str(calcularDelete(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularDelete(arbol.hijos[1],ts))


    elif len(arbol.hijos) == 3:
        id = inc()

        if(arbol.etiqueta == 'comparison_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.COMPARACION

            #se valida si se puede obtener directamente la hoja o hay que sintetizar
            # str(calcularDelete(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].etiqueta == 'value_expression'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularDelete(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal.valor

            if(arbol.hijos[1].etiqueta == 'comp_op'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularDelete(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal.valor

            if(arbol.hijos[2].etiqueta == 'value_expression'):
                temporal3 = arbol.hijos[2].lexema
            elif(arbol.hijos[2].etiqueta == 'fun_now'):
                temporal3 = 'now'                
            else:
                calcularDelete(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal.valor
            
            #se almacena como un temporal porque probablemente existan mas item como lista 
            #valTemp = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.COMPARACION)
            #ts.valor_temporal.valor = TS.ValorTemporal(valTemp, None)
            #expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.IN)
            # ts.agregarCondicionDelete(expIn) 
            #ts.agregarCondicionDelete(expComparacion)
            valTemp = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.COMPARACION)
            ts.valor_temporal = TS.ValorTemporal(valTemp, None)            

        elif(arbol.etiqueta == 'search_condition'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.COMPARACION

            # valorRetorno1 = str(calcularDelete(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularDelete(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal            

            #valorRetorno2 = str(calcularDelete(arbol.hijos[1],ts))
            #temporal2 = arbol.hijos[1].lexema
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularDelete(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal            

            # valorRetorno3 = str(calcularDelete(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularDelete(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal              

            #Como es item unico se envía directamente a la lista de comparación
            #expComparacion = TS.ExpresionListaComparadores(temporal1,temporal2,temporal3)
            valTemp = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.COMPARACION)
            ts.valor_temporal.valor = TS.ValorTemporal(valTemp, None)            

            #ts.agregarCondicionDelete(expComparacion)   
        elif(arbol.etiqueta == 'boolean_term'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.COMPARACION

            # valorRetorno1 = str(calcularDelete(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularDelete(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal              

            # valorRetorno2 = str(calcularDelete(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal.valor
            if(arbol.hijos[1].etiqueta == 'opAnd' or arbol.hijos[1].etiqueta == 'opOr'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularDelete(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal.valor

            # valorRetorno3 = str(calcularDelete(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularDelete(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal                

            expComparacion = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.COMPARACION)

            ts.valor_temporal = expComparacion

        elif(arbol.etiqueta == 'in_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.IN

            # str(calcularDelete(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularDelete(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal                


            if(arbol.hijos[1].etiqueta == 'predicatein'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularDelete(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal.valor

            # str(calcularDelete(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularDelete(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal                

            expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.IN)
            ts.agregarCondicionDelete(expIn) 
        # elif(arbol.etiqueta == 'null_predicate'):
        #     ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.NULL

        #     str(calcularDelete(arbol.hijos[0],ts))
        #     temporal1 = ts.valor_temporal.valor

        #     str(calcularDelete(arbol.hijos[1],ts))
        #     temporal2 = ts.valor_temporal.valor

        #     str(calcularDelete(arbol.hijos[2],ts))
        #     temporal3 = ts.valor_temporal.valor

            # expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.NULL)
            # ts.agregarCondicionDelete(expIn)                     
        elif(arbol.etiqueta == 'like_percent_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.LIKE

            #str(calcularDelete(arbol.hijos[0],ts))
            temporal1 = arbol.hijos[0]

            #str(calcularDelete(arbol.hijos[1],ts))
            temporal2 = arbol.hijos[1]

            #str(calcularDelete(arbol.hijos[2],ts))
            temporal3 = arbol.hijos[2]

            expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.LIKE)
            ts.agregarCondicionDelete(expIn)
        elif(arbol.etiqueta == 'column_reference'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.SUBSTRING

            temporal1 = arbol.hijos[0].lexema
            temporal2 = arbol.hijos[1].lexema
            temporal3 = arbol.hijos[2].lexema

            # str(calcularDelete(arbol.hijos[3],ts))
            # temporal4 = ts.valor_temporal.valor
            
            #se almacena como un temporal porque probablemente existan mas item como lista 
            ts.valor_temporal = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.SUBSTRING)                                         
        else:
                valorRetorno1 = str(calcularDelete(arbol.hijos[0],ts))
                valorRetorno2 = str(calcularDelete(arbol.hijos[1],ts))
                valorRetorno3 = str(calcularDelete(arbol.hijos[2],ts))    
        return id
                                                
        #************************************
        #             ARBOL CON 4 HIJOS 
        #************************************  
    
    elif len(arbol.hijos) == 4:
        id = inc()

        if(arbol.etiqueta == 'null_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.NOT_NULL

            # str(calcularDelete(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularDelete(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal                

            # str(calcularDelete(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal.valor
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularDelete(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal                

            # str(calcularDelete(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularDelete(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal                

            # str(calcularDelete(arbol.hijos[3],ts))
            # temporal4 = ts.valor_temporal.valor                  
            if(arbol.hijos[3].esHoja == 'S'):
                temporal4 = arbol.hijos[3].lexema
            else:
                calcularDelete(arbol.hijos[3],ts)
                temporal4 = ts.valor_temporal                

            expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,temporal4,TS.TIPO_SELECT_CONDICION.NOT_NULL)
            ts.agregarCondicionDelete(expIn)                     
        elif(arbol.etiqueta == 'substring_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.SUBSTRING


            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularDelete(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal


            # str(calcularDelete(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularDelete(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal


            # str(calcularDelete(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularDelete(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal            

            # str(calcularDelete(arbol.hijos[3],ts))
            # temporal4 = ts.valor_temporal                    
            if(arbol.hijos[3].esHoja == 'S'):
                temporal4 = arbol.hijos[3].lexema
            else:
                calcularDelete(arbol.hijos[3],ts)
                temporal4 = ts.valor_temporal            

            expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,temporal4,TS.TIPO_SELECT_CONDICION.SUBSTRING)
            ts.agregarCondicionDelete(expIn)                    
        else:
            valorRetorno1 = str(calcularDelete(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularDelete(arbol.hijos[1],ts))
            valorRetorno3 = str(calcularDelete(arbol.hijos[2],ts))
            valorRetorno4 = str(calcularDelete(arbol.hijos[3],ts))

        return id


        #************************************
        #             ARBOL CON 5 HIJOS 
        #************************************  
    
    elif len(arbol.hijos) == 5:
        id = inc()

        #region
        if(arbol.etiqueta == 'between_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.BETWEEN
            temporal1 = arbol.hijos[0].lexema
            temporal2 = arbol.hijos[1].lexema
            temporal3 = arbol.hijos[2].lexema
            temporal4 = arbol.hijos[3].lexema                        
            temporal5 = arbol.hijos[4].lexema


            expComparacion = TS.ExpresionComparacion(temporal3,temporal1,temporal5,None,TS.TIPO_SELECT_CONDICION.BETWEEN)
            ts.agregarCondicionDelete(expComparacion) 
        elif(arbol.etiqueta == 'distinct_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.DISTINCT
            temporal1 = arbol.hijos[0].lexema
            temporal2 = arbol.hijos[1].lexema
            temporal3 = arbol.hijos[2].lexema
            temporal4 = arbol.hijos[3].lexema                        
            temporal5 = arbol.hijos[4].lexema


            expComparacion = TS.ExpresionComparacion(temporal3,temporal1,temporal5,None,TS.TIPO_SELECT_CONDICION.DISTINCT)
            ts.agregarCondicionDelete(expComparacion)                       
        #endregion
        else:
            valorRetorno1 = str(calcularDelete(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularDelete(arbol.hijos[1],ts))
            valorRetorno3 = str(calcularDelete(arbol.hijos[2],ts))
            valorRetorno4 = str(calcularDelete(arbol.hijos[3],ts))
            valorRetorno5 = str(calcularDelete(arbol.hijos[4],ts))

        return id


        #************************************
        #             ARBOL CON 6 HIJOS 
        #************************************
    
    elif len(arbol.hijos) == 6:
        id = inc()
        #region
        if(arbol.etiqueta == 'between_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.NOT_BETWEEN

            # str(calcularDelete(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularDelete(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal  

            # str(calcularDelete(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal.valor
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularDelete(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal              

            # str(calcularDelete(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularDelete(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal              

            # str(calcularDelete(arbol.hijos[3],ts))
            # temporal4 = ts.valor_temporal.valor
            if(arbol.hijos[3].esHoja == 'S'):
                temporal4 = arbol.hijos[3].lexema
            else:
                calcularDelete(arbol.hijos[3],ts)
                temporal4 = ts.valor_temporal              

            # str(calcularDelete(arbol.hijos[4],ts))
            # temporal5 = ts.valor_temporal.valor
            if(arbol.hijos[4].esHoja == 'S'):
                temporal5 = arbol.hijos[4].lexema
            else:
                calcularDelete(arbol.hijos[4],ts)
                temporal5 = ts.valor_temporal              

            # str(calcularDelete(arbol.hijos[5],ts))
            # temporal6 = ts.valor_temporal.valor                    
            if(arbol.hijos[5].esHoja == 'S'):
                temporal6 = arbol.hijos[5].lexema
            else:
                calcularDelete(arbol.hijos[5],ts)
                temporal6 = ts.valor_temporal  

            expComparacion = TS.ExpresionComparacion(temporal4,temporal1,temporal6,None,TS.TIPO_SELECT_CONDICION.NOT_BETWEEN)
            ts.agregarCondicionDelete(expComparacion)   
        #endregion
        else:
            valorRetorno1 = str(calcularDelete(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularDelete(arbol.hijos[1],ts))
            valorRetorno3 = str(calcularDelete(arbol.hijos[2],ts))
            valorRetorno4 = str(calcularDelete(arbol.hijos[3],ts))
            valorRetorno5 = str(calcularDelete(arbol.hijos[4],ts))
            valorRetorno6 = str(calcularDelete(arbol.hijos[5],ts))                        

