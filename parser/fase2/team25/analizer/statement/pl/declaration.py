from analizer.abstract import instruction
from analizer.abstract.expression import TYPE
from analizer.symbol.environment import Environment
import analizer.symbol.c3dSymbols as SymbolTable
from analizer.statement.functions.call import FunctionCall
from analizer.statement.expressions.identifiers import Identifiers
from datetime import datetime

class Declaration(instruction.Instruction):
    def __init__(self,nombre,tipo,valor,row,column):
        instruction.Instruction.__init__(self,row,column)
        self.nombre=nombre
        self.tipo=tipo
        self.valor=valor
        self.row=row
        self.column=column
        self.classType=str(self.valor.__class__.__name__).casefold()
    def execute(self,environment):
        pass
    def generate3d(self,environment,instanciaAux):
        tipo=self.tipo[0].casefold()
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
            print("Error nuevo valor")
            pass
            print(self.valor,tipo)
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
                print("Nuevo valor:",self.valor)
                if isinstance(self.valor,FunctionCall):
                    callValue=self.valor.execute(environment).value
                    SymbolTable.add_symbol(self.nombre,TypeV,callValue,self.row,self.column,None)
                    instanciaAux.addToCode(f'\t{self.nombre} =  {callValue}')
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