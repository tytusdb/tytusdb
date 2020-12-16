import Gramatica as g
import tablasimbolos as TS
from expresiones import *
from instrucciones import *
from reporteAST import *
from temporal import *
from storageManager import jsonMode as EDD

#---------variables globales
listaInstrucciones = []
listaTablas = [] #guarda las cabeceras de las tablas creadas
outputTxt=' '
baseActiva = 'pruebas' #Guarda la base temporalmente activa
#--------Ejecucion Datos temporales-----------
def insertartabla(columnas,nombre):
    nuevaTabla=Tabla_run()
    Tabla_run.nombre=nombre
    Tabla_run.Atributos=columnas

    global listaTablas
    listaTablas.append(nuevaTabla)

def EliminarTablaTemp(baseAc,nombre):
    global listaTablas
    pos=0
    #all para eliminar todas las tablas de una base de datos
    if(nombre=='all'):
        while pos< len(listaTablas):
            if(listaTablas[pos].basepadre==baseAc):
                listaTablas.pop(pos)
            else:
                pos=pos+1
    else:
        while pos< len(listaTablas):
            if(listaTablas[pos].nombre==nombre and listaTablas[pos].basepadre==baseAc):
                listaTablas.pop(pos)
                break
            else:
                pos=pos+1


#---------Ejecucion Funciones EDD-------------
def crear_BaseDatos(instr,ts):
    nombreDB=resolver_operacion(instr.nombre,ts)
    crearOK=False

    global outputTxt
    outputTxt+='\n> Creando base de datos: '+nombreDB

    #result=0 operacion exitosa
    #result=1 error en la operacion
    #result=2 base de datos existente       
    result = EDD.createDatabase(nombreDB)

    if instr.reemplazar and result==2:
        #eliminar
        EDD.dropDatabase(nombreDB)
        EliminarTablaTemp(nombreDB,'all')#eliminar los temporales
        #crear
        result = EDD.createDatabase(nombreDB)
        crearOK=True
        if result==1:
            crearOK=False
            outputTxt+='\n\tError en EDD'
        else:
            outputTxt+='\n\tFue Reemplazada'
    elif instr.verificacion:
        if result==2:
            crearOK=False
        else:
            crearOK=True
            #si retorna error no se muestra
    else:
        if result==2:
            crearOK=False
            outputTxt+='\n\tError base de existente: '+nombreDB
        else:
            crearOK=True
            outputTxt+='\n\tTodo OK'
    #print('reemplazar:',instr.reemplazar,'verificar:',instr.verificacion,'nombre:',instr.nombre,'propietario:',instr.propietario,'modo:',instr.modo)

def eliminar_BaseDatos(instr,ts):
    nombreDB=str(resolver_operacion(instr.nombre,ts))
    eliminarOK=False;
    #result=0 operacion exitosa
    #result=1 error en la operacion
    #result=2 base de datos no existente  
    result = EDD.dropDatabase(nombreDB)
    print('result edd:',result)
    global outputTxt
    outputTxt+='\n> Eliminado Base de datos: '+nombreDB;

    if(instr.existencia):
        if(result==0):
            eliminarOK=True;
            outputTxt+='\n\tTodo OK'
        else:
            eliminarOK=False
            #si retorna error no se muestra
    else:
        if(result==0):
            eliminarOK=True;
            outputTxt+='\n\tTodo OK'
        elif(result==1):
            eliminarOK=False
            outputTxt+='\n\tError en EDD'
        else:
            outputTxt+='\n\tError base de datos no existente: '+nombreDB
    
    if eliminarOK:
        EliminarTablaTemp(nombreDB,'all')#eliminar los temporales

    print('nombre:',instr.nombre,'validarExistencia',instr.existencia)

def mostrar_db(instr,ts):
    #retorna una lista[db1,db2...], si no hay estara vacia[]
    result=EDD.showDatabases()
    global outputTxt
    if not result:
        outputTxt+='\n> No existen bases de datos ...'    
    else:
        outputTxt+='\n> Listado de base de datos'
        for val in result:
            outputTxt+='\n>\t'+val
    
def eliminar_Tabla(instr,ts):
    nombreT=''
    nombreT=resolver_operacion(instr.nombre,ts)

    #Valor de retorno: 0 operación exitosa
    # 1 error en la operación, 
    # 2 database no existente, 
    # 3 table no existente.
    result=EDD.dropTable(baseActiva,nombreT)
    eliminarOK=False;

    global outputTxt
    outputTxt+='\n> Funcion Drop table'
    if(instr.existencia):
        if(result==0):
            outputTxt+='\n\tTabla eliminada:'+nombreT
            eliminarOK=True
        else:
            ''
        #si retorna error no se muestra
    else:
        if(result==0):
            outputTxt+='\n\tTabla eliminada:'+nombreT
            eliminarOK=True
        elif(result==1):
            outputTxt+='\n\tError en EDD'
        elif(result==2):
            outputTxt+='\n\tError en la base de datos activa:'+baseActiva
        elif(result==3):
            outputTxt+='\n\tError Tabla no existe:'+nombreT
        
    if eliminarOK:
        EliminarTablaTemp(baseActiva,nombreT)

    print('nombre:',instr.nombre,'validarExistencia',instr.existencia)





#-----pendientes

def crear_Tabla(instr,ts):
    nombreT=resolver_operacion(instr.nombre,ts)
    listaColumnas=[]

    global outputTxt
    outputTxt+='\n> Creando Tabla: '+nombreT
    contC=0# variable para contar las columnas a mandar a EDD

    print('nombre:',instr.nombre,'padre:',instr.padre)
    
    for colum in instr.columnas :
        if isinstance(colum, llaveTabla) : 
            print('llaves Primaria:',colum.tipo,'lista:',colum.columnas,'tablaref',colum.referencia,'listaref',colum.columnasRef)
        elif isinstance(colum, columnaTabla) :
            contC=contC+1 
            print('id:',colum.id,'Tipo:',colum.tipo,'valor',colum.valor,'zonahoraria',colum.zonahoraria)
            for atributoC in colum.atributos :
                if isinstance(atributoC, atributoColumna):
                    print('atributos-->','default:',atributoC.default,'constraint:',atributoC.constraint,'null:',atributoC.null,'unique:',atributoC.unique,'primary:',atributoC.primary,'check:',atributoC.check)
                    if(atributoC.check != None):
                        for exp in atributoC.check:
                            print('resultado: ',resolver_operacion(exp,ts))

    #analisas si las columnas estan bien
    #buscar las tablas de una base de datos retorna una lista de tablas
    result=EDD.showTables(baseActiva)
    crearOK=True
    if(result!=None):
        for tab in result:
            if tab==nombreT:
                outputTxt+='\n>\tError La tabla existe: '+nombreT
                crearOK=False
                break
        if crearOK:
            EDD.createTable(baseActiva,nombreT,contC)
            insertartabla(listaColumnas,nombreT)
    else:
        outputTxt+='\n>\tno existe la base de datos: '+baseActiva

def crear_Type(instr,ts):
    nombreT=resolver_operacion(instr.nombre,ts)

    global outputTxt
    outputTxt+='\n> Creando Type: '+nombreT
    print('nombre:',instr.nombre,'valores:',instr.valores)






def insertar_en_tabla(instr,ts):
    print('nombre:',instr.nombre,'valores:',instr.valores)
    nombreT=''
    nombreT=resolver_operacion(instr.nombre,ts)
    values=''

    for val in instr.valores:
        values+=str(resolver_operacion(val,ts))+' '

    global outputTxt
    outputTxt+='\n> Insertado en Tabla: '+nombreT
    outputTxt+='\n> Valores: '+values
    outputTxt+='\n> '+str(len(instr.valores))+' Filas afectadas'

def actualizar_en_tabla(instr,ts):
    print('nombre:',instr.nombre,'condicion:',instr.condicion,'valores:',instr.valores)
    nombreT=''
    nombreT=resolver_operacion(instr.nombre,ts)
    values=''

    for val in instr.valores:
        values+=resolver_operacion(val.nombre,ts)+'='+str(resolver_operacion(val.valor,ts))+' '

    global outputTxt
    outputTxt+='\n> Actualizado en Tabla: '+nombreT
    outputTxt+='\n> Valores: '+values
    outputTxt+='\n> '+str(len(instr.valores))+' Filas afectadas'

def eliminar_de_tabla(instr,ts):
    print('nombre:',instr.nombre,'condicion:',instr.condicion)
    nombreT=''
    nombreT=resolver_operacion(instr.nombre,ts)

    global outputTxt
    outputTxt+='\n> Eliminacion de Tabla: '+nombreT

def eleccion(instr,ts):
    print('nombre:',instr.nombre)
    nombreT=''
    nombreT=resolver_operacion(instr.nombre,ts)

    global outputTxt
    outputTxt+='\n> Base de Datos '+nombreT+' seleccionada'

def resolver_operacion(operacion,ts):
    if isinstance(operacion, Operacion_Logica_Unaria):
        op = resolver_operacion(operacion.op, ts)
        if isinstance(op, bool):
            return not(op)
        else:
            print('Error: No se permite operar los tipos involucrados')
    elif isinstance(operacion, Operacion_Logica_Binaria):
        op1 = resolver_operacion(operacion.op1,ts)
        op2 = resolver_operacion(operacion.op2,ts)
        if isinstance(op1, bool) and isinstance(op2, bool):
            if operacion.operador == OPERACION_LOGICA.AND: return op1 and op2
            elif operacion.operador == OPERACION_LOGICA.OR: return op1 or op2 
        else:
            print('Error: No se permite operar los tipos involucrados')
    elif isinstance(operacion, Operacion_Relacional):
        op1 = resolver_operacion(operacion.op1,ts)
        op2 = resolver_operacion(operacion.op2,ts)
        if isinstance(op1, (int,float)) and isinstance(op2, (int,float)):
            if operacion.operador == OPERACION_RELACIONAL.IGUAL: return op1 == op2
            elif operacion.operador == OPERACION_RELACIONAL.DIFERENTE: return op1 != op2
            elif operacion.operador == OPERACION_RELACIONAL.MAYORIGUALQUE: return op1 >= op2
            elif operacion.operador == OPERACION_RELACIONAL.MENORIGUALQUE: return op1 <= op2
            elif operacion.operador == OPERACION_RELACIONAL.MAYOR_QUE: return op1 > op2
            elif operacion.operador == OPERACION_RELACIONAL.MENOR_QUE: return op1 < op2
        elif isinstance(op1, (str)) and isinstance(op2, (str)):
            if operacion.operador == OPERACION_RELACIONAL.IGUAL: return op1 == op2
            elif operacion.operador == OPERACION_RELACIONAL.DIFERENTE: return op1 != op2
            elif operacion.operador == OPERACION_RELACIONAL.MAYORIGUALQUE: return op1 >= op2
            elif operacion.operador == OPERACION_RELACIONAL.MENORIGUALQUE: return op1 <= op2
            elif operacion.operador == OPERACION_RELACIONAL.MAYOR_QUE: return op1 > op2
            elif operacion.operador == OPERACION_RELACIONAL.MENOR_QUE: return op1 < op2
        else:
            print('Error: No se permite operar los tipos involucrados') 
    elif isinstance(operacion, Operacion_Aritmetica):
        op1 = resolver_operacion(operacion.op1,ts)
        op2 = resolver_operacion(operacion.op2,ts)
        if isinstance(op1, (int,float)) and isinstance(op2, (int,float)):
            if operacion.operador == OPERACION_ARITMETICA.MAS: return op1 + op2
            elif operacion.operador == OPERACION_ARITMETICA.MENOS: return op1 - op2
            elif operacion.operador == OPERACION_ARITMETICA.POR: return op1 * op2
            elif operacion.operador == OPERACION_ARITMETICA.DIVIDIDO: return op1 / op2
            elif operacion.operador == OPERACION_ARITMETICA.POTENCIA: return op1 ** op2
            elif operacion.operador == OPERACION_ARITMETICA.MODULO: return op1 % op2
        else:
            print('Error: No se permite operar los tipos involucrados') 
    elif isinstance(operacion, Operacion_Especial_Binaria):
        op1 = resolver_operacion(operacion.op1,ts)
        op2 = resolver_operacion(operacion.op2,ts)
        if isinstance(op1, int) and isinstance(op2, int):
            if operacion.operador == OPERACION_ESPECIAL.AND2: return op1 & op2
            elif operacion.operador == OPERACION_ESPECIAL.OR2: return op1 | op2
            elif operacion.operador == OPERACION_ESPECIAL.XOR: return op1 ^ op2
            elif operacion.operador == OPERACION_ESPECIAL.DEPDER: return op1 >> op2
            elif operacion.operador == OPERACION_ESPECIAL.DEPIZQ: return op1 << op2
        else:
            print('Error: No se permite operar los tipos involucrados')
    elif isinstance(operacion, Operacion_Especial_Unaria):
        op = resolver_operacion(operacion.op,ts)
        if isinstance(op, (int,float)):
            if operacion.operador == OPERACION_ESPECIAL.SQRT2: return op ** (1/2)
            elif operacion.operador == OPERACION_ESPECIAL.CBRT2: return op ** (1/3)
            elif operacion.operador == OPERACION_ESPECIAL.NOT2: 
                if isinstance(op, int): return ~op
                else: print('Error: No se permite operar los tipos involucrados')
            else:
                print('Error: No se permite operar los tipos involucrados')
    elif isinstance(operacion, Negacion_Unaria):
        op = resolver_operacion(operacion.op,ts)
        if isinstance(op, (int,float)):
            return op * -1
        else:
            print('Error: No se permite operar los tipos involucrados')
    elif isinstance(operacion, Operando_Booleano):
        return operacion.valor
    elif isinstance(operacion, Operando_Numerico):
        return operacion.valor
    elif isinstance(operacion, Operando_Cadena):
        return operacion.valor
    elif isinstance(operacion, Operando_ID):
        return operacion.id 

def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    global listaInstrucciones 
    listaInstrucciones  = instrucciones
    for instr in instrucciones :
        if isinstance(instr, CrearBD) : crear_BaseDatos(instr,ts)
        elif isinstance(instr, CrearTabla) : crear_Tabla(instr,ts)
        elif isinstance(instr, CrearType) : crear_Type(instr,ts)
        elif isinstance(instr, EliminarDB) : eliminar_BaseDatos(instr,ts)
        elif isinstance(instr, EliminarTabla) : eliminar_Tabla(instr,ts)
        elif isinstance(instr, Insertar) : insertar_en_tabla(instr,ts)
        elif isinstance(instr, Actualizar) : actualizar_en_tabla(instr,ts)
        elif isinstance(instr, Eliminar) : eliminar_de_tabla(instr,ts)
        elif isinstance(instr, DBElegida) : eleccion(instr,ts)
        elif isinstance(instr, MostrarDB) : mostrar_db(instr,ts)
        else : print('Error: instrucción no válida')



def Analisar(input):
    global outputTxt
    outputTxt='------------SALIDA--------------\n'
    EDD.dropAll() #eliminar para ir haciendo pruebas
    instrucciones = g.parse(input)
    print(instrucciones)
    ts_global = TS.TablaDeSimbolos()
    procesar_instrucciones(instrucciones,ts_global)
    return outputTxt

#Metodos para graficar el ast 
def generarAST():
    global listaInstrucciones
    astGraph = DOTAST()
    astGraph.getDot(listaInstrucciones)

