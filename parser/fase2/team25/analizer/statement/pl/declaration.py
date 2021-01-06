from analizer.abstract import instruction
from analizer.abstract.expression import TYPE
from analizer.symbol.environment import Environment
import analizer.symbol.c3dSymbols as SymbolTable
from analizer.statement.functions.call import FunctionCall
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
        self.tipo=self.tipo[0].casefold()
        try:
            TypeV=self.valor.execute(environment).type
            print('El tipo es: '+TypeV.name)
        except:
            instruction.semanticErrors.append(
                    ( "ERROR: 42P18: tipo de dato indeterminado en '%s'" %self.nombre,self.row)
            )
            return None
        try:
            self.valor=self.valor.value
        except:
            pass
        
        try:
            if 'primitive'==self.classType:
                if self.valor == None:
                    if 'integer' in self.tipo or 'bigint' in self.tipo:
                        self.valor=0
                    elif 'numeric' in self.tipo or 'double precision' in self.tipo or 'money' in self.tipo or 'decimal' in self.tipo:
                        self.valor=0.0
                    elif 'text' in self.tipo or 'varchar' in self.tipo or 'char' in self.tipo or 'varying' in self.tipo:
                        self.valor='\'\''
                    elif 'boolean' in self.tipo:
                        self.valor=False
                    elif 'timestamp' in self.tipo:
                        self.valor=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    elif 'date' in self.tipo:
                        self.valor=datetime.now().strftime("%Y-%m-%d")
                    elif 'time' in self.tipo:
                        self.valor=datetime.now().strftime("%H:%M:%S")
                    else:
                        pass
                else:
                    if 'text' in self.tipo or 'varchar' in self.tipo or 'char' in self.tipo or 'varying' in self.tipo:
                        if TypeV==TYPE.STRING:
                            self.valor='\''+self.valor+'\''
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print("ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre)
                            return None
                            #return error de tipo
                    elif 'timestamp' in self.tipo:
                        if TypeV==TYPE.TIMESTAMP:
                            self.valor='\''+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\''
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print("ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre)
                            return None
                    elif 'date' in self.tipo:
                        if TypeV==TYPE.DATE:
                            self.valor='\''+datetime.now().strftime("%Y-%m-%d")+'\''
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print("ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre)
                            return None
                    elif 'time' in self.tipo:
                        if TypeV==TYPE.TIME:
                            self.valor='\''+datetime.now().strftime("%H:%M:%S")+'\''
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print("ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre)
                            return None
                    elif 'integer' in self.tipo or 'bigint' in self.tipo:
                        if TypeV==TYPE.NUMBER:
                            if not type(self.valor)==float:
                                self.valor=self.valor
                            else:
                                instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                                )
                                print("ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre)
                                return None
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print("ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre)
                            return None
                    elif 'numeric' in self.tipo or 'double precision' in self.tipo or 'money' in self.tipo or 'decimal' in self.tipo:
                        if type(self.valor)==float:
                            self.valor=self.valor
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print("ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre)
                            return None
                    elif 'boolean' in self.tipo:
                        if TypeV==TYPE.BOOLEAN:
                            self.valor=self.valor
                        else:
                            instruction.semanticErrors.append(
                                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
                            )
                            print("ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre)
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
                else:    
                    newTemp=self.valor.generate3d(environment,instanciaAux)
                    callValue=self.valor.execute(environment).value
                    SymbolTable.add_symbol(self.nombre,TypeV,callValue,self.row,self.column,None)
                    instanciaAux.addToCode(f'\t{self.nombre} =  {newTemp}')
        except:
            instruction.semanticErrors.append(
                ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre,self.row)
            )
            print("ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.nombre)
            return None