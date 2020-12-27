import typeChecker.typeEnum as typeEnum
from astExpresion import ExpresionID
from astDDL import Instruccion
import storageManager.jsonMode as DBMS
from useDB.instanciaDB import DB_ACTUAL
import typeChecker.typeReference as TypeCheck
import entorno as env
from astExpresion import TIPO_DE_DATO
from astFunciones import FuncionTime,FuncionCadena
from useDB import instanciaDB
from reporteErrores.errorReport import ErrorReport
import sqlErrors as sqlErrors

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
    def __init__(self, tabla, valores,listaColumnas=None,linea=0):
        self.tabla = tabla
        self.valores = valores
        self.listaColumnas=listaColumnas
        self.linea=linea
    
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
            return ErrorReport('Semántico',"ERROR: database does not exist",self.linea)
        else:
            # Check if the table exists into the db
            tables=TypeCheck.tableExist(dbName,tabla1)
            if tables == False:
                sqlError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_table
                return ErrorReport('Semántico',"ERROR "+sqlError.value+": "+str(sqlError.name)+" \'"+tabla1+"\'",self.linea)
            else:
                flag=False
                counter=0
                result = []
                columnsNameList=list(TypeCheck.getColumns(dbName,tabla1).keys())
                if listaCol==None:
                    # INSERT CHECKING ALL COLUMNS ON THEIR RESPECTIVE ORDER
                    if len(columnsNameList)==len(valores1):
                        for val in valores1:
                            if isinstance(val,FuncionTime) or isinstance(val,FuncionCadena):
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
                                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
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
                                        return ErrorReport('Semántico',"ERROR: la longitud de la cadena es mayor a lo permitido por el tipo de dato",self.linea)
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
                                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                        else:
                                            if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                                check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                                dictCheck={columnsNameList[counter]:val.val}
                                                if eval(check,dictCheck):
                                                    result.append(val.val)
                                                else:
                                                    sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                    flag=True
                                                    break
                                            else:
                                                result.append(val.val)
                                    else:
                                        return ErrorReport('Semántico',"ERROR: el tamaño de la cadena es mayor a lo permitido por el tipo de dato",self.linea)
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
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                    else:
                                        if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                            check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                            dictCheck={columnsNameList[counter]:val.val}
                                            if eval(check,dictCheck):
                                                result.append(val.val)
                                            else:
                                                sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
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
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                flag=True
                                                break
                                        else:
                                            result.append(val.val)
                                    else:
                                        flag=True
                                        sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                elif typeEnum.enumExist(TypeCheck.getType(dbName,tabla1,columnsNameList[counter])):
                                        enumVals=typeEnum.getEnum(TypeCheck.getType(dbName,tabla1,columnsNameList[counter]))
                                        if val.val in enumVals:
                                            result.append(val.val)
                                        else:
                                            flag=True
                                            sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+val.val+"' no coincide con el tipo "+TypeCheck.getType(dbName,tabla1,columnsNameList[counter]),self.linea)
                                        
                                else:
                                    flag=True
                                    sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
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
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                flag=True
                                                break
                                        else:
                                            result.append(val.val)
                                    else:
                                        return ErrorReport('Semántico',"ERROR: el tamaño del número no coincide con el tipo de dato",self.linea)
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
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                flag=True
                                                break
                                        else:
                                            result.append(val.val)
                                    else:
                                        return ErrorReport('Semántico',"ERROR: el tamaño del número no coincide con el tipo de dato",self.linea)
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
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                flag=True
                                                break
                                        else:
                                            result.append(val.val)
                                    else:
                                        return ErrorReport('Semántico',"ERROR: el tamaño del número no coincide con el tipo de dato",self.linea)
                                        flag=True
                                elif typeEnum.enumExist(TypeCheck.getType(dbName,tabla1,columnsNameList[counter])):
                                    enumVals=typeEnum.getEnum(TypeCheck.getType(dbName,tabla1,columnsNameList[counter]))
                                    if val.val in enumVals:
                                        result.append(val.val)
                                    else:
                                        flag=True
                                        sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+val.val+"' no coincide con el tipo "+TypeCheck.getType(dbName,tabla1,columnsNameList[counter]),self.linea)
                                else:
                                    flag=True
                                    sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                            elif val.tipo==TIPO_DE_DATO.DECIMAL:
                                if TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="decimal".casefold() or \
                                    TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="numeric".casefold():
                                    if not TypeCheck.getLenght(dbName,tabla1,columnsNameList[counter])==None:
                                                precision=TypeCheck.getPrecision(dbName,tabla1,columnsNameList[counter])
                                                scale_=TypeCheck.getScale(dbName,tabla1,columnsNameList[counter])
                                                flagPrecision=False
                                                flagScale=False
                                                
                                                if str(val.val).index('.')==len(str(val.val))-scale_-1 or str(val.val).index('.')==len(str(val.val))-scale_:
                                                    flagPrecision=True
                                                else:
                                                    flag=True
                                                    sqlTypeError=sqlErrors.sql_error_data_exception.numeric_value_out_of_range
                                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+str(val.val)+"' no coincide con con la escala del campo",self.linea)
                                                if len(str(val.val).replace('.',''))<=precision:
                                                    flagScale=True
                                                else:
                                                    flag=True
                                                    sqlTypeError=sqlErrors.sql_error_data_exception.numeric_value_out_of_range
                                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+str(val.val)+"' no coincide con con la precisión del campo",self.linea)
                                                if flagPrecision and flagScale:
                                                    result.append(val.val)
                                                
                                                    
                                elif TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="real".casefold() or \
                                    TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="double_precision".casefold() or \
                                    TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="money".casefold():
                                    if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                        check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                        dictCheck={columnsNameList[counter]:val.val}
                                        if eval(check,dictCheck):
                                            result.append(val.val)
                                        else:
                                            sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                            flag=True
                                            break
                                    else:
                                        result.append(val.val)
                                elif typeEnum.enumExist(TypeCheck.getType(dbName,tabla1,columnsNameList[counter])):
                                    enumVals=typeEnum.getEnum(TypeCheck.getType(dbName,tabla1,columnsNameList[counter]))
                                    if val.val in enumVals:
                                        result.append(val.val)
                                    else:
                                        flag=True
                                        sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+val.val+"' no coincide con el tipo "+TypeCheck.getType(dbName,tabla1,columnsNameList[counter]),self.linea)
                                else:
                                    flag=True
                                    sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                            elif val.tipo==TIPO_DE_DATO.BOOLEANO:
                                if TypeCheck.getType(dbName,tabla1,columnsNameList[counter]).casefold()=="boolean".casefold():
                                    if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter])==None:
                                        check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[counter]).lower()
                                        dictCheck={columnsNameList[counter]:val.val}
                                        if eval(check,dictCheck):
                                            result.append(val.val)
                                        else:
                                            sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                    else:
                                        result.append(val.val)
                                elif typeEnum.enumExist(TypeCheck.getType(dbName,tabla1,columnsNameList[counter])):
                                    enumVals=typeEnum.getEnum(TypeCheck.getType(dbName,tabla1,columnsNameList[counter]))
                                    if val.val in enumVals:
                                        result.append(val.val)
                                    else:
                                        flag=True
                                        sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+val.val+"' no coincide con el tipo "+TypeCheck.getType(dbName,tabla1,columnsNameList[counter]),self.linea)
                                else:
                                    flag=True
                                    sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)    
                            else:
                                flag=True
                                sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                            counter+=1
                        if not flag:
                            print("Llamando a la funcion insert("+dbName+","+tabla1+","+str(result)+").")
                            print(DBMS.insert(dbName,tabla1,result))
                        else:
                            print("ERROR AL INSERTAR EN LA BD")
                    else:
                        return ErrorReport('Semántico',"ERROR: La cantidad de parámetros indicados no coincide con los campos de la tabla",self.linea)
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
                                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                else:
                                                    if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                        check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                        dictCheck={columnsNameList[colIndex]:val.val}
                                                        if eval(check,dictCheck):
                                                            columnsDict[listaCol[counter]]=val.val
                                                        else:
                                                            sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                            flag=True
                                                            break
                                                    else:
                                                        columnsDict[listaCol[counter]]=val.val
                                                    
                                            else:
                                                return ErrorReport('Semántico',"ERROR: la longitud de la cadena es mayor a lo permitido por el tipo de dato",self.linea)
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
                                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                else:
                                                    if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                        check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                        dictCheck={columnsNameList[colIndex]:val.val}
                                                        if eval(check,dictCheck):
                                                            columnsDict[listaCol[counter]]=val.val
                                                        else:
                                                            sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                            flag=True
                                                            break
                                                    else:
                                                        columnsDict[listaCol[counter]]=val.val
                                            else:
                                                return ErrorReport('Semántico',"ERROR: el tamaño de la cadena es mayor a lo permitido por el tipo de dato",self.linea)
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
                                                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                            else:
                                                if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                    check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                    dictCheck={columnsNameList[colIndex]:val.val}
                                                    if eval(check,dictCheck):
                                                        columnsDict[listaCol[counter]]=val.val
                                                    else:
                                                        sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
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
                                                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                        flag=True
                                                        break
                                                else:
                                                    columnsDict[listaCol[counter]]=val.val
                                            else:
                                                flag=True
                                                sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                        elif typeEnum.enumExist(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex])):
                                            enumVals=typeEnum.getEnum(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]))                                       
                                            if val.val in enumVals:
                                                columnsDict[listaCol[counter]]=val.val
                                            else:
                                                flag=True
                                                sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+val.val+"' no coincide con el tipo "+TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]),self.linea)
                                        else:
                                            flag=True
                                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_column
                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+" 1 "+listaCol[counter],self.linea)
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
                                                return ErrorReport('Semántico',"ERROR: el tamaño del número no coincide con el tipo de dato",self.linea)
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
                                                return ErrorReport('Semántico',"ERROR: el tamaño del número no coincide con el tipo de dato",self.linea)
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
                                                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                        flag=True
                                                        break
                                                else:
                                                    columnsDict[listaCol[counter]]=val.val
                                            else:
                                                return ErrorReport('Semántico',"ERROR: el tamaño del número no coincide con el tipo de dato",self.linea)
                                                flag=True
                                        elif typeEnum.enumExist(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex])):
                                            enumVals=typeEnum.getEnum(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]))
                                            if val.val in enumVals:
                                                columnsDict[listaCol[counter]]=val.val
                                            else:
                                                flag=True
                                                sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+val.val+"' no coincide con el tipo "+TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]),self.linea)
                                        else:
                                            flag=True
                                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                    elif val.tipo==TIPO_DE_DATO.DECIMAL:
                                        if TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="decimal".casefold() or \
                                            TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="numeric".casefold():
                                             if not TypeCheck.getLenght(dbName,tabla1,columnsNameList[colIndex])==None:
                                                precision=TypeCheck.getPrecision(dbName,tabla1,columnsNameList[colIndex])
                                                scale_=TypeCheck.getScale(dbName,tabla1,columnsNameList[colIndex])
                                                flagPrecision=False
                                                flagScale=False
                                                if str(val.val).index('.')==len(str(val.val))-scale_-1 or str(val.val).index('.')==len(str(val.val))-scale_:
                                                    flagPrecision=True
                                                else:
                                                    flag=True
                                                    sqlTypeError=sqlErrors.sql_error_data_exception.numeric_value_out_of_range
                                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+str(val.val)+"' no coincide con con la escala del campo",self.linea)

                                                if len(str(val.val).replace('.',''))<=precision:
                                                    flagScale=True
                                                else:
                                                    flag=True
                                                    sqlTypeError=sqlErrors.sql_error_data_exception.numeric_value_out_of_range
                                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+str(val.val)+"' no coincide con con la precisión del campo",self.linea)

                                                if flagPrecision and flagScale:
                                                    columnsDict[listaCol[counter]]=val.val

                                        elif TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="real".casefold() or \
                                            TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="double_precision".casefold() or \
                                            TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="money".casefold():
                                            if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                                check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                                dictCheck={columnsNameList[colIndex]:val.val}
                                                if eval(check,dictCheck):
                                                    columnsDict[listaCol[counter]]=val.val
                                                else:
                                                    sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                    flag=True
                                                    break
                                            else:
                                                columnsDict[listaCol[counter]]=val.val
                                        elif typeEnum.enumExist(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex])):
                                            enumVals=typeEnum.getEnum(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]))
                                            if val.val in enumVals:
                                                columnsDict[listaCol[counter]]=val.val
                                            else:
                                                flag=True
                                                sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+val.val+"' no coincide con el tipo "+TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]),self.linea)
                                        else:
                                            flag=True
                                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+ " "+columnsNameList[colIndex] + " "+str(val.val),self.linea)
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
                                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                    flag=True
                                                    break
                                            else:
                                                columnsDict[listaCol[counter]]=val.val
                                        elif typeEnum.enumExist(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex])):
                                            enumVals=typeEnum.getEnum(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]))
                                            if val.val in enumVals:
                                                columnsDict[listaCol[counter]]=val.val
                                            else:
                                                flag=True
                                                sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+val.val+"' no coincide con el tipo "+TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]),self.linea)
                                        else:
                                            flag=True
                                            sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                            return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+ " "+columnsNameList[colIndex] + " "+str(val.val),self.linea)
                                    elif val.tipo==TIPO_DE_DATO.BOOLEANO and \
                                        TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]).casefold()=="boolean".casefold():
                                        if not TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex])==None:
                                            check=TypeCheck.getCheck(dbName,tabla1,columnsNameList[colIndex]).lower()
                                            dictCheck={columnsNameList[colIndex]:val.val}
                                            if eval(check,dictCheck):
                                                columnsDict[listaCol[counter]]=val.val
                                            else:
                                                sqlTypeError=sqlErrors.sql_error_integrity_constraint_violation.check_violation
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name),self.linea)
                                                flag=True
                                                break
                                        elif typeEnum.enumExist(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex])):
                                            enumVals=typeEnum.getEnum(TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]))
                                            if val.val in enumVals:
                                                columnsDict[listaCol[counter]]=val.val
                                            else:
                                                flag=True
                                                sqlTypeError=sqlErrors.sql_error_data_exception.invalid_parameter_value
                                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+": el valor indicado '"+val.val+"' no coincide con el tipo "+TypeCheck.getType(dbName,tabla1,columnsNameList[colIndex]),self.linea)
                                        else:
                                            columnsDict[listaCol[counter]]=val.val
                                    else:
                                        flag=True
                                        sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch
                                        return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name) + " "+columnsNameList[colIndex] + " "+str(val.val),self.linea)
                                else:
                                    flag=True
                                    return ErrorReport('Semántico',"ERROR: se está intentando ingresar una misma columna dentro de una sentencia INSERT",self.linea)
                                    break
                                counter+=1
                            else:
                                flag=True
                                sqlTypeError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_column
                                return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+" 2 "+listaCol[counter],self.linea)
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
                                    return ErrorReport('Semántico',"ERROR "+sqlTypeError.value+": "+str(sqlTypeError.name)+" 3 "+listaCol[counter],self.linea)
                            else:
                                return ErrorReport('Semántico',"ERROR: Una o varias columnas no han sido especificadas y no pueden ser nulas",self.linea)
                        else:
                            print("ERROR AL INSERTAR EN LA BD")
                    else:
                        return ErrorReport('Semántico',"ERROR: La cantidad de parámetros no coincide con la cantidad de datos a ingresar",self.linea)        


# Delete from a table
class DeleteTabla(Instruccion):
    def __init__(self, tabla, condiciones = None,linea=0):
        self.tabla = tabla
        self.condiciones = condiciones
        self.linea=linea

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

    def transalateExpresion(self,input_:str)->str:
        input_=input_.replace(" = "," == ")
        input_=input_.replace(" ^ "," ** ")
        return input_

    def ejecutar(self,ts):
        # print(self.tabla)
        # print(self.condiciones.getExpresionToString())
        # print(self.linea)
        dbName=DB_ACTUAL.getName()
        # dbName="test"
        # Check if a db is in use
        if dbName==None:
            # Add this error to the errors Tree
            return ErrorReport('Semántico',"ERROR: database \'"+str(dbName)+"\' does not exist",self.linea)
        else:
            # Check if the table exists into the db
            tables=TypeCheck.tableExist(dbName,self.tabla)
            if not tables:
                sqlError=sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_table
                return ErrorReport('Semántico',"ERROR "+sqlError.value+": "+str(sqlError.name)+" \'"+self.tabla+"\'",self.linea)
            else:
                # dataList returns a list of lists
                dataList=DBMS.extractTable(dbName,self.tabla)
                # columnsList returns a list with the name of the columns
                if not self.condiciones==None:
                    print(self.transalateExpresion(self.condiciones.getExpresionToString()))
                    try:
                        columnsList=list(TypeCheck.getColumns(dbName,self.tabla))
                        evalDict={}
                        deleted=False
                        counter=0
                        for data in dataList:
                            index=len(data)
                            for i in range(index):
                                evalDict[columnsList[i]]=data[i]

                            if eval(self.transalateExpresion(self.condiciones.getExpresionToString()),evalDict):
                                pkFound=False
                                pkLists=[]
                                for item in columnsList:
                                    if TypeCheck.getPK(dbName,self.tabla,item):
                                        pkIndex=columnsList.index(item)
                                        pkLists.append(data[pkIndex])
                                        pkFound=True
                                if pkFound:
                                    print(DBMS.delete(dbName,self.tabla,pkLists))
                                    deleted=True
                                    counter+=1
                                else:
                                    print(DBMS.delete(dbName,self.tabla,dataList.index(data)))
                                    deleted=True
                                    counter+=1
                        if deleted:
                            print("Sentencia DELETE ejecutada correctamente, "+str(counter)+" filas afectadas.")
                        else:
                            print("Ninguna fila fue eliminada.")

                    except Exception as e:
                        sqlError=sqlErrors.sql_error_internal_error.internal_error
                        print(e)
                        return ErrorReport('Semántico',"ERROR "+sqlError.value+": "+str(sqlError.name),self.linea)
                else:
                    try:
                        columnsList=list(TypeCheck.getColumns(dbName,self.tabla))
                        evalDict={}
                        deleted=False
                        counter=0
                        for data in dataList:
                            index=len(data)
                            for i in range(index):
                                evalDict[columnsList[i]]=data[i]                        
                            pkFound=False
                            pkLists=[]
                            for item in columnsList:
                                if TypeCheck.getPK(dbName,self.tabla,item):
                                    pkIndex=columnsList.index(item)
                                    pkLists.append(data[pkIndex])
                                    pkFound=True
                            if pkFound:
                                print(DBMS.delete(dbName,self.tabla,pkLists))
                                deleted=True
                                counter+=1
                            else:
                                print(DBMS.delete(dbName,self.tabla,dataList.index(data)))
                                deleted=True
                                counter+=1
                        if deleted:
                            print("Sentencia DELETE ejecutada correctamente, "+str(counter)+" filas afectadas.")
                        else:
                            print("Ninguna fila fue eliminada.")

                    except:
                        sqlError=sqlErrors.sql_error_internal_error.internal_error
                        return ErrorReport('Semántico',"ERROR "+sqlError.value+": "+str(sqlError.name),self.linea)
                    


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
            nodo += "\n" + str(hash(asignacion)) + "[ label = \" " + asignacion + " = " + str(self.asignaciones[asignacion].val) + "\" ];"

        if self.condiciones:
            nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
            nodo += "\n" + identificador + " -> WHERE" + identificador + ";"

            for condicion in self.condiciones:
                nodo += "\nWHERE" + identificador + " -> " + str(hash(condicion)) + ";"
                nodo += condicion.dibujar()

        return nodo

    def ejecutar(self, ts):
        try:
            if DB_ACTUAL.getName() == None:
                return ErrorReport('Semantico', 'Not defined database to used', 0)
            elif not TypeCheck.databaseExist(DB_ACTUAL.getName()):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_invalid_schema_name.invalid_schema_name), 0)
            elif not TypeCheck.tableExist(DB_ACTUAL.getName(), self.tabla):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_table), 0)


            columnas = TypeCheck.getColumns(DB_ACTUAL.getName(),self.tabla)
            columnasIndex = self.__auxDict(columnas)

            #Evaluamos las nuevas expresiones xd
            posiblesValores = dict()
            for asign in self.asignaciones:
                temp = self.asignaciones[asign].ejecutar(None)
                if isinstance(temp, ErrorReport):
                    return temp
                posiblesValores[asign] = temp

            #Procesamos cada valor para determinar si podemos ingresar
            for valor in posiblesValores:
                temp = self.__processUpdateField(columnas[valor], posiblesValores[valor])
                if isinstance(temp, ErrorReport):
                    return temp
                posiblesValores[valor] = temp

            #Ahora evaluamos los checks en base a cada registroCambiado
            for cheq in posiblesValores:
                if columnas[cheq]['Check']:
                    try:
                        posible = eval(columnas[cheq]['Check'], posiblesValores)
                        if not posible:
                            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.check_violation), 0) 
                    except:
                        return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.integrity_constraint_violation), 0) 


        
            #Traemos todos los valores de las columnas
            registros = DBMS.extractTable(DB_ACTUAL.getName(),self.tabla)
            #Validacion WHERE
            if self.condiciones:
                tsLocal = env.Entorno()
                tsLocal = env.toEnviroment(columnas,tsLocal)

                auxAceptadas = list()
                for reg in range(len(registros)):
                    #Insertamos valores en la tabla de simbolos
                    for field in columnasIndex:
                        tsLocal.modificarSimbolo(field, registros[reg][columnasIndex[field]])
                    
                    valido = self.condiciones.ejecutar(tsLocal)
                    if valido.tipo != TIPO_DE_DATO.BOOLEANO:
                        raise Exception()

                    if valido.val:
                        auxAceptadas.append( reg )
                
                pkWhere = TypeCheck.getIndexPK(DB_ACTUAL.getName(), self.tabla)
                #Con PK
                if len(pkWhere) != 0:
                    for regCamb in auxAceptadas:
                        pkReg = list()
                        for pk in pkWhere:
                            pkReg.append(registros[regCamb][pk])
                        DBMS.update(DB_ACTUAL.getName(),self.tabla,posiblesValores,pkReg)
                #Sin PK
                else:
                    for regCamb in auxAceptadas:
                        DBMS.update(DB_ACTUAL.getName(),self.tabla,posiblesValores,[regCamb])
            #SIN WHERE
            else:
                pkNormal = TypeCheck.getIndexPK(DB_ACTUAL.getName(), self.tabla)
                #Con PK
                if len(pkNormal) != 0:
                    for regCamb in registros:
                        pkReg = list()
                        for pk in pkNormal:
                            pkReg.append(regCamb[pk])
                        DBMS.update(DB_ACTUAL.getName(),self.tabla,posiblesValores,pkReg)
                #Sin PK
                else:
                    for regCamb in range(len(registros)):
                        DBMS.update(DB_ACTUAL.getName(),self.tabla,posiblesValores,[regCamb])
                    
            
            return 'Deleted successful'
        except:
            return ErrorReport('Semantico', 'Error Fatal', 0)

    def __auxDict(self,columns: dict) -> dict:
        dicc = dict()
        aux = 0

        for item in columns:
            dicc[item] = aux
            aux += 1

        return dicc

    def __processUpdateField(self, pureColumn: dict, newValue: any) -> any:
        #Comprobamos esto antes de seguir
        if pureColumn['PK']:
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.integrity_constraint_violation), 0)
        if pureColumn['FK']:
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.foreign_key_violation), 0)
        if pureColumn['Unique']:
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.unique_violation), 0)

        #Comprobación de tipos
        pureValue = newValue.val
        if pureValue != None:
            if pureColumn['Type'] in ("SMALLINT", "BIGINT", "INTEGER") and newValue.tipo == TIPO_DE_DATO.ENTERO:
                if pureColumn['Type'] == "SMALLINT" and ( pureValue <= 32767 and pureValue >= -32768 ):
                    pass
                elif pureColumn['Type'] == "BIGINT" and ( pureValue <= 9223372036854775807 and pureValue >= -9223372036854775808 ):
                    pass
                elif pureColumn['Type'] == "INTEGER" and ( pureValue <= 2147483647 and pureValue >= -2147483648 ):
                    pass
                else:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch), 0)
            elif pureColumn['Type'] in ("DECIMAL", "NUMERIC", "REAL", "DOUBLE_PRECISION", "MONEY") and \
            (newValue.tipo == TIPO_DE_DATO.ENTERO or newValue.tipo == TIPO_DE_DATO.DECIMAL):
                #Forma de calcular la forma xd
                auxDecimal = (len(str(pureValue)),0)
                if isinstance(pureValue, float):
                    auxDecimal = str(pureValue).split('.')
                    auxDecimal = (len(str(pureValue)),len(auxDecimal[1]))

                if pureColumn['Type'] in ("DECIMAL","NUMERIC") and \
                (auxDecimal[0] <= pureColumn['Lenght']['Precision'] and auxDecimal[1] <=  pureColumn['Lenght']['Scale']) :
                    pass
                elif pureColumn['Type'] == "REAL" and auxDecimal[1] < 6:
                    pass
                elif pureColumn['Type'] == "DOUBLE_PRECISION" and auxDecimal[1] < 15:
                    pass
                elif pureColumn['Type'] == "MONEY" and auxDecimal[1] < 2:
                    pass
                else: 
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch), 0)           
                
            elif pureColumn['Type'] in ("CHAR", "TEXT", "VARCHAR", "DATE") and newValue.tipo == TIPO_DE_DATO.CADENA:
                if pureColumn['Type'] in ("CHAR","VARCHAR") and len(pureValue) < pureColumn['Lenght']:
                    pass
                elif pureColumn['Type'] == "DATE" and newValue.isFecha:
                    pass
                elif pureColumn['Type'] == "TEXT":
                    pass
                else: 
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch), 0)
            elif pureColumn['Type'] == "BOOLEAN" and newValue.tipo == TIPO_DE_DATO.BOOLEANO:
                pass
            elif typeEnum.enumExist(pureColumn['Type']):
                if not pureValue in typeEnum.getEnum(pureColumn['Type']):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch), 0)
            else:
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch), 0)

        #Comprobaciones especiales, excluyendo checks
        if not pureColumn['Null'] and pureValue == None:
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.not_null_violation), 0)

        return pureValue
        