import Gramatica as g
import tablasimbolos as TS
from expresiones import *
from instrucciones import *
from reporteAST import *
from temporal import *
from storageManager import jsonMode as EDD
import Funciones as f
import math
import random
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from prettytable import PrettyTable


#---------variables globales
listaInstrucciones = []
listaTablas = [] #guarda las cabeceras de las tablas creadas
outputTxt = [] #guarda los mensajes a mostrar en consola
baseActiva = "" #Guarda la base temporalmente activa
#--------Ejecucion Datos temporales-----------
def reiniciarVariables():
    global outputTxt
    outputTxt=[]
    global listaTablas
    listaTablas=[]
    EDD.dropAll() #eliminar para ir haciendo pruebas, quitarlo al final
    baseActiva =""#eliminar para ir haciendo pruebas, quitarlo al final

def insertartabla(columnas,nombre):
    global listaTablas
    listaTablas.append(Tabla_run(baseActiva,nombre,columnas))

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

def agregarMensjae(tipo,mensaje,codigo):
    global outputTxt
    txtOut=MensajeOut()
    txtOut.tipo=tipo
    txtOut.mensaje=mensaje
    txtOut.codigo=codigo
    outputTxt.append(txtOut)

def buscarTabla(baseAc,nombre):
    pos=0
    while pos< len(listaTablas):
            if(listaTablas[pos].nombre==nombre and listaTablas[pos].basepadre==baseAc):
                return listaTablas[pos]
            else:
                pos=pos+1
    return None

def use_db(nombre):
    global baseActiva
    baseActiva = nombre

'''def elim_use():
    global baseActiva
    baseActiva = ""'''

#---------Ejecucion Funciones EDD-------------
def crear_BaseDatos(instr,ts):
    nombreDB=resolver_operacion(instr.nombre,ts).lower()
    
    msg='Creando base de datos: '+nombreDB
    agregarMensjae('normal',msg,'')

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
            agregarMensjae('error',msg,'')
        else:
            msg='Fue Reemplazada'
            agregarMensjae('alert',msg,'')

    elif instr.verificacion:
        if result==0:
            msg='Todo OK'
            agregarMensjae('exito',msg,'')
        elif result==2 :
            msg='existe pero se omite error'
            agregarMensjae('alert',msg,'')
            #si retorna error no se muestra
    else:
        if result==0:
            msg='Todo OK'
            agregarMensjae('exito',msg,'')
        elif result==2:
            msg='Error base de existente: '+nombreDB
            agregarMensjae('error',msg,'')
        elif result==1:
            msg='Error en EDD'
            agregarMensjae('error',msg,'')

    #print('reemplazar:',instr.reemplazar,'verificar:',instr.verificacion,'nombre:',instr.nombre,'propietario:',instr.propietario,'modo:',instr.modo)

def eliminar_BaseDatos(instr,ts):
    nombreDB=str(resolver_operacion(instr.nombre,ts)).lower()
    eliminarOK=False;
    #result=0 operacion exitosa
    #result=1 error en la operacion
    #result=2 base de datos no existente  
    result = EDD.dropDatabase(nombreDB)
    msg='Eliminado Base de datos: '+nombreDB;
    agregarMensjae('normal',msg,'')
    
    if(instr.existencia):
        if(result==0):
            eliminarOK=True;
            msg='Todo OK'
            agregarMensjae('exito',msg,'')
        else:
            eliminarOK=False
            msg='no se muestra el error'
            agregarMensjae('alert',msg,'')
            #si retorna error no se muestra
    else:
        if(result==0):
            eliminarOK=True;
            msg='Todo OK'
            agregarMensjae('exito',msg,'')
        elif(result==1):
            eliminarOK=False
            msg='Error en EDD'
            agregarMensjae('error',msg,'')
        else:
            msg='Error base de datos no existente: '+nombreDB
            agregarMensjae('error',msg,'')
    
    if eliminarOK:
        EliminarTablaTemp(nombreDB,'all')#eliminar los temporales
        #elim_use()

    #print('nombre:',instr.nombre,'validarExistencia',instr.existencia)

def mostrar_db(instr,ts):
    #retorna una lista[db1,db2...], si no hay estara vacia[]
    result=EDD.showDatabases()
    msg='Lista de bases de datos'
    agregarMensjae('normal',msg,'')

    if not result:
        msg='No existen bases de datos ...' 
        agregarMensjae('alert',msg,'')   
    else:
        for val in result:
            agregarMensjae('exito',val,'')

def eliminar_Tabla(instr,ts):
    nombreT=''
    nombreT=resolver_operacion(instr.nombre,ts).lower()

    #Valor de retorno: 0 operación exitosa
    # 1 error en la operación, 
    # 2 database no existente, 
    # 3 table no existente.
    result=EDD.dropTable(baseActiva,nombreT)
    eliminarOK=False;

    msg='Eliminar Tabla:'+nombreT
    agregarMensjae('normal',msg,'')
    if(instr.existencia):
        if(result==0):
            msg='Tabla eliminada'
            agregarMensjae('exito',msg,'')
            eliminarOK=True
        else:
            msg='se omite error'
            agregarMensjae('alert',msg,'')
    else:
        if(result==0):
            msg='Tabla eliminada'
            agregarMensjae('exito',msg,'')
            eliminarOK=True
        elif(result==1):
            msg='Error en EDD'
            agregarMensjae('error',msg,'')
        elif(result==2):
            msg='no existe la base de datos activa:'+baseActiva
            agregarMensjae('error',msg,'')
        elif(result==3):
            msg='42P01:Tabla no existe:'+nombreT
            agregarMensjae('error',msg,'42P01')
        
    if eliminarOK:
        EliminarTablaTemp(baseActiva,nombreT)


    #print('nombre:',instr.nombre,'validarExistencia',instr.existencia)

def seleccion_db(instr,ts):
    nombreDB = resolver_operacion(instr.nombre,ts).lower()
    result=EDD.showDatabases()
    msg='Seleccionando base de datos: '+nombreDB
    agregarMensjae('normal',msg,'')
    if not result: # Lista Vacia
        msg='No existen bases de datos ...'
        agregarMensjae('alert',msg,'')  
    elif nombreDB in result: # Encontrada
        msg='Base de datos seleccionada'
        agregarMensjae('exito',msg,'')
        use_db(nombreDB)
    else: # No encontrada
        msg='Base de datos \"'+str(nombreDB)+'\" no registrada'
        agregarMensjae('error',msg,'')
        
#---------pendientes-----------------------
def crear_Tabla(instr,ts):
    #Pendiente
    # -foraneas
    # -default igual al tipo de la columna
    # -tipo columna TYPE
    # -zonahoraria
    # -check
    # -herencia

    nombreT=resolver_operacion(instr.nombre,ts).lower()
    listaColumnas=[]
    crearOK=True
    pkCompuesta=False
    msg='Creando Tabla:'+nombreT
    agregarMensjae('normal',msg,'')
    contC=0# variable para contar las columnas a mandar a EDD

    print('padre:',instr.padre)
    #recorrer las columnas
    for colum in instr.columnas :
        colAux=Columna_run()#columna temporal para almacenar
        if isinstance(colum, llaveTabla) :
            if(colum.tipo==True):
                if(pkCompuesta==False):
                    pkCompuesta=True#primer bloque pk(list)
                    #pk compuesta, revisar la lista
                    for pkC in colum.columnas:
                        exCol=False
                        for lcol in listaColumnas:
                            if(lcol.nombre==pkC.lower()):
                                exCol=True
                                if(lcol.primary==None):
                                    lcol.primary=True
                                else:
                                    crearOK=False
                                    msg='primary key repetida:'+pkC.lower()
                                    agregarMensjae('error',msg,'42P16')   
                        if(exCol==False):
                            crearOK=False
                            msg='42P16:No se puede asignar como primaria:'+pkC.lower()
                            agregarMensjae('error',msg,'42P16')
                else:
                    crearOK=False
                    msg='42P16:Solo puede existir un bloque de PK(list)'
                    agregarMensjae('error',msg,'42P16')
            else:
                #bloque de foraneas
                print('llaves Primaria:',colum.tipo,'lista:',colum.columnas,'tablaref',colum.referencia,'listaref',colum.columnasRef)
        elif isinstance(colum, columnaTabla) :
            contC=contC+1
            colAux.nombre=resolver_operacion(colum.id,ts).lower()#guardar nombre col
            #revisar columnas repetidas
            pos=0
            colOK=True
            while pos< len(listaColumnas):
                if(listaColumnas[pos].nombre==colAux.nombre):
                    crearOK=False;
                    colOK=False
                    msg='42701:nombre de columna repetido:'+colAux.nombre
                    agregarMensjae('error',msg,'42701')
                    break;
                else:
                    pos=pos+1
            #si no existe el nombre de la columna revisa el resto de errores
            if(colOK):
                if isinstance(colum.tipo,Operando_ID):
                    colAux.tipo=resolver_operacion(colum.tipo,ts).lower()#guardar tipo col
                    #revisar la lista de Types
                    crearOK=False
                    msg='42704:No existe el Type '+colAux.tipo+' en la columna '+colAux.nombre
                    agregarMensjae('error',msg,'42704')
                else:
                    colAux.tipo=colum.tipo.lower() #guardar tipo col
                if(colum.valor!=False):
                    if(colAux.tipo=='character varying' or colAux.tipo=='varchar' or colAux.tipo=='text' or colAux.tipo=='character' or colAux.tipo=='char'):
                        if(len(colum.valor)==1):
                            errT=True;#variable error en p varchar(p)
                            if isinstance(colum.valor[0],Operando_Numerico):
                                val=resolver_operacion(colum.valor[0],ts)
                                if(type(val) == int):
                                    colAux.size=val
                                    errT=False#no existe error
                            if errT:
                                crearOK=False
                                msg='42601:el tipo '+colAux.tipo+' acepta enteros como parametro: '+colAux.nombre
                                agregarMensjae('error',msg,'42601')
                        else:
                            crearOK=False
                            msg='42601:el tipo '+colAux.tipo+' solo acepta 1 parametro: '+colAux.nombre
                            agregarMensjae('error',msg,'42601')
                    elif(colAux.tipo=='decimal' or colAux.tipo=='numeric' or colAux.tipo=='double precision'):
                        if(len(colum.valor)==1):
                            errT=True;#variable error en p varchar(p)
                            if isinstance(colum.valor[0],Operando_Numerico):
                                val=resolver_operacion(colum.valor[0],ts)
                                if(type(val) == int):
                                    colAux.size=val
                                    errT=False#no existe error
                            if errT:
                                crearOK=False
                                msg='42601:el tipo '+colAux.tipo+' acepta enteros como parametro: '+colAux.nombre
                                agregarMensjae('error',msg,'42601')
                        elif(len(colum.valor)==2):
                            errT=True;#variable error en p varchar(p)
                            if (isinstance(colum.valor[0],Operando_Numerico) and isinstance(colum.valor[1],Operando_Numerico)):
                                val1=resolver_operacion(colum.valor[0],ts)
                                val2=resolver_operacion(colum.valor[1],ts)
                                if(type(val1) == int and type(val2) == int):
                                    colAux.size=val1
                                    colAux.precision=val2
                                    errT=False#no existe error
                            if errT:
                                crearOK=False
                                msg='42601:el tipo '+colAux.tipo+' acepta enteros como parametro: '+colAux.nombre
                                agregarMensjae('error',msg,'42601')
                        else:
                            crearOK=False
                            msg='42601:el tipo '+colAux.tipo+' acepta maximo 2 parametro: '+colAux.nombre
                            agregarMensjae('error',msg,'42601')
                    else:
                        crearOK=False
                        msg='42601:el tipo '+colAux.tipo+' no acepta parametros:'+colAux.nombre
                        agregarMensjae('error',msg,'42601')
                if(colum.zonahoraria!=False):
                    '''aca se debe verificar la zonahoraria es una lista'''
                    print('zonahoraria',colum.zonahoraria)
                if(colum.atributos!=False):
                    #aca se debe verificar la lista de atributos de una columna
                    for atributoC in colum.atributos :
                        if isinstance(atributoC, atributoColumna):
                            if(atributoC.default!=None):
                                if(colAux.default==None):
                                    colAux.default=resolver_operacion(atributoC.default,ts)#guardar default
                                else:
                                    crearOK=False
                                    msg='42P16:atributo default repetido en Col:'+colAux.nombre
                                    agregarMensjae('error',msg,'42P16')
                            elif(atributoC.constraint!=None):
                                if(colAux.constraint==None):
                                    colAux.constraint=atributoC.constraint#guardar constraint
                                else:
                                    crearOK=False
                                    msg='42P16:atributo constraint repetido en Col:'+colAux.nombre
                                    agregarMensjae('error',msg,'42P16')
                            elif(atributoC.null!=None):
                                if(colAux.anulable==None):
                                    colAux.anulable=atributoC.null#guardar anulable
                                else:
                                    crearOK=False
                                    msg='42P16:atributo anulable repetido en Col:'+colAux.nombre
                                    agregarMensjae('error',msg,'42P16')
                            elif(atributoC.unique!=None):
                                if(colAux.unique==None):
                                    colAux.unique=atributoC.unique#guardar unique
                                else:
                                    crearOK=False
                                    msg='42P16:atributo unique repetido en Col:'+colAux.nombre
                                    agregarMensjae('error',msg,'42P16')
                            elif(atributoC.primary!=None):
                                if(colAux.primary==None):
                                    colAux.primary=atributoC.primary#guardar primary
                                else:
                                    crearOK=False
                                    msg='42P16:atributo primary repetido en Col:'+colAux.nombre
                                    agregarMensjae('error',msg,'42P16')
                            elif(atributoC.check != None):
                                #el atributo check trae otra lista
                                print('check:',atributoC.check)
                                for exp in atributoC.check:
                                    print('resultado: ',resolver_operacion(exp,ts))
                listaColumnas.append(colAux)
 
                
            

    #analisas si las columnas estan bien
    #buscar las tablas de una base de datos retorna una lista de tablas
    if(crearOK):
        result=EDD.showTables(baseActiva)
        if(result!=None):
            for tab in result:
                if tab==nombreT:
                    msg='42P07:Error la tabla ya existe:'+nombreT
                    agregarMensjae('error',msg,'42P07')
                    crearOK=False
                    break
            if crearOK:
                EDD.createTable(baseActiva,nombreT,contC)
                insertartabla(listaColumnas,nombreT)
                msg='Todo OK'
                agregarMensjae('exito',msg,'')
        else:
            msg='no existe la base de datos activa:'+baseActiva
            agregarMensjae('error',msg,'')

def crear_Type(instr,ts):
    nombreT=resolver_operacion(instr.nombre,ts).lower()
    msg='Creacion de Type: '+nombreT
    agregarMensjae('normal',msg,'')
    if baseActiva != "":
        result=EDD.showTables(baseActiva)
        cont=0
        flag=False
        lvalores=[]
        if instr.valores is not None:  
            if nombreT in result: # Repetido
                msg='42P07:Nombre repetido ...'
                agregarMensjae('error',msg,'42P07')
            else:
                for valor in instr.valores: # Verificacion tipos
                    val=resolver_operacion(valor,ts)
                    if isinstance(val, str):
                        lvalores.append(resolver_operacion(valor,ts))
                        cont=cont+1
                if cont != len(instr.valores):
                    msg='42804:No todos los valores son del mismo tipo'
                    agregarMensjae('error',msg,'42804')
                else:
                    flag=True
            if(flag): # crea e inserta valores
                respuestatype=EDD.createTable(baseActiva,nombreT,cont)
                if respuestatype==0:
                    msg='Type registrado con exito'
                    agregarMensjae('exito',msg,'')
                    insertartabla(None,nombreT)
                    respuestavalores=EDD.insert(baseActiva,nombreT,lvalores)
                    if respuestavalores==0:
                        msg='con valores: '+str(lvalores)
                        agregarMensjae('exito',msg,'')
                    elif respuestavalores==1:
                        msg='42P16:Error insertando valores'
                        agregarMensjae('error',msg,'42P16')
                    elif respuestavalores==2:
                        msg='Base de datos no existe'
                        agregarMensjae('error',msg,'')
                    elif respuestavalores==3:
                        msg='Type no encontrado'
                        agregarMensjae('error',msg,'')
                elif respuestatype==1:
                    msg='Error al crear type'
                    agregarMensjae('error',msg,'42P16')
                elif respuestatype==2:
                    msg='Base de datos no existe'
                    agregarMensjae('error',msg,'')
                elif respuestatype==3:
                    msg='42P07:Nombre repetido ...'
                    agregarMensjae('error',msg,'42P07')
    else:
        msg='No hay una base de datos activa'
        agregarMensjae('alert',msg,'')


def insertar_en_tabla(instr,ts):
    #pendiente
    # -Datos de tipo fecha
    # -Datos TYPE
    # -size and precision
    #
    #-si columas!=false----> #columnas[] =#valores[]
    #   -verificar si las columas existen en esa tabla
    #   -verificar si Tipocolum=Tipovalores
    #-sino   
    #-llaves primaras y foraneas deben estar en los valores
    insertOK=True
    ValInsert=[] #lista de valores a insertar
    nombreT=resolver_operacion(instr.nombre,ts).lower()
    msg='Insertado en Tabla:'+nombreT
    agregarMensjae('normal',msg,'')
    
    #-Tabla existente
    result=EDD.showTables(baseActiva)
    tablaInsert=None
    if(result!=None):
        if(nombreT not in result):
            insertOK=False
            msg='42P01'+':la tabla no existe en DB:'+baseActiva
            agregarMensjae('error',msg,'42P01')
        else:
            tablaInsert = buscarTabla(baseActiva,nombreT)
    else:
        insertOK=False
        msg='no existe la base de datos activa:'+baseActiva
        agregarMensjae('error',msg,'')
        
    #tabla no guardada en temporal
    if(tablaInsert == None):
        insertOK=False
        msg='No se encuentra en memoria los tipos de valor para esta tabla'
        agregarMensjae('error',msg,'')
    #-entrada solo con valores
    elif(instr.columnas==False):
        #no exeder numero de columnas
        if(len(tablaInsert.atributos)>=len(instr.valores)):
            pos=0
            for col in instr.valores:
                #error al colocar un id
                if isinstance(col,Operando_ID):
                    insertOK=False
                    msg='42804:no se pueden insertar valores de tipo ID:'+resolver_operacion(col,ts)
                    agregarMensjae('error',msg,'42804')
                else:
                    #Tipocolum[n]=Tipovalores[n]
                    valCOL=resolver_operacion(col,ts)#valor de la columna
                    T=tablaInsert.atributos[pos].tipo
                    #acepta int
                    if(valCOL==None):
                        insertOK=False;
                        msg='42804:El tipo de dato no es correcto:'
                        agregarMensjae('error',msg,'42804')
                    elif(T=="smallint" or T=="integer" or T=="bigint"):
                        try:
                            valCOL=int(valCOL)
                            ValInsert.append(valCOL)
                        except ValueError:
                            insertOK=False;
                            msg='42804:El tipo de dato no es correcto:'+valCOL
                            agregarMensjae('error',msg,'42804')
                    #acepta float
                    elif(T=="decimal" or T=="numeric" or T=="real" or T=="double precision" or T=="money"):
                        try:
                            valCOL=float(valCOL)
                            ValInsert.append(valCOL)
                        except ValueError:
                            insertOK=False;
                            msg='42804:El tipo de dato no es correcto:'+valCOL
                            agregarMensjae('error',msg,'42804')
                    #acepta str        
                    elif(T=="character varying" or T=="varchar" or T=="text" or T=="character" or T=="char"):
                        try:
                            valCOL=str(valCOL)
                            #validar size para 
                            ValInsert.append(valCOL)
                        except ValueError:
                            insertOK=False;
                            msg='42804:El tipo de dato no es correcto:'+valCOL
                            agregarMensjae('error',msg,'42804')
                    #acepta date
                    elif(T=="date" or T=="timestamp" or T=="time" or T=="interval" or T=="boolean"):
                        print("falta validar las fechas")
                        ValInsert.append(valCOL)
                    else:
                        print("falta validar los Type")
                        ValInsert.append(valCOL)
                pos=pos+1
        else:
            insertOK=False
            msg='42601:la tabla solo posee '+str(len(tablaInsert.atributos))+' columas'
            agregarMensjae('error',msg,'42601')
                
    else:
        if(len(instr.columnas)!=len(instr.valores)):
            insertOK=False
            msg='#columas no es igual a #valores, '+str(len(instr.columnas))+'!='+str(len(instr.valores))
            agregarMensjae('error',msg,'')
        else:
            #-entrada con valores y columas
            #   -verificar si las columas existen en esa tabla
            #   -verificar si Tipocolum=Tipovalores
            ''
    #-llaves primaras y foraneas deben estar en los valores




    if(insertOK):
        #llamar metodo insertar EDD
        msg='valores insertados:'+str(ValInsert)
        agregarMensjae('exito',msg,'')


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

#EMPIEZA MIO --------------------------------------------




def AlterDBF(instr,ts):

    print("nombre:",instr.Id,"Tipo:",instr.TipoCon,"Valor:",instr.valor)
    outputTxt=""
    #Nombre de la base de datos
    NombreBaseDatos= instr.Id
    #Instruccion RENAME O OWNER
    TipoOperacion= (instr.TipoCon).upper()
    #Valor de la operacion, ID , CURREN_USER O SESSION_USER
    ValorInstruccion=instr.valor

    if TipoOperacion=="RENAME":
        retorno=EDD.alterDatabase(NombreBaseDatos, ValorInstruccion)

        if retorno==0:
            outputTxt='La base de datos Old_Name: '+NombreBaseDatos +', New_Name: '+ValorInstruccion 
            outputTxt+='\n> se ha renombrado exitosamente '
            agregarMensjae('normal',outputTxt)
            print ("La base de datos se ha renombrado exitosamente")
        elif retorno==1:
            outputTxt='Hubo un error durante la modificacion de la bd  '
            agregarMensjae('normal',outputTxt)
            print ("Hubo un error durante la modificacion de la bd")  
        elif retorno==2:
            outputTxt='La base de datos :'+NombreBaseDatos +' ,no existe '
            agregarMensjae('normal',outputTxt)
            print ("La base de datos no existe")
        elif retorno==3:
            outputTxt='El nombre de la base de datos :'+ValorInstruccion +' ,ya esta en uso '
            agregarMensjae('normal',outputTxt)
            print ("El nombre de la bd ya esta en uso")
            
    else:
        #reconoce OWNER 
        if ValorInstruccion.upper()=="CURRENT_USER":
            outputTxt='Se ha ejecutado con exito la modificacion DB CURRENT_USER'
            agregarMensjae('normal',outputTxt)
        elif ValorInstruccion.upper()=="SESSION_USER":
            outputTxt='Se ha ejecutado con exito la modificacion DB SESSION_USER'
            agregarMensjae('normal',outputTxt)
        else:
            outputTxt='Se ha ejecutado con exito la modificacion DB ID'
            agregarMensjae('normal',outputTxt)







def AlterTBF(instr,ts):
    print("nombreT:",instr.Id,"CuerpoT:",instr.cuerpo)
    print(instr)
    #TABLA A ANALIZAR
    NombreTabla=instr.Id

    #RENAME , ALTER_TABLE_SERIE,   ALTER_TABLE_DROP,   ALTER_TABLE_ADD
    ObjetoAnalisis=instr.cuerpo



    #ANALISIS ALTER RENAME
    if isinstance(ObjetoAnalisis,ALTERTBO_RENAME ):
        #Primer ID
        ID1=ObjetoAnalisis.Id1
        #Segundo ID
        ID2=ObjetoAnalisis.Id2
        #Operacion Column ,Constraint o nula
        OPERACION=ObjetoAnalisis.operacion

        #determinar si es RENAME COLUMN , RENAME COLUMN , RENAME CONSTRAINT, RENAME TABLE
        if OPERACION.upper()=="CONSTRAINT":
            ' '
        elif OPERACION.upper()=="TO":
            #Alterara el NOMBRE de una tabla de una db Seleccionada
            print("BASEACTIVA:",baseActiva)
            retorno=EDD.alterTable(baseActiva, NombreTabla,ID1)
            #Verifica Respuesta
            if retorno==0:
                outputTxt='Se Renombro la Tabla exitosamente,'+NombreTabla +' TO '+ID1 
                agregarMensjae('normal',outputTxt)
            elif retorno==1:
                outputTxt='Hubo un error durante la modificacion de la Tabla  '
                agregarMensjae('normal',outputTxt)
            elif retorno==2:
                outputTxt='La Base de datos :'+ baseActiva +' ,no existe '
                agregarMensjae('normal',outputTxt)
            elif retorno==3:
                outputTxt='La Tabla :'+NombreTabla +' ,no existe en la bd'
                agregarMensjae('normal',outputTxt)
            elif retorno==4:
                outputTxt='El nombre de la Tabla :'+ ID1 +' ,ya esta en uso '
                agregarMensjae('normal',outputTxt)
            else:
                print("operacion desconocida 0")
        elif OPERACION.upper()=="COLUMN" or OPERACION.upper()=="ID" :
            ' '

           



    #ANALISIS ALTER DE ALTERS
    elif isinstance(ObjetoAnalisis,ALTERTBO_ALTER_SERIE ):

        #Lista de Alter's
        Lista_Alter = ObjetoAnalisis.listaval

        #Recorre Lista Alters 
        for alter_list_temp in Lista_Alter:


            #Instruccion a procesar COLUMN extra
            INSTRUCCION=alter_list_temp.instruccion

            #ID en columna o constraint
            ID=alter_list_temp.id

            #Analisis continuacion Column Alter , no Constraint
            Obj_Ext=alter_list_temp.extra
            '''alttbalter1  : SET     NOT       NULL
                            | DROP    NOT       NULL
                            | SET     DATA      TYPE tipo valortipo
                            | TYPE    tipo      valortipo
                            | SET     DEFAULT   exp
                            | DROP    DEFAULT  '''


            OPE1=Obj_Ext.prop1 #set  ,drop ,type        
            OPE2=Obj_Ext.prop2 #not  ,data ,tipo        ,default
            OPE3=Obj_Ext.prop3 #null ,type ,valortipo   , exp
            #si es exp ni idea

            OPEE1=Obj_Ext.prop4 #tipo
            OPEE2=Obj_Ext.prop5 # valor tipo


            #Modificara una propieda de una columna
            if INSTRUCCION.upper()=="COLUMN":
                ' '
            
            elif INSTRUCCION.upper()=="CONSTRAINT":
                ' '


    #ANALISIS ALTER DROP
    elif isinstance(ObjetoAnalisis,ALTERTBO_DROP ):
        #Definicion de Instruccion  COLUMN , CONSTRAINT o nula
        INSTRUCCION=ObjetoAnalisis.instruccion
        #Identificador 
        ID=ObjetoAnalisis.id

        if INSTRUCCION.upper()=="COLUMN" or INSTRUCCION.upper()=="ID":
            #busco la columna en las cabeceras
            #retorna No. de columna
            No_col=0
            retorno=1
            try:
                retorno=EDD.alterDropColumn(baseActiva,NombreTabla,No_col)
            except:
                ' '
            #Verifica Respuesta
            if retorno==0:
                outputTxt='Se elimino exitosamente la columna:'+ ID+' de Tabla:'+NombreTabla 
                agregarMensjae('normal',outputTxt)
            elif retorno==1:
                outputTxt='Hubo un error durante la eliminacion de la columna  '
                agregarMensjae('normal',outputTxt)
            elif retorno==2:
                outputTxt='La Base de datos :'+ baseActiva +' ,no existe '
                agregarMensjae('normal',outputTxt)
            elif retorno==3:
                outputTxt='La Tabla :'+NombreTabla +' ,no existe en la bd'
                agregarMensjae('normal',outputTxt)
            elif retorno==4:
                outputTxt='La Tabla no puede quedar vacia o se trata eliminar Primary Key '
                agregarMensjae('normal',outputTxt)
            elif retorno==5:
                outputTxt='El valor de columna esta fuera de la tabla'
                agregarMensjae('normal',outputTxt)
            else:
                print("operacion desconocida 0")
        elif INSTRUCCION.upper()=="CONSTRAINT":
            ' '
        else:
            ' '#Error

    #ANALISIS ALTER ADD
    elif isinstance(ObjetoAnalisis,ALTERTBO_ADD ):
        '''alttbadd : ADD ID tipo valortipo
                  | ADD COLUMN ID tipo valortipo
                  | ADD CONSTRAINT ID alttbadd2
                  | ADD alttbadd2  '''

        #Identificador
        ID=ObjetoAnalisis.id

        #Etiqueta tipo de dato y su especificacion
        TIPO=ObjetoAnalisis.tipo
        VALORTIPO=ObjetoAnalisis.valortipo

        #Recupera prefijo column constraint
        INSTRUCCION=ObjetoAnalisis.instruccion

        #Recupera posible multiple constraint
        Obj_Extras=list(ObjetoAnalisis.extra)
        
        #clasificacion constraints 
        Check_Obj = []
        Unique_Obj = []
        Primary_Obj = []
        Foreign_Obj = []

        for val in Obj_Extras:
            Uptemp=(val.instruccion).upper()
            if  Uptemp=="CHECK":
                Check_Obj = (Check_Obj+[val])
            elif Uptemp =="UNIQUE":
                Unique_Obj = (Unique_Obj+[val])
            elif Uptemp =="PRIMARY":
                Primary_Obj = (Primary_Obj+[val])
            elif Uptemp =="FOREIGN":
                Foreign_Obj = (Foreign_Obj+[val])
            else:
                print("Instruccion desconocida")



def Mostrar_TB(operacion,ts):

    listaR=EDD.showTables(baseActiva)
    try:

        outputTxt="Nombre BD: "+baseActiva
        for val in listaR:
            outputTxt+='\n> Tabla Name: '+val
        agregarMensjae('normal',outputTxt)
    
    except:
        if listaR==None:
            outputTxt='La base de datos no Existe, ShowTables'
            agregarMensjae('normal',outputTxt)
        else:
            outputTxt='La tabla no existe en la bd, ShowTables'
            agregarMensjae('normal',outputTxt)



#FIN MIO --------------------------------------------


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
    elif isinstance(operacion, Operacion_Math_Unaria):
        op = resolver_operacion(operacion.op,ts)
        print("Entre a math unaria")
        if isinstance(op, (int,float)):
            if operacion.operador == OPERACION_MATH.ABS: return abs(op) 
            elif operacion.operador == OPERACION_MATH.CBRT: return f.func_cbrt(op)
            elif operacion.operador == OPERACION_MATH.CEIL: return math.ceil(op)
            elif operacion.operador == OPERACION_MATH.CEILING: return math.ceil(op)
            elif operacion.operador == OPERACION_MATH.DEGREES: return math.degrees(op)
            elif operacion.operador == OPERACION_MATH.EXP: return math.exp(op)
            elif operacion.operador == OPERACION_MATH.FACTORIAL: return math.factorial(op)
            elif operacion.operador == OPERACION_MATH.FLOOR: return math.floor(op)
            elif operacion.operador == OPERACION_MATH.LN: return math.log(op)
            elif operacion.operador == OPERACION_MATH.LOG: return math.log10(op)
            elif operacion.operador == OPERACION_MATH.RADIANS: return math.radians(op)
            elif operacion.operador == OPERACION_MATH.SIGN: return f.func_sign(op)
            elif operacion.operador == OPERACION_MATH.SQRT: return  math.sqrt(op)
            elif operacion.operador == OPERACION_MATH.TRUNC: return math.trunc(op)

            elif operacion.operador == OPERACION_MATH.ACOS: return math.acos(op)
            elif operacion.operador == OPERACION_MATH.ACOSD: return math.acos(math.radians(op))
            elif operacion.operador == OPERACION_MATH.ASIN: return math.asin(op)
            elif operacion.operador == OPERACION_MATH.ASIND: return math.asin(math.radians(op))
            elif operacion.operador == OPERACION_MATH.ATAN: return math.atan(op)
            elif operacion.operador == OPERACION_MATH.ATAND: return math.atan(math.radians(op))
            elif operacion.operador == OPERACION_MATH.ATAN2: return math.atan2(op)
            elif operacion.operador == OPERACION_MATH.ATAN2D: return math.atan2(math.radians(op))
            elif operacion.operador == OPERACION_MATH.COS: return math.cos(op)
            elif operacion.operador == OPERACION_MATH.COSD: return math.cos(math.radians(op))
            elif operacion.operador == OPERACION_MATH.COT: return f.func_cot(op)
            elif operacion.operador == OPERACION_MATH.COTD: return f.func_cot(math.radians(op))
            elif operacion.operador == OPERACION_MATH.SIN: return math.sin(op)
            elif operacion.operador == OPERACION_MATH.SIND: return math.sin(math.radians(op))
            elif operacion.operador == OPERACION_MATH.TAN: return math.tan(op)
            elif operacion.operador == OPERACION_MATH.TAND: return math.tan(math.radians(op))
            elif operacion.operador == OPERACION_MATH.SINH: return math.sinh(op)
            elif operacion.operador == OPERACION_MATH.COSH: return math.cosh(op)
            elif operacion.operador == OPERACION_MATH.TANH: return math.tanh(op)
            elif operacion.operador == OPERACION_MATH.ASINH: return math.asinh(op)
            elif operacion.operador == OPERACION_MATH.ACOSH: return math.acosh(op)
            elif operacion.operador == OPERACION_MATH.ATANH: return math.atanh(op)

    elif isinstance(operacion, Operacion_Math_Binaria):
        op1 = resolver_operacion(operacion.op1,ts)
        op2 = resolver_operacion(operacion.op2,ts)
        if isinstance(op1,(int,float)) and isinstance(op2,(int,float)):
            if operacion.operador == OPERACION_MATH.DIV: return op1//op2
            elif operacion.operador == OPERACION_MATH.MOD: return math.fmod(op1,op2)
            elif operacion.operador == OPERACION_MATH.GCD: return math.gcd(op1,op2)
            elif operacion.operador == OPERACION_MATH.POWER: return math.pow(op1,op2)
            elif operacion.operador == OPERACION_MATH.ROUND: return f.func_round(op1,op2)

    elif isinstance(operacion,Operacion__Cubos):
        op1 = resolver_operacion(operacion.op1,ts)
        op2 = resolver_operacion(operacion.op12,ts)
        op3 = resolver_operacion(operacion.op3,ts)
        op4 = resolver_operacion(operacion.op4,ts)
        if isinstance(op1,(int,float)) and isinstance(op2,(int,float)) and isinstance(op3,(int,float)) and isinstance(op4,(int,float)) :
            if operacion.operador == OPERACION_MATH.WIDTH_BUCKET: return f.func_width_bucket(op1,op2,op3,op4)
            else: print("Error width bucket en tipo de parametros")
            
    elif isinstance(operacion, Operacion_Definida):
        if operacion.operador == OPERACION_MATH.PI: return math.pi
        elif operacion.operador == OPERACION_MATH.RANDOM: return f.func_random() 

    elif isinstance(operacion, Operacion_Strings):
        op = resolver_operacion(operacion.cadena,ts)
        if isinstance (op,(str)):
            if operacion.operador == OPERACION_BINARY_STRING.MD5: return f.func_md5(op)
            elif operacion.operador == OPERACION_BINARY_STRING.SHA256: return f.func_md5(op)
            elif operacion.operador == OPERACION_BINARY_STRING.LENGTH: return f.func_length(op)

    elif isinstance(operacion,Operacion_String_Binaria):
        op1 = resolver_operacion(operacion.op1,ts)
        op2 = resolver_operacion(operacion.op2,ts)
        if isinstance(op1,(str)) and isinstance(op2,(int)):
            if(operacion.operador == OPERACION_BINARY_STRING.GET_BYTE): return f.func_get_byte(op1,op2)
        elif isinstance(op1,(str)) and isinstance(op2,(str)):
            if (operacion.operador == OPERACION_BINARY_STRING.ENCODE) : return f.func_encode(op1,op2)
            elif (operacion.operador == OPERACION_BINARY_STRING.DECODE) : return f.func_decode(op1,op2) 
       
    elif isinstance(operacion,Operacion_String_Compuesta):
        op1 = resolver_operacion(operacion.op1,ts)
        op2 = resolver_operacion(operacion.op2,ts)
        op3 = resolver_operacion(operacion.op3,ts)
        if isinstance(op1,(str)) and isinstance(op2,(int)) and isinstance(op3,(int)) :
            if operacion.operador == OPERACION_BINARY_STRING.SUBSTR: return f.func_substring(op1,op2,op3)
            elif operacion.operador == OPERACION_BINARY_STRING.SUBSTRING: return f.func_substring(op1,op2,op3)
            elif operacion.operador == OPERACION_BINARY_STRING.SET_BYTE: return f.func_set_byte(op1,op2,op3)
        

    elif isinstance(operacion, Operacion_Patron):
        op1 = resolver_operacion(operacion.op1,ts)
        if operacion.operador == OPERACION_PATRONES.BETWEEN: return f.Between(op1,operacion.op2,ts)
        elif operacion.operador == OPERACION_PATRONES.NOT_BETWEEN: return not(f.Between(op1,operacion.op2,ts))
        elif operacion.operador == OPERACION_PATRONES.IN: return f.In(op1,operacion.op2,ts)
        elif operacion.operador == OPERACION_PATRONES.NOT_IN: return not(f.In(op1,operacion.op2,ts))
        elif operacion.operador == OPERACION_PATRONES.LIKE: return f.Like(op1,operacion.op2,ts)
        elif operacion.operador == OPERACION_PATRONES.NOT_LIKE: return not(f.Like(op1,operacion.op2,ts))
        elif operacion.operador == OPERACION_PATRONES.ILIKE: return f.Ilike(op1,operacion.op2,ts)
        elif operacion.operador == OPERACION_PATRONES.NOT_ILIKE: return not(f.Ilike(op1,operacion.op2,ts))
        elif operacion.operador == OPERACION_PATRONES.SIMILAR: return f.Similar(op1,operacion.op2,ts)
        elif operacion.operador == OPERACION_PATRONES.NOT_SIMILAR: return not(f.Similar(op1,operacion.op2,ts))
    elif isinstance(operacion, Operacion_NOW): return f.Now()
    elif isinstance(operacion, Operacion_CURRENT):
        if operacion.tipo=="date": return f.Date()
        else: return f.Time()
    elif isinstance(operacion, Operando_EXTRACT): return f.Extract(operacion.medida,operacion.valores,ts)
    elif isinstance(operacion, Operacion_DATE_PART): return f.Date_Part(operacion.val1,operacion.val2,ts)
    elif isinstance(operacion, Operacion_TIMESTAMP):
        op = resolver_operacion(operacion.valor,ts) 
        if op=='now': return f.Now()
    elif isinstance(operacion, Operacion_Great_Least):
        if operacion.tipo == 'greatest': return f.Greatest(operacion.expresion,ts)
        else: return f.Least(operacion.expresion,ts)
    

def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    global listaInstrucciones 
    listaInstrucciones  = instrucciones
    if instrucciones is not None:
        for instr in instrucciones :
            if isinstance(instr, CrearBD) : crear_BaseDatos(instr,ts)
            elif isinstance(instr, CrearTabla) : crear_Tabla(instr,ts)
            elif isinstance(instr, CrearType) : crear_Type(instr,ts)
            elif isinstance(instr, EliminarDB) : eliminar_BaseDatos(instr,ts)
            elif isinstance(instr, EliminarTabla) : eliminar_Tabla(instr,ts)
            elif isinstance(instr, Insertar) : insertar_en_tabla(instr,ts)
            elif isinstance(instr, Actualizar) : actualizar_en_tabla(instr,ts)
            elif isinstance(instr, Eliminar) : eliminar_de_tabla(instr,ts)
            elif isinstance(instr, DBElegida) : seleccion_db(instr,ts)
            elif isinstance(instr, MostrarDB) : mostrar_db(instr,ts)
            elif isinstance(instr, ALTERDBO) : AlterDBF(instr,ts)
            elif isinstance(instr, ALTERTBO) : AlterTBF(instr,ts)
            elif isinstance(instr, MostrarTB) : Mostrar_TB(instr,ts)
            else : print('Error: instrucción no válida')
    else:
        agregarMensjae('error','El arbol no se genero debido a un error en la entrada','')







def Analisar(input):
    reiniciarVariables()#reiniciar variables (revisar algunas son para pruebas)
    instrucciones = g.parse(input)
    print(instrucciones)
    ts_global = TS.TablaDeSimbolos()
    procesar_instrucciones(instrucciones,ts_global)

    #crea la consola y muestra el resultado
    '''consola = tkinter.Tk() # Create the object
    consola.geometry('950x200')
    text = tkinter.Text(consola,height=200, width=1280)
    consola.title("Consola")
    text.pack()
    text.insert(END,outputTxt)'''
    return outputTxt

#Metodos para graficar el ast 
def generarAST():
    global listaInstrucciones
    astGraph = DOTAST()
    astGraph.getDot(listaInstrucciones)

#metodo para mostrar las tablas temporales
def mostrarTablasTemp():
    global listaTablas
    misTablas=[]
    
    for tab in listaTablas:
        texTab=PrettyTable()
        texTab.title='DB:'+tab.basepadre+'\tTABLA:'+tab.nombre
        texTab.field_names = ["nombre","tipo","size","precision","unique","anulable","default","primary","foreign","refence","check","constraint"]
        #recorrer las columans
        if tab.atributos!=None:
            for col in tab.atributos:
                texTab.add_row([col.nombre,col.tipo,col.size,col.precision,col.unique,col.anulable,col.default,col.primary,col.foreign,col.refence,col.check,col.constraint])
        misTablas.append(texTab)

    return misTablas

   
'''
#usar las tablas
table = PrettyTable()
table.title = 'Results for method Foo'
table.field_names = ['Experiment', 'Value']
table.add_row(['bla', 3.14])
table.add_row(['baz', 42.0])

Salida
+-------------------------+
|  Results for method Foo |
+---------------+---------+
|   Experiment  |  Value  |
+---------------+---------+
|      bla      |   3.14  |
|      baz      |   42.0  |
+---------------+---------+

'''