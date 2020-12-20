from pandas.core.frame import DataFrame
from controllers.data_controller import *
from prettytable import PrettyTable
import pandas as pd 
def operating_list_number(array, environment):
    lista1 = []
    lista2 = []
    for index, _ in enumerate(array):
        lista1.append(array[index].process(environment))
        lista2.append(lista1[index].value)
    return lista2
def format_table_list(array, enviroment):
    
    lista1 = []
    for index, data in enumerate(array):
        lista1.append(data.alias)
    table_value = PrettyTable(list(lista1))
    lista1 = []
    for index, data in enumerate(array):
        valores = data.process(enviroment)
        lista1.append(valores.value)
    table_value.add_row(lista1)
    return str(table_value)

def loop_list(array, enviroment):
    lista1 = []
    for _, data in enumerate(array):
        valores = data.process(enviroment)
        lista1.append(valores.value)
    return lista1

def select_all(array,linea, column):
    database_id = SymbolTable().useDatabase
    if not database_id:
        desc = f": Database not selected"
        ErrorController().addExecutionError(4, 'Execution', desc, linea,column)#manejar linea y columna
        return None
        #Base de datos existe --> Obtener tabla
    table_tp = TypeChecker().searchTable(database_id, array[0])
    if not table_tp:
        desc = f": Table does not exists"
        ErrorController().addExecutionError(4, 'Execution', desc, linea , column)#manejar linea y columna
        return None
    table_cont = DataController().extractTable(array[0],linea,column)
    headers = TypeChecker().searchColumns(table_tp)
    tabla_select = pd.DataFrame(table_cont)
    # print(headers)
    tabla_select.columns = headers
    
    return tabla_select

def select_with_columns(columns, table):
    table_f = table[columns]
    return table_f

def format_df(df: DataFrame):
    table = PrettyTable([''] + list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    return str(table)
        
def width_bucket_func(numberToEvaluate, initRange, endRange, numberOfCubes):
    numberOfCubes += 0.0
    contador = 0
    initPointer = initRange
    intervalo = (endRange - initRange) / numberOfCubes
    rest = 0

    if((intervalo%1) == 0):   #Es entero
        rest = 1
    else:
        rest = getDecimals(intervalo)   #No es entero

    if numberToEvaluate < initRange:    #Si esta fuera de rango por ser menor al limite inf
        return 0

    if numberToEvaluate >= endRange:    #Si esta sobre el rango al exceder el limite sup
        return numberOfCubes + 1

    contador += 1

    while contador <= numberOfCubes:
        if (numberToEvaluate >= initPointer) and (numberToEvaluate <= (initPointer + intervalo - rest)):
            break
        else:
            initPointer = initPointer + intervalo
        contador += 1

    return contador

def obtain_string(array):
        alias = ""
        for index, data in enumerate(array):
            if index == len(array) - 1:
                alias += data.alias
            else:
                alias += data.alias + ","
        return alias 

def getDecimals(number):
    txt = str(number)
    contadorDecimales = 0.0
    contadorFinal = 0.0
    numbers = txt.split('.')
    decimales = str(numbers[1])

    for i in decimales:
	    contadorDecimales += 1

    for j in decimales:
        if(j == 0 and contadorDecimales == contadorFinal):
            break
        else:
	        contadorFinal += 1

    rest = 1 / (10**contadorFinal) 
    return rest

