from parse.ast_node import ASTNode
from parse.symbol_table import *




class IndexPG(ASTNode):    
    def __init__(self,name, table, lista=[]  , line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name =name
        self.table = table
        self.lista = lista
        self.graph_ref = graph_ref
 

    def execute(self, table, tree):
        super().execute(table, tree)
        obj = IndexSymbol(self.name,self.table,self.lista,table.get_current_db())
        table.add(obj)
        return 'Indice Guardado'
    
    def generate(self, table, tree):

        parameter ='' 

        for par in self.lista:
            if len(self.lista) > 1 and  len(self.lista) != 0 :
                parameter = parameter + par + ","
            else:
                parameter = parameter + par
               
        temp = len(parameter)
        if parameter[temp - 1] == ",":
            parameter = parameter[:temp - 1]
        
        k = 'CREATE INDEX 'self.name + ' ON '+ self.table '( '+parameter+' );'
        return k