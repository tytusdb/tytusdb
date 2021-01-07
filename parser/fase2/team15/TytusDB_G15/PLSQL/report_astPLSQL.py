from PLSQL.instruccionesPLSQL import *
from PLSQL.expresionesPLSQL import *
from graphviz import Digraph

dot = Digraph('AST', node_attr={'shape': 'note','color': 'lightblue2', 'style': 'filled'})
contadorNodos = 0
instrucciones_Global = []

class AST: 

    def __init__(self):
        '''print('AST')'''


    def generarAST(self,instrucciones):
        global contadorNodos, dot, instrucciones_Global
        instrucciones_Global = instrucciones
        dot = Digraph('AST')
        contadorNodos = 2
        dot.node('node1','INIT')
        dot.node('node2','INSTRUCCIONES 3D')
        dot.edge('node1','node2')
        indice = 0
        while indice < len(instrucciones_Global) :
            instruccion = instrucciones_Global[indice]
            if isinstance(instruccion, Funcion):
                self.crearNodoFuncion("node2", instruccion)
            elif isinstance(instruccion, CreateDatabase):
                self.crearNodoCreateDatabase("node2", instruccion)
            elif isinstance(instruccion, DropDatabase):
                self.crearNodoDropDatabase("node2", instruccion)
            elif isinstance(instruccion, ShowDatabases):
                self.crearNodoShowDataBase("node2", instruccion)
            elif isinstance(instruccion, DropTable):
                self.crearNodoDropTable("node2", instruccion)
            elif isinstance(instruccion, AlterDatabase):
                self.crearNodoAlterDataBase("node2", instruccion)
            elif isinstance(instruccion, AlterTable):
                self.crearNodoAlterTable("node2", instruccion)
            elif isinstance(instruccion, InsertTable):
                self.crearNodoInsertTable("node2", instruccion)
            elif isinstance(instruccion, SelectTable):
                self.crearNodoSelectTable("node2", instruccion)
            elif isinstance(instruccion, SelectUniones):
                self.crearNodoSelectUnionTable("node2", instruccion)
            elif isinstance(instruccion, FuncionIndex):
                self.crearNodoFuncionIndex("node2", instruccion)
            elif isinstance(instruccion, CreateTable):
                self.crearNodoCreateTable("node2", instruccion)
            elif isinstance(instruccion, UseDatabase):
                self.crearNodoUseDataBase("node2", instruccion)
            indice = indice +1
        dot.view('reportes/ASTPLSQL', cleanup=True)


    def crearNodoCreateDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    def crearNodoCreateTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    def crearNodoDropDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DROP DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    def crearNodoShowDataBase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'SHOW DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    def crearNodoDropTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DROP TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    def crearNodoAlterDataBase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ALTER DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    def crearNodoInsertTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'INSERT TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    
    
    def crearNodoAlterTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ALTER TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

      

    def crearNodoSelectTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'SELECT TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    def crearNodoSelectUnionTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'SELECT UNION TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    def crearNodoFuncionIndex(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'FuncionIndex')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    def crearNodoUseDataBase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'USE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.cadena)

    
    def crearNodoFuncion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'FUNCION')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoFuncionTipo(temp1,instruccion)
        self.crearNodoFuncionid(temp1,instruccion)
        self.crearNodoFuncionparametros(temp1, instruccion)
        self.crearNodoCuerpoFuncion(temp1, instruccion)


    def crearNodoFuncionTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(instruccion.tipo))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1, instruccion.tipo)
    
    def crearNodoFuncionid(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(instruccion.id))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        

    def crearNodoFuncionparametros(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Parametros')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

 


    def crearNodoCuerpoFuncion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Cuerpo Funciones')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        
        if isinstance(instruccion.instrucciones, Principal):
            for declara in instruccion.instrucciones.instrucciones:
                if isinstance(declara, ListaDeclaraciones):
                    self.crearNodoDeclaracion(temp1,instruccion)
                if isinstance(declara, Asignacion):
                    self.crearNodoAsignacion(temp1, instruccion)
                if isinstance(declara, SentenciaIf):
                    self.crearNodoSentenciaIf(temp1, instruccion)
                    self.crearCuerpoIf(temp1, instruccion)
                if isinstance(declara, SentenciaCase):
                    self.crearNodoSentenciaCase(temp1, instruccion)
                if isinstance(declara, LlamadaFuncion):
                    self.crearNodoLlamadaFuncion(temp1, instruccion)
                if isinstance(declara, Caso):
                    self.crearNodoCaso(temp1, instruccion)

    def crearCuerpoIf(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Cuerpo_If')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
    
        if isinstance(instruccion.instrucciones, Principal):
            for declara in instruccion.instrucciones.instrucciones:
                if isinstance(declara, SentenciaIf):
                    if isinstance(declara.si, Principal):
                        for prueba in declara.si.instrucciones:
                            if isinstance(prueba, ListaDeclaraciones):
                                self.crearNodoDeclaracion(temp1,instruccion)
                            if isinstance(prueba, Asignacion):
                                self.crearNodoAsignacion(temp1, instruccion)
                            if isinstance(prueba, SentenciaIf):
                                self.crearNodoSentenciaIf(temp1, instruccion)
                            if isinstance(prueba, SentenciaCase):
                                self.crearNodoSentenciaCase(temp1, instruccion)
                            if isinstance(prueba, LlamadaFuncion):
                                self.crearNodoLlamadaFuncion(temp1, instruccion)
                            if isinstance(prueba, Caso):
                                self.crearNodoCaso(temp1, instruccion)

    def crearNodoSentenciaCase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Sentencia Case')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 

        if isinstance(instruccion.instrucciones, Principal):
            for declara in instruccion.instrucciones.instrucciones:
                if isinstance(declara, SentenciaCase):
                    self.crearNodoSentenciaCase_Expesion(temp1, instruccion)
                    for casos in declara.casos:
                        if isinstance(casos, Caso):
                            self.crearNodoSentenciaCase_ExpesionCaso(temp1, instruccion)
                            self.crearNodoSentenciaCase_CuerpoCaso(temp1, instruccion)
                        

                    
    def crearNodoSentenciaCase_CuerpoCaso(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Cuerpo Caso')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
        if isinstance(instruccion.instrucciones, Principal):
            print(instruccion.instrucciones)
         

    def crearNodoSentenciaCase_ExpesionCaso(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Expresion Caso')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 

    
    def crearNodoSentenciaCase_Expesion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Expesion')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 

    def crearNodoSentenciaCase_Casos(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Casos')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
                            

    def crearNodoCaso(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Caso')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)


    def crearNodoLlamadaFuncion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Llamada Funcion')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 



    def crearNodoSentenciaIf(self, padre, instruccion):
        
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Sentencia If')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)   


    def crearNodoSentenciaExpresionIf(self, padre, instruccion):
        
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Expresion If')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)   

    def crearNodoDeclaracion(self, padre, instruccion):
        
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DECLARACION')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
                                

    def crearNodoAsignacion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Asignacion')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)   

    def crearNodoExpresion(self, padre, expresion):
        global contadorNodos, dot
        if isinstance(expresion, ExpresionIdentificador):
            if expresion.val != "":
                contadorNodos = contadorNodos + 1
                dot.node("node" + str(contadorNodos), str(expresion.val))
                dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionBinaria):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.exp1))
            dot.node("node" + str(contadorNodos), str(expresion.exp2))
            dot.node("node" + str(contadorNodos), str(expresion.operador))
            dot.edge(padre, "node" + str(contadorNodos))
        else:
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion))
            dot.edge(padre, "node" + str(contadorNodos))    
        
    
    