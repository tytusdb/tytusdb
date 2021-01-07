from parse.ast_node import ASTNode
from TAC.quadruple import *
from TAC.tac_enum import *
from parse.symbol_table import *

class Function(ASTNode):    
    # Function declaration for plpgsql
    #'''stm_create_function : CREATE FUNCTION ID PARA list_param_function_opt PARC RETURNS type as_opt stm_begin'''
    def __init__(self, name, parameters, returntype, body , line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name
        self.parameters = parameters
        self.returntype = returntype
        self.body = body
        self.graph_ref = graph_ref

    def execute(self, table, tree):# this execute must return tac list
        super().execute(table, tree)
        self.generate(table, tree)
        return f'Function {self.name} created.'
    #for this test tree will contains the thre address code list
    #pay atention in the order to call genrate function for each childnode because it will affect the TAC list (order of eleents)
    def generate(self, table, tree):  
        # 1 instance a list for TACS
        # 2 get tacs from parameters and body , optimize it
        # 3 add funtion to Symbol table
        # 4 Create a Label for ths function
        # 5 cretate or append file.py for the frunction         
        tac_parameters = []
        tac_body = []
        #TODO: implemet ->
        #self.parameters.generate(table, tac_parameters)
        self.body.generate(table, tac_body)
        
        #now add this new TAC to the list
        labelname = generate_label()
        this_tac = Quadruple(None, labelname, None, None, OpTAC.LABEL)
        endGoto = Quadruple(None, 'exit', None, None, OpTAC.GOTO)
        tree = [this_tac]+tac_body+[endGoto]        
        #add this functi on to ST
        currDB = table.get_current_db()
        #TODO: set params
        sym = FunctionSymbol(currDB.id, self.name, labelname, 0)
        table.add(sym)        
        #write File.py
        Save_TAC_obj(f'{currDB.name}_func_{self.name}', tree)
        
        return f'Function -{self.name}- created.'


class FunctionBody(ASTNode):    
    # Function declaration for plpgsql
    #'''stm_begin   : declare_opt BEGIN statements_begin    exception_opt  return_opt   END  if_opt '''
    def __init__(self, var_declara, func_statements, func_exception, func_return , line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.var_declara = var_declara
        self.func_statements = func_statements
        self.func_exception = func_exception
        self.func_return = func_return        
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)        
        return f'Execution of AST FunctionBody not implemented'
    
    def generate(self, table, tree):
        if self.var_declara: 
            self.var_declara.generate(table, tree)
        for s in self.func_statements:
            s.generate(table, tree)
        #TODO: Implement this.
        #self.func_exception.generate(self, table, tree)
        #self.func_return.generate(self, table, tree)

class Parameter(ASTNode):
    def __init__(self, param_name, param_mode, param_type, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.param_name = param_name #str
        self.param_mode = param_mode #ParamMode
        self.param_type = param_type #Typedef   
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)        
        return f'Exeute from param node not mplemented.'
    
    def generate(self, table, tree): 
        pass

class ParamMode(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val  # token name: IN, OUT INOUT        
        self.graph_ref = graph_ref
    
    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val.upper()   

    def generate(self, table, tree):
        super().generate(table, tree)
        return self.val.upper()



class Parameters(ASTNode):
    def __init__(self, name, parameters, returntype, body , line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name
        self.parameters = parameters if parameters else []
        self.returntype = returntype
        self.body = body
        self.graph_ref = graph_ref

    def execute(self, table, tree):# this execute must return tac list
        super().execute(table, tree)
        self.generate(table, tree)
        return f'Function {name} created.'
    #for this test tree will contains the thre address code list
    #pay atention in the order to call genrate function for each childnode because it will affect the TAC list (order of eleents)
    def generate(self, table, tree): 
        pass