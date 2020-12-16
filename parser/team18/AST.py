import Gramatica as g
import tablasimbolos as TS
from expresiones import *
from instrucciones import *
from reporteAST import *
from temporal import *

#---------variables globales
listaInstrucciones = []
DB_existente = []
outputTxt=' '


def crear_BaseDatos(instr,ts):
    nombreDB=resolver_operacion(instr.nombre,ts)

    global outputTxt
    outputTxt+='\n> Creando base de datos: '+nombreDB

    #crear la nueva base de datos de forma temporal
    nuevaDB=Base_run()
    nuevaDB.nombre=nombreDB
    nuevaDB.activa=False;
    nuevaDB.tabla=[]

    #agregar la nueva base de datos a la lista temporal
    global DB_existente
    DB_existente.append(nuevaDB)

    #verificacion crea la base de datos si no existe, si existe no devuelve error
    #reemplazar si la base de datos si existe la reemplaza
    if instr.reemplazar:
        outputTxt+='\n\tReemplazar si existe'
        #eliminar
        #crear
    elif instr.verificacion:
        outputTxt+='\n\tsi existe no mostrar error'
        #buscar si existe
            #si existe break
            #si no existe se crea
    else:
        outputTxt+='\n\tsi hay error mostrarlo'
        #buscar si existe
            #si existe, mostrar error
            #si no existe , se crea
    print('reemplazar:',instr.reemplazar,'verificar:',instr.verificacion,'nombre:',instr.nombre,'propietario:',instr.propietario,'modo:',instr.modo)

def crear_Tabla(instr,ts):
    nombreT=resolver_operacion(instr.nombre,ts)

    global outputTxt
    outputTxt+='\n> Creando Tabla: '+nombreT

    print('nombre:',instr.nombre,'padre:',instr.padre)
    for colum in instr.columnas :
        if isinstance(colum, llaveTabla) : 
            print('llaves Primaria:',colum.tipo,'lista:',colum.columnas,'tablaref',colum.referencia,'listaref',colum.columnasRef)
        elif isinstance(colum, columnaTabla) : 
            print('id:',colum.id,'Tipo:',colum.tipo,'valor',colum.valor,'zonahoraria',colum.zonahoraria)
            for atributoC in colum.atributos :
                if isinstance(atributoC, atributoColumna):
                    print('atributos-->','default:',atributoC.default,'constraint:',atributoC.constraint,'null:',atributoC.null,'unique:',atributoC.unique,'primary:',atributoC.primary,'check:',atributoC.check)
                    if(atributoC.check != None):
                        for exp in atributoC.check:
                            print('resultado: ',resolver_operacion(exp,ts))

def crear_Type(instr,ts):
    nombreT=resolver_operacion(instr.nombre,ts)

    global outputTxt
    outputTxt+='\n> Creando Type: '+nombreT
    print('nombre:',instr.nombre,'valores:',instr.valores)

def eliminar_BaseDatos(instr,ts):
    nombreDB=resolver_operacion(instr.nombre,ts)

    global outputTxt
    outputTxt+='\n> Eliminado Base de datos: '+nombreDB
    #verificar si hay existencia
    #eliminar
    if(instr.existencia):
        outputTxt+='\n\tVerificar existencia y omitir error'
        #si retorna error no se muestra
    else:
        outputTxt+='\n\tno verificar existencia y mostrar error'
        #si retorna error se muestra

    print('nombre:',instr.nombre,'validarExistencia',instr.existencia)

def eliminar_Tabla(instr,ts):
    print('nombre:',instr.nombre,'validarExistencia',instr.existencia)
    nombreT=''
    nombreT=resolver_operacion(instr.nombre,ts)

    global outputTxt
    outputTxt+='\n> Eliminado Tabla: '+nombreT
    #verificar si hay existencia
    #eliminar
    if(instr.existencia):
        outputTxt+='\n\tVerificar existencia y omitir error'
        #si retorna error no se muestra
    else:
        outputTxt+='\n\tno verificar existencia y mostrar error'
        #si retorna error se muestra

    print('nombre:',instr.nombre,'validarExistencia',instr.existencia)


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

def mostrar_db(instr,ts):
    '''
        Despliega el listado de base de datos
    '''
    global outputTxt
    outputTxt+='\n> Listado de base de datos ...'

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

