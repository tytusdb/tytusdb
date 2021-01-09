from analizer.abstract import instruction
from analizer.abstract.expression import TYPE
from analizer.symbol.environment import Environment
import analizer.symbol.c3dSymbols as SymbolTable
from analizer.statement.functions.call import FunctionCall
from analizer.statement.expressions.identifiers import Identifiers
from datetime import datetime
from analizer.statement.instructions.select.select import Select
from analizer.statement.pl.instruccionesF1 import F1
from analizer.reports.Nodo import Nodo
from analizer.reports.AST import AST

class Declaration(instruction.Instruction):
    def __init__(self,nombre,tipo,valor,row,column):
        instruction.Instruction.__init__(self,row,column)
        self.nombre=nombre
        self.tipo=tipo
        self.valor=valor
        self.row=row
        self.column=column
        self.classType=str(self.valor.__class__.__name__).casefold()
        self.exp = self.valor
    def execute(self,environment):
        pass
    def generate3d(self,environment,instanciaAux):
        tipo=self.tipo[0].casefold()
        if not isinstance(self.valor,F1):
            try:
                TypeV = None
                if type(self.valor) in (str, bool, float, int):
                    self.valor = None
                if self.valor != None:
                    TypeV=self.valor.execute(environment).type
                    print('El tipo es: '+TypeV.name)
            except:
                instruction.semanticErrors.append(
                        ( "ERROR: 42P18: tipo de dato indeterminado en '%s'" %self.nombre,self.row)
                )
                return None
        try:
            if not isinstance(self.valor, Identifiers):
                self.valor=self.valor.value
        except:
            pass
        try:
            if 'primitive'==self.classType or self.valor == None:
                if self.valor == None:
                    if 'integer' in tipo or 'bigint' in tipo:
                        self.valor=0
                        TypeV = TYPE.NUMBER
                    elif 'numeric' in tipo or 'double precision' in tipo or 'money' in tipo or 'decimal' in tipo:
                        self.valor=0.0
                        TypeV = TYPE.NUMBER
                    elif 'text' in tipo or 'varchar' in tipo or 'char' in tipo or 'varying' in tipo:
                        self.valor='\'\''
                        TypeV = TYPE.STRING
                    elif 'boolean' in tipo:
                        self.valor=False
                        TypeV = TYPE.BOOLEAN
                    elif 'timestamp' in tipo:
                        self.valor=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        TypeV = TYPE.TIMESTAMP
                    elif 'date' in tipo:
                        self.valor=datetime.now().strftime("%Y-%m-%d")
                        TypeV = TYPE.DATE
                    elif 'time' in tipo:
                        self.valor=datetime.now().strftime("%H:%M:%S")
                        TypeV = TYPE.TIME
                    else:
                        pass
                else:
                    if 'text' in tipo or 'varchar' in tipo or 'char' in tipo or 'varying' in tipo:
                        if TypeV==TYPE.STRING:
                            self.valor='\''+self.valor+'\''
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print(1)
                            return None
                            #return error de tipo
                    elif 'timestamp' in tipo:
                        if TypeV==TYPE.TIMESTAMP:
                            self.valor='\''+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\''
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print(2)
                            return None
                    elif 'date' in tipo:
                        if TypeV==TYPE.DATE:
                            self.valor='\''+datetime.now().strftime("%Y-%m-%d")+'\''
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print(3)
                            return None
                    elif 'time' in tipo:
                        if TypeV==TYPE.TIME:
                            self.valor='\''+datetime.now().strftime("%H:%M:%S")+'\''
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print(4)
                            return None
                    elif 'integer' in tipo or 'bigint' in tipo:
                        if TypeV==TYPE.NUMBER:
                            if not type(self.valor)==float:
                                self.valor=self.valor
                            else:
                                instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                                )
                                print(5)
                                return None
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print(6)
                            return None
                    elif 'numeric' in tipo or 'double precision' in tipo or 'money' in tipo or 'decimal' in tipo:
                        if type(self.valor)==float:
                            self.valor=self.valor
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print(7)
                            return None
                    elif 'boolean' in tipo:
                        if TypeV==TYPE.BOOLEAN:
                            self.valor=self.valor
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print(8)
                            return None

                    else:
                        instruction.semanticErrors.append(
                                 "ERROR: 42P18: tipo de dato indeterminado en '%s'" %self.nombre
                        )
                        return None
                SymbolTable.add_symbol(self.nombre,TypeV,self.valor,self.row,self.column,None)
                instanciaAux.addToCode(f'\t{self.nombre} =  {self.valor}')
    
            elif not self.classType == None:
                if isinstance(self.valor,FunctionCall):
                    callValue=self.valor.execute(environment).value
                    SymbolTable.add_symbol(self.nombre,TypeV,callValue,self.row,self.column,None)
                    instanciaAux.addToCode(f'\t{self.nombre} =  {callValue}')
                elif isinstance(self.valor,F1):
                    callTemp=self.valor.generate3d(environment,instanciaAux)
                    SymbolTable.add_symbol(self.nombre,'Query',callTemp,self.row,self.column,None)
                    instanciaAux.addToCode(f'\t{self.nombre} =  {callTemp}')
                else:    
                    newTemp=self.valor.generate3d(environment,instanciaAux)
                    callValue=self.valor.execute(environment).value
                    if isinstance(self.valor, Identifiers):
                        callValue=self.valor.name
                    SymbolTable.add_symbol(self.nombre,TypeV,callValue,self.row,self.column,None)
                    instanciaAux.addToCode(f'\t{self.nombre} =  {newTemp}')
        except Exception() as e:
            instruction.semanticErrors.append(
                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
            )
            print(9, e)
            return None
    def dot(self):
        nuevo_nodo = Nodo("DECLARACION")
        id_nodo = Nodo("IDENTIFICADOR")
        tipo_nodo = Nodo("TIPO")
        ident_nodo = Nodo(self.nombre)
        type_nodo = Nodo(self.tipo[0])
        if isinstance (self.tipo[1], list):
            if self.tipo[1][0]!=None:
                dim = Nodo("DIMENSION")
                dim.addNode(str(self.tipo[1][0]))
                tipo_nodo.addNode(dim)
        elif self.tipo[1]!=None:
            dim = Nodo("DIMENSION")
            dim.addNode(str(self.tipo[1]))
            tipo_nodo.addNode(dim) 
        id_nodo.addNode(ident_nodo)
        tipo_nodo.addNode(type_nodo)
        nuevo_nodo.addNode(id_nodo)
        nuevo_nodo.addNode(tipo_nodo)
        if self.exp != None:
            exp_nodo = Nodo("EXPRESION")
            exp_nodo.addNode(self.exp.dot())
            nuevo_nodo.addNode(exp_nodo)
        return nuevo_nodo