from subprocess import check_call

from Instrucciones.Sql_create import CreateDatabase


class AST:
    def __init__(self, sentencias):
        self.contador = 0
        self.c = ""
        self.sentencias = sentencias
        self.pe = 0


    def ReportarAST(self):
        print('Graficando AST....')
        #print(self.sentencias)
        f = open('AST.dot', 'w')
        self.c = 'digraph G{\n' 
        self.c += 'edge [color=black]; rankdir = TB;\n'
        self.c += 'Nodo'+ str(self.contador)+ '[label="INICIO"]\n'
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instrucciones"]\n' 
        self.c += 'Nodo' + '0' +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.TiposInstruccion(self.sentencias, str(self.contador))
        self.c += "}\n"
        #print(arbol)
        f.write(self.c)
        f.close()
        check_call(['dot', '-Tsvg', 'AST.dot', '-o', 'AST.svg'])

        
    def TiposInstruccion(self, inst, padre):
        if inst != None:
            for i in inst:
                print("=======>>>", i)
                if 'CreateDatabase' in str(i):
                    self.CreateDatabase(i, padre)
                # elif isinstance(i, InsertInto):
                #     self.InsertInto(i, padre)
                # elif isinstance(i, CreateReplace):
                #     self.CreateReplace(i, padre)
                elif 'Show' in str(i):
                    self.Show(padre)
                elif 'Use' in str(i):
                    self.Use(i, padre)
                elif 'AlterDatabase' in str(i):
                    self.AlterDatabase(i, padre)
                elif 'AlterDBOwner' in str(i):
                    self.AlterDBOwner(i, padre)
                elif 'CreateOrReplace' in str(i):
                    self.CreateOrReplace(i, padre)
                elif 'CreateTable' in str(i):
                    self.CreateTable(i, padre)
                elif 'insertTable' in str(i):
                    self.insertTable(i, padre)
                elif 'UpdateTable' in str(i):
                    self.Update(i, padre)
                # elif isinstance(i, AlterTable):
                #     self.AlterTable(i, padre)
                # elif isinstance(i, Delete):
                #     self.Delete(i, padre)
                # elif isinstance(i, Select):
                #     self.Select(i, padre)
                # elif isinstance(i, Union):
                #     self.Union(i, padre)
                # elif isinstance(i, Drop):
                #     self.Drop(i, padre)
                # elif isinstance(i, CreateType):
                #     self.CreateType(i, padre)
    

    def CreateDatabase(self, inst, padre):
        label = ""
        label = 'CREATE DATABASE'
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="'+label+'"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        if inst.existe != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="IF NOT EXISTS"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.base + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        if inst.owner != None:
            if 'ComplementoCR' in str(inst.complemento):
                self.contador = self.contador + 1
                self.c += 'Nodo'+ str(self.contador)+ '[label="OWNER: ' + inst.owner + '"]\n' 
                self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        if inst.mode != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="MODE: ' + str(inst.mode) + '"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n' 
    
    def CreateOrReplace(self, inst, padre):
        label = ""
        label = 'CREATE OR REPLACE DATABASE'
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="'+label+'"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        if inst.existe != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="IF NOT EXISTS"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.base + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        if inst.owner != None:
            if 'ComplementoCR' in str(inst.complemento):
                self.contador = self.contador + 1
                self.c += 'Nodo'+ str(self.contador)+ '[label="OWNER: ' + inst.owner + '"]\n' 
                self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        if inst.mode != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="MODE: ' + str(inst.mode) + '"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n' 

    def Show(self, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="SHOW DATABASES"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def CrearNodo(self, label, padre):
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + label + '"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
    
    def Use(self, inst, padre):
        self.CrearNodo('USE DATABASE ['+ inst.valor +']', padre)

    def AlterDatabase(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="ALTER DATABASE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.nombreAntiguo + ' [old]"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador = self.contador + 1
        label = ""
        label = 'RENAME TO'
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + label + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador = self.contador + 1
        
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.nombreNuevo + ' [new]"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def AlterDBOwner(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="ALTER DATABASE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.id + ' [BD]"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador = self.contador + 1
        label = ""
        label = 'OWNER TO'
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + label + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador = self.contador + 1
        
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.owner + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def CreateTable(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: CREATE TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Id: ' + inst.tabla + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        #recorrer campos
        for campo in inst.campos:
            if 'Columna' in str(campo): 
                self.contador = self.contador + 1
                self.c += 'Nodo'+ str(self.contador)+ '[label="Campo"]\n' 
                self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                ncp = str(self.contador) 
                # if campo.caso == 1:
                self.contador = self.contador + 1

                self.c += 'Nodo'+ str(self.contador)+ '[label="Id: ' + campo.nombre + '"]\n' 
                self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                self.contador = self.contador + 1
                self.c += 'Nodo'+ str(self.contador)+ '[label="Tipo: ' + str(campo.tipo.tipo) + '"]\n' 
                self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

                if campo.constraint != None:
                    for acom in campo.constraint:
                        self.contador = self.contador + 1
                        a = str(self.contador)
                        if acom.tipo == 'DEFAULT':
                            self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + ': '+ str(acom.valorDefault.valor) + '"]\n' 
                        elif acom.tipo == 'UNIQUE':
                            if acom.valorDefault != None:
                                print(">>>>>>>>>", acom.valorDefaul)
                                if isinstance(acom.valorDefault, Id):
                                    self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + ': ' + acom.valorDefault.id +'"]\n' 
                                else:    
                                    self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + '"]\n'
                                    #listaId padre self.contador 
                                    self.listaID(acom.valorDefault, str(self.contador))
                            else:    
                                self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + '"]\n' 
                        elif acom.tipo == 'CHECK':
                            self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + '"]\n'
                            if isinstance(acom.valorDefault, Expresion):
                                self.E(acom.valorDefault, ncp)
                            else:
                                self.listaID(acom.valorDefault, ncp)
                        else:
                            self.c += 'Nodo'+ str(self.contador)+ '[label="' + str(acom.tipo) + '"]\n' 
                        self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ a + ';\n'

        #     if campo.caso == 2 or campo.caso == 3:
        #         if campo.caso == 2:
        #             self.contador = self.contador + 1
        #             self.c += 'Nodo'+ str(self.contador)+ '[label="CONSTRAINT: ' + campo.id + '"]\n' 
        #             self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        #         self.contador = self.contador + 1
        #         a = str(self.contador)
        #         if len(campo.idFk) == 1:
        #             self.c += 'Nodo'+ str(self.contador)+ '[label="FOREIGN KEY: ' + campo.idFk[0].id + '"]\n' 
        #         else:
        #             self.c += 'Nodo'+ str(self.contador)+ '[label="FOREIGN KEY"]\n' 
        #             self.listaID(campo.idFk, str(self.contador))
        #         self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ a + ';\n'
        #         self.contador = self.contador + 1
        #         self.c += 'Nodo'+ str(self.contador)+ '[label="REFERENCES: ' + campo.tablaR + '"]\n' 
        #         self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        #         self.contador = self.contador + 1
        #         a = str(self.contador)
        #         if len(campo.idR) == 1:
        #             self.c += 'Nodo'+ str(self.contador)+ '[label="Columna: ' + campo.idR[0].id + '"]\n' 
        #         else:
        #             self.c += 'Nodo'+ str(self.contador)+ '[label="Columnas"]\n' 
        #             self.listaID(campo.idR, str(self.contador))    
        #         self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ a + ';\n'                     
        #     if campo.caso == 4:
        #         self.contador = self.contador + 1
        #         a = str(self.contador)
        #         #if len(campo.id) == 1:
        #             #   self.c += 'Nodo'+ str(self.contador)+ '[label="PRIMARY KEY: '+ campo.id +'"]\n' 
        #         #else:
        #         self.c += 'Nodo'+ str(self.contador)+ '[label="PRIMARY KEY"]\n' #
        #         self.listaID(campo.id, str(self.contador))#
        #         self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ a + ';\n'


        if inst.herencia != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="INHERITS: '+ inst.herencia +'"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def listaID(self, inst, padre):
        for var in inst:
            #modificacion, pasa esto a metodo Valor
            self.Valor(var, padre)

    def Valor(self, var, padre):
        print("*****************", var)
        
        if 'ID' in str(var):
            self.contador += self.contador
            self.c += 'Nodo'+ str(self.contador)+ '[label="' + str(var) + '"]\n' 
            self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        elif'IdId' in str(var):
            self.CrearNodo(str(var) + '.' + str(var), padre)
        elif 'Primitivo' in str(var):
            self.contador += self.contador
            self.c += 'Nodo'+ str(self.contador)+ '[label="' + str(var.valor) + '"]\n' 
            self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        # elif 'Time' in str(var):
        #     self.Time(var, padre)
        # elif 'Math_' in str(var):
        #     self.Math_(var, padre)
        # elif 'Trigonometrica' in str(var):
        #     self.Trig(var, padre)
        # elif 'Binario' in str(var):
        #     self.Binario(var, padre)
        # #para que tambien sea lista de expresiones
        # elif 'Expresion' in str(var):
        #     self.E(var, padre)

    def insertTable(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: INSERT INTO"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1

        self.c += 'Nodo'+ str(self.contador)+ '[label="Table: ' + inst.valor + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        if inst.lcol != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="Columnas"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            self.listaID(inst.lcol, str(self.contador))  
        if inst.lexpre != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="Value"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            self.listaID(inst.lexpre, str(self.contador))      

    def Update(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: UPDATE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.CrearNodo('Table: ' + inst.identificador, np)
        self.CrearNodo('SET', np)
        for asign in inst.asignaciones:
            print(">>>>>>>>>", asign)
            if isinstance(asign, Expresion):
                if asign.operador == '=':
                    self.Asignacion(asign, np)
        if inst.where != None:
            self.CrearNodo('WHERE', np)
            #where
            #puede ser expresion, primitivo o where
            print(">>>>>>>>> =====>", inst.where)
            if isinstance(inst.where, Expresion):#asignacion, andOr
                self.E(inst.where, np)
            elif isinstance(inst.where, Primitivo):
                self.Primitivo(inst.where, np)
            elif isinstance(inst.where, Where):
                self.Where(inst.where, np)



