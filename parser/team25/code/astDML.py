from astDDL import Instruccion
import storageManager.jsonMode as DBMS
from useDB.instanciaDB import DB_ACTUAL
import typeChecker.typeReference as TypeCheck
from astExpresion import TIPO_DE_DATO
from astFunciones import FuncionTime
from useDB import instanciaDB
import sqlErrors

def parseToNumber(input:str):
    try:
        result=int(input)
        # print("Es un entero")
        return result
    except ValueError:
        try:
            result=float(input)
            # print("Es un float")
            return result
        except ValueError:
            # print("No es un número")
            return None

# Returns True if the column is already a key in this dictionary, otherwise, returns False
def checkColumnsDictionary(dictionary:dict,key:str) -> bool:
    try:
        a=dictionary[key]
        return True
    except:
	    return False

def getColumnIndex(columnList:list,name:str):
    try:
        return columnList.index(name)
    except:
        return None

# ------------------------ DML ----------------------------
# Insert into table
class InsertTable(Instruccion):
    def __init__(self, tabla, valores,listaColumnas=None):
        self.tabla = tabla
        self.valores = valores
        self.listaColumnas=listaColumnas
    
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"INSERT TABLE\" ];"

        nodo += "\nINTO" + identificador + "[ label = \"INTO\" ];"
        nodo += "\n" + identificador + " -> INTO" + identificador + ";"
        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\nINTO" + identificador + " -> NAME" + identificador + ";"
        nodo += "\nVALUES" + identificador + "[ label = \"VALUES\" ];"
        nodo += "\n" + identificador + " -> VALUES" + identificador + ";"
        
        for valor in self.valores:
            nodo += "\nVALUES" + identificador + " -> " + str(hash(valor)) + ";"
            nodo += valor.dibujar()

        return nodo
    
    def ejecutar(self,ts):
        tabla1=self.tabla
        valores1=self.valores
        listaCol=self.listaColumnas
        dbName=DB_ACTUAL.getName()
        # dbName="test"
        # Check if a db is in use
        if dbName==None:
            # Add this error to the errors Tree
            print("ERROR: database \'"+dbName+"\' does not exist")
        else:
            # Check if the table exists into the db
            tables=TypeCheck.tableExist(dbName,tabla1)
            if tables == None:
                sqlError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_table
                print("ERROR "+sqlError.value+": "+str(sqlError.name)+" \'"+tabla1+"\'")
            else:
                flag=False
                counter=0
                result = []
                columnsNameList=list(TypeCheck.getColumns(dbName,tabla1).keys())
                if listaCol==None:
                    # INSERT CHECKING ALL COLUMNS ON THEIR RESPECTIVE ORDER
                    if len(columnsNameList)==len(valores1):
                        for val in valores1:
                            if isinstance(val,FuncionTime):
                                val=val.ejecutar(ts)
                            if val.tipo==TIPO_DE_DATO.CADENA:
                                if TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="varchar".casefold() or TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="character varying".casefold():
                                    if len(val.val)<=TypeCheck.getLenght(dbName,tabla1,columnsNameList[counter]):
                                        if len(val.val)==0:
                                            if TypeCheck.getNull(dbName,tabla1,columnsNameList[counter]):
                                                if TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter])!=None:
                                                    result.append(TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter]))
                                                else:
                                                    result.append(None)
                                            else:
                                                if TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter])!=None:
                                                    result.append(TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter]))
                                                else:
                                                    flag=True
                                                    sqlTypeError=sqlErrors.sql_error_data_exception.null_value_not_allowed
                                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                        else:
                                            if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                                check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                                dictCheck={columnsNameList[counter]:val.val}
                                                if eval(check,dictCheck):
                                                    result.append(val.val)
                                                else:
                                                    sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                    flag=True
                                                    break
                                            else:
                                                result.append(val.val)
                                    else:
                                        print("ERROR: la longitud de la cadena es mayor a lo permitido por el tipo de dato")
                                        flag=True
                                elif TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="char".casefold() or TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="character".casefold():
                                    if len(val.val.encode('utf-8'))<=TypeCheck.getLenght(dbName,tabla1,columnsNameList[counter]):
                                        if len(val.val)==0:
                                            if TypeCheck.getNull(dbName,tabla1,columnsNameList[counter]):
                                                if TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter])!=None:
                                                    result.append(TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter]))
                                                else:
                                                    result.append(None)
                                            else:
                                                if TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter])!=None:
                                                    result.append(TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter]))
                                                else:
                                                    flag=True
                                                    sqlTypeError=sqlErrors.sql_error_data_exception.null_value_not_allowed
                                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                        else:
                                            if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                                check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                                dictCheck={columnsNameList[counter]:val.val}
                                                if eval(check,dictCheck):
                                                    result.append(val.val)
                                                else:
                                                    sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                    flag=True
                                                    break
                                            else:
                                                result.append(val.val)
                                    else:
                                        print("ERROR: el tamaño de la cadena es mayor a lo permitido por el tipo de dato")
                                        flag=True
                                elif TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="text".casefold():
                                    if len(val.val)==0:
                                        if TypeCheck.getNull(dbName,tabla1,columnsNameList[counter]):
                                            if TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter])!=None:
                                                result.append(TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter]))
                                            else:
                                                result.append(None)
                                        else:
                                            if TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter])!=None:
                                                result.append(TypeCheck.detDefault(dbName,tabla1,columnsNameList[counter]))
                                            else:
                                                flag=True
                                                sqlTypeError=sqlErrors.sql_error_data_exception.null_value_not_allowed
                                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                    else:
                                        if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                            check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                            dictCheck={columnsNameList[counter]:val.val}
                                            if eval(check,dictCheck):
                                                result.append(val.val)
                                            else:
                                                sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                flag=True
                                                break
                                        else:
                                            result.append(val.val)
                                elif TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="date".casefold() or\
                                    TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="time".casefold() or\
                                        TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="interval".casefold() :
                                    if val.isFecha:
                                        if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                            check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                            dictCheck={columnsNameList[counter]:val.val}
                                            if eval(check,dictCheck):
                                                result.append(val.val)
                                            else:
                                                sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                flag=True
                                                break
                                        else:
                                            result.append(val.val)
                                    else:
                                        flag=True
                                        sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                        print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                else:
                                    flag=True
                                    sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                            elif val.tipo==TIPO_DE_DATO.ENTERO:
                                if TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="smallint".casefold():
                                    if val.val>=-32768 and val.val<=32767:
                                        if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                            check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                            dictCheck={columnsNameList[counter]:val.val}
                                            if eval(check,dictCheck):
                                                result.append(val.val)
                                            else:
                                                sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                flag=True
                                                break
                                        else:
                                            result.append(val.val)
                                    else:
                                        print("ERROR: el tamaño del número no coincide con el tipo de dato")
                                        flag=True
                                elif TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="integer".casefold():
                                    if val.val>=-2147483648 and val.val<=2147483647:
                                        if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                            check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                            dictCheck={columnsNameList[counter]:val.val}
                                            if eval(check,dictCheck):
                                                result.append(val.val)
                                            else:
                                                sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                flag=True
                                                break
                                        else:
                                            result.append(val.val)
                                    else:
                                        print("ERROR: el tamaño del número no coincide con el tipo de dato")
                                        flag=True
                                elif TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="bigint".casefold():
                                    if val.val>=-9223372036854775808  and val.val<=9223372036854775807:
                                        if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                            check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                            dictCheck={columnsNameList[counter]:val.val}
                                            if eval(check,dictCheck):
                                                result.append(val.val)
                                            else:
                                                sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                flag=True
                                                break
                                        else:
                                            result.append(val.val)
                                    else:
                                        print("ERROR: el tamaño del número no coincide con el tipo de dato")
                                        flag=True
                                else:
                                    flag=True
                                    sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                            elif val.tipo==TIPO_DE_DATO.DECIMAL:
                                if TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="decimal".casefold() or \
                                    TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="numeric".casefold() or \
                                    TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="real".casefold() or \
                                    TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="double precision".casefold() or \
                                    TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="money".casefold():
                                    if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                        check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                        dictCheck={columnsNameList[counter]:val.val}
                                        if eval(check,dictCheck):
                                            result.append(val.val)
                                        else:
                                            sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                            print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                            flag=True
                                            break
                                    else:
                                        result.append(val.val)
                                else:
                                    flag=True
                                    sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                            elif val.tipo==TIPO_DE_DATO.BOOLEANO and \
                                TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="boolean".casefold():
                                if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                    check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                    dictCheck={columnsNameList[counter]:val.val}
                                    if eval(check,dictCheck):
                                        result.append(val.val)
                                    else:
                                        sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                        print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                        flag=True
                                        break
                                else:
                                    result.append(val.val)
                            else:
                                flag=True
                                sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                            counter+=1
                        if not flag:
                            print("Llamando a la funcion insert("+dbName+","+tabla1+","+str(result)+").")
                            print(DBMS.insert(dbName,tabla1,result))
                        else:
                            print("ERROR AL INSERTAR EN LA BD")
                    else:print("ERROR: La cantidad de parámetros indicados no coincide con los campos de la tabla")
                    # INSERT VALIDATING THE COLUMNS LIST
                else:
                    if len(listaCol)==len(valores1):
                        columnsDict={}
                        columnsIndex=0
                        counter=0
                        for val in valores1:
                            if isinstance(val,FuncionTime):
                                val=val.ejecutar(ts)
                            colIndex=getColumnIndex(columnsNameList,listaCol[counter])
                            if not colIndex==None:
                                if not checkColumnsDictionary(columnsDict,listaCol[counter]):
                                    if val.tipo==TIPO_DE_DATO.CADENA:
                                        if TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="varchar".casefold() or TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="character varying".casefold():
                                            if len(val.val)<=TypeCheck.getLenght(dbName,tabla1,columnsNameList[colIndex]):
                                                if len(val.val)==0:
                                                    if TypeCheck.getNull(dbName,tabla1,columnsNameList[colIndex]):
                                                        if TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])!=None:
                                                            columnsDict[listaCol[counter]]=TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])
                                                        else:
                                                            columnsDict[listaCol[counter]]=None
                                                    else:
                                                        if TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])!=None:
                                                            columnsDict[listaCol[counter]]=TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])
                                                        else:
                                                            flag=True
                                                            sqlTypeError=sqlErrors.sql_error_data_exception.null_value_not_allowed
                                                            print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                else:
                                                    if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                        check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                        dictCheck={columnsNameList[colIndex]:val.val}
                                                        if eval(check,dictCheck):
                                                            columnsDict[listaCol[counter]]=val.val
                                                        else:
                                                            sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                            print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                            flag=True
                                                            break
                                                    else:
                                                        columnsDict[listaCol[counter]]=val.val
                                                    
                                            else:
                                                print("ERROR: la longitud de la cadena es mayor a lo permitido por el tipo de dato")
                                                flag=True
                                        elif TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="char".casefold() or TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="character".casefold():
                                            if len(val.val.encode('utf-8'))<=TypeCheck.getLenght(dbName,tabla1,columnsNameList[colIndex]):
                                                if len(val.val)==0:
                                                    if TypeCheck.getNull(dbName,tabla1,columnsNameList[colIndex]):
                                                        if TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])!=None:
                                                            columnsDict[listaCol[counter]]=TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])
                                                        else:
                                                            columnsDict[listaCol[counter]]=None
                                                    else:
                                                        if TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])!=None:
                                                            columnsDict[listaCol[counter]]=TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])
                                                        else:
                                                            flag=True
                                                            sqlTypeError=sqlErrors.sql_error_data_exception.null_value_not_allowed
                                                            print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                else:
                                                    if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                        check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                        dictCheck={columnsNameList[colIndex]:val.val}
                                                        if eval(check,dictCheck):
                                                            columnsDict[listaCol[counter]]=val.val
                                                        else:
                                                            sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                            print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                            flag=True
                                                            break
                                                    else:
                                                        columnsDict[listaCol[counter]]=val.val
                                            else:
                                                print("ERROR: el tamaño de la cadena es mayor a lo permitido por el tipo de dato")
                                                flag=True
                                        elif TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="text".casefold():
                                            if len(val.val)==0:
                                                if TypeCheck.getNull(dbName,tabla1,columnsNameList[colIndex]):
                                                    if TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])!=None:
                                                        columnsDict[listaCol[counter]]=TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])
                                                    else:
                                                        columnsDict[listaCol[counter]]=None
                                                else:
                                                    if TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])!=None:
                                                        columnsDict[listaCol[counter]]=TypeCheck.detDefault(dbName,tabla1,columnsNameList[colIndex])
                                                    else:
                                                        flag=True
                                                        sqlTypeError=sqlErrors.sql_error_data_exception.null_value_not_allowed
                                                        print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                            else:
                                                if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                    check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                    dictCheck={columnsNameList[colIndex]:val.val}
                                                    if eval(check,dictCheck):
                                                        columnsDict[listaCol[counter]]=val.val
                                                    else:
                                                        sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                        print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                        flag=True
                                                        break
                                                else:
                                                    columnsDict[listaCol[counter]]=val.val
                                        elif TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="date".casefold() or\
                                             TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="time".casefold() or\
                                             TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="interval".casefold() :
                                            if val.isFecha:
                                                if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                    check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                    dictCheck={columnsNameList[colIndex]:val.val}
                                                    if eval(check,dictCheck):
                                                        columnsDict[listaCol[counter]]=val.val
                                                    else:
                                                        sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                        print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                        flag=True
                                                        break
                                                else:
                                                    columnsDict[listaCol[counter]]=val.val
                                            else:
                                                flag=True
                                                sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                        else:
                                            flag=True
                                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_column
                                            print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+" "+listaCol[counter])
                                    elif val.tipo==TIPO_DE_DATO.ENTERO:
                                        if TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="smallint".casefold():
                                            if val.val>=-32768 and val.val<=32767:
                                                if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                    check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                    dictCheck={columnsNameList[colIndex]:val.val}
                                                    if eval(check,dictCheck):
                                                        columnsDict[listaCol[counter]]=val.val
                                                    else:
                                                        sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                        print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                        flag=True
                                                        break
                                                else:
                                                    columnsDict[listaCol[counter]]=val.val
                                            else:
                                                print("ERROR: el tamaño del número no coincide con el tipo de dato")
                                                flag=True
                                        elif TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="integer".casefold():
                                            if val.val>=-2147483648 and val.val<=2147483647:
                                                if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                    check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                    dictCheck={columnsNameList[colIndex]:val.val}
                                                    if eval(check,dictCheck):
                                                        columnsDict[listaCol[counter]]=val.val
                                                    else:
                                                        sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                        print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                        flag=True
                                                        break
                                                else:
                                                    columnsDict[listaCol[counter]]=val.val
                                            else:
                                                print("ERROR: el tamaño del número no coincide con el tipo de dato")
                                                flag=True
                                        elif TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="bigint".casefold():
                                            if val.val>=-9223372036854775808  and val.val<=9223372036854775807:
                                                if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                    check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                    dictCheck={columnsNameList[colIndex]:val.val}
                                                    if eval(check,dictCheck):
                                                        columnsDict[listaCol[counter]]=val.val
                                                    else:
                                                        sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                        print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                        flag=True
                                                        break
                                                else:
                                                    columnsDict[listaCol[counter]]=val.val
                                            else:
                                                print("ERROR: el tamaño del número no coincide con el tipo de dato")
                                                flag=True
                                        else:
                                            flag=True
                                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                            print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                    elif val.tipo==TIPO_DE_DATO.DECIMAL:
                                        if TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="decimal".casefold() or \
                                            TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="numeric".casefold() or \
                                            TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="real".casefold() or \
                                            TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="double precision".casefold() or \
                                            TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="money".casefold():
                                            if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                dictCheck={columnsNameList[colIndex]:val.val}
                                                if eval(check,dictCheck):
                                                    columnsDict[listaCol[counter]]=val.val
                                                else:
                                                    sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                    flag=True
                                                    break
                                            else:
                                                columnsDict[listaCol[counter]]=val.val
                                        else:
                                            flag=True
                                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                            print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+ " "+columnsNameList[colIndex] + " "+str(val.val))
                                        # FALTA COMPROBAR FECHAS Y TYPES
                                    elif val.tipo==TIPO_DE_DATO.DATE:
                                        if TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="date".casefold() or \
                                            TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="time".casefold() or \
                                                TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="interval".casefold():
                                            if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                dictCheck={columnsNameList[colIndex]:val.val}
                                                if eval(check,dictCheck):
                                                    columnsDict[listaCol[counter]]=val.val
                                                else:
                                                    sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                    flag=True
                                                    break
                                            else:
                                                columnsDict[listaCol[counter]]=val.val
                                        else:
                                            flag=True
                                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                            print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+ " "+columnsNameList[colIndex] + " "+str(val.val))
                                    elif val.tipo==TIPO_DE_DATO.BOOLEANO and \
                                        TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="boolean".casefold():
                                        if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                            check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                            dictCheck={columnsNameList[colIndex]:val.val}
                                            if eval(check,dictCheck):
                                                columnsDict[listaCol[counter]]=val.val
                                            else:
                                                sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name))
                                                flag=True
                                                break
                                        else:
                                            columnsDict[listaCol[counter]]=val.val
                                    else:
                                        flag=True
                                        sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                        print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name) + " "+columnsNameList[colIndex] + " "+str(val.val))
                                else:
                                    flag=True
                                    print("ERROR: se está intentando ingresar una misma columna dentro de una sentencia INSERT")
                                    break
                                counter+=1
                            else:
                                flag=True
                                sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_column
                                print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+" "+listaCol[counter])
                        if not flag:
                            # THIS SECOND FLAG WILL CHECK IF A REMAINING COLUMN CAN BE NULL, IF NOT, RETURNS TRUE AND IS AN ERROR
                            secondFlag=False
                            for column in columnsNameList:
                                # print(column)
                                if not checkColumnsDictionary(columnsDict,column):
                                    # print("La columna "+column+" no esta especificada en el diccionario, buscando si puede tener un valor nulo")
                                    # THIS MEANS A COLUMN EXISTS IN THE TABLE, BUT IT WAS NOT DECLARED ON THE INSERT SENTENCE
                                    # print("La anulabilidad de "+column+" es "+ str(TypeCheck.getNull(dbName,tabla1,column)))
                                    # print("El valor default de "+column+ " es "+str(TypeCheck.getDefault(dbName,tabla1,column)))
                                    if not TypeCheck.getNull(dbName,tabla1,column):
                                        
                                        
                                        # IF GETNULL RETURNS TRUE, THE DEFAULT VALUE HAS TO BE INSERTED, SO LET'S FIND IT
                                        if TypeCheck.getDefault(dbName,tabla1,column)!=None:
                                            # IF THE DEFAULT VALUE IS DISTINCT FROM NULL (IN THIS CASE IS NONE), APPEND IT TO THE INSERT LIST
                                            result.append(TypeCheck.getDefault(dbName,tabla1,column))
                                        else:
                                            # THERE WAS NOT A DEFAULT VALUE FOR THIS COLUMN, SO THIS IS AN ERROR, SO WE HAVE TO BREAK THE CYCLE
                                            secondFlag=True
                                            break
                                    else:
                                        if TypeCheck.getDefault(dbName,tabla1,column)!=None:
                                            result.append(TypeCheck.getDefault(dbName,tabla1,column))
                                        else:
                                            # THERE WAS NOT A DEFAULT VALUE FOR THIS COLUMN, SO THIS IS AN ERROR, SO WE HAVE TO BREAK THE CYCLE
                                            result.append(None)
                                else:
                                    # IF THE COLUMN EXISTS IN THE DICTIONARY, THE JUST APPEND IT TO THE INSERT LIST
                                    # THE ORDER IS DEFINED BY COLUMNSNAMELIST
                                    result.append(columnsDict[column])
                            # CHECKING IF NO ERRORS WERE PRODUCED
                            if not secondFlag:
                                # FINALLY, WE MUST ENSURE ALL THE COLUMNS FROM THE DICTIONARY ARE COLUMNS FROM THE TABLE
                                # WE ARE GONNA USE A THIRD FLAG :/
                                thirdFlag=False
                                for itemDict in list(columnsDict.keys()):
                                    # print(itemDict)
                                    if not itemDict in columnsNameList:
                                        thirdFlag=True
                                        break
                                if not thirdFlag:
                                    print("Llamando a la funcion insert("+dbName+","+tabla1+","+str(result)+").")
                                    print(DBMS.insert(dbName,tabla1,result))
                                else:
                                    sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_column
                                    print("ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+" "+listaCol[counter])
                            else:
                                print("ERROR: Una o varias columnas no han sido especificadas y no pueden ser nulas")
                        else:
                            print("ERROR AL INSERTAR EN LA BD")
                    else:
                        print("ERROR: La cantidad de parámetros no coincide con la cantidad de datos a ingresar")        


# Delete from a table
class DeleteTabla(Instruccion):
    def __init__(self, tabla, condiciones = None):
        self.tabla = tabla
        self.condiciones = condiciones

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DELETE TABLE\" ];"

        nodo += "\nFROM" + identificador + "[ label = \"FROM\" ];"
        nodo += "\n" + identificador + " -> FROM" + identificador + ";"
        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\nFROM" + identificador + " -> NAME" + identificador + ";"

        if self.condiciones:
            nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
            nodo += "\n" + identificador + " -> WHERE" + identificador + ";"

            for condicion in self.condiciones:
                nodo += "\nWHERE" + identificador + " -> " + str(hash(condicion)) + ";"
                nodo += condicion.dibujar()

        return nodo

class UpdateTable(Instruccion):
    def __init__(self, tabla, asignaciones, condiciones = None):
        self.tabla = tabla
        self.asignaciones = asignaciones
        self.condiciones = condiciones

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DELETE TABLE\" ];"

        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";"

        nodo += "\nSET" + identificador + "[ label = \"SET\" ];"
        nodo += "\n" + identificador + " -> SET" + identificador + ";"

        for asignacion in self.asignaciones:
            nodo += "\nSET" + identificador + " -> " + str(hash(asignacion)) + ";"
            nodo += asignacion.dibujar()

        if self.condiciones:
            nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
            nodo += "\n" + identificador + " -> WHERE" + identificador + ";"

            for condicion in self.condiciones:
                nodo += "\nWHERE" + identificador + " -> " + str(hash(condicion)) + ";"
                nodo += condicion.dibujar()

        return nodo