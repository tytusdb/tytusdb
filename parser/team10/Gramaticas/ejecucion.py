from instruccion import *
from funcionesTS import *
from expresiones import *
from conexionDB import *
from VerificarDatos import *
from funcionesNativas import * 
from  datetime import datetime
import EjecutarOperacion  as ejec
import EjecutarMatematicas as mate
import cDatabases as usoTabla
import funcionAlter as usoAlter
import funcionDrop as usoDrop
import ejeInsert as usoInsert
import funcionShow as mostrar
listTablas = []





class evaluacion():
    def __init__(self, conectar, ts):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = ''
        self.baseActual = ''
        self.imprimir=""

    def ejecutarDDL(self, instru):
        if isinstance(instru.instru , Replace):
            self.ejecReplace(instru.instru)
        elif isinstance(instru.instru ,  Create):
            self.ejecCreate(instru.instru)
        elif isinstance(instru.instru , alter):
            self.ejecAlter(instru.instru)
        elif isinstance(instru.instru, Drop):
            self.ejecDrop(instru.instru)
        elif isinstance(instru.instru, Truncate):
            self.ejecTruncate(instru.instru)
        else:
            print('verificar Instruccion ddl')

    def ejecReplace(self, instru):
        if isinstance(instru.instru , CreateDatabase):
            obsBase = usoTabla.replaceBases(self.tablaActual,self.baseActual,self.conectar,self.ts,listTablas)
            obsBase.obIfNot(instru, self.conectar)   
            self.baseActual = obsBase.getBaseActual()
            print('creacion Base')

        elif isinstance(instru.instru, CreateTable):
            objsReplace = usoTabla.ReplaceTabla(self.tablaActual,self.baseActual,self.conectar,self.ts,listTablas)
            objsReplace.replaceTabla(instru)
        elif isinstance(instru.instru, CreateType):
            print('creacion de tipos')
        else:
            print('verificar Instruccion')


    def ejecCreate(self, instru):
        if isinstance(instru.instru , CreateDatabase):
           obsBase = usoTabla.crearBases(self.tablaActual,self.baseActual,self.conectar,self.ts,listTablas)
           obsBase.obIfNot(instru, self.conectar)   
           self.baseActual = obsBase.getBaseActual()
           print('creacion Base')
                   
        elif isinstance(instru.instru, CreateTable):
            
            #obtener list de campos coltabla , obtener finTabla
            obsTabla = usoTabla.crearTablas(self.tablaActual,self.baseActual, self.conectar, self.ts, listTablas)
            obsTabla.crearTabla(instru)
            self.tablaActual = obsTabla.getTablaActual()
            self.baseActual = obsTabla.getBaseActual()
            print('final tabla')
        elif isinstance(instru.instru, CreateType):
            print('objetos create')
        else:
            print('verificar Instruccion')

    def ejecAlter(self, instru):
        objAlter = usoAlter.ejecutarAlter(self.tablaActual,self.baseActual,self.conectar,self.ts, listTablas)
        objAlter.inicialAlter(instru)



    def ejecDrop(self, instru):
        objsDrop = usoDrop.ejecutarDrop(self.tablaActual,self.baseActual,self.conectar, self.ts, listTablas)
        objsDrop.iniciarDrop(instru)   

    def ejecTruncate(self, instru):
        objsTruncate = usoDrop.ejecutarTruncate(self.tablaActual,self.baseActual,self.conectar, self.ts, listTablas)
        objsTruncate.iniciarTruncate(instru)



    def ejecutarDML(self, instru):
        print('viendo que instancia es')
        if isinstance(instru.instru,seleccion):
            self.selects(instru)
        elif isinstance(instru.instru, INSERTAR):
            self.sentInsert(instru.instru)
        elif isinstance(instru.instru, seleccionF ):
            print('ES UNA SELECCION DE FECHA')
            return self.opcionesFecha(instru.instru)

        elif isinstance(instru.instru, SentenciaShow):
            self.sentShow(instru.instru)

        elif isinstance(instru.instru, seleccionCont ):
            exMath = mate.MateFunction(self.conectar,self.ts)
            print('aca debe ejecutarse las operaciones ')
            if isinstance(instru.instru.cont, aritmetica2):
                resp=exMath.procesar_funcion(instru.instru.cont)
                self.imprimir=resp
                return resp
            else: 
                print('no es aritmetica')
            #self.operaAritmetica(instru.instru.cont)
    
    def sentShow(self, instru):
        objShow = mostrar.ejeShow(self.tablaActual,self.baseActual,self.conectar,self.ts, listTablas)
        objShow.iniciarShow(instru)


    def operaAritmetica(self,opera):
        print('operando aritmetica')
        execute = ejec.ExecOperacion(self.conectar,self.ts)
        print(execute.ejecutar_operacion(opera.operacion.funcion.op1))
    
    def opcionesFecha(self, instru):
        if isinstance(instru.fechas,OpcionesFecha3):
            print('instancia de fecha 3')
            valor =  instru.fechas.getValor()
            self.imprimir =str(valor)
            return valor
        elif isinstance(instru.fechas,OpcionesFecha2):
            valor = instru.fechas.getValor()
            self.imprimir=str(valor)
            return valor;
        elif isinstance(instru.fechas, Opcionesfecha4):
            print('fecha 4')
            valor = instru.fechas.getValor()
            self.imprimir =str(valor)
            return valor


    def sentInsert(self,instru):
        objInsert = usoInsert.analisisInsert(self.tablaActual,self.baseActual,self.conectar,self.ts,listTablas)
        objInsert.iniciarInsert(instru)

    def selects(self, instru):
        ContenidoSelect = []
        ListaidsNormal = []
        ContenidoSelect = instru.instru.cont
        ListadoFrom = instru.instru.listFrom
        Condicion = instru.instru.cond

        #REVISION DEL TIPO DE SELECT
            # Select con *
        if isinstance(ContenidoSelect , ast):
            print('Es un Select * From normal')

            # Select con Distinct
        elif isinstance(ContenidoSelect , Distinct):
            print('Distincion en Select Disctinct')
        
        else:
            contt = 0
            for index in range(len(ContenidoSelect)):
                if contt < len(ContenidoSelect):
                    ListaidsNormal.append(ContenidoSelect[contt].ids)
                    contt += 1
                else:
                    break


            print(ListaidsNormal)
        #REVISION DEL LISTADO DE FROM

        Idtabla = ''
        if isinstance(ListadoFrom , ids):
            IdTabla = ListadoFrom.ids

        elif isinstance(ListadoFrom, como):
            print('Listado From con idtabla as t1')
        
        
        # REVISION DEL TIPO DE WHERE
        if isinstance(Condicion, WheresExist):
            print('WheresExist aqui')
        
        elif isinstance(Condicion, whereAgrupado):
            print('Whereagrupado aqui')
        
        elif isinstance(Condicion, WhereSimple):
            if Condicion.op1.op2.name == 'MAYOR':
                signo = '>'
            elif Condicion.op1.op2.name == 'MENOR':
                signo = '<'
            elif Condicion.op1.op2.name == 'MAYI':
                signo = '>='
            elif Condicion.op1.op2.name == 'MENI':
                signo = '<='
            elif Condicion.op1.op2.name == 'II':
                signo = '=='
            elif Condicion.op1.op2.name == 'NI':
                signo = '<>'

            WhereOperacionCompleta = Condicion.op1.op1.ids + signo + '\"' + Condicion.op1.operacion.numero + '\"' 
            WhereOperadoresID = [Condicion.op1.op1.ids]
            print('WhereSimple expresion->')
            print(WhereOperacionCompleta)
            print(WhereOperadoresID)
            #Select Col1, Col2, etc From tabla Where Col1>5;
            self.conectar.cmd_extractTable("nuevadb5", IdTabla,  WhereOperacionCompleta, WhereOperadoresID, ListaidsNormal)
        elif isinstance(Condicion, Empty):
            #Select * From id;
            self.conectar.cmd_extractTable("nuevadb5", IdTabla, "-1", "-1", "1")
        else:
            print('LLego al final')
            #Select Col1, Col2, etc From tabla;
            self.conectar.cmd_extractTable("nuevadb5", IdTabla, "-1", "-1", ListaidsNormal)

        print('instrucciones select')

        
    def contSelect(self,instru):
        result = 'algo'
        return result


    def ejecutarLinea(self, instru):
        for line in instru:
            if isinstance(line, insDML):
                print('ejecutando DML')
                print('tabla:', self.ejecutarDML(line))
            
            elif  isinstance(line, insDDL):
                self.ejecutarDDL(line)

            elif isinstance(line, instruccionL):
                print('linea')

    def iniciar(self, instru):
        print('iniciando ejecucion')
        self.ejecutarLinea(instru)


    def getBaseActual(self):
        return self.baseActual

    def getTablaActual(self):
        return self.tablaActual

  


 