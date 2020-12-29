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
    

def calcularSelectWhere(arbol,ts):
    global lstResultado
    global contador
    contador += 1


    print("--#Iniciando calcular[" + str(contador)+"]"+"[\'\'\'"+str(arbol.etiqueta)+"]")
    if arbol.esHoja == 'S':
        if len(arbol.hijos) == 1:
            id = inc()

            simbolo = TS.Simbolo(str(arbol.etiqueta), TS.TIPO_DATO.ETIQUETA, str(arbol.lexema)) 
            ts.agregar(simbolo)

            #********************* HOJAS PARA UNA SENTENCIA SELECT **************
            if(ts.tipo_operacion == TS.TIPO_OPERACION.SELECT) :

                #estamos en una hoja de la seccion campos, almacenamos en lista campos
                if(ts.operacion_actual == TS.TIPO_SELECT.CAMPOS) :
                    if(arbol.etiqueta == 'column_name_func' or arbol.etiqueta == 'select_function_element') :
                        ts.valor_temporal = TS.ValorTemporal(str(arbol.lexema), str(arbol.etiqueta))
                
                    #se comento ya que daba error en lista de id...
                    # elif(arbol.etiqueta == 'column_name_id' or arbol.etiqueta == 'value_expression') :
                    #     ts.valor_temporal = TS.ValorTemporal(str(arbol.lexema), str(arbol.etiqueta))
                    elif(arbol.etiqueta == 'column_name_opmult') :
                        ts.valor_temporal = TS.ValorTemporal(str(arbol.lexema), str(arbol.etiqueta))                        
                        expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.SELECT_ASTERISCO.name),str(arbol.lexema),None,None,None,None)
                        ts.agregarCampoSelect(expCampo)

                    elif(arbol.etiqueta == 'column_name_now') :
                        ts.valor_temporal = TS.ValorTemporal(str(arbol.lexema), str(arbol.etiqueta))                        
                        expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.NOW.name),str(arbol.lexema),None,None,None,None)
                        ts.agregarCampoSelect(expCampo)                        

                    elif(arbol.etiqueta == 'column_name_current_date') :
                        ts.valor_temporal = TS.ValorTemporal(str(arbol.lexema), str(arbol.etiqueta))                        
                        expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_DATE.name),str(arbol.lexema),None,None,None,None)
                        ts.agregarCampoSelect(expCampo)   

                    elif(arbol.etiqueta == 'column_name_current_time') :
                        ts.valor_temporal = TS.ValorTemporal(str(arbol.lexema), str(arbol.etiqueta))                        
                        expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.CURRENT_TIME.name),str(arbol.lexema),None,None,None,None)
                        ts.agregarCampoSelect(expCampo)                                                

                    elif(arbol.etiqueta == 'column_name_random') :
                        ts.valor_temporal = TS.ValorTemporal(str(arbol.lexema), str(arbol.etiqueta))                        
                        expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.RANDOM.name),str(arbol.lexema),None,None,None,None)
                        ts.agregarCampoSelect(expCampo)    

                    else:
                        expCampo = TS.ExpresionCampo(str(TS.CAMPO_FUNCION.ID.name),str(arbol.lexema),None,None,None,None)
                        ts.agregarCampoSelect(expCampo)
                        #ts.agregarCampoSelect(str(arbol.lexema))

                #estamos en una hoja de la sección tablas, alamcenamos en lista tablas
                elif(ts.operacion_actual == TS.TIPO_SELECT.TABLAS) :
                    ts.agregarTablaSelect(str(arbol.lexema))

                #estamos en una hoja de la sección condicion, enviamos como temporal el valor
                elif(ts.operacion_actual == TS.TIPO_SELECT.CONDICION) :
                    ts.valor_temporal = TS.ValorTemporal(str(arbol.lexema), str(arbol.etiqueta))

                #estamos en una hoja de la seccion grupo, almacenamos en lista grupo
                elif(ts.operacion_actual == TS.TIPO_SELECT.GRUPO) :
                    ts.agregarGrupoSelect(str(arbol.lexema))
            return id
        elif len(arbol.hijos) > 1 :
            id = inc()
            if len(arbol.hijos) == 3 :
                if(ts.tipo_operacion == TS.TIPO_OPERACION.SELECT and ts.operacion_actual == TS.TIPO_SELECT.CONDICION) :
                    if(arbol.etiqueta == 'like_percent_predicate') :
                        ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.IN
                        expComparacion = TS.ExpresionListaComparadores(str(arbol.hijos[0]),str(arbol.hijos[1]),str(arbol.hijos[2]))
                        ts.agregarCondicionSelect(expComparacion)
            else :
                for x in range(0,len(arbol.hijos)):
                    pass
                    # dot.edge(str(id),'#'+str(id)+'[' +str(arbol.hijos[x])+']')
                return id   

    #region
    elif len(arbol.hijos) == 1:
        id = inc()
        #arbol.hijos[0].etiquetaPadre = arbol.etiqueta
        if(arbol.etiqueta =='in_value_list'):
            if(arbol.hijos[0].esHoja == 'S'):
                ts.valor_temporal = arbol.hijos[0].lexema
            else:
                calcularSelectWhere(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal
        else:              
            valorRetorno = str(calcularSelectWhere(arbol.hijos[0],ts))

        if(arbol.etiqueta == 'WHERE_CONDITION'):
            if(hasattr(ts, 'TIPO_SELECT_CONDICION') and ts.TIPO_SELECT_CONDICION == TS.TIPO_SELECT_CONDICION.COMPARACION) :
                if(len(ts.lstcondiciones) == 0) :
                    ts.agregarCondicionSelect(ts.valor_temporal)         
            else:
                #se utiliza pruebas
                ts.agregarCondicionSelect(ts.valor_temporal)         
        return id


    elif len(arbol.hijos) == 2:
        id = inc()
        if(arbol.etiqueta == 'in_value_list'):

            # str(calcularSelectWhere(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = str(arbol.hijos[0].lexema)
            else:
                calcularSelectWhere(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal             

            # str(calcularSelectWhere(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal.valor
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = str(arbol.hijos[1].lexema)
            else:
                calcularSelectWhere(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal             


            ts.valor_temporal = temporal1+','+temporal2
        else:
            valorRetorno1 = str(calcularSelectWhere(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularSelectWhere(arbol.hijos[1],ts))


    elif len(arbol.hijos) == 3:
        id = inc()

        if(arbol.etiqueta == 'comparison_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.COMPARACION

            #se valida si se puede obtener directamente la hoja o hay que sintetizar
            # str(calcularSelectWhere(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].etiqueta == 'value_expression'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularSelectWhere(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal.valor

            if(arbol.hijos[1].etiqueta == 'comp_op'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularSelectWhere(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal.valor

            if(arbol.hijos[2].etiqueta == 'value_expression'):
                temporal3 = arbol.hijos[2].lexema
            elif(arbol.hijos[2].etiqueta == 'fun_now'):
                temporal3 = 'now'                
            else:
                calcularSelectWhere(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal.valor
            
            #se almacena como un temporal porque probablemente existan mas item como lista 
            #valTemp = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.COMPARACION)
            #ts.valor_temporal.valor = TS.ValorTemporal(valTemp, None)
            #expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.IN)
            # ts.agregarCondicionSelect(expIn) 
            #ts.agregarCondicionSelect(expComparacion)
            valTemp = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.COMPARACION)
            ts.valor_temporal = TS.ValorTemporal(valTemp, None)            

        elif(arbol.etiqueta == 'search_condition'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.COMPARACION

            # valorRetorno1 = str(calcularSelectWhere(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                if(arbol.hijos[0].etiqueta == 'like_percent_predicate'):
                    ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.IN
                    expComparacion = TS.ExpresionListaComparadores(str(arbol.hijos[0].hijos[0]),str(arbol.hijos[0].hijos[1]),str(arbol.hijos[0].hijos[2]))
                    ts.agregarCondicionSelect(expComparacion)
                    temporal1 = ts.valor_temporal
            else:
                calcularSelectWhere(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal            

            #valorRetorno2 = str(calcularSelectWhere(arbol.hijos[1],ts))
            #temporal2 = arbol.hijos[1].lexema
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularSelectWhere(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal            

            # valorRetorno3 = str(calcularSelectWhere(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularSelectWhere(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal              

            #Como es item unico se envía directamente a la lista de comparación
            #expComparacion = TS.ExpresionListaComparadores(temporal1,temporal2,temporal3)
            expComparacion = TS.ExpresionListaComparadores(temporal1,temporal2,temporal3)
            #ts.valor_temporal.valor = TS.ValorTemporal(valTemp, None)            

            ts.agregarCondicionSelect(expComparacion)   
        elif(arbol.etiqueta == 'boolean_term'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.COMPARACION

            # valorRetorno1 = str(calcularSelectWhere(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularSelectWhere(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal              

            # valorRetorno2 = str(calcularSelectWhere(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal.valor
            if(arbol.hijos[1].etiqueta == 'opAnd'): # or arbol.hijos[1].etiqueta == 'opOr'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularSelectWhere(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal.valor

            # valorRetorno3 = str(calcularSelectWhere(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularSelectWhere(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal                

            expComparacion = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.COMPARACION)

            ts.valor_temporal = expComparacion

        elif(arbol.etiqueta == 'in_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.IN

            # str(calcularSelectWhere(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularSelectWhere(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal                


            if(arbol.hijos[1].etiqueta == 'predicatein'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularSelectWhere(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal.valor

            # str(calcularSelectWhere(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularSelectWhere(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal                

            expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.IN)
            ts.agregarCondicionSelect(expIn) 
        # elif(arbol.etiqueta == 'null_predicate'):
        #     ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.NULL

        #     str(calcularSelectWhere(arbol.hijos[0],ts))
        #     temporal1 = ts.valor_temporal.valor

        #     str(calcularSelectWhere(arbol.hijos[1],ts))
        #     temporal2 = ts.valor_temporal.valor

        #     str(calcularSelectWhere(arbol.hijos[2],ts))
        #     temporal3 = ts.valor_temporal.valor

            # expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.NULL)
            # ts.agregarCondicionSelect(expIn)                     
        elif(arbol.etiqueta == 'like_percent_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.LIKE

            #str(calcularSelectWhere(arbol.hijos[0],ts))
            temporal1 = arbol.hijos[0]

            #str(calcularSelectWhere(arbol.hijos[1],ts))
            temporal2 = arbol.hijos[1]

            #str(calcularSelectWhere(arbol.hijos[2],ts))
            temporal3 = arbol.hijos[2]

            expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.LIKE)
            ts.agregarCondicionSelect(expIn)
        elif(arbol.etiqueta == 'column_reference'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.SUBSTRING

            temporal1 = arbol.hijos[0].lexema
            temporal2 = arbol.hijos[1].lexema
            temporal3 = arbol.hijos[2].lexema

            # str(calcularSelectWhere(arbol.hijos[3],ts))
            # temporal4 = ts.valor_temporal.valor
            
            #se almacena como un temporal porque probablemente existan mas item como lista 
            ts.valor_temporal = TS.ExpresionComparacion(temporal1,temporal2,temporal3,None,TS.TIPO_SELECT_CONDICION.SUBSTRING)                                         
        else:
                valorRetorno1 = str(calcularSelectWhere(arbol.hijos[0],ts))
                valorRetorno2 = str(calcularSelectWhere(arbol.hijos[1],ts))
                valorRetorno3 = str(calcularSelectWhere(arbol.hijos[2],ts))    
        return id
                                                
        #************************************
        #             ARBOL CON 4 HIJOS 
        #************************************  
    
    elif len(arbol.hijos) == 4:
        id = inc()

        if(arbol.etiqueta == 'null_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.NOT_NULL

            # str(calcularSelectWhere(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularSelectWhere(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal                

            # str(calcularSelectWhere(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal.valor
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularSelectWhere(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal                

            # str(calcularSelectWhere(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularSelectWhere(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal                

            # str(calcularSelectWhere(arbol.hijos[3],ts))
            # temporal4 = ts.valor_temporal.valor                  
            if(arbol.hijos[3].esHoja == 'S'):
                temporal4 = arbol.hijos[3].lexema
            else:
                calcularSelectWhere(arbol.hijos[3],ts)
                temporal4 = ts.valor_temporal                

            expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,temporal4,TS.TIPO_SELECT_CONDICION.NOT_NULL)
            ts.agregarCondicionSelect(expIn)                     
        elif(arbol.etiqueta == 'substring_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.SUBSTRING


            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularSelectWhere(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal


            # str(calcularSelectWhere(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularSelectWhere(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal


            # str(calcularSelectWhere(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularSelectWhere(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal            

            # str(calcularSelectWhere(arbol.hijos[3],ts))
            # temporal4 = ts.valor_temporal                    
            if(arbol.hijos[3].esHoja == 'S'):
                temporal4 = arbol.hijos[3].lexema
            else:
                calcularSelectWhere(arbol.hijos[3],ts)
                temporal4 = ts.valor_temporal            

            expIn = TS.ExpresionComparacion(temporal1,temporal2,temporal3,temporal4,TS.TIPO_SELECT_CONDICION.SUBSTRING)
            ts.agregarCondicionSelect(expIn)                    
        else:
            valorRetorno1 = str(calcularSelectWhere(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularSelectWhere(arbol.hijos[1],ts))
            valorRetorno3 = str(calcularSelectWhere(arbol.hijos[2],ts))
            valorRetorno4 = str(calcularSelectWhere(arbol.hijos[3],ts))

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
            #ts.agregarCondicionSelect(expComparacion) 
            #valTemp = TS.ExpresionComparacion(temporal1, None, None,None,TS.TIPO_SELECT_CONDICION.COMPARACION)
            ts.valor_temporal = TS.ValorTemporal(expComparacion, None)               
        elif(arbol.etiqueta == 'distinct_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.DISTINCT
            temporal1 = arbol.hijos[0].lexema
            temporal2 = arbol.hijos[1].lexema
            temporal3 = arbol.hijos[2].lexema
            temporal4 = arbol.hijos[3].lexema                        
            temporal5 = arbol.hijos[4].lexema


            expComparacion = TS.ExpresionComparacion(temporal3,temporal1,temporal5,None,TS.TIPO_SELECT_CONDICION.DISTINCT)
            ts.agregarCondicionSelect(expComparacion)                       
        #endregion
        else:
            valorRetorno1 = str(calcularSelectWhere(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularSelectWhere(arbol.hijos[1],ts))
            valorRetorno3 = str(calcularSelectWhere(arbol.hijos[2],ts))
            valorRetorno4 = str(calcularSelectWhere(arbol.hijos[3],ts))
            valorRetorno5 = str(calcularSelectWhere(arbol.hijos[4],ts))

        return id


        #************************************
        #             ARBOL CON 6 HIJOS 
        #************************************
    
    elif len(arbol.hijos) == 6:
        id = inc()
        #region
        if(arbol.etiqueta == 'between_predicate'):
            ts.TIPO_SELECT_CONDICION = TS.TIPO_SELECT_CONDICION.NOT_BETWEEN

            # str(calcularSelectWhere(arbol.hijos[0],ts))
            # temporal1 = ts.valor_temporal.valor
            if(arbol.hijos[0].esHoja == 'S'):
                temporal1 = arbol.hijos[0].lexema
            else:
                calcularSelectWhere(arbol.hijos[0],ts)
                temporal1 = ts.valor_temporal  

            # str(calcularSelectWhere(arbol.hijos[1],ts))
            # temporal2 = ts.valor_temporal.valor
            if(arbol.hijos[1].esHoja == 'S'):
                temporal2 = arbol.hijos[1].lexema
            else:
                calcularSelectWhere(arbol.hijos[1],ts)
                temporal2 = ts.valor_temporal              

            # str(calcularSelectWhere(arbol.hijos[2],ts))
            # temporal3 = ts.valor_temporal.valor
            if(arbol.hijos[2].esHoja == 'S'):
                temporal3 = arbol.hijos[2].lexema
            else:
                calcularSelectWhere(arbol.hijos[2],ts)
                temporal3 = ts.valor_temporal              

            # str(calcularSelectWhere(arbol.hijos[3],ts))
            # temporal4 = ts.valor_temporal.valor
            if(arbol.hijos[3].esHoja == 'S'):
                temporal4 = arbol.hijos[3].lexema
            else:
                calcularSelectWhere(arbol.hijos[3],ts)
                temporal4 = ts.valor_temporal              

            # str(calcularSelectWhere(arbol.hijos[4],ts))
            # temporal5 = ts.valor_temporal.valor
            if(arbol.hijos[4].esHoja == 'S'):
                temporal5 = arbol.hijos[4].lexema
            else:
                calcularSelectWhere(arbol.hijos[4],ts)
                temporal5 = ts.valor_temporal              

            # str(calcularSelectWhere(arbol.hijos[5],ts))
            # temporal6 = ts.valor_temporal.valor                    
            if(arbol.hijos[5].esHoja == 'S'):
                temporal6 = arbol.hijos[5].lexema
            else:
                calcularSelectWhere(arbol.hijos[5],ts)
                temporal6 = ts.valor_temporal  

            expComparacion = TS.ExpresionComparacion(temporal4,temporal1,temporal6,None,TS.TIPO_SELECT_CONDICION.NOT_BETWEEN)
            ts.agregarCondicionSelect(expComparacion)   
        #endregion
        else:
            valorRetorno1 = str(calcularSelectWhere(arbol.hijos[0],ts))
            valorRetorno2 = str(calcularSelectWhere(arbol.hijos[1],ts))
            valorRetorno3 = str(calcularSelectWhere(arbol.hijos[2],ts))
            valorRetorno4 = str(calcularSelectWhere(arbol.hijos[3],ts))
            valorRetorno5 = str(calcularSelectWhere(arbol.hijos[4],ts))
            valorRetorno6 = str(calcularSelectWhere(arbol.hijos[5],ts))                        

