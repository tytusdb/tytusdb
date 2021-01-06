from subprocess import check_call



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
                try:
                    # print("=======>>>", i)
                    if 'CreateDatabase' in str(i):
                        self.CreateDatabase(i, padre)
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
                    elif 'DropTable' in str(i):
                        self.DropTable(i, padre)
                    elif 'DropDatabase' in str(i):
                        self.DropDatabase(i, padre)
                    elif 'DeleteTable' in str(i):
                        self.DeleteTable(i, padre)
                    elif 'CreateType' in str(i):
                        self.CreateType(i, padre)
                    elif 'truncate' in str(i):
                        self.truncate(i, padre)
                    elif 'AlterTableAddColumn' in str(i):
                        self.AlterTableAddColumn(i, padre)
                    elif 'AlterTableAddCheck' in str(i):
                        self.AlterTableAddCheck(i, padre)
                    elif 'AlterTableAddConstraint' in str(i):
                        self.AlterTableAddConstraint(i, padre)
                    elif 'AlterTableAddConstraintFK' in str(i):
                        self.AlterTableAddConstraintFK(i, padre)
                    elif 'AlterTableAddFK' in str(i):
                        self.AlterTableAddFK(i, padre)
                    elif 'AlterTableAlterColumnType' in str(i):
                        self.AlterTableAlterColumnType(i, padre)
                    elif 'AlterTableDropConstraint' in str(i):
                        self.AlterTableDropConstraint(i, padre)
                    elif 'SelectLista' in str(i):
                        self.SelectLista(i, padre)
                    # elif isinstance(i, Select):
                    #     self.Select(i, padre)
                    # elif isinstance(i, Union):
                    #     self.Union(i, padre)
                except:
                    #print('Instruccion no reconocida o con problemas: ', i)
                    pass
    

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
                                # print(">>>>>>>>>", acom.valorDefaul)
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
        # print("*****************", var)
        
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
        # print(1)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: UPDATE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.CrearNodo('Table: ' + str(inst.identificador.id), np)
        self.CrearNodo('SET', np)
        # for asign in inst.asignaciones:
        #     print(">>>>>>>>>", asign)
        #     if isinstance(asign, Expresion):
        #         if asign.operador == '=':
        #             self.Asignacion(asign, np)
        # if inst.where != None:
        #     self.CrearNodo('WHERE', np)
        #     #where
        #     #puede ser expresion, primitivo o where
        #     print(">>>>>>>>> =====>", inst.where)
        #     if isinstance(inst.where, Expresion):#asignacion, andOr
        #         self.E(inst.where, np)
        #     elif isinstance(inst.where, Primitivo):
        #         self.Primitivo(inst.where, np)
        #     elif isinstance(inst.where, Where):
        #         self.Where(inst.where, np)

    def DropTable(self, inst, padre):
        self.CrearNodo('Instruccion: Drop', padre)
        np = str(self.contador)
        self.CrearNodo('TABLE', np)
        self.CrearNodo(inst.valor, np)
        
    def DropDatabase(self, inst, padre):
        self.CrearNodo('Instruccion: Drop', padre)
        np = str(self.contador)
        self.CrearNodo('DATABASE', np)
        if inst.existe:
            self.CrearNodo('IF EXISTS', np)
        self.CrearNodo(inst.id, np)

    def DeleteTable(self, inst, padre):
        self.CrearNodo('Instruccion: Delete', padre)
        np = str(self.contador)
        self.CrearNodo('Table: ' + inst.valor, np)
        if inst.insWhere != None:
            
            if 'DateTimeTypes' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Time(inst.where.valor, np)
            elif 'Identificador' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.CrearNodo(inst.where.valor , np)
            # elif 'Alias' in col:
            #     self.IdAsId(col, np)
            elif 'Expresiones' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Math_(inst.where.valor, np)
            elif 'FunctionAgregate' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Agregate(inst.where.valor, np)
            elif 'FunctionBinaryString' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Binario(inst.where.valor, np)
            elif 'FunctionMathematical' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Fun_Math_(inst.where.valor, np)
            elif 'FunctionTrigonometric' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Trig(inst.where.valor, np)
            elif 'Relacional' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Relacional(inst.where.valor, np)

            # self.CrearNodo('WHERE', np)
            # #where
            # #puede ser expresion, primitivo o where
            # if isinstance(inst.where, Expresion):#asignacion, andOr
            #     self.E(inst.where, np)
            # elif isinstance(inst.where, Primitivo):
            #     self.Primitivo(inst.where, np)
            # elif isinstance(inst.where, Where):
            #     self.Where(inst.where, np)

    def CreateType(self, inst, padre):
        self.CrearNodo('Instruccion: CREATE TYPE', padre)
        np = str(self.contador)
        self.CrearNodo('CREATE TYPE', np)
        self.CrearNodo(inst.valor, np)
        self.CrearNodo('AS ENUM', np)
        self.listaID(inst.listaExpre, np)
        
    def truncate(self, inst, padre):
        self.CrearNodo('Instruccion: TRUNCATE', padre)
        np = str(self.contador)
        self.CrearNodo('TRUNCATE', np)
        self.CrearNodo(inst.valor, np)
        self.CrearNodo('AS ENUM', np)
        self.listaID(inst.listaExpre, np)

    def AlterTableAddColumn(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.id + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        for alt in inst.alter:
            self.listaID(inst.id, str(self.contador))    
            self.contador = self.contador + 1
            label = inst.tipo.tipo
            if inst.tipo.longitud != None:
                label += '(' + str(inst.tipo.longitud.valor) + ')'
            self.c += 'Nodo'+ str(self.contador)+ '[label="Tipo: ' + label + '"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            
    def AlterTableAddCheck(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.id + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        for alt in inst.alter:
            if 'Expresiones' in inst.check:
                self.Expresiones(inst.check, str(self.contador))
            else: #lista de valores
                self.listaID(inst.check, str(self.contador))
                
    def AlterTableAddConstraint(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.id + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        for alt in inst.alter:
            self.Identificador(inst.id, np) 
            
    def AlterTableAddConstraintFK(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.tabla + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        for alt in inst.alter:
            self.listaID(inst.id_constraint, str(self.contador))
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="REFERENCES: ' + inst.tabla2 + '"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="Columnas"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            self.listaID(inst.lista_id2, str(self.contador)) 

    def AlterTableAddFK(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.tabla + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        for alt in inst.alter:
            self.listaID(inst.lista_col, str(self.contador))
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="REFERENCES: ' + inst.tabla_ref + '"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="Columnas"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            self.listaID(inst.lista_fk, str(self.contador)) 

    def AlterTableAlterColumnType(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.tabla + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        for alt in inst.alter:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.tabla + '"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            self.listaID(inst.lista_col, str(self.contador))

            # self.Id(inst.id, np)
            # self.contador = self.contador + 1
            # self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.typeSet + '"]\n' 
            # self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            # if inst.tipo != None:
            #     self.contador = self.contador + 1
            #     self.c += 'Nodo'+ str(self.contador)+ '[label="Tipo: ' + str(inst.tipo) + '"]\n'
            #     self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def AlterTableDropColumn(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.tabla + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        for alt in inst.alter:
            self.listaID(inst.lista_col, str(self.contador))

    def AlterTableDropConstraint(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.tabla + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        for alt in inst.alter:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="Constraint: ' + inst.col + '"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def Select(self, inst, padre):
        np = padre
        if inst.dist != None:
            self.CrearNodo('DISTINCT', np)

        for col in inst.lcol:
            if col == '*':
                self.CrearNodo('ALL (*)', np)
            # elif 'Select'in str(col):
            #     self.SelectLista(col, np)
            elif 'DateTimeTypes' in str(col):
                self.Time(col, np)
            elif 'Identificador' in str(col):
                self.CrearNodo(col.id , np)
            # elif 'Alias' in col:
            #     self.IdAsId(col, np)
            elif 'Expresiones' in str(col):
                self.Math_(col, np)
            elif 'FunctionAgregate' in str(col):
                self.Agregate(col, np)
            elif 'FunctionBinaryString' in str(col):
                self.Binario(col, np)
            elif 'FunctionMathematical' in str(col):
                self.Fun_Math_(col, np)
            elif 'FunctionTrigonometric' in str(col):
                self.Trig(col, np)

        for col in inst.lcol2:
            if 'DateTimeTypes' in str(col):
                self.CrearNodo('FROM', np)
                self.Time(col, np)
            elif 'Identificador' in str(col):
                self.CrearNodo('FROM', np)
                self.CrearNodo(col.id , np)
            # elif 'Alias' in col:
            #     self.IdAsId(col, np)
            elif 'Expresiones' in str(col):
                self.CrearNodo('FROM', np)
                self.Math_(col, np)
            elif 'FunctionAgregate' in str(col):
                self.CrearNodo('FROM', np)
                self.Agregate(col, np)
            elif 'FunctionBinaryString' in str(col):
                self.CrearNodo('FROM', np)
                self.Binario(col, np)
            elif 'FunctionMathematical' in str(col):
                self.CrearNodo('FROM', np)
                self.Fun_Math_(col, np)
            elif 'FunctionTrigonometric' in str(col):
                self.CrearNodo('FROM', np)
                self.Trig(col, np)
        
        if inst.linners != None:
            self.CrearNodo('INNERS', np)
            self.SelectLista(col, np)
            # if 'GroupBy' in str(col):
            #     self.GroupBy(col, np)
        
        if inst.where != None:
            # print("@@@ >>>", inst.where.valor)
            # self.CrearNodo('WHERE', np)
            # # self.Columnas(inst.where, np)if 'Select'in str(col):
            if 'DateTimeTypes' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Time(inst.where.valor, np)
            elif 'Identificador' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.CrearNodo(inst.where.valor , np)
            # elif 'Alias' in col:
            #     self.IdAsId(col, np)
            elif 'Expresiones' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Math_(inst.where.valor, np)
            elif 'FunctionAgregate' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Agregate(inst.where.valor, np)
            elif 'FunctionBinaryString' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Binario(inst.where.valor, np)
            elif 'FunctionMathematical' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Fun_Math_(inst.where.valor, np)
            elif 'FunctionTrigonometric' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Trig(inst.where.valor, np)
            elif 'Relacional' in str(inst.where.valor):
                self.CrearNodo('WHERE', np)
                self.Relacional(inst.where.valor, np)
            
        if inst.lrows != None:
            if 'GroupBy' in str(inst.lrows):
                self.CrearNodo('Group By', np)
                for a in inst.lrows:
                    for b in a.valor:
                        self.CrearNodo( str(b.id) , np)
            elif 'Limit' in str(inst.lrows):
                self.CrearNodo('LIMIT', np)
                for a in inst.lrows:
                    self.CrearNodo( str(a.listaExpre) , np)
            elif 'OrderBy' in str(inst.lrows):
                self.CrearNodo('Order By', np)
                for a in inst.lrows:
                    self.CrearNodo('Order By', np)
            elif 'Having' in str(inst.lrows):
                self.CrearNodo('Having', np)


    def SelectLista(self, inst, padre):
        self.CrearNodo('Instruccion: Select', padre)
        np = str(self.contador)

        for sub_inst in inst.lista:
            self.Select(sub_inst,np)


    def Expresiones(self, inst, padre):
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="E"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        eiz = False
        edr = False
        prim = False
        prim2 = False
        # print('expresion')

    def Identificador(self, id, padre):
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="Identificador: ' + id + '"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def Columnas(self, inst, padre):
        self.CrearNodo('Columnas', padre)
        np = str(self.contador)
        for col in str(inst):
            #modificacion, pasa esto a metodo Columna
            self.Columna(col, np)

    def Columna(self, col, padre):
        # print("@@@ >", col)
        self.CrearNodo('Columna', padre)
        np = str(self.contador)

        if 'Select'in str(col):
            self.SelectLista(col, np)
        elif 'DateTimeTypes' in str(col):
            self.Time(col, np)
        elif 'Identificador' in str(col):
            self.CrearNodo(col.id , np)
        # elif 'Alias' in col:
        #     self.IdAsId(col, np)
        elif 'Expresiones' in str(col):
            self.Math_(col, np)
        elif 'FunctionAgregate' in str(col):
            self.Agregate(col, np)
        elif 'FunctionBinaryString' in str(col):
            self.Binario(col, np)
        elif 'FunctionMathematical' in str(col):
            self.Fun_Math_(col, np)
        elif 'FunctionTrigonometric' in str(col):
            self.Trig(col, np)

    def Time(self, inst, padre):
        self.CrearNodo('Funciones con Fechas', padre)
        np = str(self.contador)
        if 'Case' in str(inst):
            self.CrearNodo('CASE', np)
            self.CrearNodo(inst.identificador + ' [ID]', np)
            self.CrearNodo(inst.valor + ' [valor]', np)
            self.CrearNodo(inst.operacion + ' [operacion]', np)
        elif 'CurrentDate' in str(inst):
            self.CrearNodo('CURRENT_DATE', np)
        elif 'CurrentTime' in str(inst):
            self.CrearNodo('CURRENT_TIME', np)
        elif 'DatePart' in str(inst):
            self.CrearNodo('DatePart', np)
            self.CrearNodo(inst.identificador, np)
            self.CrearNodo('INTERVAL', np)
            self.CrearNodo(inst.valor, np)
        elif 'Extract' in str(inst):
            self.CrearNodo('EXTRACT', np)
            self.CrearNodo(inst.tiempo, np)
            self.CrearNodo('FROM TIMESTAMP', np)
            self.CrearNodo(inst.caracter, np)
        elif 'Now' in str(inst):
            self.CrearNodo('NOW', np)
        elif 'Por' in str(inst):
            self.CrearNodo('Por', np)
            self.CrearNodo(inst.identificador + ' [ID]', np)
            self.CrearNodo(inst.valor + ' [valor]', np)
            self.CrearNodo(inst.operacion + ' [operacion]', np)
    
    def Math_(self, inst, padre):
        self.CrearNodo('Operaciones Matematicas', padre)
        np = str(self.contador)
        if 'Aritmetica' in str(inst):
            self.CrearNodo('Aritmetica', np)
            self.CrearNodo(str(inst.opIzq) , np)
            self.CrearNodo(inst.operador , np)
            self.CrearNodo(str(inst.opDer) , np)
        elif 'Between' in str(inst):
            self.CrearNodo('Between', np)
            self.CrearNodo(str(inst.opIzq) , np)
            self.CrearNodo(inst.operador , np)
            self.CrearNodo(str(inst.opDer) , np)
            self.CrearNodo(str(inst.opDer2) , np)
        elif 'Enum' in str(inst):
            self.CrearNodo('Enum', np)
            self.CrearNodo(inst.id , np)
            for carac in inst.listaValores:
                self.CrearNodo(carac , np)
        elif 'Logica' in str(inst):
            self.CrearNodo('Logica', np)
            self.CrearNodo(str(inst.opIzq) , np)
            self.CrearNodo(inst.operador , np)
            self.CrearNodo(str(inst.opDer) , np)
        elif 'Primitivo' in str(inst):
            self.CrearNodo('Primitivo', np)
            self.CrearNodo(str(inst.valor) , np)
        elif 'Relacional' in str(inst):
            self.CrearNodo('Relacional', np)
            # self.CrearNodo(inst.opIzq , np)
            self.Math_(inst.opIzq , np)
            self.CrearNodo(inst.operador , np)
            # self.CrearNodo(inst.opDer , np)
            self.Math_(inst.opDer , np)

    def Agregate(self, inst, padre):
        self.CrearNodo('Funciones Agregate', padre)
        np = str(self.contador)
        if 'Avg' in str(inst):
            self.CrearNodo('Avg', np)
            self.CrearNodo(inst.valor , np)
        elif 'Count' in str(inst):
            self.CrearNodo('Count', np)
            self.CrearNodo(inst.valor , np)
        elif 'Greatest' in str(inst):
            self.CrearNodo('Greatest', np)
            self.CrearNodo(inst.valor , np)
        elif 'Least' in str(inst):
            self.CrearNodo('Least', np)
            self.CrearNodo(inst.valor , np)
        elif 'Max' in str(inst):
            self.CrearNodo('Max', np)
            self.CrearNodo(inst.valor , np)
        elif 'Min' in str(inst):
            self.CrearNodo('Min', np)
            self.CrearNodo(inst.valor , np)
        elif 'Sum' in str(inst):
            self.CrearNodo('Sum', np)
            self.CrearNodo(inst.valor , np)
        elif 'Top' in str(inst):
            self.CrearNodo('Top', np)
            self.CrearNodo(inst.valor , np)

    def Binario(self, inst, padre):
        self.CrearNodo('Funciones Binarias', padre)
        np = str(self.contador)
        if 'Convert' in str(inst):
            self.CrearNodo('Convert', np)
            self.CrearNodo(inst.valor , np)
            self.CrearNodo(inst.tipo , np)
            self.CrearNodo(inst.tipo_salida + ' [tipo_salida]' , np)
        elif 'Decode' in str(inst):
            self.CrearNodo('Decode', np)
            self.CrearNodo(inst.valor , np)
            self.CrearNodo(inst.codificacion , np)
        elif 'Encode' in str(inst):
            self.CrearNodo('Encode', np)
            self.CrearNodo(inst.valor , np)
            self.CrearNodo(inst.codificacion , np)
        elif 'GetByte' in str(inst):
            self.CrearNodo('GetByte', np)
            self.CrearNodo(inst.valor , np)
            self.CrearNodo(inst.indice , np)
        elif 'Length' in str(inst):
            self.CrearNodo('Length', np)
            self.CrearNodo(inst.valor , np)
        elif 'Md5' in str(inst):
            self.CrearNodo('Md5', np)
            self.CrearNodo(inst.valor , np)
            self.CrearNodo(inst.tipo , np)
        elif 'SetByte' in str(inst):
            self.CrearNodo('SetByte', np)
            self.CrearNodo(inst.valor , np)
            self.CrearNodo(inst.tipo , np)
            self.CrearNodo(inst.indice , np)
            self.CrearNodo(inst.caracter , np)
        elif 'Sha256' in str(inst):
            self.CrearNodo('Sha256', np)
            self.CrearNodo(inst.valor , np)
        elif 'Substr' in str(inst):
            self.CrearNodo('Substr', np)
            self.CrearNodo(inst.valor , np)
        elif 'Substring' in str(inst):
            self.CrearNodo('Substring', np)
            self.CrearNodo(inst.valor , np)
            self.CrearNodo(inst.inicio , np)
            self.CrearNodo(inst.fin , np)
        elif 'Trim' in str(inst):
            self.CrearNodo('Trim', np)
            self.CrearNodo(inst.valor , np)
            
    def Fun_Math_(self, inst, padre):
        self.CrearNodo('Funciones Matematicas', padre)
        np = str(self.contador)
        if 'Abs' in str(inst):
            self.CrearNodo('Abs', np)
            self.CrearNodo(inst.valor , np)
        elif 'Cbrt' in str(inst):
            self.CrearNodo('Cbrt', np)
            self.CrearNodo(inst.valor , np)
        elif 'Ceil' in str(inst):
            self.CrearNodo('Ceil', np)
            self.CrearNodo(inst.valor , np)
        elif 'Ceiling' in str(inst):
            self.CrearNodo('Ceiling', np)
            self.CrearNodo(inst.valor , np)
        elif 'Degrees' in str(inst):
            self.CrearNodo('Degrees', np)
            self.CrearNodo(inst.valor , np)
        elif 'Div' in str(inst):
            self.CrearNodo('Div', np)
            self.CrearNodo(inst.opIzq , np)
            self.CrearNodo(inst.opDer , np)
        elif 'Exp' in str(inst):
            self.CrearNodo('Exp', np)
            self.CrearNodo(inst.valor , np)
        elif 'Factorial' in str(inst):
            self.CrearNodo('Factorial', np)
            self.CrearNodo(inst.valor , np)
        elif 'Floor' in str(inst):
            self.CrearNodo('Floor', np)
            self.CrearNodo(inst.valor , np)
        elif 'Gcd' in str(inst):
            self.CrearNodo('Gcd', np)
            self.CrearNodo(inst.opIzq , np)
            self.CrearNodo(inst.opDer , np)
        elif 'Lcm' in str(inst):
            self.CrearNodo('Lcm', np)
            self.CrearNodo(inst.valor , np)
        elif 'Ln' in str(inst):
            self.CrearNodo('Ln', np)
            self.CrearNodo(inst.valor , np)
        elif 'Log' in str(inst):
            self.CrearNodo('Log', np)
            self.CrearNodo(inst.valor , np)
        elif 'Log10' in str(inst):
            self.CrearNodo('Log10', np)
            self.CrearNodo(inst.valor , np)
        elif 'MinScale' in str(inst):
            self.CrearNodo('MinScale', np)
            self.CrearNodo(inst.valor , np)
        elif 'Mod' in str(inst):
            self.CrearNodo('Mod', np)
            self.CrearNodo(inst.opIzq , np)
            self.CrearNodo(inst.opDer , np)
        elif 'PI' in str(inst):
            self.CrearNodo('PI', np)
        elif 'Power' in str(inst):
            self.CrearNodo('Power', np)
            self.CrearNodo(inst.opIzq , np)
            self.CrearNodo(inst.opDer , np)
        elif 'Radians' in str(inst):
            self.CrearNodo('Radians', np)
            self.CrearNodo(inst.valor , np)
        elif 'Random' in str(inst):
            self.CrearNodo('Random', np)
        elif 'Round' in str(inst):
            self.CrearNodo('Round', np)
            self.CrearNodo(inst.valor , np)
        elif 'Scale' in str(inst):
            self.CrearNodo('Scale', np)
            self.CrearNodo(inst.valor , np)
        elif 'SetSeed' in str(inst):
            self.CrearNodo('SetSeed', np)
            self.CrearNodo(inst.valor , np)
        elif 'Sign' in str(inst):
            self.CrearNodo('Sign', np)
            self.CrearNodo(inst.valor , np)
        elif 'Sqrt' in str(inst):
            self.CrearNodo('Sqrt', np)
            self.CrearNodo(inst.valor , np)
        elif 'TrimScale' in str(inst):
            self.CrearNodo('TrimScale', np)
            self.CrearNodo(inst.valor , np)
        elif 'Trunc' in str(inst):
            self.CrearNodo('Trunc', np)
            self.CrearNodo(inst.valor , np)
        elif 'WidthBucket' in str(inst):
            self.CrearNodo('WidthBucket', np)
            self.CrearNodo(inst.valor , np)
            self.CrearNodo(inst.min + ' [min]' , np)
            self.CrearNodo(inst.max + ' [max]', np)
            self.CrearNodo(inst.count , np)

    def Trig(self, inst, padre):
        self.CrearNodo('Funciones Trigonometricas', padre)
        np = str(self.contador)
        if 'Acos' in str(inst):
            self.CrearNodo('Acos', np)
            self.CrearNodo(inst.valor , np)
        elif 'Acosd' in str(inst):
            self.CrearNodo('Acosd', np)
            self.CrearNodo(inst.valor , np)
        elif 'Acosh' in str(inst):
            self.CrearNodo('Acosh', np)
            self.CrearNodo(inst.valor , np)
        elif 'Asind' in str(inst):
            self.CrearNodo('Asind', np)
            self.CrearNodo(inst.valor , np)
        elif 'Asinh' in str(inst):
            self.CrearNodo('Asinh', np)
            self.CrearNodo(inst.valor , np)
        elif 'Atan' in str(inst):
            self.CrearNodo('Atan', np)
            self.CrearNodo(inst.valor , np)
        elif 'Atan2' in str(inst):
            self.CrearNodo('Atan2', np)
            self.CrearNodo(inst.opIzq , np)
            self.CrearNodo(inst.opDer , np)
        elif 'Atan2d' in str(inst):
            self.CrearNodo('Atan2d', np)
            self.CrearNodo(inst.opIzq , np)
            self.CrearNodo(inst.opDer , np)
        elif 'Atand' in str(inst):
            self.CrearNodo('Atand', np)
            self.CrearNodo(inst.valor , np)
        elif 'Atanh' in str(inst):
            self.CrearNodo('Atanh', np)
            self.CrearNodo(inst.valor , np)
        elif 'Cos' in str(inst):
            self.CrearNodo('Cos', np)
            self.CrearNodo(inst.valor , np)
        elif 'Cosd' in str(inst):
            self.CrearNodo('Cosd', np)
            self.CrearNodo(inst.valor , np)
        elif 'Cosh' in str(inst):
            self.CrearNodo('Cosh', np)
            self.CrearNodo(inst.valor , np)
        elif 'Cot' in str(inst):
            self.CrearNodo('Cot', np)
            self.CrearNodo(inst.valor , np)
        elif 'Cotd' in str(inst):
            self.CrearNodo('Cotd', np)
            self.CrearNodo(inst.valor , np)
        elif 'Sin' in str(inst):
            self.CrearNodo('Sin', np)
            self.CrearNodo(inst.valor , np)
        elif 'Sind' in str(inst):
            self.CrearNodo('Sind', np)
            self.CrearNodo(inst.valor , np)
        elif 'Tan' in str(inst):
            self.CrearNodo('Tan', np)
            self.CrearNodo(inst.valor , np)
        elif 'Sinh' in str(inst):
            self.CrearNodo('Sinh', np)
            self.CrearNodo(inst.valor , np)
        elif 'Tand' in str(inst):
            self.CrearNodo('Tand', np)
            self.CrearNodo(inst.valor , np)
        elif 'Tanh' in str(inst):
            self.CrearNodo('Tanh', np)
            self.CrearNodo(inst.valor , np)

    def Relacional(self, inst, padre):
        self.CrearNodo('Funcion Relacionales', padre)
        np = str(self.contador)
        self.CrearNodo(inst.opIzq , np)
        self.CrearNodo(inst.operador , np)
        self.CrearNodo(inst.opDer , np) 

    def Limit(self, inst, padre):
        if inst.all:
            self.CrearNodo('ALL', padre)
        if inst.e1 != None:
            self.CrearNodo(inst.e1, padre)
        if inst.e2 != None:
            self.CrearNodo('OFFSET', padre)
            self.CrearNodo(inst.e2, padre)

    def Union(self, inst, padre):
        self.CrearNodo('Instruccion: Combinar Queries', padre)
        np = str(self.contador)
        self.Select(inst.q1, np)
        self.CrearNodo(inst.tipo, np)
        if inst.all:
            self.CrearNodo('ALL', np)
        self.Select(inst.q2, np)