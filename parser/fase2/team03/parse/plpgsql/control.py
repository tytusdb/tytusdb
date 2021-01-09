from parse.ast_node import ASTNode
from TAC.quadruple import *
from TAC.tac_enum import *
from parse.symbol_table import *


class IfNode(ASTNode):    
    #'''stm_if   : IF condition THEN   if_inst   elseif_opt  else_opt  END IF '''
    def __init__(self, condition, then_block, elif_block, else_block , line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.condition = condition
        self.then_block = then_block
        self.elif_block = elif_block #maybe annother IFNode
        self.else_block = else_block #maybe annother IFNode withot conditions
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        #self.generate(table, [])
        #return f'If node not executable, generating three address code...'
    
    def generate(self, table, tree):
        # 1 instance a list for TACS
        # 2 get tacs from if conditional and body , optimize it
        # 3 add funtion to Symbol table
        # 4 Create a Label for ths function
        # 5 cretate or append file.py for the frunction         
        tac_if_cond = []
        tac_body = [] #Statements1 
        tac_elif_block = []
        tac_else_block = []        
        
        label_true = generate_label()#L1
        label_false = generate_label() # L2     goto other else if adn else blocks
        label_end_block = generate_label() #L3
        
        lastTAC = self.condition.generate(table, tac_if_cond)# a < b and x + y == 0
        IFFF = Quadruple(None, lastTAC.res if isinstance(lastTAC,Quadruple) else lastTAC, None, label_true, OpTAC.CONDITIONAL)# if a<b goto ...
        gotoL2 = Quadruple(None, label_false, None, None, OpTAC.GOTO) #goto L2
        gotoL3 = Quadruple(None, label_end_block, None, None, OpTAC.GOTO)#goto L3
        L1 = Quadruple(None, label_true, None, None, OpTAC.LABEL)
        L2 = Quadruple(None, label_false, None, None, OpTAC.LABEL)
        L3 = Quadruple(None, label_end_block, None, None, OpTAC.LABEL)
        #S1:
        if isinstance(self.then_block, list):#each inner sentence
            for i in self.then_block:
                i.generate(table, tac_body)

        #TODO: implement...
        if isinstance(self.elif_block, IfNode):
            self.elif_block.generate(table, tac_elif_block)#take Quedruple for Ln value

        if isinstance(self.else_block, ElseNode):
            self.else_block.generate(table, tac_else_block)#take Quedruple for Ln value

        tree += tac_if_cond
        tree.append(IFFF)
        tree.append(gotoL2)
        tree.append(L1)
        tree += tac_body
        tree.append(gotoL3)
        tree.append(L2)
        #here elseif .... else -optional
        if len(tac_elif_block)>0:
            tree += tac_elif_block
        if len(tac_else_block)>0:
            tree += tac_else_block
        #TODO print all en block labels
        tree.append(L3)
        
        return L3

class ElseNode(ASTNode):
    def __init__(self, else_block , line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.else_block = else_block
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        #self.generate(table, [])
        return f'Else node not executable.'
    
    def generate(self, table, tree):
        if isinstance(self.else_block, list):#each inner sentence
            for i in self.else_block:
                i.generate(table, tree)



class CaseNode(ASTNode):    
    def __init__(self, condition, when_block, when_list_block, else_block , line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.condition = condition
        self.when_block = when_block
        self.when_list_block = when_list_block #maybe annother CaseNode
        self.else_block = else_block #maybe annother CaseNode withot conditions
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        pass
    
    def generate(self, table, tree):   
        tac_if_cond = []
        tac_body = [] #Statements1 
        tac_when_list_block = []
        tac_else_block = []        
        
        label_true = generate_label()#L1
        label_false = generate_label() # L2     goto other else if adn else blocks
        label_end_block = generate_label() #L3
        
        lastTAC = self.condition.generate(table, tac_if_cond)# a < b and x + y == 0
        IFFF = Quadruple(None, lastTAC.res if isinstance(lastTAC,Quadruple) else lastTAC, None, label_true, OpTAC.CONDITIONAL)# if a<b goto ...
        gotoL2 = Quadruple(None, label_false, None, None, OpTAC.GOTO) #goto L2
        gotoL3 = Quadruple(None, label_end_block, None, None, OpTAC.GOTO)#goto L3
        L1 = Quadruple(None, label_true, None, None, OpTAC.LABEL)
        L2 = Quadruple(None, label_false, None, None, OpTAC.LABEL)
        L3 = Quadruple(None, label_end_block, None, None, OpTAC.LABEL)
        #S1:
        if isinstance(self.when_block, list):#each inner sentence
            for i in self.when_block:
                i.generate(table, tac_body)

        #TODO: implement...
        if isinstance(self.when_list_block, IfNode):
            self.when_list_block.generate(table, tac_when_list_block)#take Quedruple for Ln value

        if isinstance(self.else_block, ElseNode):
            self.else_block.generate(table, tac_else_block)#take Quedruple for Ln value

        tree += tac_if_cond
        tree.append(IFFF)
        tree.append(gotoL2)
        tree.append(L1)
        tree += tac_body
        tree.append(gotoL3)
        tree.append(L2)
        #here whens_list_block .... else -optional
        if len(tac_when_list_block)>0:
            tree += tac_when_list_block
        if len(tac_else_block)>0:
            tree += tac_else_block
        #TODO print all en block labels
        tree.append(L3)
        
        return L3