from parse.ast_node import ASTNode
from TAC.quadruple import *
from TAC.tac_enum import *
from parse.symbol_table import *


'''declaration  :     ID ID PORCENTAJE ROWTYPE PUNTOCOMA
                    | ID ID PUNTO ID PORCENTAJE TYPE PUNTOCOMA
                    | ID RECORD PUNTOCOMA
                    | ID constant_opt type collate_opt not_null_opt expression_opt PUNTOCOMA 
                    | ID ALIAS FOR DOLLAR ENTERO PUNTOCOMA'''
class Declaration(ASTNode):
    # Var declaration for plpgsql
    def __init__(self, name, is_constant, type_, allow_null, exp, aliasfor, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name
        self.exp = exp        
        self.alias = aliasfor #index of parameter alias
        self.type_ = type_
        self.graph_ref = graph_ref
        self.default = None
        #set the dafult values by type:
        if self.type_ in ['SMALLINT','INTEGER', 'BIGINT']:
            self.default = 0
        if self.type_ in ['DECIMAL', 'NUMERIC', 'REAL', 'DOUBLE', 'MONEY']:
            self.default = 0.0
        if self.type_ in ['CARACTER', 'VARCHAR', 'CHARACTER', 'CHAR', 'TEXT']:
            self.default = ''
        if self.type_ in ['BOOLEAN']:
            self.default = False                       

    def execute(self, table, tree):# this execute must return tac list
        super().execute(table, tree)
        #self.generate(table, tree)
        #return f'{self.name} declared'
    #for this test tree will contains the thre address code list
    #pay atention in the order to call genrate function for each childnode because it will affect the TAC list (order of eleents)
    def generate(self, table, tree):  
        this_tac = None
        if self.alias is None:
            #TODO:validate tacs len
            if self.exp is None:
                this_tac = Quadruple(None, str(self.default), None, self.name, OpTAC.ASSIGNMENT) #I put the word 'None' for TA python syntax to print the word None
            else:
                exp_tacs = self.exp.generate(table, tree)#should return the last quadruple generated                                
                this_tac = Quadruple(None,exp_tacs.res if isinstance(exp_tacs, Quadruple) else exp_tacs,None, self.name, OpTAC.ASSIGNMENT)
        else:
            this_tac = Quadruple(None, f'{getParamNameFormat()}{self.alias}', None, self.name, OpTAC.ASSIGNMENT)
        #now add this new TAC to the list
        tree.append(this_tac)
        return this_tac 

class DeclarationList(ASTNode):
    def __init__(self, initialObj, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.decList = []
        if initialObj:
            self.decList.append(initialObj)
        self.graph_ref = graph_ref

    def execute(self, table, tree):# this execute must return tac list
        super().execute(table, tree)
        self.generate(table, tree)
        return f'TAC genrated'

    def append(self, obj: Declaration):
        self.decList.append(obj)

    def generate(self, table, tree):
        tacs = []
        for i in self.decList:
            i.generate(table, tacs)
        print('***********This is the thre address code generated:*********')
        printL(tacs)
        #Do the optimization...        
        print('*****************Optimization code generated:***************')
        optimi = DoOptimization(tacs)        
        printL(optimi[0])
        print("RemovedItems:")
        printL(optimi[1])
        print('***************************TAC END**************************')
        #Do python code...


        return tree
