from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.storageManager.jsonMode import *
from Analisis_Ascendente.Instrucciones.expresion import * #Expresion
from Analisis_Ascendente.Instrucciones.expresion import Primitivo
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

tipos_de_dato = {
    'smallint': 'SMALLINT', 'integer': 'INTEGER', 'bigint': 'BIGINT', 'decimal': 'DECIMAL',
    'numeric': 'NUMERIC', 'double': 'DOUBLE', 'precision': 'PRECISION', 'real': 'REAL',
    'money': 'MONEY', 'text': 'TEXT', 'varying': 'VARYING', 'varchar': 'VARCHAR',
    'character': 'CHARACTER', 'char': 'CHAR', 'timestamp': 'TIMESTAMP', 'date': 'DATE',
    'time': 'TIME', 'interval': 'INTERVAL', 'year': 'YEAR', 'month': 'MONTH',
    'day': 'DAY', 'hour': 'HOUR', 'minute': 'MINUTE', 'second': 'SECOND', 'to': 'TO',
    'boolean': 'BOOLEAN', 'true': 'TRUE', 'false': 'FALSE', 'null': 'NULL', 'avg': 'AVG',
    'sum': 'SUM', 'distinct': 'DISTINCT', 'abs': 'ABS', 'cbrt': 'CBRT', 'ceil': 'CEIL',
    'ceiling': 'CEILING', 'degrees': 'DEGREES', 'div': 'DIV', 'exp': 'EXP',
    'factorial': 'FACTORIAL', 'floor': 'FLOOR',
    'gcd': 'GCD', 'lcm': 'LCM', 'ln': 'LN', 'log': 'LOG',
    'log10': 'LOG10', 'min_scale': 'MIN_SCALE',
    'mod': 'MOD', 'pi': 'PI', 'power': 'POWER', 'radians': 'RADIANS', 'round': 'ROUND',
    'scale': 'SCALE', 'sign': 'SIGN',
    'sqrt': 'SQRT', 'trim_scale': 'TRIM_SCALE', 'truc': 'TRUC', 'width_bucket': 'WIDTH_BUCKET',
    'random': 'RANDOM', 'setseed': 'SETSEED', 'max': 'MAX', 'min': 'MIN', 'acos': 'ACOS',
    'acosd': 'ACOSD', 'asin': 'ASIN', 'asind': 'ASIND', 'atan': 'ATAN', 'atand': 'ATAND',
    'atan2': 'ATAN2', 'atan2d': 'ATAN2D', 'cos': 'COS', 'cosd': 'COSD', 'cot': 'COT',
    'cotd': 'COTD', 'sin': 'SIN', 'sind': 'SIND', 'tan': 'TAN', 'tand': 'TAND', 'sinh': 'SINH',
    'cosh': 'COSH', 'tanh': 'TANH', 'asinh': 'ASINH', 'acosh': 'ACOSH', 'atanh': 'ATANH',
    'current_date': 'CURRENT_DATE', 'current_time': 'CURRENT_TIME',
    'date_part': 'date_part',
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',
    'unknown': 'UNKNOWN',
    'serial': 'SERIAL',
    'md5': 'MD5',
    'sing': 'SING',
    'width_bucket': 'WIDTH_BUCKET',
    'trunc': 'TRUNC',
    'length': 'LENGTH',
    'substring': 'SUBSTRING',
    'trim': 'TRIM',
    'sha256': 'SHA256',
    'substr': 'SUBSTR',
    'get_byte': 'GET_BYTE',
    'set_byte': 'SET_BYTE',
    'convert': 'CONVERT',
    'encode': 'ENCODE',
    'decode': 'DECODE',
    'greatest': 'GREATEST',
    'least': 'LEAST',
    'charactervarying':'CHARACTERVARYING" '
}


class Campo(Instruccion):
    '''#1 ID tipo
       #2 CONSTRAINT
       #3 FOREIGN
       #4 PRIMARY'''
    def __init__(self, caso, id, tipo, acompaniamiento, idFk, tablaR, idR,fila,columna):
        self.caso = caso
        self.id = id
        self.tipo = tipo
        self.acompaniamiento = acompaniamiento
        self.idFk = idFk
        self.tablaR = tablaR
        self.idR = idR
        self.fila = fila
        self.columna = columna


    def ejecutar(campo, ts, consola, exceptions):

        nombreCampo = campo.id
        valor=True

        if campo.caso == 1:
            # id con su tipo
            # verificamos tipo si viene
            #print("1->>>>>>>>>>>>>>>>> ",campo.id)

            #if campo.tipo != None and ts.validar_sim(campo.id) == -1:
            if ts.validar_sim(campo.id) == -1:
                if str(campo.tipo.longitud) != None:
                    pass#print("campo: ",str(campo.tipo.tipo))

                if "VARCHAR" in str(campo.tipo.tipo).upper() or "CHARACTER" in str(campo.tipo.tipo).upper() or "CHARACTERVARYING" in str(campo.tipo.tipo).upper() or "DECIMAL" in str(campo.tipo.tipo).upper():
                    valores = []
                    if str(campo.acompaniamiento) != str(None):
                        for data in campo.acompaniamiento:
                            #print(data.tipo ," - ",data.valorDefault)
                            if str(data.valorDefault) == str(None):
                                valores.append(data.tipo)
                            else:
                                valores.append(str(data.tipo)+":"+str(data.valorDefault))

                    campo_nuevo = TS.Simbolo(TS.TIPO_DATO.CAMPO, campo.id, str(campo.tipo.tipo).upper(), valores, None)
                    ts.agregar_sim(campo_nuevo)
                    return valor
                elif str(campo.tipo.tipo).lower() in tipos_de_dato and ts.validar_sim(campo.id) == -1:
                    valores = []
                    check = []
                    if str(campo.acompaniamiento) != str(None):
                        for data in campo.acompaniamiento:
                            #print(data.tipo, " - ", data.valorDefault)
                            if str(data.valorDefault) == str(None):
                                valores.append(data.tipo)
                            else:
                                if isinstance(data.valorDefault,Expresion):
                                    check.append(data.valorDefault)
                                    valores.append(str(data.tipo) + ":" + "expresion")
                                else:
                                    valores.append(str(data.tipo)+":"+str(data.valorDefault))

                    #print("campo-> ",str(campo.tipo.tipo)," ",campo.acompaniamiento)
                    campo_nuevo = TS.Simbolo(TS.TIPO_DATO.CAMPO, campo.id, str(campo.tipo.tipo).upper(), valores, check)
                    ts.agregar_sim(campo_nuevo)
                    return valor

                else:
                    if ts.validar_sim(campo.id) == 1:
                        consola.append(f"Repeat identificador {campo.id}")
                    else:
                        consola.append(f"42P18	indeterminate_datatype, Tipo de dato no valido para {campo.id}\n")
                        exceptions.append(f"Error Semantico-NUMERO-info-fila-columna")
                    valor= False
            return valor
            # ts.agregar_sim()

        elif campo.caso == 2:
            # constraint
            #print("")
            #print("2->>>>>>>>>>>>>>>>> ", campo.id)
            for idcito in campo.idFk:
                #print(idcito.id)
                if ts.validar_sim(idcito.id) == 1:
                    obtenerCampo = ts.buscar_sim(idcito.id)
                    #print("ejecutando campos------------------------------------------!!!!!!1")
                    tablita = []
                    for dataReferencia in campo.idR:
                        tablita.append(dataReferencia.id)

                    obtenerCampo.valor.append(f"CONSTRAINT:{campo.id}:FOREIGNKEY:{campo.tablaR}:{tablita}")
                    # para llegar antes debe validarse que existe la tabla y los campos a los cuales
                    # se referencia


                else:
                    consola.append(f"42P10	invalid_column_reference, Campo{idcito.id} no encontrado")
                    exceptions.append("Error Semantico - 42P10- invalid_column_reference-fila-columna")
                    valor = False
            #print("")

        elif campo.caso == 3:
            # foreing key
            #print("3->>>>>>>>>>>>>>>>> ", campo.idFk)
            for idcito in campo.idFk:
                #print(idcito.id)
                if ts.validar_sim(idcito.id) == 1:
                    obtenerCampo = ts.buscar_sim(idcito.id)
                    #print("ejecutando campos------------------------------------------!!!!!!1")
                    tablita = []
                    for dataReferencia in campo.idR:
                        tablita.append(dataReferencia.id)

                    obtenerCampo.valor.append(f"FOREIGNKEY:{campo.tablaR},{tablita}")
                    #para llegar antes debe validarse que existe la tabla y los campos a los cuales
                    #se referencia


                else:
                    consola.append(f"42P10	invalid_column_reference, Campo{idcito.id} no encontrado")
                    exceptions.append("Error Semantico - 42P10- invalid_column_reference-fila-columna")
                    valor = False
            #print("")

        elif campo.caso == 4:
            # primary key
            #print("caso 4")
            for campito in nombreCampo:

                if ts.validar_sim(campito.id) == 1:

                    data =ts.buscar_sim(campito.id)
                    if str(data.valor) == str(None):
                        valores = []
                        campo_actualizado = TS.Simbolo(TS.TIPO_DATO.CAMPO, data.id, data.tipo,valores, data.Entorno)
                        ts.actualizar_sim(campo_actualizado)
                        valor = True
                    else:
                        data.valor.append('PRIMARYKEY')
                        campo_actualizado = TS.Simbolo(TS.TIPO_DATO.CAMPO, data.id, data.tipo, data.valor, data.Entorno)
                        ts.actualizar_sim(campo_actualizado)
                        valor=True
                else:
                    valor= False
                    consola.append(f"Error: el identificador {campito.id},no esta definido\n")
                    break
            #print(valor)
        else:
            #print("5->>>>>>>>>>>>>>>>> ", campo.id)
            # id con su tipo
            # verificamos tipo si viene
            #print("1->>>>>>>>>>>>>>>>> ", campo.id)

            # if campo.tipo != None and ts.validar_sim(campo.id) == -1:
            if ts.validar_sim(campo.id) == -1:

                if ts.validar_sim(campo.id) == -1:
                    valores = []
                    check = []
                    if str(campo.acompaniamiento) != str(None):
                        for data in campo.acompaniamiento:
                            #print(data.tipo, " - ", data.valorDefault)
                            if str(data.valorDefault) == str(None):
                                valores.append(data.tipo)
                            else:
                                if isinstance(data.valorDefault, Expresion):
                                    check.append(data.valorDefault)
                                    valores.append(str(data.tipo) + ":" + "expresion")
                                else:
                                    valores.append(str(data.tipo) + ":" + str(data.valorDefault))


                    campo_nuevo = TS.Simbolo(TS.TIPO_DATO.CAMPO, campo.id, campo.tipo.upper(), valores, check)
                    ts.agregar_sim(campo_nuevo)
                    return valor

                else:
                    if ts.validar_sim(campo.id) == 1:
                        consola.append(f"Repeat identificador {campo.id}")
                    else:
                        consola.append(f"42P18	indeterminate_datatype, Tipo de dato no valido para {campo.id}\n")
                        exceptions.append(f"Error Semantico-NUMERO-info-fila-columna")
                    valor = False
            return valor
            # ts.agregar_sim()

        #print(valor)
        return valor

    def getC3D(self, lista_optimizaciones_C3D):
        codigo_quemado = ''
        if self.caso == 1: #ID tipo acompaniamiento || ID tipo  Da lo mismo son la misma chingadera pero uno con complemento = None
            tipo = ''
            lista_tipo = self.tipo.tipo.split('-')
            if len(lista_tipo) == 1:
                tipo = self.tipo.tipo
            elif len(lista_tipo) == 2:
                if lista_tipo[0] == 'CHARACTERVARYING':
                    tipo = 'CHARACTER VARYING ( %s )' % lista_tipo[1]
                else:
                    tipo = '%s ( %s )' % (lista_tipo[0], lista_tipo[1])
            else:
                tipo = '%s ( %s, %s )' % (lista_tipo[0], lista_tipo[1], lista_tipo[2])
            acompaniamiento = ''
            if self.acompaniamiento is not None:
                for acom in self.acompaniamiento:
                    acompaniamiento += '%s ' % acom.getC3D(lista_optimizaciones_C3D)
            return '%s %s %s' % (self.id, tipo, acompaniamiento)
        elif self.caso == 2: #CONSTRAINT ID FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR'
            idFk = None
            for var in self.idFk:
                if idFk is None:
                    idFk = var.id
                else:
                    idFk += ', %s' % var.id
            idR = None
            for var in self.idR:
                if idR is None:
                    idR = var.id
                else:
                    idR += ', %s' % var.id
            return 'constraint %s foreign key ( %s ) references %s ( %s )' % (self.id, idFk, self.tablaR, idR)
        elif self.caso == 3: #FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR'
            idFk = None
            for var in self.idFk:
                if idFk is None:
                    idFk = var.id
                else:
                    idFk += ', %s' % var.id
            idR = None
            for var in self.idR:
                if idR is None:
                    idR = var.id
                else:
                    idR += ', %s' % var.id
            return 'foreign key ( %s ) references %s ( %s )' % (idFk, self.tablaR, idR)
        elif self.caso == 4: #PRIMARY KEY PARIZQ listaID PARDR
            idFk = None
            for var in self.id:
                if idFk is None:
                    idFk = var.id
                else:
                    idFk += ', %s' % var.id
            return 'primary key ( %s )' % idFk
        elif self.caso == 5: #ID ID
            return '%s %s' % (self.id, self.tipo)
        return codigo_quemado