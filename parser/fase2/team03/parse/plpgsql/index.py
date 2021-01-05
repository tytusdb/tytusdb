from parse.ast_node import ASTNode
from parse.symbol_table import *




class IndexPG(ASTNode):    
    def __init__(self,unique, name, table, lista , line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.unique =unique
        self.name =name
        self.table = table
        self.lista = lista
        self.graph_ref = graph_ref
 

    def execute(self, table, tree):
        super().execute(table, tree)        
        obj = IndexSymbol(self.name,self.table,table.get_current_db(),self.lista)
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
        
        k = ''
        return k


class IndexAtributo(ASTNode):
    def __init__(self,exp1, ident, par1,par2,par3, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.ident = ident
        self.par1 = par1
        self.par2 = par2
        self.par3 = par3
        self.graph_ref=graph_ref
        
    def IndexSTR():
        if self.exp1 != None:
            return f'{self.exp1.generate(table, tree)}'
        if self.par1 == None:
            return f'{self.ident} '
        if self.par1 != None and self.par2 ==None:
            return f'{self.ident} {self.par1} '
        if self.par2 != None and self.par3 != None:
            return f'{self.ident} {self.par1} {self.par2} {self.par3} '

        

    def execute(self, table, tree):
        super().execute(table, tree)
        
        if self.exp1 != None:
            return f'{self.exp1.generate(table, tree)}'
        if self.par1 == None:
            return f'{self.ident} '
        if self.par1 != None and self.par2 ==None:
            return f'{self.ident} {self.par1} '
        if self.par2 != None and self.par3 != None:
            return f'{self.ident} {self.par1} {self.par2} {self.par3} '


    def generate(self, table, tree):
        super().generate(table, tree)
        if self.exp1 != None:
            return f'{self.exp1.generate(table, tree)}'
        if self.par1 == None:
            return f'{self.ident} '
        if self.par1 != None and self.par2 ==None:
            return f'{self.ident} {self.par1} '
        if self.par2 != None and self.par3 != None:
            return f'{self.ident} {self.par1} {self.par2} {self.par3} '
