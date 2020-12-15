import Gramatica as g
import tablasimbolos as TS
from expresiones import *
from instrucciones import *
from reporteAST import *

listaInstrucciones = []

def crear_BaseDatos(instr,ts):
    #verificacion crea la base de datos si no existe, si existe no devuelve error
    #reemplazar si la base de datos si existe la reemplaza
    if instr.reemplazar:
        ''
        #eliminar
        #crear
    elif instr.verificacion:
        ''
        #buscar si existe
            #si existe break
            #si no existe se crea
    else:
        ''
        #buscar si existe
            #si existe, mostrar error
            #si no existe , se crea

    print('reemplazar:',instr.reemplazar,'verificar:',instr.verificacion,'nombre:',instr.nombre,'propietario:',instr.propietario,'modo:',instr.modo)


def crear_Tabla(instr,ts):
    print('nombre:',instr.nombre,'padre:',instr.padre)
    for colum in instr.columnas :
        if isinstance(colum, llaveTabla) : 
            print('llaves Primaria:',colum.tipo,'lista:',colum.columnas,'tablaref',colum.referencia,'listaref',colum.columnasRef)
        elif isinstance(colum, columnaTabla) : 
            print('id:',colum.id,'Tipo:',colum.tipo,'valor',colum.valor,'zonahoraria',colum.zonahoraria)
            for atributoC in colum.atributos :
                if isinstance(atributoC, atributoColumna):
                    print('atributos-->','default:',atributoC.default,'constraint:',atributoC.constraint,'null:',atributoC.null,'unique:',atributoC.unique,'primary:',atributoC.primary,'check:',atributoC.check)
                        




def resolver_cadena(expCad, tablasimbolos) :
    if isinstance(expCad, ExpresionConcatenar) :
        exp1 = resolver_cadena(expCad.exp1, tablasimbolos)
        exp2 = resolver_cadena(expCad.exp2, tablasimbolos)
        return exp1 + exp2
    elif isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    elif isinstance(expCad, ExpresionCadenaNumerico) :
        return str(resolver_expresion_aritmetica(expCad.exp, tablasimbolos))
    else :
        print('Error: Expresión cadena no válida')


def resolver_expresion_logica(expLog, tablasimbolos) :
    exp1 = resolver_expresion_aritmetica(expLog.exp1, tablasimbolos)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, tablasimbolos)
    if expLog.operador == OPERACION_LOGICA.MAYOR_QUE : return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MENOR_QUE : return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
    if expLog.operador == OPERACION_LOGICA.DIFERENTE : return exp1 != exp2
    if expLog.operador == OPERACION_LOGICA.MAYORIGUALQUE : return exp1 >= exp2
    if expLog.operador == OPERACION_LOGICA.MENORIGUALQUE : return exp1 <= exp2

def resolver_expresion_aritmetica(expNum, tablasimbolos) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, tablasimbolos)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, tablasimbolos)
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.POTENCIA : return pow(exp1,exp2)
        if expNum.operador == OPERACION_ARITMETICA.MODULO : return exp1 % exp2
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, tablasimbolos)
        return exp * -1
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador) :
        return tablasimbolos.obtener(expNum.id).valor

def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    global listaInstrucciones 
    listaInstrucciones  = instrucciones
    for instr in instrucciones :
        if isinstance(instr, CrearBD) : crear_BaseDatos(instr,ts)
        elif isinstance(instr, CrearTabla) : crear_Tabla(instr,ts)
        else : print('Error: instrucción no válida')



def Analisar(input):
    instrucciones = g.parse(input)
    print(instrucciones)
    ts_global = TS.TablaDeSimbolos()
    procesar_instrucciones(instrucciones,ts_global)

#Metodos para graficar el ast 
def generarAST():
    global listaInstrucciones
    astGraph = DOTAST()
    astGraph.getDot(listaInstrucciones)

