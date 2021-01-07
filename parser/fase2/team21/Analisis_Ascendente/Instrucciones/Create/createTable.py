# from Instrucciones.instruccion import Instruccion
# from storageManager.jsonMode import *
# import Tabla_simbolos.TablaSimbolos as TS
from  tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from  tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
from  tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Create.Campo import Campo
from  tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos import Simbolo


# CREATE TABLE
#from Instrucciones.instruccion import Instruccion
#from storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as TS
from  tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from  tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
import  tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

#from Instrucciones.instruccion import Instruccion
tipos_de_dato = {
    'smallint': 'SMALLINT','integer': 'INTEGER', 'bigint': 'BIGINT','decimal': 'DECIMAL',
    'numeric': 'NUMERIC','double': 'DOUBLE','precision': 'PRECISION', 'real': 'REAL',
    'money': 'MONEY', 'text': 'TEXT', 'varying': 'VARYING', 'varchar': 'VARCHAR',
    'character': 'CHARACTER','char': 'CHAR','timestamp': 'TIMESTAMP',  'date': 'DATE',
    'time': 'TIME','interval': 'INTERVAL',  'year': 'YEAR', 'month': 'MONTH',
    'day': 'DAY', 'hour': 'HOUR', 'minute': 'MINUTE', 'second': 'SECOND',  'to': 'TO',
    'boolean': 'BOOLEAN', 'true': 'TRUE',  'false': 'FALSE', 'null': 'NULL','avg': 'AVG',
    'sum': 'SUM', 'distinct': 'DISTINCT','abs': 'ABS', 'cbrt': 'CBRT', 'ceil': 'CEIL',
    'ceiling': 'CEILING','degrees': 'DEGREES', 'div': 'DIV',  'exp': 'EXP',
    'factorial': 'FACTORIAL', 'floor': 'FLOOR',
    'gcd': 'GCD','lcm': 'LCM','ln': 'LN', 'log': 'LOG',
    'log10': 'LOG10', 'min_scale': 'MIN_SCALE',
    'mod': 'MOD',  'pi': 'PI', 'power': 'POWER', 'radians': 'RADIANS', 'round': 'ROUND',
    'scale': 'SCALE', 'sign': 'SIGN',
    'sqrt': 'SQRT','trim_scale': 'TRIM_SCALE','truc': 'TRUC',  'width_bucket': 'WIDTH_BUCKET',
    'random': 'RANDOM', 'setseed': 'SETSEED', 'max': 'MAX', 'min': 'MIN', 'acos': 'ACOS',
    'acosd': 'ACOSD', 'asin': 'ASIN','asind': 'ASIND','atan': 'ATAN','atand': 'ATAND',
    'atan2': 'ATAN2','atan2d': 'ATAN2D', 'cos': 'COS', 'cosd': 'COSD', 'cot': 'COT',
    'cotd': 'COTD', 'sin': 'SIN','sind': 'SIND','tan': 'TAN','tand': 'TAND', 'sinh': 'SINH',
    'cosh': 'COSH','tanh': 'TANH', 'asinh': 'ASINH','acosh': 'ACOSH', 'atanh': 'ATANH',
    'current_date': 'CURRENT_DATE','current_time': 'CURRENT_TIME',
    'date_part': 'date_part',
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',
    'unknown': 'UNKNOWN',
    'serial':'SERIAL',
    'md5':'MD5',
    'sing':'SING',
    'width_bucket':'WIDTH_BUCKET',
    'trunc':'TRUNC',
    'length':'LENGTH',
    'substring':'SUBSTRING',
    'trim':'TRIM',
    'sha256':'SHA256',
    'substr':'SUBSTR',
    'get_byte':'GET_BYTE',
    'set_byte':'SET_BYTE',
    'convert':'CONVERT',
    'encode':'ENCODE',
    'decode':'DECODE',
    'greatest':'GREATEST',
    'least':'LEAST'
}

#CREATE TABLE
class CreateTable(Instruccion):
    def __init__(self, id, campos, idInherits,concatena,fila,columna):
        self.id = id
        self.campos = campos
        self.idInherits = idInherits
        self.concatena = concatena
        self.fila = fila
        self.columna = columna


    def ejecutar(CreateTable, ts, consola, exceptions):

        if ts.validar_sim("usedatabase1234") == 1:


            # nombre de la bd
            bdactual = ts.buscar_sim("usedatabase1234")
            # se busca el simbolo y por lo tanto se pide el entorno de la bd
            BD = ts.buscar_sim(bdactual.valor)
            entornoBD = BD.Entorno




            if entornoBD.validar_sim(CreateTable.id) == 1:
                consola.append("42P07	duplicate_table\n")
                consola.append(f"22005	error_in_assignment,No se creo la tabla {CreateTable.id}\n")

                return


            # creo el entorno de la tabla
            print("Creando entorno tabla")
            nuevo_entorno_tabla = {}
            tsTabla = TS.TablaDeSimbolos(nuevo_entorno_tabla)
            # recorrer campos y le mando el entorno de la tabla quien es el que adentro de este
            # existaran los campos


            banderaTodoBien = True
            cantidad_columnas = len(CreateTable.campos)
            for campo in CreateTable.campos:

                if campo.caso == 2 or campo.caso == 3:
                    if entornoBD.validar_sim(campo.tablaR) == 1:
                        #referencia la tabla a cual se desea hacer la llave foranea
                        obtener_simbolo =entornoBD.buscar_sim(campo.tablaR)

                        entornoTablarefrencia = obtener_simbolo.Entorno

                        for campito in campo.idR:
                            if entornoTablarefrencia.validar_sim(campito.id) == 1:
                                print("todo bien")
                            else:
                                banderaTodoBien = False
                                break;

                        if banderaTodoBien:
                            print("todo esta bien")
                            banderaTodoBien = Campo.ejecutar(campo, tsTabla, consola, exceptions)
                            print(banderaTodoBien)
                            if campo.caso == 2 or campo.caso == 3 or campo.caso == 4:
                                cantidad_columnas = cantidad_columnas - 1
                            if not banderaTodoBien:
                                break

                    else:
                        banderaTodoBien= False

                else:
                    banderaTodoBien = Campo.ejecutar(campo, tsTabla, consola, exceptions)
                    print(banderaTodoBien)
                    if campo.caso == 2 or campo.caso==3 or campo.caso==4:
                        cantidad_columnas=cantidad_columnas-1
                    if not banderaTodoBien:
                        break

            if banderaTodoBien:

                if str(CreateTable.idInherits) != str(None):
                    print("---------",CreateTable.idInherits)
                    print(entornoBD.validar_sim(CreateTable.idInherits))
                    if entornoBD.validar_sim(CreateTable.idInherits) == 1:


                        simboloTabla = entornoBD.buscar_sim(CreateTable.idInherits)
                        entornoTablaPadre = simboloTabla.Entorno
                        lista_campos = entornoTablaPadre.simbolos
                        contador=0
                        for item in lista_campos:
                            simbolo_nuevo = TS.Simbolo(lista_campos.get(item).categoria,lista_campos.get(item).id,lista_campos.get(item).tipo,lista_campos.get(item).valor,lista_campos.get(item).Entorno)
                            tsTabla.agregar_sim(simbolo_nuevo)
                            contador=contador+1

                        nueva_tabla = TS.Simbolo(TS.TIPO_DATO.TABLA, CreateTable.id, None, cantidad_columnas+contador, tsTabla)
                        entornoBD.agregar_sim(nueva_tabla)
                        createTable(bdactual.valor, CreateTable.id, cantidad_columnas+contador)
                        columnas = tsTabla.simbolos
                        print("Agregando llaves primarias")
                        i = 0
                        pks = []
                        for columna in columnas:
                            print(columnas.get(columna).id)

                            for data in columnas.get(columna).valor:
                                print("     data: ", data)
                                if 'PRIMARYKEY' in data:
                                    pks.append(i)

                            i = i + 1
                        alterAddPK(BD.id, CreateTable.id, pks)
                        consola.append(f"Se creo la tabla {CreateTable.id}, exitosamente\n")

                    else:
                        consola.append(f"f42P16	invalid_table_definition, no se creo la tabla {CreateTable.id}")


                else:
                    nueva_tabla = TS.Simbolo(TS.TIPO_DATO.TABLA, CreateTable.id, None, cantidad_columnas, tsTabla)
                    entornoBD.agregar_sim(nueva_tabla)

                    createTable(bdactual.valor, CreateTable.id, cantidad_columnas)
                    columnas = tsTabla.simbolos
                    print("Agregando llaves primarias")
                    i = 0
                    pks = []
                    for columna in columnas:
                        print(columnas.get(columna).id)

                        for data in columnas.get(columna).valor:
                            print("     data: ",data)
                            if 'PRIMARYKEY' in data:
                                pks.append(i)

                        i = i +1
                    alterAddPK(BD.id, CreateTable.id, pks)
                    consola.append(f"Se creo la tabla {CreateTable.id}, exitosamente\n")

            else:
                consola.append(f"22005	error_in_assignment,No se creo la tabla {CreateTable.id} campos incosistente \n")
                exceptions.append("Error semantico-22005	error_in_assignment-Columnas check-fila-columna")


        else:

            consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")
            exceptions.append("Error semantico-22005	error_in_assignment-No se ha seleccionado DB-fila-columna")

    def traducir(CreateTable,consola,tv):

        #iniciar traduccion
        info = "" #info contiene toda el string a mandar como parametros
        print("concatena \n")
        print(CreateTable.concatena)
        obtenerTemporal = tv.Temp()

        for data in CreateTable.concatena:
            info += data

        consola.append(f"\n\t{obtenerTemporal} = f\" {info} ;\"")


        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({obtenerTemporal})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")

class Acompaniamiento(Instruccion):
    def __init__(self, tipo, valorDefault,fila,columna):
        self.tipo = tipo
        self.valorDefault = valorDefault
        self.fila = fila
        self.columna = columna

