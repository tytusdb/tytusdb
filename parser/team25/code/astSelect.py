
from enum import Enum
from sys import float_repr_style

from ply.yacc import errok
from astDDL import Instruccion
from useDB.instanciaDB import DB_ACTUAL
from storageManager.jsonMode import extractTable
from typeChecker.typeReference import getColumns
from prettytable import PrettyTable
from astExpresion import ExpresionID, Expresion , TuplaCompleta
from reporteErrores.errorReport import ErrorReport
import sqlErrors

class COMBINE_QUERYS(Enum):
    UNION = 1
    INTERSECT = 2
    EXCEPT = 3

class JOIN(Enum):
    INNER = 1
    LEFT = 2
    RIGHT = 3
    FULL = 4
class TABLA_TIPO(Enum):
    PRODUCTO_CRUZ = 0
    UNICA = 1
    SELECCIONADA = 2
    SELECT_SIMPLE = 3
    TABLAWHERE = 4    
    TABLAUNION = 5
    TABLAINTERSECCION = 6
    TABLAEXCEPT = 7

    

class SelectSimple(Instruccion):
    def __init__(self, campos,linea=0):
        self.campos = campos
        self.linea = linea
    
    def ejecutar(self,ts):
        columnas = []
        filas = []
        for actual in self.campos:
            if isinstance(actual, ITEM_ALIAS):
                if isinstance(actual.item, ExpresionID):
                    print("Error semántico, solo se aceptan expresiones.")
                    sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                elif isinstance(actual.item, Expresion):
                    filas.append(actual.item.ejecutar(ts).val)
                    columnas.append(actual.alias)
                else:
                    print("Error semántico, solo se aceptan expresiones.")
                    sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
            elif isinstance(actual, ExpresionID):
                print("Error semántico, solo se aceptan expresiones.")
                sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
            elif isinstance(actual, Expresion):
                filas.append(actual.ejecutar(ts).val)
                columnas.append('???')
                print("Error semántico, solo se aceptan expresiones.")
                sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)

        salida = matriz(columnas, [filas], TABLA_TIPO.SELECT_SIMPLE, "nueva tabla", None, None)
        return salida.ejecutar(ts)
# Select From
class SelectFrom(Instruccion):
    def __init__(self, fuentes, campos, alias=None,linea=0):
        self.fuentes = fuentes
        self.campos = campos # tal vez que lista de campos viniera como    [ ( item , alias)   , ( item , alias)  , ( item , alias)   ] donde item puede ser una expresion , funcion o algo simple
        self.alias = alias
        self.linea = linea
    
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador
        if self.alias:
            nodo += "[ label = \"AS: " + self.alias + "\" ];"
            nodo += "\n" + identificador + " -> " + str(hash(self.fuente)) + ";"
            if isinstance(self.fuente, str):
                nodo += "\n" + str(hash(self.fuente)) + "[ label = \"" + self.fuente + "\" ];\n"
            else:
                nodo += self.fuente.dibujar()
        else:
            if isinstance(self.fuente, str):
                nodo += "[ label = \"" + self.fuente + "\" ];\n"
            else:
                nodo += "[ label = \"SUBQUERY\" ];"
                nodo += "\n" + identificador + " -> " + str(hash(self.fuente)) + ";"
                nodo += self.fuente.dibujar()
        return nodo
    def ejecutar(self, ts): 
        columnas = []
        for col in self.campos:
            if isinstance (col, ExpresionID):
                columnas.append(col.val)
            elif isinstance(col, str):
                columnas.append(col)
            elif isinstance(col, Expresion):
                columnas.append(col)
            elif isinstance(col, ITEM_ALIAS):
                columnas.append(col)      
        tabla_base = FROM(self.fuentes)
        salida = SELECT(columnas, tabla_base.ejecutar(ts),self.linea)
        return salida.ejecutar(ts)

class FROM():
    def __init__(self, fuentes:list):
        self.fuentes = fuentes
    def ejecutar(self, ts):
        if len(self.fuentes)>1:
            encabezados = []
            lista = []
            columns = []
            nuevasFuentes = []
            for tabla in self.fuentes:
                if isinstance(tabla, ITEM_ALIAS):
                    tb = extractTable(DB_ACTUAL.name,tabla.item)
                    lista.append(tb)
                    clm = getColumns(DB_ACTUAL.name,tabla.item)
                    columns.append(clm)
                    for encabezado in clm:
                        encabezados.append(tabla.alias+"."+encabezado)
                    nuevasFuentes.append(tabla.alias)
                else:
                    tb = extractTable(DB_ACTUAL.name,tabla)
                    lista.append(tb)
                    clm = getColumns(DB_ACTUAL.name,tabla)
                    columns.append(clm)
                    for encabezado in clm:
                        encabezados.append(tabla+"."+encabezado)
                    nuevasFuentes.append(tabla)
            tabla_fuente = productoCruz(lista)
            resultado = matriz(encabezados, tabla_fuente, TABLA_TIPO.PRODUCTO_CRUZ, "nueva tabla", nuevasFuentes, columns)
            return resultado 
        else:
            if isinstance(self.fuentes[0],ITEM_ALIAS):
                encabezados = []
                tb = extractTable(DB_ACTUAL.name,self.fuentes[0].item)
                clm = getColumns(DB_ACTUAL.name,self.fuentes[0].item)
                for encabezado in clm:
                    encabezados.append(self.fuentes[0].alias+"."+encabezado)
                resultado = matriz(encabezados,tb, TABLA_TIPO.UNICA, self.fuentes[0].alias, [self.fuentes[0].alias] , clm) 
                return resultado
            else:
                encabezados = []
                tb = extractTable(DB_ACTUAL.name,self.fuentes[0])
                clm = getColumns(DB_ACTUAL.name,self.fuentes[0])
                for encabezado in clm:
                    encabezados.append(self.fuentes[0]+"."+encabezado)
                resultado = matriz(encabezados,tb, TABLA_TIPO.UNICA, self.fuentes[0], self.fuentes , clm) 
                return resultado

class SELECT():
    def __init__(self, columnas:list, resultado: list,linea=0):
        self.columnas = columnas
        self.resultado = resultado
        self.linea = linea
    def ejecutar(self,ts):
        salida = None
        if len(self.resultado.fuentes)>1:
            seleccion_columnas = []
            for actual in self.columnas:
                if isinstance(actual, ITEM_ALIAS):
                    if isinstance(actual.item, ExpresionID):
                        actual.item = actual.item.val
                        if actual.item.count('.') == 1:
                            seleccion_columnas.append(actual)
                        elif esAmbiguo(actual.item,self.resultado.columnas,self.resultado.fuentes):
                            print("Error semántico, el identificador  \"", actual, "\"  es ambiguo")
                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.ambiguous_column
                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                        else:
                            actual = aclarar(actual.item, self.resultado.columnas, self.resultado.fuentes)
                            seleccion_columnas.append(actual)
                    elif isinstance(actual.item, Expresion):
                        seleccion_columnas.append(actual)
                    elif actual.item.count('.') == 1:
                        seleccion_columnas.append(actual)
                    elif actual.item == "*":
                        print("Error semántico, el operador \"*\" no es aplicable con alias.")
                        sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                    else:
                        if esAmbiguo(actual,self.resultado.columnas,self.resultado.fuentes):
                            print("Error semántico, el identificador  \"", actual, "\"  es ambiguo")
                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.ambiguous_column
                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                        else:
                            actual = aclarar(actual, self.resultado.columnas, self.fuentes)
                            seleccion_columnas.append(actual)
                elif isinstance(actual, Expresion):
                    seleccion_columnas.append(actual)
                elif actual.count('.') == 1:
                    seleccion_columnas.append(actual)
                elif actual == "*":
                    seleccion_columnas.append(actual)
                else:
                    if esAmbiguo(actual,self.resultado.columnas,self.resultado.fuentes):
                        print("Error semántico, el identificador  \"", actual, "\"  es ambiguo")
                        sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.ambiguous_column
                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                    else:
                        actual = aclarar(actual, self.resultado.columnas, self.fuentes)
                        seleccion_columnas.append(actual)
            salida = self.resultado.obtenerColumnas(seleccion_columnas)
            if salida == None:
                print("Algo salió mal")
            return salida
        else:
            seleccion_columnas = []
            for actual in self.columnas:
                if isinstance(actual, ITEM_ALIAS):
                    if isinstance(actual.item, ExpresionID):
                        actual.item = actual.item.val
                        seleccion_columnas.append(actual)
                else:
                    seleccion_columnas.append(actual)
            salida = self.resultado.obtenerColumnas(self.columnas)
            return salida
def productoCruz(lista:list):
    
    return execProduct(lista)

def execProduct(lista:list):
    nuevo = realizarProducto(lista)
    if len(lista)>=2:
        return realizarProducto(lista)
    else:
        return nuevo
        
def realizarProducto(operandos:list):
    res = []
    iterado = operandos.pop()
    base = operandos.pop()
    for item_base in base:
        for item_iterado in iterado:
            nuevo = item_base[:]
            for item_item in item_iterado:
                nuevo.append(item_item)
            res.append(nuevo)
    operandos.append(res)
    return res  
class matriz():
    def __init__(self, columnas:list, filas:list, tipo, nombre, fuentes: list , clm ,linea=0):
        self.columnas = columnas
        self.filas = filas
        self.tipo = tipo
        self.nombre = nombre
        self.fuentes = fuentes
        self.clm = clm 
        self.linea=linea

    def imprimirMatriz(self):
        x = PrettyTable()
        x.field_names = sinRepetidos(self.columnas)
        for fila in self.filas:
            x.add_row(fila)
        print(x)
    def getTablaToString(self) ->str:
        x = PrettyTable()
        x.field_names = sinRepetidos(self.columnas)
        for fila in self.filas:
            x.add_row(fila)
        return x.get_string()
    def obtenerColumnas(self, ids:list):
        error = False
        resultante = []
        flag = True
        columnas_resultantes = []
        for actual in ids:
            if isinstance(actual,ITEM_ALIAS):
                if isinstance(actual.item , Expresion):
                    ColumnaCompleta = []
                    MinitablaSimbolos = []
                    filas = self.filas
                    columnas = self.columnas
                    i = 0 
                    while(i < len(filas)):
                        indiceColumna = 0
                        while(indiceColumna < len(columnas)): 
                            if len(self.fuentes)==1:
                                MinitablaSimbolos.append({'id': columnas[indiceColumna] , 'val': filas[i][indiceColumna] , 'tipo':self.clm[quitarRef(columnas[indiceColumna])]['Type']})
                            else:
                                MinitablaSimbolos.append({'id': columnas[indiceColumna] , 'val': filas[i][indiceColumna] , 'tipo':self.clm[obtenerIndice(self.fuentes,obtenerRef(columnas[indiceColumna]))][quitarRef(columnas[indiceColumna])]['Type']})
                            indiceColumna+=1
                        tupla = TuplaCompleta(MinitablaSimbolos)
                        casillaResultante = actual.item.ejecutar(tupla)
                        if isinstance(casillaResultante , ErrorReport): 
                            print(casillaResultante.description)
                        ColumnaCompleta.append(casillaResultante.val) 
                        MinitablaSimbolos.clear()
                        i+=1
                    if flag:
                        for k in ColumnaCompleta:
                            nuevaColumna = [] 
                            nuevaColumna.append(k)
                            resultante.append(nuevaColumna)
                        flag = False
                        columnas_resultantes.append(actual.alias)
                    else:
                        h = 0 
                        for j in resultante:
                            resultante[h].append(ColumnaCompleta[h])
                            h+=1
                        flag = False
                        columnas_resultantes.append(actual.alias)
                elif self.columnas.__contains__(self.nombre+"."+actual.item) and self.tipo == TABLA_TIPO.UNICA:
                    i = 0
                    for columna in self.columnas:
                        if columna == self.nombre+"."+actual.item:
                            break
                        else:
                            i+=1
                    j = 0
                    for fila in self.filas:
                        if flag:
                            nuevaColumna = []
                            nuevaColumna.append(fila[i])
                            resultante.append(nuevaColumna)
                        else:
                            resultante[j].append(fila[i])
                        j+=1
                    flag = False
                    columnas_resultantes.append(actual.alias)
                else:
                    i = 0
                    bandera = False
                    for columna in self.columnas:
                        if columna == actual.item:
                            bandera = True
                            break
                        else:
                            i+=1
                    if bandera:
                        j = 0
                        for fila in self.filas:
                            if flag:
                                nuevaColumna = []
                                nuevaColumna.append(fila[i])
                                resultante.append(nuevaColumna)
                            else:
                                resultante[j].append(fila[i])
                            j+=1
                        flag = False
                        columnas_resultantes.append(actual.alias)
                    else:                        
                        print("Error semántico, la columna:  \" ", actual.item," \"  no se encuentra o su referencia es ambigua.")
                        error = True
                        sqlTypeError=sqlErrors.sql_error_fdw_error.fdw_column_name_not_found
                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                        





            else:
                if isinstance(actual , Expresion):
                    ColumnaCompleta = []
                    MinitablaSimbolos = []
                    filas = self.filas
                    columnas = self.columnas
                    i = 0 
                    while(i < len(filas)):
                        indiceColumna = 0
                        while(indiceColumna < len(columnas)): 
                            if len(self.fuentes)==1:
                                MinitablaSimbolos.append({'id': columnas[indiceColumna] , 'val': filas[i][indiceColumna] , 'tipo':self.clm[quitarRef(columnas[indiceColumna])]['Type']})
                            else:
                                MinitablaSimbolos.append({'id': columnas[indiceColumna] , 'val': filas[i][indiceColumna] , 'tipo':self.clm[obtenerIndice(self.fuentes,obtenerRef(columnas[indiceColumna]))][quitarRef(columnas[indiceColumna])]['Type']})
                            indiceColumna+=1
                        tupla = TuplaCompleta(MinitablaSimbolos)
                        casillaResultante = actual.ejecutar(tupla)
                        if isinstance(casillaResultante , ErrorReport): 
                            print(casillaResultante.description)
                        ColumnaCompleta.append(casillaResultante.val) 
                        MinitablaSimbolos.clear()
                        i+=1
                    if flag:
                        for k in ColumnaCompleta:
                            nuevaColumna = [] 
                            nuevaColumna.append(k)
                            resultante.append(nuevaColumna)
                        flag = False
                        columnas_resultantes.append('exp')
                    else:
                        h = 0 
                        for j in resultante:
                            resultante[h].append(ColumnaCompleta[h])
                            h+=1
                        flag = False
                        columnas_resultantes.append('exp')
                elif actual == "*":
                    j = 0
                    for fila in self.filas:
                        if flag:
                            nuevaColumna = []
                            for k in fila:
                                nuevaColumna.append(k)
                            resultante.append(nuevaColumna)
                        else:
                            for k in fila:
                                resultante[j].append(k)
                        j+=1
                    for c in self.columnas:
                        columnas_resultantes.append(c)
                    flag = False
                elif self.columnas.__contains__(self.nombre+"."+actual) and self.tipo == TABLA_TIPO.UNICA:
                    i = 0
                    for columna in self.columnas:
                        if columna == self.nombre+"."+actual:
                            break
                        else:
                            i+=1
                    j = 0
                    for fila in self.filas:
                        if flag:
                            nuevaColumna = []
                            nuevaColumna.append(fila[i])
                            resultante.append(nuevaColumna)
                        else:
                            resultante[j].append(fila[i])
                        j+=1
                    flag = False
                    columnas_resultantes.append(actual)
                else:
                    i = 0
                    bandera = False
                    for columna in self.columnas:
                        if columna == actual:
                            bandera = True
                            break
                        else:
                            i+=1
                    if bandera:
                        j = 0
                        for fila in self.filas:
                            if flag:
                                nuevaColumna = []
                                nuevaColumna.append(fila[i])
                                resultante.append(nuevaColumna)
                            else:
                                resultante[j].append(fila[i])
                            j+=1
                        flag = False
                        columnas_resultantes.append(actual)
                    else:                        
                        print("Error semántico, la columna:  \" ", actual," \"  no se encuentra o su referencia es ambigua.")
                        error = True
                        sqlTypeError=sqlErrors.sql_error_fdw_error.fdw_column_name_not_found
                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)

        if not error:
            salida = matriz(columnas_resultantes, resultante, TABLA_TIPO.SELECCIONADA, "nueva tabla", self.fuentes , self.clm)
        else: 
            salida = None
        return salida

def esAmbiguo(id, columnas, tablas):
    contador = 0
    for col in columnas:
        for tb in tablas:
            actual = tb+"."+id
            if col == actual:
                contador +=1    
    if contador>1:
        return True
    else:
        return False

def aclarar(id, columnas, tablas):
    for col in columnas:
        for tb in tablas:
            actual = tb+"."+id
            if col == actual:
                return actual

def sinRepetidos(lista: list) -> list:
    aux = dict()

    for item in lista:
        aux[item] = 0

    nuevaLista = list()
    for item in lista:
        if aux[item] != 0:
            nuevaLista.append(item + '(' + str(aux[item]) + ')' )
        else:
            nuevaLista.append(item)
        aux[item] += 1

    return nuevaLista
def quitarRef(cadena):# le quito la referencia de su tabla 
        cadena = cadena.split('.')
        return cadena[1]

def obtenerRef(cadena):
    cadena = cadena.split('.')
    return cadena[0]   

def obtenerIndice(fuentes, id):
    i = 0
    for fuente in fuentes:
        if fuente ==  id:
            return i
        else:
            i+=1

class ITEM_ALIAS():
    def __init__(self, item, alias) -> None:
        self.item = item
        self.alias = alias




# Select filter
class SelectFilter(Instruccion):
    def __init__(self, where, groupby = None, having = None):
        self.where = where # ES UNA EXPRESION
        self.groupby = groupby
        self.having = having

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"FILTER\" ];"

        # Para el where
        nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
        nodo += "\n" + identificador + " -> WHERE" + identificador + ";"
        nodo += "\nWHERE" + identificador + " -> " + str(hash(self.where)) + ";"

        # Para el group by
        if self.groupby:
            nodo += "\nGROUPBY" + identificador + "[ label = \"GROUP BY\" ];"
            nodo += "\n" + identificador + " -> GROUPBY" + identificador + ";"
            nodo += "\nGROUPBY" + identificador + " -> " + str(hash(self.groupby)) + ";"

        if self.having:
            nodo += "\nHAVING" + identificador + "[ label = \"HAVING\" ];"
            nodo += "\n" + identificador + " -> HAVING" + identificador + ";"
            nodo += "\nHAVING" + identificador + " -> " + str(hash(self.having)) + ";"        

        return nodo
    def ejecutar(self, ts):
        if self.groupby == None and self.having == None:
            if isinstance(self.where , WHERE):
                return self.where.ejecutar(ts)

class WHERE():
    def __init__(self, expresion):
        self.exp = expresion

    
    def ejecutar(self, ts): # NECESITO LA TABLOTA :v 
        
        lista_litas = []
        MinitablaSimbolos = []
        filas = ts.filas
        columnas = ts.columnas
        i = 0 
        while(i < len(filas)):
            indiceColumna = 0
            while(indiceColumna < len(columnas)): 
                if len(ts.fuentes)==1:
                    MinitablaSimbolos.append({'id': columnas[indiceColumna] , 'val': filas[i][indiceColumna] , 'tipo':ts.clm[quitarRef(columnas[indiceColumna])]['Type']})
                else:
                    MinitablaSimbolos.append({'id': columnas[indiceColumna] , 'val': filas[i][indiceColumna] , 'tipo':ts.clm[obtenerIndice(ts.fuentes,obtenerRef(columnas[indiceColumna]))][quitarRef(columnas[indiceColumna])]['Type']})
                indiceColumna+=1
            tupla = TuplaCompleta(MinitablaSimbolos)
            casillaResultante = self.exp.ejecutar(tupla)
            if isinstance(casillaResultante , ErrorReport): 
                print(casillaResultante.description)
                
            if casillaResultante.val:
                fila = []
                for t in MinitablaSimbolos:
                    fila.append(t['val'])    
                lista_litas.append(fila)

            MinitablaSimbolos.clear()
            i+=1
        return matriz(ts.columnas, lista_litas, TABLA_TIPO.TABLAWHERE, "nueva tabla", ts.fuentes, ts.clm)

class SelectFromWhere(Instruccion):
    def __init__(self, fuentes, campos, filtro,linea=0):
        self.fuentes = fuentes
        self.campos = campos # tal vez que lista de campos viniera como    [ ( item , alias)   , ( item , alias)  , ( item , alias)   ] donde item puede ser una expresion , funcion o algo simple
        self.filtro = filtro
        self.linea = linea
    def dibujar(self):
        pass
    def ejecutar(self, ts): 
        columnas = []
        for col in self.campos:
            if isinstance (col, ExpresionID):
                columnas.append(col.val)
            elif isinstance(col, str):
                columnas.append(col)
            elif isinstance(col, Expresion):
                columnas.append(col)
            elif isinstance(col, ITEM_ALIAS):
                columnas.append(col)      
        tabla_base = FROM(self.fuentes)
        
        SALIDA_FILTRADA = self.filtro.ejecutar(tabla_base.ejecutar(ts))
        if isinstance(SALIDA_FILTRADA , ErrorReport):
            return SALIDA_FILTRADA
             
        salida = SELECT(columnas,SALIDA_FILTRADA) 
        matriz = salida.ejecutar(ts)
        matriz.imprimirMatriz()
        return matriz

class combineQuery(Instruccion):
    def __init__(self, izq, operador, der,linea=0):
        self.izq = izq
        self.operador = operador
        self.der = der
        self.linea = linea
    def ejecutar(self, ts):
        izquierdo = self.izq.ejecutar(ts)
        derecho = self.der.ejecutar(ts)
        if len(izquierdo.filas) == len(derecho.filas) and len(izquierdo.columnas) == len(derecho.columnas):
            if self.operador == COMBINE_QUERYS.UNION:
                set1 = set(tuple(x) for x in izquierdo.filas)
                set2 = set(tuple(x) for x in derecho.filas)
                union = set1 | set2
                lista_intermedia = list(union)
                lista_final = []
                for actual in lista_intermedia:
                    lista_final.append(list(actual))
                nuevas_columnas = []
                for actual in lista_final[0]:
                    nuevas_columnas.append("Union")
                nuevas_fuentes = []
                for actual in izquierdo.fuentes:
                    nuevas_fuentes.append(actual)
                for actual in derecho.fuentes:
                    nuevas_fuentes.append(actual)
                nuevo_clm = []
                for actual in izquierdo.clm:
                    nuevo_clm.append(actual)
                for actual in derecho.clm:
                    nuevo_clm.append(actual)
                salida = matriz(nuevas_columnas, lista_final,TABLA_TIPO.TABLAUNION,'nueva tabla',nuevas_fuentes, nuevo_clm )
                salida.imprimirMatriz()
                return salida
            elif self.operador == COMBINE_QUERYS.INTERSECT:
                set1 = set(tuple(x) for x in izquierdo.filas)
                set2 = set(tuple(x) for x in derecho.filas)
                union = set1 & set2
                lista_intermedia = list(union)
                lista_final = []
                for actual in lista_intermedia:
                    lista_final.append(list(actual))
                nuevas_columnas = []
                if len(lista_final)>0:
                    for actual in lista_final[0]:
                        nuevas_columnas.append("Intersect")
                nuevas_fuentes = []
                for actual in izquierdo.fuentes:
                    nuevas_fuentes.append(actual)
                for actual in derecho.fuentes:
                    nuevas_fuentes.append(actual)
                nuevo_clm = []
                for actual in izquierdo.clm:
                    nuevo_clm.append(actual)
                for actual in derecho.clm:
                    nuevo_clm.append(actual)
                salida = matriz(nuevas_columnas, lista_final,TABLA_TIPO.TABLAINTERSECCION,'nueva tabla',nuevas_fuentes, nuevo_clm )
                salida.imprimirMatriz()
                return salida
            elif self.operador == COMBINE_QUERYS.EXCEPT:
                set1 = set(tuple(x) for x in izquierdo.filas)
                set2 = set(tuple(x) for x in derecho.filas)
                union = set1 - set2
                lista_intermedia = list(union)
                lista_final = []
                for actual in lista_intermedia:
                    lista_final.append(list(actual))
                nuevas_columnas = []
                for actual in lista_final[0]:
                    nuevas_columnas.append("Except")
                nuevas_fuentes = []
                for actual in izquierdo.fuentes:
                    nuevas_fuentes.append(actual)
                for actual in derecho.fuentes:
                    nuevas_fuentes.append(actual)
                nuevo_clm = []
                for actual in izquierdo.clm:
                    nuevo_clm.append(actual)
                for actual in derecho.clm:
                    nuevo_clm.append(actual)
                salida = matriz(nuevas_columnas, lista_final,TABLA_TIPO.TABLAEXCEPT,'nueva tabla',nuevas_fuentes, nuevo_clm )
                salida.imprimirMatriz()
                return salida
        else:
            print("Error semántico, el número de filas de los operandos es diferente.")   
            sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)