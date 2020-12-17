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
outputTxt = [] #guarda los mensajes a mostrar en consola
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

def agregarMensjae(tipo,mensaje):
    global outputTxt
    txtOut=MensajeOut()
    txtOut.tipo=tipo
    txtOut.mensaje=mensaje
    outputTxt.append(txtOut)


#---------Ejecucion Funciones EDD-------------
def crear_BaseDatos(instr,ts):
    nombreDB=resolver_operacion(instr.nombre,ts)
    
    msg='Creando base de datos: '+nombreDB
    agregarMensjae('normal',msg)

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
        if result==1:
            msg='Error en EDD'
            agregarMensjae('error',msg)
        else:
            msg='Fue Reemplazada'
            agregarMensjae('alert',msg)

    elif instr.verificacion:
        if result==0:
            msg='Todo OK'
            agregarMensjae('exito',msg)
        elif result==2 :
            msg='existe pero se omite error'
            agregarMensjae('alert',msg)
            #si retorna error no se muestra
    else:
        if result==0:
            msg='Todo OK'
            agregarMensjae('exito',msg)
        elif result==2:
            msg='Error base de existente: '+nombreDB
            agregarMensjae('error',msg)
        elif result==1:
            msg='Error en EDD'
            agregarMensjae('error',msg)

    #print('reemplazar:',instr.reemplazar,'verificar:',instr.verificacion,'nombre:',instr.nombre,'propietario:',instr.propietario,'modo:',instr.modo)

def eliminar_BaseDatos(instr,ts):
    nombreDB=str(resolver_operacion(instr.nombre,ts))
    eliminarOK=False;
    #result=0 operacion exitosa
    #result=1 error en la operacion
    #result=2 base de datos no existente  
    result = EDD.dropDatabase(nombreDB)
    msg='Eliminado Base de datos: '+nombreDB;
    agregarMensjae('normal',msg)
    
    if(instr.existencia):
        if(result==0):
            eliminarOK=True;
            msg='Todo OK'
            agregarMensjae('exito',msg)
        else:
            eliminarOK=False
            msg='no se muestra el error'
            agregarMensjae('alert',msg)
            #si retorna error no se muestra
    else:
        if(result==0):
            eliminarOK=True;
            msg='Todo OK'
            agregarMensjae('exito',msg)
        elif(result==1):
            eliminarOK=False
            msg='Error en EDD'
            agregarMensjae('error',msg)
        else:
            msg='Error base de datos no existente: '+nombreDB
            agregarMensjae('error',msg)
    
    if eliminarOK:
        EliminarTablaTemp(nombreDB,'all')#eliminar los temporales

    #print('nombre:',instr.nombre,'validarExistencia',instr.existencia)

def mostrar_db(instr,ts):
    #retorna una lista[db1,db2...], si no hay estara vacia[]
    result=EDD.showDatabases()
    msg='Lista de bases de datos'
    agregarMensjae('normal',msg)

    if not result:
        msg='No existen bases de datos ...' 
        agregarMensjae('alert',msg)   
    else:
        for val in result:
            agregarMensjae('exito',val)

def eliminar_Tabla(instr,ts):
    nombreT=''
    nombreT=resolver_operacion(instr.nombre,ts)

    #Valor de retorno: 0 operación exitosa
    # 1 error en la operación, 
    # 2 database no existente, 
    # 3 table no existente.
    result=EDD.dropTable(baseActiva,nombreT)
    eliminarOK=False;

    msg='Eliminar Tabla:'+nombreT
    agregarMensjae('normal',msg)
    if(instr.existencia):
        if(result==0):
            msg='Tabla eliminada'
            agregarMensjae('exito',msg)
            eliminarOK=True
        else:
            msg='se omite error'
            agregarMensjae('alert',msg)
    else:
        if(result==0):
            msg='Tabla eliminada'
            agregarMensjae('exito',msg)
            eliminarOK=True
        elif(result==1):
            msg='Error en EDD'
            agregarMensjae('error',msg)
        elif(result==2):
            msg='no existe la base de datos activa:'+baseActiva
            agregarMensjae('error',msg)
        elif(result==3):
            msg='Tabla no existe:'+nombreT
            agregarMensjae('error',msg)
        
    if eliminarOK:
        EliminarTablaTemp(baseActiva,nombreT)

    #print('nombre:',instr.nombre,'validarExistencia',instr.existencia)





#-----pendientes
def crear_Tabla(instr,ts):
    nombreT=resolver_operacion(instr.nombre,ts)
    listaColumnas=[]
    crearOK=True

    msg='Creando Tabla:'+nombreT
    agregarMensjae('normal',msg)
    contC=0# variable para contar las columnas a mandar a EDD

    print('padre:',instr.padre)
    #recorrer las columnas
    for colum in instr.columnas :
        colAux=Columna_run()#columna temporal para almacenar
        if isinstance(colum, llaveTabla) :
            #listado de foraneas o primarias compuestas
            print('llaves Primaria:',colum.tipo,'lista:',colum.columnas,'tablaref',colum.referencia,'listaref',colum.columnasRef)
        elif isinstance(colum, columnaTabla) :
            contC=contC+1
            colAux.nombre=resolver_operacion(colum.id,ts)#guardar nombre col
            if isinstance(colum.tipo,Operando_ID):
                #revisar la lista de Types
                ' '
            else:
                colAux.tipo=colum.tipo #guardar tipo col

            #atributos es una lista o False
                #el atributo check trae otra lista
            print('id:',colum.id,'Tipo:',colum.tipo,'valor',colum.valor,'zonahoraria',colum.zonahoraria)
            if(colum.valor!=False):
                '''aca se debe verificar el valor es una lista'''
            if(colum.zonahoraria!=False):
                '''aca se debe verificar la zonahoraria es una lista'''
            if(colum.atributos!=False):
                #aca se debe verificar la lista de atributos de una columna
                for atributoC in colum.atributos :
                    if isinstance(atributoC, atributoColumna):
                        print('atributos-->','primary:',atributoC.primary,'check:',atributoC.check)
                        if(atributoC.default!=None):
                            if(colAux.default==None):
                                colAux.default=resolver_operacion(atributoC.default,ts)#guardar default
                            else:
                                crearOK=False
                                msg='atributo default repetido en Col:'+colAux.nombre
                                agregarMensjae('error',msg)
                        elif(atributoC.constraint!=None):
                            if(colAux.constraint==None):
                                colAux.constraint=atributoC.constraint#guardar constraint
                            else:
                                crearOK=False
                                msg='atributo constraint repetido en Col:'+colAux.nombre
                                agregarMensjae('error',msg)
                        elif(atributoC.null!=None):
                            if(colAux.anulable==None):
                                colAux.anulable=atributoC.null#guardar anulable
                            else:
                                crearOK=False
                                msg='atributo anulable repetido en Col:'+colAux.nombre
                                agregarMensjae('error',msg)
                        elif(atributoC.unique!=None):
                            if(colAux.unique==None):
                                colAux.unique=atributoC.unique#guardar unique
                            else:
                                crearOK=False
                                msg='atributo unique repetido en Col:'+colAux.nombre
                                agregarMensjae('error',msg)
                        elif(atributoC.primary!=None):
                            if(colAux.primary==None):
                                colAux.primary=atributoC.primary#guardar primary
                            else:
                                crearOK=False
                                msg='atributo primary repetido en Col:'+colAux.nombre
                                agregarMensjae('error',msg)
                        elif(atributoC.check != None):
                            for exp in atributoC.check:
                                print('resultado: ',resolver_operacion(exp,ts))
            

            #agregar la columna
            listaColumnas.append(Columna_run)

    #analisas si las columnas estan bien
    #buscar las tablas de una base de datos retorna una lista de tablas
    if(crearOK):
        result=EDD.showTables(baseActiva)
        if(result!=None):
            for tab in result:
                if tab==nombreT:
                    msg='Error la tabla ya existe:'+nombreT
                    agregarMensjae('error',msg)
                    crearOK=False
                    break
            if crearOK:
                EDD.createTable(baseActiva,nombreT,contC)
                insertartabla(listaColumnas,nombreT)
                msg='Todo OK'
                agregarMensjae('exito',msg)
        else:
            msg='no existe la base de datos activa:'+baseActiva
            agregarMensjae('error',msg)

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
    outputTxt=[]
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

