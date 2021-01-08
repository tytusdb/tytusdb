import sys, os.path
import json
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Start\\')
sys.path.append(nodo_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\C3D\\')
sys.path.append(c3d_dir)

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\ENTORNO\\')
sys.path.append(nodo_dir)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\typeChecker')
sys.path.append(storage)

variables_globales = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')))
sys.path.append(variables_globales)
from VariablesGlobales import *

from prettytable import PrettyTable
from Libraries import Nodo
from Libraries import Database
from Libraries import Table
from Libraries import Use
from Libraries import Type
from Libraries import Select
from Libraries import InsertTable
from Libraries import UnionAll
from Libraries import Union
from Libraries import Intersect
from Libraries import Except
from Libraries import UpdateTable
from Libraries import AlterTable
from Libraries import Index
from Libraries import Procedure
from Libraries import Execute
from Traduccion import *
from Label import *
from Temporal import *
from Entorno import *
from typeChecker.typeChecker import TypeChecker
tc = TypeChecker()

# Importación de Clases para Execute


class Start(Nodo):
    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
        self.listaSemanticos = []
            
    def addChild(self, node):
        self.hijos.append(node)

    def createChild(self, nombreNodo, fila = -1, columna =-1, valor = None):
        nuevo = Start(nombreNodo,fila,columna,valor)
        self.hijos.append(nuevo)
    
    def createTerminal(self, lexToken):
        nuevo = Start(lexToken.type, lexToken.lineno, lexToken.lexpos, lexToken.value)
        self.hijos.append(nuevo)

    def tabular_data(self, encabezados : list, data : list) -> str: 
        print(encabezados)
        index = 0
        for i in encabezados:
            if i == "?column?":
                encabezados[index] = "?column?"+str(index)
            index += 1

        x = PrettyTable()
        x.field_names = encabezados
        for item in data:
            if len(item) == len(encabezados):
                x.add_row(item)
        return x.get_string()
        
    # recursiva por la izquierda
    def execute(self, enviroment):
        
        entornoGlobal = Entorno(None)
        entornoGlobal.Global = entornoGlobal
        entornoGlobal.nombreEntorno = 'Global'

        for hijo in self.hijos:
            if hijo.nombreNodo == 'SENTENCIA_FUNCTION':
                hijo.execute(entornoGlobal)
        
        #entornoGlobal.recorrerEntorno()
        
        for hijo in self.hijos:
            if hijo.nombreNodo == 'CREATE_DATABASE':
                nuevaBase=Database()                
                # Recibe un json
                message = nuevaBase.execute(hijo)
                self.listaSemanticos.append(message)
            elif hijo.nombreNodo == 'SENTENCIA_USE':
                useDB = Use()
                message = useDB.execute(hijo)
                self.listaSemanticos.append(message)
            elif hijo.nombreNodo == 'CREATE_TABLE':
                nuevaTabla = Table()
                res = nuevaTabla.execute(hijo, enviroment)
                if res.code != "00000":
                    self.listaSemanticos.append({"Code":res.code,"Message": res.responseObj.descripcion, "Data" : ""})
                else:
                    self.listaSemanticos.append({"Code":"0000","Message": res.responseObj, "Data" : ""})
            elif hijo.nombreNodo == 'CREATE_TYPE_ENUM':
                nuevoEnum = Type()
                nuevoEnum.execute(hijo)
            elif hijo.nombreNodo == 'SENTENCIA_SELECT' or hijo.nombreNodo == 'SENTENCIA_SELECT_DISTINCT':
                hijo.execute(entornoGlobal)
                respuesta = hijo.dataResult
                if respuesta.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(respuesta.encabezados, respuesta.data)})
            elif hijo.nombreNodo == 'E':
                hijo.execute(entornoGlobal)
                print("Tipo Expresion: "+str(hijo.tipo.data_type))
                print("Expresion valor: "+str(hijo.valorExpresion))
            elif hijo.nombreNodo == 'SENTENCIA_INSERT':
                nuevoInsert = InsertTable()
                res = nuevoInsert.execute(hijo,enviroment)
                if res.code != "00000":
                    self.listaSemanticos.append({"Code":res.code,"Message": res.responseObj.descripcion, "Data" : ""})
                else:
                    self.listaSemanticos.append({"Code":"0000","Message": res.responseObj, "Data" : ""})
            elif hijo.nombreNodo == "SENTENCIA_SHOW":
                self.listaSemanticos.append(hijo.execute(None))
            elif hijo.nombreNodo == "SENTENCIA_ALTER_INDEX":
                self.listaSemanticos.append(hijo.execute(None))                
            elif hijo.nombreNodo == "SENTENCIA_DROP":
                self.listaSemanticos.append(hijo.execute(None))
            elif hijo.nombreNodo == "SENTENCIA_DELETE":
                self.listaSemanticos.append(hijo.execute(None))
            elif hijo.nombreNodo == 'SENTENCIA_UNION_ALL':
                nuevoUnionAll = UnionAll()
                resp = nuevoUnionAll.execute(hijo)
                if resp.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(resp.encabezados, resp.data)})
            elif hijo.nombreNodo == 'SENTENCIA_UNION':
                nuevoUnion = Union()
                resp = nuevoUnion.execute(hijo)
                if resp.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(resp.encabezados, resp.data)})
            elif hijo.nombreNodo == 'SENTENCIA_INTERSECT':
                nuevoIntersect = Intersect()
                resp = nuevoIntersect.execute(hijo)
                if resp.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(resp.encabezados, resp.data)})
            elif hijo.nombreNodo == 'SENTENCIA_EXCEPT':
                nuevoExcept = Except()
                
                resp = nuevoExcept.execute(hijo)
                if resp.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(resp.encabezados, resp.data)})            

            elif hijo.nombreNodo == 'SENTENCIA_UPDATE':
                nuevoUpdate = UpdateTable()
                res = nuevoUpdate.execute(hijo,enviroment)
                if res.code != "00000":
                    self.listaSemanticos.append({"Code":res.code,"Message": res.responseObj.descripcion, "Data" : ""})
                else:
                    self.listaSemanticos.append({"Code":"0000","Message": res.responseObj, "Data" : ""})
            elif hijo.nombreNodo == 'SENTENCIA_ALTER_TABLE':
                nuevoAlterT = AlterTable()
                res = nuevoAlterT.execute(hijo,enviroment)
                if res.code != "00000":
                    self.listaSemanticos.append({"Code":res.code,"Message": res.responseObj.descripcion, "Data" : ""})
                else:
                    self.listaSemanticos.append({"Code":"0000","Message": res.responseObj, "Data" : ""})
            elif hijo.nombreNodo == 'CREATE_INDEX' or hijo.nombreNodo == 'CREATE_UNIQUE_INDEX':
                nuevoIndex = Index()
                resp = nuevoIndex.execute(hijo)
            
            entornoGlobal.recorrerEntorno()


    def compile(self, enviroment):
        global variablesProcedure

        #region Declaracion de Variables Execute (SQL)
        entornoGlobal = Entorno(None)
        entornoGlobal.Global = entornoGlobal
        entornoGlobal.nombreEntorno = 'Global'
        #endregion

        #region Recorrido para la sentencia Function
        for hijo in self.hijos:
            if hijo.nombreNodo == 'SENTENCIA_FUNCTION':
                hijo.execute(entornoGlobal)
        #endregion
        
        #region Declaracion de las variables
        listaInstrucciones = []
        listaInstrucciones.append("")
        listaInstrucciones.append("")
        listaInstrucciones.append("def execute():")
        listaInstrucciones.append("\tglobal p")
        listaInstrucciones.append("\tp=p-1")
        #listaInstrucciones.append("\tprint(display[p])")
        listaInstrucciones.append("\tresp = run_method(display[p])")
        listaInstrucciones.append("\tresp.execute(None)")
        listaInstrucciones.append("\tp=p+1")
        listaInstrucciones.append("")
        listaInstrucciones.append("")

        #endregion

        #region Execute de las sentencias no PLSQL y algunas PLSQL 
        # (solo el exec tendrá C3D ya que se crean primero los procedures)
        for hijo in self.hijos:
            if hijo.nombreNodo == 'CREATE_DATABASE':
                nuevaBase=Database()                
                message = nuevaBase.execute(hijo)
                self.listaSemanticos.append(message)
                listaInstrucciones += self.compile1(nuevaBase.compile(hijo)).splitlines()
            elif hijo.nombreNodo == 'DECLARACION_VARIABLE':
                print(hijo.compile(entornoGlobal))
            elif hijo.nombreNodo == 'SENTENCIA_USE':
                useDB = Use()
                message = useDB.execute(hijo)
                self.listaSemanticos.append(message)
                listaInstrucciones += self.compile1(useDB.compile(hijo)).splitlines()
            elif hijo.nombreNodo == 'CREATE_TABLE':
                nuevaTabla = Table()
                res = nuevaTabla.execute(hijo, enviroment)
                if res.code != "00000":
                    self.listaSemanticos.append({"Code":res.code,"Message": res.responseObj.descripcion, "Data" : ""})
                else:
                    self.listaSemanticos.append({"Code":"0000","Message": res.responseObj, "Data" : ""})
                listaInstrucciones += self.compile1(self.getText()).splitlines()

            elif hijo.nombreNodo == 'CREATE_TYPE_ENUM':
                nuevoEnum = Type()
                nuevoEnum.execute(hijo)

            elif hijo.nombreNodo == 'SENTENCIA_SELECT' or hijo.nombreNodo == 'SENTENCIA_SELECT_DISTINCT':
                hijo.execute(entornoGlobal)
                respuesta = hijo.dataResult
                if respuesta.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(respuesta.encabezados, respuesta.data)})

                listaInstrucciones += self.compile1(self.getText()).splitlines()

            elif hijo.nombreNodo == 'E':
                hijo.execute(entornoGlobal)
                print("Tipo Expresion: "+str(hijo.tipo.data_type))
                print("Expresion valor: "+str(hijo.valorExpresion))
                listaInstrucciones += self.compile1(hijo.getText()).splitlines()

            elif hijo.nombreNodo == 'SENTENCIA_INSERT':
                nuevoInsert = InsertTable()
                res = nuevoInsert.execute(hijo,enviroment)
                if res.code != "00000":
                    self.listaSemanticos.append({"Code":res.code,"Message": res.responseObj.descripcion, "Data" : ""})
                else:
                    self.listaSemanticos.append({"Code":"0000","Message": res.responseObj, "Data" : ""})
                listaInstrucciones += hijo.compile().splitlines()
                
            elif hijo.nombreNodo == "SENTENCIA_SHOW":
                self.listaSemanticos.append(hijo.execute(None))
                listaInstrucciones += hijo.compile().splitlines()

            elif hijo.nombreNodo == "SENTENCIA_ALTER_INDEX":
                self.listaSemanticos.append(hijo.execute(None))  
                listaInstrucciones += hijo.compile().splitlines()

            elif hijo.nombreNodo == "SENTENCIA_DROP":
                self.listaSemanticos.append(hijo.execute(None))
                listaInstrucciones += hijo.compile().splitlines()

            elif hijo.nombreNodo == "SENTENCIA_DELETE":
                self.listaSemanticos.append(hijo.execute(None))
                listaInstrucciones += hijo.compile().splitlines()


            elif hijo.nombreNodo == 'SENTENCIA_UNION_ALL':
                nuevoUnionAll = UnionAll()
                resp = nuevoUnionAll.execute(hijo)
                if resp.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(resp.encabezados, resp.data)})
                a = nuevoUnionAll.compile(hijo).replace(";"," ",1)
                b = a.replace(";"," ",1)
                listaInstrucciones += b.splitlines()
                
            elif hijo.nombreNodo == 'SENTENCIA_UNION':
                nuevoUnion = Union()
                resp = nuevoUnion.execute(hijo)
                if resp.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(resp.encabezados, resp.data)})
                a = nuevoUnion.compile(hijo).replace(";"," ",1)
                b = a.replace(";"," ",1)
                listaInstrucciones += b.splitlines()                    


            elif hijo.nombreNodo == 'SENTENCIA_INTERSECT':
                nuevoIntersect = Intersect()
                resp = nuevoIntersect.execute(hijo)
                if resp.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(resp.encabezados, resp.data)})
                a = nuevoIntersect.compile(hijo).replace(";"," ",1)
                b = a.replace(";"," ",1)
                listaInstrucciones += b.splitlines()   

            elif hijo.nombreNodo == 'SENTENCIA_EXCEPT':
                nuevoExcept = Except()
                resp = nuevoExcept.execute(hijo)
                if resp.data != None:
                    self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(resp.encabezados, resp.data)})            
                a = nuevoExcept.compile(hijo).replace(";"," ",1)
                b = a.replace(";"," ",1)
                listaInstrucciones += b.splitlines()   
                    
            elif hijo.nombreNodo == 'SENTENCIA_UPDATE':
                nuevoUpdate = UpdateTable()
                res = nuevoUpdate.execute(hijo,enviroment)
                if res.code != "00000":
                    self.listaSemanticos.append({"Code":res.code,"Message": res.responseObj.descripcion, "Data" : ""})
                else:
                    self.listaSemanticos.append({"Code":"0000","Message": res.responseObj, "Data" : ""})
                try:
                    listaInstrucciones += hijo.compile().splitlines()
                except:
                    pass

            elif hijo.nombreNodo == 'SENTENCIA_ALTER_TABLE':
                nuevoAlterT = AlterTable()
                res = nuevoAlterT.execute(hijo,enviroment)
                if res.code != "00000":
                    self.listaSemanticos.append({"Code":res.code,"Message": res.responseObj.descripcion, "Data" : ""})
                else:
                    self.listaSemanticos.append({"Code":"0000","Message": res.responseObj, "Data" : ""})

            elif hijo.nombreNodo == 'CREATE_INDEX' or hijo.nombreNodo == 'CREATE_UNIQUE_INDEX':
                nuevoIndex = Index()
                resp = nuevoIndex.execute(hijo)
                try:
                    listaInstrucciones += self.compile1(self.getText()).splitlines()
                except:
                    pass
                
            elif hijo.nombreNodo == 'SENTENCIA_PROCEDURE':
                print("Sentencia Procedure")
                nuevoProcedure = Procedure()
                nuevoProcedure.execute(hijo,entornoGlobal)
            elif hijo.nombreNodo == 'EXECUTE':
                nuevoExecute = Execute()
                listaInstrucciones = listaInstrucciones +  nuevoExecute.compile(hijo)
            elif hijo.nombreNodo == 'SENTENCIA_CASE':
                cod = hijo.compile(enviroment)
                listaInstrucciones = listaInstrucciones + cod.splitlines()
            entornoGlobal.recorrerEntorno()
        #endregion

        

        encabezados = self.crearEncabezado()
        procedimientos = self.crearListaProcedimientos()
        if procedimientos != None:
            finalList = encabezados + procedimientos + listaInstrucciones
        else:
            finalList = encabezados + listaInstrucciones
        self.crearArchivo(finalList)

    '''def compile(self,enviroment = None):

        pilaInstrucciones = []
        pilaProcedimientos = []
        instanceLabel.labelActual = 1
        instanceTemporal.temporalActual = 1
        entornoGlobal = Entorno(None)
        entornoGlobal.Global = entornoGlobal
        entornoGlobal.nombreEntorno = 'Global'
        
        for hijo in self.hijos:
            if hijo.nombreNodo == 'CREATE_DATABASE':
                nuevaDB = Database()
                texto = "listaParams.append(\""
                texto = texto + nuevaDB.compile(hijo)
                texto = texto + "\")"
                pilaInstrucciones.append(texto)
            elif hijo.nombreNodo == 'SENTENCIA_USE':
                nuevoUse = Use()
                texto = "listaParams.append(\""
                texto = texto + nuevoUse.compile(hijo)
                texto = texto + "\")"
                pilaInstrucciones.append(texto)
            elif hijo.nombreNodo == 'E':
                cod = hijo.compile(enviroment)
                print(cod)
            elif hijo.nombreNodo == 'SENTENCIA_PROCEDURE':
                nuevoProcedure = Procedure()
                nuevoProcedure.compile(hijo, entornoGlobal)
                pilaInstrucciones = nuevoProcedure.cuerpoResult
            elif hijo.nombreNodo == 'SENTENCIA_SELECT' or hijo.nombreNodo == 'SENTENCIA_SELECT_DISTINCT':
                respuesta = hijo.compile(enviroment)
            elif hijo.nombreNodo == 'SENTENCIA_IF':
                print(hijo.compile(entornoGlobal))
            elif hijo.nombreNodo == 'EXECUTE':
                nuevoExecute = Execute()
                nuevoExecute.compile(hijo)
                if nuevoExecute.procedimiento != None:
                    pilaProcedimientos+=nuevoExecute.codigo3Dimensiones
                    pilaInstrucciones.append(nuevoExecute.procedimiento)
        
        
        pilaFinal = pilaEncabezados
        pilaFinal += pilaProcedimientos
        pilaFinal += pilaInstrucciones
        archivo = open('src/C3D/CompileFile.py',"w")
        for line in pilaFinal:
            archivo.write(line)
            archivo.write("\n")
        archivo.close()
'''
    def getText(self):

        textoEntrada = ''
        
        for hijo in self.hijos:
            
            if hijo.nombreNodo == 'SENTENCIA_SELECT':
                textoEntrada += traduccionSelect(hijo)
            elif hijo.nombreNodo == 'CREATE_TYPE_ENUM':
                pass    
            elif hijo.nombreNodo == 'CREATE_DATABASE':
                textoEntrada += traduccionCreate_database(hijo) 
            elif hijo.nombreNodo == 'CREATE_TABLE':
                textoEntrada += traduccion_create_table(hijo)                                                           
            elif hijo.nombreNodo == 'CREATE_INDEX':
                textoEntrada += traduccion_index(hijo) 
            elif hijo.nombreNodo == 'CREATE_UNIQUE_INDEX':
                textoEntrada += traduccion_unique_index(hijo)
            elif hijo.nombreNodo == 'SENTENCIA_UNION':
                ne = Union()
                textoEntrada += ne.getText(hijo)
            elif hijo.nombreNodo == 'SENTENCIA_UNION_ALL':                
                ne = UnionAll()
                textoEntrada += ne.getText(hijo)
            elif hijo.nombreNodo == 'SENTENCIA_INTERSECT':                
                ne = Intersect()
                textoEntrada += ne.getText(hijo)        
            elif hijo.nombreNodo == 'SENTENCIA_EXCEPT':                
                ne = Except()
                textoEntrada += ne.getText(hijo)                     



        return textoEntrada

    def crearEncabezado(self):
        pilaEncabezados = []
        pilaEncabezados.append("# Seccion de Imports")
        pilaEncabezados.append("import sys, os.path")
        pilaEncabezados.append("import sys, os.path")
        pilaEncabezados.append("gramaticaDir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))")
        pilaEncabezados.append("sys.path.append(gramaticaDir)")
        pilaEncabezados.append("from goto import with_goto")
        pilaEncabezados.append("from gramatica import run_method")
        pilaEncabezados.append("")
        pilaEncabezados.append("")
        pilaEncabezados.append("#Declaracion de variables")
        pilaEncabezados.append("display = {}")
        pilaEncabezados.append("p = 0")
        return pilaEncabezados

    def crearListaProcedimientos(self):
        # Verifica si hay una base de datos activa, se utiliza para cualquier instrucción
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        dbUse = config['databaseIndex']
        if dbUse == None:
            #print("Se debe seleccionar una base de datos")
            return None
        listaProcedimientos = []
        res = tc.get_all_procedure(dbUse.upper())
        if res != None:
            for pro in res:
                listaProcedimientos = listaProcedimientos + pro['C3D']
        return listaProcedimientos

    def crearArchivo(self,listaTexto):
        archivo = open('src/C3D/CompileFile.py',"w")
        for line in listaTexto:
            archivo.write(line)
            archivo.write("\n")
        archivo.close()

    def compile1(self,texto):
        tmp = instanceTemporal.getTemporal()
        dir = f"{tmp} = \"{texto}\"\n"
        dir += f'display[p] = {tmp}\n'
        dir += 'p = p + 1\n'
        print("EL TEMPORAL",dir)
        return dir
