from .executeOptimization_result import *
from prettytable import PrettyTable


class Optimization():

    def __init__(self, rule: int, line: int, before: str, after: str, description: str, type_):
        self.rule = rule
        self.line = line
        self.before = before
        self.after = after
        self.description = description
        self.type_ = type_ #0 -> Delete, 1 -> Modify


class Line_data():

    def __init__(self, line_number: int, text_: str, spaces_and_tabs: str, number_of_arguments: int, variable: str, operation: str, argument1: str, operator: str, argument2: str, valid: bool, remove: bool):
        #Basic information
        self.line_number = line_number
        self.text_ = text_
        self.spaces_and_tabs = spaces_and_tabs
        #Specific information
        self.number_of_arguments = number_of_arguments
        self.variable = variable
        self.operation = operation
        self.argument1 = argument1
        self.operator = operator
        self.argument2 = argument2
        self.valid = valid
        self.remove = remove


class executeOptimization():

    def optimize(self, input_text): 
        
        split_input_text = input_text.split("\n")

        #getting statements and assignments
        statements_and_assignments = self.get_statements_and_assignments(split_input_text)

        optimizations = []

        #applying optimization rules
        self.rule1(statements_and_assignments, optimizations)
        self.rule8(statements_and_assignments, optimizations)
        self.rule9(statements_and_assignments, optimizations)
        self.rule10(statements_and_assignments, optimizations)
        self.rule11(statements_and_assignments, optimizations)
        self.rule12(statements_and_assignments, optimizations)
        self.rule13(statements_and_assignments, optimizations)
        self.rule14(statements_and_assignments, optimizations)
        self.rule15(statements_and_assignments, optimizations)
        self.rule16(statements_and_assignments, optimizations)
        self.rule17(statements_and_assignments, optimizations)
        self.rule18(statements_and_assignments, optimizations)

        #getting c3d optimized
        c3d_optimized: str = ""
        i = 0
        while i < len(statements_and_assignments):
            if  statements_and_assignments[i].remove == False:
                c3d_optimized += str(statements_and_assignments[i].spaces_and_tabs) + str(statements_and_assignments[i].text_)
                if (i+1)!=len(statements_and_assignments):
                    c3d_optimized += "\n"
            i += 1

        #getting print optimization table
        x = PrettyTable(["Number", "Rule", "Line", "Before", "After", "Description"])
        i = 0
        while i < len(optimizations):
            x.add_row([(i+1), str(optimizations[i].rule), str((optimizations[i].line+1)), str(optimizations[i].before), str(optimizations[i].after), str(optimizations[i].description)])
            i += 1
        print_ = x.get_string(title="Optimization Table")

        executeOptimization_result_ = executeOptimization_result(c3d_optimized, print_)

        return executeOptimization_result_


    def get_statements_and_assignments(self, split_input_text):

        statements_and_assignments = []
        
        i = 0
        while i<len(split_input_text):
            
            line_number = i#line
            spaces_and_tabs: str = ""
            number_of_tabs = 0
            number_of_arguments = None
            variable = None
            operation = None
            argument1 = None
            operator = None
            argument2 = None
            
            spaces_and_tabs = self.get_spaces_and_tabs(split_input_text[i])

            split_input_text[i] = split_input_text[i].strip()

            if ("=" in split_input_text[i]) == True:
                split_input_text_1 = split_input_text[i].split("=")
                a = 0
                while a < len(split_input_text_1):
                    split_input_text_1[a] = split_input_text_1[a].strip()
                    a += 1

                #arithmetic
                if len(split_input_text_1) == 2:
                    operation = "="#operation
                    variable = split_input_text_1[0]#variable
                    variable = variable.strip()
                    
                    #binary
                    if ("+" in split_input_text_1[1])==True:
                        operator = "+"#operator
                    elif ("-" in split_input_text_1[1])==True:
                        operator = "-"#operator
                    elif ("*" in split_input_text_1[1])==True:
                        operator = "*"#operator
                    elif ("/" in split_input_text_1[1])==True:
                        operator = "/"#operator
                    if operator != None:
                        split_input_text_2 = split_input_text_1[1].split(operator)
                        b = 0
                        while b < len(split_input_text_2):
                            split_input_text_2[b] = split_input_text_2[b].strip()
                            b += 1
                        if len(split_input_text_2) == 2:
                            argument1 = split_input_text_2[0]#argument1
                            argument1 = argument1.strip()
                            argument2 = split_input_text_2[1]#argument2
                            argument2 = argument2.strip()

                    #unary
                    else:
                        argument1 = split_input_text_1[1]#argument1
                        argument1 = argument1.strip()

                    
            if line_number!=None and variable!=None and operation!=None and argument1!=None and operator!=None and argument2!=None:
                number_of_arguments=2
                operation_ = Line_data(line_number, split_input_text[i], spaces_and_tabs, number_of_arguments, variable, operation, argument1, operator, argument2, True, False)
                statements_and_assignments.append(operation_)

            elif line_number!=None and variable!=None and operation!=None and argument1!=None:
                number_of_arguments=1
                operation_ = Line_data(line_number, split_input_text[i], spaces_and_tabs, number_of_arguments, variable, operation, argument1, operator, argument2, True, False)
                statements_and_assignments.append(operation_)

            else:
                operation_ = Line_data(line_number, split_input_text[i], spaces_and_tabs, None, None, None, None, None, None, False, False)
                statements_and_assignments.append(operation_)

            i += 1

        return statements_and_assignments


    def get_spaces_and_tabs(self, input_text):
        spaces_and_tabs: str = ""
        i: int = 0
        while (i<len(input_text)) and (input_text[i]==" " or input_text[i]=="\t"):
            spaces_and_tabs += input_text[i]
            i += 1
        return spaces_and_tabs


    def rule1(self, statements_and_assignments, optimizations):
        i = 0
        while i<len(statements_and_assignments):
            data_one = statements_and_assignments[i]
            if data_one.valid == True and data_one.remove == False and data_one.number_of_arguments == 1:
                    j = i + 1
                    while j<len(statements_and_assignments):
                        data_two = statements_and_assignments[j]
                        if data_two.valid == True and data_two.remove == False and data_two.number_of_arguments == 1:
                            if data_one.variable == data_two.argument1 and data_one.argument1 == data_two.variable:
                                before = str(data_one.variable) + str(data_one.operation) + str(data_one.argument1)
                                before += "\n" + str(data_two.variable) + str(data_two.operation) + str(data_two.argument1)
                                after = str(data_one.variable) + str(data_one.operation) + str(data_one.argument1)
                                description = "Line " + str((data_two.line_number+1)) + " deleted"
                                optimization_ = Optimization(1, data_one.line_number, before, after, description, 0)
                                optimizations.append(optimization_)
                                data_two.remove = True #equivalent to delete
                        j += 1
            i += 1

    def rule8(self, statements_and_assignments, optimizations):
        self.rule_8_9_10_11(statements_and_assignments, optimizations, "+", "0", 8)

    def rule9(self, statements_and_assignments, optimizations):
        self.rule_8_9_10_11(statements_and_assignments, optimizations, "-", "0", 9)

    def rule10(self, statements_and_assignments, optimizations):
        self.rule_8_9_10_11(statements_and_assignments, optimizations, "*", "1", 10)

    def rule11(self, statements_and_assignments, optimizations):
        self.rule_8_9_10_11(statements_and_assignments, optimizations, "/", "1", 11)

    def rule_8_9_10_11(self, statements_and_assignments, optimizations, operator_condition: str, argument2_condition, rule: int):
        i = 0
        while i<len(statements_and_assignments):
            data = statements_and_assignments[i]
            if data.valid == True and data.remove == False and data.number_of_arguments == 2:
                variable = data.variable
                operation = data.operation
                argument1 = data.argument1
                operator = data.operator
                argument2 = data.argument2
                if operation == "=" and variable == argument1 and operator == operator_condition and argument2 == argument2_condition:
                    before = str(variable) + str(operation) + str(argument1) + str(operator) + str(argument2) 
                    after = ""
                    description = "Line " + str((data.line_number+1)) + " deleted"
                    optimization_ = Optimization(rule, data.line_number, before, after, description, 0)
                    optimizations.append(optimization_)
                    data.remove = True #equivalent to delete
            i += 1

    def rule12(self, statements_and_assignments, optimizations):
        self.rule_12_13_14_15(statements_and_assignments, optimizations, "+", "0", 12)

    def rule13(self, statements_and_assignments, optimizations):
        self.rule_12_13_14_15(statements_and_assignments, optimizations, "-", "0", 13)

    def rule14(self, statements_and_assignments, optimizations):
        self.rule_12_13_14_15(statements_and_assignments, optimizations, "*", "1", 14)

    def rule15(self, statements_and_assignments, optimizations):
        self.rule_12_13_14_15(statements_and_assignments, optimizations, "/", "1", 15)

    def rule_12_13_14_15(self, statements_and_assignments, optimizations, operator_condition: str, argument2_condition, rule: int):
        i = 0
        while i<len(statements_and_assignments):
            data = statements_and_assignments[i]
            if data.valid== True and data.remove == False and data.number_of_arguments == 2:
                variable = data.variable
                operation = data.operation
                argument1 = data.argument1
                operator = data.operator
                argument2 = data.argument2
                if operation == "=" and variable != argument1 and operator == operator_condition and argument2 == argument2_condition:
                    before = str(variable) + str(operation) + str(argument1) + str(operator) + str(argument2)
                    after = str(variable) + str(operation) + str(argument1)
                    description = "Line " + str((data.line_number+1)) + " modified"
                    optimization_ = Optimization(rule, data.line_number, before, after, description, 1)
                    optimizations.append(optimization_)
                    data.text_ = after
            i += 1

    def rule16(self, statements_and_assignments, optimizations):
        i = 0
        while i<len(statements_and_assignments):
            data = statements_and_assignments[i]
            if data.valid == True and data.remove == False and data.number_of_arguments == 2:
                variable = data.variable
                operation = data.operation
                argument1 = data.argument1
                operator = data.operator
                argument2 = data.argument2
                if operation == "=" and operator == "*" and argument2 == "2":
                    before = str(variable) + str(operation) + str(argument1) + str(operator) + str(argument2) 
                    after = str(variable) + str(operation) + str(argument1) + "+" + str(argument1)
                    description = "Line " + str((data.line_number+1)) + " modified"
                    optimization_ = Optimization(16, data.line_number, before, after, description, 1)
                    optimizations.append(optimization_)
                    data.text_ = after
            i += 1

    def rule17(self, statements_and_assignments, optimizations):
        i = 0
        while i<len(statements_and_assignments):
            data = statements_and_assignments[i]
            if data.valid == True and data.remove == False and data.number_of_arguments == 2:
                variable = data.variable
                operation = data.operation
                argument1 = data.argument1
                operator = data.operator
                argument2 = data.argument2
                if operation == "=" and operator == "*" and argument2 == "0":
                    before = str(variable) + str(operation) + str(argument1) + str(operator) + str(argument2)
                    after = str(variable) + str(operation) + "0"
                    description = "Line " + str((data.line_number+1)) + " modified"
                    optimization_ = Optimization(17, data.line_number, before, after, description, 1)
                    optimizations.append(optimization_)
                    data.text_ = after
            i += 1

    def rule18(self, statements_and_assignments, optimizations):
        i = 0
        while i<len(statements_and_assignments):
            data = statements_and_assignments[i]
            if data.valid == True and data.remove == False and data.number_of_arguments == 2:
                variable = data.variable
                operation = data.operation
                argument1 = data.argument1
                operator = data.operator
                argument2 = data.argument2
                if operation == "=" and argument1 == "0" and operator == "/":
                    before = str(variable) + str(operation) + str(argument1) + str(operator) + str(argument2) 
                    after = str(variable) + str(operation) + "0"
                    description = "Line " + str((data.line_number+1)) + " modified"
                    optimization_ = Optimization(17, data.line_number, before, after, description, 1)
                    optimizations.append(optimization_)
                    data.text_ = after
            i += 1