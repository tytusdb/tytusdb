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
        self.returntype = returntype #if is None this instance repreents a Store Procedure
        self.body = body
        self.graph_ref = graph_ref

    def execute(self, table, tree):# this execute must return tac list
        super().execute(table, tree)
        self.generate(table, tree)
        if self.returntype is None:
            return f'Store Procedure -{self.name}- created.'
        else:            
            return f'Function -{self.name}- created.'
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
        tac_file_name = ''
        sym = None
        if self.returntype is None:
            tac_file_name = f'{currDB.name}_proc_{self.name}'
            sym = ProcedureSymbol(currDB.id, self.name, labelname, paramCounter, tac_file_name )
        else:
            tac_file_name = f'{currDB.name}_func_{self.name}'
            sym = FunctionSymbol(currDB.id, self.name, labelname, paramCounter, tac_file_name )
        table.add(sym)        
        #write File.py
        Save_TAC_obj(tac_file_name, tree)
        if self.returntype is None:
            return f'Store Procedure -{self.name}- created.'
        else:
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
        if isinstance(self.func_return, Return):
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


class FuncCall(ASTNode):
    def __init__(self, func_name, param_list, is_fun_proc: SymbolType, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.func_name = func_name
        self.param_list = param_list     
        self.graph_ref = graph_ref
        self.qlist = None
        self.tempTSymbol = None
        self.is_fun_proc = is_fun_proc

    def execute(self, table, tree):
        super().execute(table, tree)
        #Search in table symbol
        #Load File
        #Execute file
        #return value
        if isinstance(table,SymbolType):
            funcObj = table.get(self.func_name, self.is_fun_proc)
        else:
            from grammarReview import ST
            funcObj = ST.get(self.func_name, self.is_fun_proc)
        tac_modue = __import__(funcObj.tac_file_name)
        from importlib import reload
        reload(tac_modue)
        
        #set parms to pseudo tack? ore heap? i don't now how is it
        #TODO maybe some type validation ?¿        

        if isinstance(self.param_list, list):
            if len(self.param_list) != funcObj.number_params:
                raise Error(self.line, self.column, ErrorType.SEMANTIC,f'La cantidad de parametros propocionada no coincide con la cantidad de parametros definidos en ({funcObj.number_params})')
            
            #revert the order             
            self.param_list.reverse()
            for p in self.param_list:
                paramval = p.execute(table, tree)
                tac_modue.push(paramval)
            self.param_list.reverse()
        tac_modue.all_code()
        #my_module = importlib.import_module('os.path')
        retval = None
        #The stack structure is for the retuened value firs we get the 0 vale next the returned values 
        #next the number 1 if a param inth pos 1 was sendes by out option same way with the otther parameter
        #lets pop it!!! tneee better use a loop jejeje
        poped = tac_modue.pop()
        isval = True
        paramval = None
        paramIndex = -1
        while poped is not None:
            if isval:
                paramval = poped
            else:
                paramIndex = poped
                #TODO: this asignation is not valid look for annother vay
                #self.param_list[paramIndex] = paramval            
            if paramIndex == 0:
                retval = paramval
                return retval
            isval = not isval 
            poped = tac_modue.pop()   
        return retval
    
    #call this function when the Func call exist in the column retuenes of a query
    def setQueryTable(self, qlist):
        self.qlist=qlist

    def setTepTableSymbol(self, st:TableSymbol):
        tempTSymbol = st

    def generate(self, table, tree):
        return 'No generate code is avaible for FuncCall'

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


class DropFunction(ASTNode):
    def __init__(self, name_function, if_exists, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name_function 
        self.if_exists = if_exists  
        self.graph_ref = graph_ref
        self.line = line
        self.column = column

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)
        result = table.drop_function(result_name)
        if result:
            return "Function \'" + str(result_name) + "\' has been dropped."
        if not result and self.if_exists:
            return "Tried to drop Function \'" + str(result_name) + " \'it does not exist."
        elif not result :
             raise Error(self.line, self.column, ErrorType.RUNTIME, '42883: function_does_not_exists')
        


    def generate(self, table, tree):
        super().generate(table, tree)
        result_name = self.name.generate(table, tree)
        if self.if_exists:
            return Quadruple(None, 'exec_sql', f'\'DROP FUNCTION  IF EXISTS {result_name};\'', generate_tmp(), OpTAC.CALL)
        else:
            return Quadruple(None, 'exec_sql', f'\'DROP FUNCTION {result_name};\'', generate_tmp(), OpTAC.CALL)

class DropProcedure(ASTNode):
    def __init__(self, name_procedure, if_exists, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name_procedure 
        self.if_exists = if_exists  
        self.graph_ref = graph_ref
        self.line = line
        self.column = column

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)
        result = table.drop_procedure(result_name)
        if result:
            return "Procedure \'" + str(result_name) + "\' has been dropped."
        if not result and self.if_exists:
            return "Tried to drop Procedure \'" + str(result_name) + " \'it does not exist."
        elif not result :
             raise Error(self.line, self.column, ErrorType.RUNTIME, '42883: procedure_does_not_exists')
        


    def generate(self, table, tree):
        super().generate(table, tree)
        result_name = self.name.generate(table, tree)
        if self.if_exists:
            return Quadruple(None, 'exec_sql', f'\'DROP PROCEDURE  IF EXISTS {result_name};\'', generate_tmp(), OpTAC.CALL)
        else:
            return Quadruple(None, 'exec_sql', f'\'DROP PROCEDURE {result_name};\'', generate_tmp(), OpTAC.CALL)


