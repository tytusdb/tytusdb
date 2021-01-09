from analizer.statement.expressions.primitive import Primitive
from analizer.abstract import instruction
import analizer.symbol.c3dSymbols as SymbolTable
from analizer.statement.functions.call import FunctionCall
from analizer.statement.expressions.identifiers import Identifiers
from analizer.abstract.expression import TYPE
from analizer.statement.pl.instruccionesF1 import F1
from analizer.reports.Nodo import Nodo
from analizer.reports.AST import AST
import analizer.symbol.c3dSymbols as SymbolTable
from analizer.abstract import expression

class Asignacion(instruction.Instruction):
    def __init__(self, identificador, expresion, row , column):
        instruction.Instruction.__init__(self, row , column)
        self.identificador = identificador
        self.expresion = expresion
        self.classType=str(self.expresion.__class__.__name__).casefold()
        
    def generate3d(self, environment, instanciaAux):
        name = None
        try:
            name,tipo,value = SymbolTable.search_symbol(self.identificador)
        except:
            instruction.semanticErrors.append(
                ( "ERROR: con variable '%s' en asignacion" %self.identificador,self.row)
            )
        if  name != None:
            newTemp = self.expresion.generate3d(environment,instanciaAux)
            instanciaAux.addToCode(f'\t{self.identificador} =  {newTemp}')
            
    def dot(self):
        nuevo_nodo = Nodo("ASIGNACION")
        identificador = Nodo("ID")
        expresion = Nodo("EXPRESION")
        id = Nodo(self.identificador)
        identificador.addNode(id)
        expresion.addNode(self.expresion.dot())
        nuevo_nodo.addNode(identificador)
        nuevo_nodo.addNode(expresion)
        return nuevo_nodo   