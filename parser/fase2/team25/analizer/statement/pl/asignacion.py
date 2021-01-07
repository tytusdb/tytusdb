from analizer.statement.expressions.primitive import Primitive
from analizer.abstract import instruction
import analizer.symbol.c3dSymbols as SymbolTable
from analizer.statement.functions.call import FunctionCall
from analizer.statement.expressions.identifiers import Identifiers
from analizer.abstract.expression import TYPE
from analizer.statement.pl.instruccionesF1 import F1


class Asignacion(instruction.Instruction):
    def __init__(self, identificador, expresion, row , column):
        instruction.Instruction.__init__(self, row , column)
        self.identificador = identificador
        self.expresion = expresion
        self.classType=str(self.expresion.__class__.__name__).casefold()
        
    def generate3d(self, environment, instanciaAux):
        try:
            name,tipo,value = SymbolTable.search_symbol(self.identificador)

            if isinstance(self.expresion, F1):
                newTemp = self.expresion.generate3d(environment,instanciaAux)
                instanciaAux.addToCode(f'\t{self.identificador} =  {newTemp}')

                if tipo == TYPE.NUMBER: value = 1
                elif tipo == TYPE.BOOLEAN: value = False
                else: value = ""
                SymbolTable.add_symbol(self.identificador,tipo,value,self.row,self.column,None)
                return

            try:
                TypeV=self.expresion.execute(environment).type
            except:
                instruction.semanticErrors.append(
                        ( "ERROR: 42P18: tipo de dato indeterminado en '%s'" %self.identificador,self.row)
                )
                return None

            if TypeV != tipo:
                instruction.semanticErrors.append(
                    ( "ERROR: 42804: discorcondancia entre los tipos de datos en '%s'" %self.identificador,self.row)
                )

            try:
                if not isinstance(self.expresion, Identifiers):
                    value=self.expresion.value
            except:
                pass
            
            if isinstance(self.expresion, Primitive):
                SymbolTable.add_symbol(self.identificador,TypeV,value,self.row,self.column,None)
                instanciaAux.addToCode(f'\t{self.identificador} =  {self.expresion.value}')
            elif not self.classType == None:
                if isinstance(self.expresion,FunctionCall):
                    callValue=self.expresion.execute(environment).value
                    SymbolTable.add_symbol(self.identificador,TypeV,callValue,self.row,self.column,None)
                    instanciaAux.addToCode(f'\t{self.identificador} =  {callValue}')
                else:    
                    newTemp=self.expresion.generate3d(environment,instanciaAux)
                    callValue=self.expresion.execute(environment).value
                    if isinstance(self.expresion, Identifiers):
                        callValue=self.expresion.name
                    SymbolTable.add_symbol(self.identificador,TypeV,callValue,self.row,self.column,None)
                    instanciaAux.addToCode(f'\t{self.identificador} =  {newTemp}')
        except:
            instruction.semanticErrors.append(
                ( "ERROR: la variable '%s' no se ha declarado" %self.identificador,self.row)
            )