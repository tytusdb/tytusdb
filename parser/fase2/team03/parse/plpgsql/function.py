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
        
        paramCounter = 0
        #gen tac for func parameters
        if isinstance(self.parameters, list):            
            for p in self.parameters:
                p.setParamIndex(paramCounter + 1)
                p.generate(table, tac_parameters)
                paramCounter +=1
        
        self.body.generate(table, tac_body)
        
        #now add this new TAC to the list
        labelname = generate_label()
        this_tac = Quadruple(None, labelname, None, None, OpTAC.LABEL)
        endGoto = Quadruple(None, 'exit', None, None, OpTAC.GOTO)
        tree = [this_tac] + tac_parameters + tac_body+[endGoto]
        tree.append(Quadruple(None,'exit',None,None,OpTAC.LABEL))
        #add this functi on to ST
        currDB = table.get_current_db()
        #TODO: set params
        sym = FunctionSymbol(currDB.id, self.name, labelname, paramCounter)
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
        tac_declaraciones = []
        tac_sentancias = []
        tac_return = []
        tec_exception = []
        if isinstance(self.var_declara, list): 
            for d in self.var_declara:
                d.generate(table, tac_declaraciones)

        if isinstance(self.func_statements, list):
            for s in self.func_statements:
                s.generate(table, tac_sentancias)

        #TODO: Implement this.
        #self.func_exception.generate(table, tree)
        self.func_return.generate(table, tac_return)
        #union all TAC arrarys
        ##tree = tree + tac_declaraciones + tac_sentancias this not work by ref ue extend() instead
        tree.extend(tac_declaraciones)
        tree.extend(tac_sentancias)
        tree.extend(tac_return)

class Parameter(ASTNode):
    def __init__(self, param_name, param_mode, param_type, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.param_name = param_name #str
        self.param_mode = param_mode #ParamMode
        self.param_type = param_type #Typedef   
        self.graph_ref = graph_ref
        self.param_index = 0 #set out of the contructior when you have all li of parameters starts with 1

    def execute(self, table, tree):
        super().execute(table, tree)        
        return f'Exeute from param node not mplemented.'
    
    def generate(self, table, tree): 
        #write declaration with param names and add pop() to assign value
        if self.param_index == 0:
            raise Exception('For generate TAC object first set a parmeter array index for the function -Paramater Class-')
        result = Quadruple(None, None, None, self.param_name, OpTAC.POP)
        if self.param_name is None or self.param_name == '':
            result.res = f'{getParamNameFormat()}{self.param_index}'
        if isinstance(tree, list):
            tree.append(result)            
        return result

    def setParamIndex(self, index_: int):
        self.param_index = index_

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


class Return(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp      
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        #self.generate(table, tree)
        return self.exp.execute(table, tree)
    
    def generate(self, table, tree):
        last_tac = self.exp.generate(table, tree)
        pushID = Quadruple(None, '0', None, None, OpTAC.PUSH)#push zero value for ndicate to caller that the next value in stack is returned vaue
        push = Quadruple(None, last_tac.res if(isinstance(last_tac,Quadruple)) else last_tac, None, None, OpTAC.PUSH)
        gotoExit = Quadruple(None, 'exit', None, None, OpTAC.GOTO)
        tree.append(pushID)
        tree.append(push)
        tree.append(gotoExit)


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