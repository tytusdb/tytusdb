from parserT28.models.objects.id import Id
from parserT28.models.objects.table_select import TablaSelect
from parserT28.models.objects.columns_select import ColumnsSelect
from pandas.core.frame import DataFrame
from parserT28.controllers.data_controller import *
from prettytable import PrettyTable
import pandas as pd


def operating_list_number(array, environment):
    try:
        lista1 = []
        lista2 = []
        for index, _ in enumerate(array):
            lista1.append(array[index].process(environment))
            lista2.append(lista1[index].value)
        return lista2
    except:
        desc = "FATAL ERROR, Funciones Select"
        ErrorController().add(34, 'Execution', desc, 0, 0)


def format_table_list(array: list):
    try:
        table_value = PrettyTable(array[0])
        table_value.add_row(array[1])
        return str(table_value)
    except:
        desc = "FATAL ERROR, Funciones Select"
        ErrorController().add(34, 'Execution', desc, 0, 0)


def list_expressions(array, enviroment):
    lista1 = []
    lista2 = []
    lista3 = []
    try:
        for _, data in enumerate(array):
            valores = data.process(enviroment)
            lista1.append(valores.value)
            lista2.append(data.alias)
        lista3.append(lista2)
        lista3.append(lista1)
        return lista3
    except:
        desc = "FATAL ERROR, Funciones Select"
        ErrorController().add(34, 'Execution', desc, 0, 0)


def list_expressions_groupby(array, enviroment):
    lista1 = []  # lista para columnas
    lista2 = []  # lista para el dictionario
    lista3 = []  # lista para los heders
    lista4 = []  # lista para los alias generales
    lista5 = []
    try:
        for _, data in enumerate(array):
            valores = data.process(enviroment)
            if isinstance(valores, list):
                if len(valores) == 3:
                    if valores[1] == "*":
                        lista2.append(valores[0])
                        lista4.append(data.alias)

                    else:
                        lista1.append(valores[0])
                        lista2.append(valores[2])
                        lista3.append(valores[1])
                        lista4.append(data.alias)
                else:
                    lista1.append(valores[0])
                    lista3.append(valores[1])
                    lista4.append(data.alias)

        if len(lista1) == len(lista3):
            dictionary = convert_dictionary(lista3, lista1)
            table = pd.DataFrame(dictionary)
            print(table)
            lista5.append(table)
            lista5.append(lista2)
            lista5.append(lista4)
            lista5.append(lista3)
            return lista5
    except:
        desc = "FATAL ERROR, Funciones Select"
        ErrorController().add(34, 'Execution', desc, 0, 0)
    # lista3.append(lista2)
    # lista3.append(lista1)
    # return lista3


def loop_list(array, enviroment):
    lista1 = []
    lista_alias = []
    tabla = None
    try:
        for _, data in enumerate(array):
            valores = data.process(enviroment)
            if isinstance(valores, DataFrame):
                tabla = valores
            else:
                lista1.append(valores.value)
                lista_alias.append(valores.alias)
        if len(lista1) >= 1:
            return [lista1, lista_alias]
        else:
            return tabla
    except:
        desc = "FATAL ERROR, Funciones Select"
        ErrorController().add(34, 'Execution', desc, 0, 0)


def loop_list_of_order_by(array, enviroment):
    lista1 = []
    try:
        for _, data in enumerate(array):
            valores = data.process(enviroment)
            if isinstance(valores, list):
                lista1.append(valores[1])
            else:
                lista1.append(valores.value)
        print(lista1)
        return lista1
    except:
        desc = "FATAL ERROR, Funciones Select"
        ErrorController().add(34, 'Execution', desc, 0, 0)


def loop_list_with_columns(array, name, enviroment):
    lista1 = []
    result = []
    alias = []
    valores = None
    try:
        name_column = ""
        # hora de simplificar esta mierda xd
        for _, data in enumerate(array):
            if hasattr(data, 'is_group'):
                if len(array) > 1:
                    desc = "FATAL ERROR,  must appear in the GROUP BY clause or be used in an aggregate function"
                    ErrorController().add(34, 'Execution', desc, 0, 0)
                    return
                else:
                    data.is_group = True
                    valores = data.process(enviroment)
                    if valores == "*":
                        valor = search_symbol(name).name.length
                        valor = [valor+1]
                        lista1.append(valor)
                        alias.append(data.alias)
                        dictionary = convert_dictionary(alias, lista1)
                        table = pd.DataFrame(dictionary)
                        return table

            else:
                valores = data.process(enviroment)
            if isinstance(valores, list):
                lista1.append(valores[0])
                alias.append(data.alias)
            else:
                result.append(valores.value)
                alias.append(data.alias)

        valor = search_symbol(name).name
        lista2 = []

        lista1 = results_list_select_columns(valor, result, lista2, lista1)
        if len(lista1) == len(alias):
            dictionary = convert_dictionary(alias, lista1)
            table = pd.DataFrame(dictionary)
            return table
    except:
        desc = "FATAL ERROR, Funciones Select"
        ErrorController().add(34, 'Execution', desc, 0, 0)


def results_list_select_columns(valor, lista1, lista2, result_list):
    count = 0
    if isinstance(valor, TablaSelect):
        for aux_value in lista1:
            while True:
                if count > valor.length:
                    break
                lista2.append(aux_value)
                count += 1
            count = 0
            result_list.append(lista2)
            lista2 = []
    return result_list


def convert_dictionary(array1, array2):
    dictionary = {}
    if len(array1) == len(array2):
        for index, data in enumerate(array2):
            dictionary[array1[index]] = data
    # print(dictionary) working uwu
    return dictionary


def select_all(table_for_type_checker, linea, column, name_tabla):
    database_id = SymbolTable().useDatabase
    lista = []
    if not database_id:
        desc = f": Database not selected"
        ErrorController().add(4, 'Execution', desc, linea,
                              column)  # manejar linea y columna
        return None
        # Base de datos existe --> Obtener tabla
    table_tp = TypeChecker().searchTable(database_id, table_for_type_checker)
    if not table_tp:
        desc = f": Table does not exists"
        ErrorController().add(4, 'Execution', desc, linea,
                              column)  # manejar linea y columna
        return None
    table_cont = DataController().extractTable(
        table_for_type_checker, linea, column)

    headers = TypeChecker().searchColumnHeadings(table_tp)

    storage_columns(table_cont, headers, linea, column)
    storage_table(table_cont, headers, name_tabla, linea, column)

    tabla_select = pd.DataFrame(table_cont)
    # print(headers)
    tabla_select.columns = headers

    return tabla_select


def storage_columns(table_cont, headers, linea, column):
    count = 0
    lista = []
    lista_aux = []
    while True:
        if count > len(headers) - 1:
            break
        for _, c in enumerate(table_cont):
            lista.append(c[count])
        lista_aux.append(lista)
        lista = []
        count += 1

    for index, data in enumerate(headers):
        valor = ColumnsSelect(lista_aux[index])
        if search_duplicate_symbol(data, valor):
            pass
        else:
            SymbolTable().add(valor, data, 'Columns_Select', None, None, linea, column)


def storage_table(table_cont, headers, name,  linea, column):
    lista = []
    for _, c in enumerate(table_cont):
        lista.append(c)

    valor = TablaSelect(lista, len(lista)-1, headers)

    if search_duplicate_symbol(name, valor):
        pass
    else:
        SymbolTable().add(valor, name, 'Tabla_Select', None, None, linea, column)


def search_duplicate_symbol(name, valor: object):
    for index, c in enumerate(SymbolTable().getList()):
        if c.value == name and (c.dataType == 'Tabla_Select' or c.dataType == 'Columns_Select') and valor != None:
            # print('Entro')
            SymbolTable().getList()[index].name = valor
            return True
        elif c.value == name and (c.dataType != 'Tabla_Select' and c.dataType != 'Columns_Select') and valor == None:
            return True
    return False


def search_symbol(name):
    for _, c in enumerate(SymbolTable().getList()):
        if c.value == name and c.dataType != 'ID':
            return c
    return None


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

    if((intervalo % 1) == 0):  # Es entero
        rest = 1
    else:
        rest = getDecimals(intervalo)  # No es entero

    if numberToEvaluate < initRange:  # Si esta fuera de rango por ser menor al limite inf
        return 0

    if numberToEvaluate >= endRange:  # Si esta sobre el rango al exceder el limite sup
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
