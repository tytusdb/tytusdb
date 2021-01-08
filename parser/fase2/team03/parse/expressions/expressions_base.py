from .expression_enum import OpArithmetic, OpRelational, OpLogic, OpPredicate
from datetime import date, datetime
from parse.errors import Error, ErrorType
from parse.ast_node import ASTNode
import hashlib
from TAC.quadruple import Quadruple
from TAC.tac_enum import *
from parse.symbol_table import generate_tmp


class Numeric(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val

    def generate(self, table, tree):
        super().generate(table, tree)
        return str(self.val)


class NumericPositive(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        self.val = self.val.execute(table, tree)
        print(type(self.val))
        if type(self.val) == int or type(self.val) == float:
            return self.val * 1
        else:
            raise Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be number')

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'+{self.val.generate(table, tree)}'


class NumericNegative(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        self.val = self.val.execute(table, tree)
        if type(self.val) == int or type(self.val) == float:
            return self.val * -1
        else:
            raise Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be number')

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'-{self.val.generate(table, tree)}'


class Text(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val

    def generate(self, table, tree):
        super().generate(table, tree)
        return f"\\'{self.val}\\'"


class BoolAST(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = (str(val).upper() == "TRUE")
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val

    def generate(self, table, tree):
        super().generate(table, tree)
        return 'TRUE' if self.val else 'FALSE'


class DateAST(ASTNode):
    def __init__(self, val, option, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.option = option
        self.graph_ref = graph_ref
        try:
            self.val = datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
            if self.option == 'YEAR':
                self.result = self.val.year
            elif self.option == 'HOUR':
                self.result = self.val.hour
            elif self.option == 'MINUTE':
                self.result = self.val.minute
            elif self.option == 'SECOND':
                self.result = self.val.second
            elif self.option == 'MONTH':
                self.result = self.val.month
            elif self.option == 'DAY':
                self.result = self.val.day

        except:
            self.result = None
            raise Error(self.line, self.column, ErrorType.SEMANTIC, 'it is not a date time format')

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.result

    def generate(self, table, tree):
        super().generate(table, tree)
        return f"EXTRACT ({self.option} FROM TIMESTAMP \\\'{self.val}\\\')"


class DateAST_2(ASTNode):
    def __init__(self, option, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.option = option
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return str(self.option)

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'{str(self.option)} FROM TIMESTAMP'


class ColumnName(ASTNode):
    def __init__(self, tName, cName, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.tName = tName
        self.cName = cName
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)

        fullname = ''
        if self.tName is None or self.tName == "":
            fullname = self.cName
        else:
            fullname = self.tName + "." + self.cName  # TODO check if is necesary go to symbol table to get the value or check if the object exists

        # yes we have to get the value of colname
        # if this AST have tree  == list it means the execute have to search for the value of colunn
        # in this case table have a row to evaluate where exp and tree has the columns header
        if isinstance(tree, list):
            try:
                index = tree.index(fullname)
                return table[index]
            except:
                raise Error(self.line, self.column, ErrorType.RUNTIME,
                            f'[AST] the name {fullname} is not belong of the selected table(s)')
        else:
            return fullname

    def generate(self, table, tree):
        super().generate(table, tree)
        fullname = self.cName
        if self.tName is not None and self.tName != "":
            fullname = f'{self.tName}.{fullname}'
        return fullname


class Now(ASTNode):
    def __init__(self, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return datetime.now()

    def generate(self, table, tree):
        super().generate(table, tree)
        return 'NOW()'


class NowDate(ASTNode):
    def __init__(self, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return str(date.today())

    def generate(self, table, tree):
        super().generate(table, tree)
        return 'CURRENT_DATE'


class NowTime(ASTNode):
    def __init__(self, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    def generate(self, table, tree):
        super().generate(table, tree)
        return 'CURRENT_TIME'


class BinaryExpression(ASTNode):
    # Class that handles every arithmetic expression
    def __init__(self, exp1, exp2, operator, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        # TODO: Validate type
        if self.operator is None:  # 'Number' or 'artirmetic function' production for example
            return self.exp1.execute(table, tree)
        if self.operator == OpArithmetic.PLUS:
            return self.exp1.execute(table, tree) + self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.MINUS:
            return self.exp1.execute(table, tree) - self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.TIMES:
            return self.exp1.execute(table, tree) * self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.DIVIDE:
            return self.exp1.execute(table, tree) / self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.MODULE:
            return self.exp1.execute(table, tree) % self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.POWER:
            return pow(self.exp1, self.exp2)

    def generate(self, table, tree):
        super().generate(table, tree)
        if tree is None:
            if self.operator is None:  # 'Number' or 'artirmetic function' production for example
                return self.exp1.generate(table, tree)
            if self.operator == OpArithmetic.PLUS:
                return f'{self.exp1.execute(table, tree)} + {self.exp2.execute(table, tree)}'
            if self.operator == OpArithmetic.MINUS:
                return f'{self.exp1.execute(table, tree)} - {self.exp2.execute(table, tree)}'
            if self.operator == OpArithmetic.TIMES:
                return f'{self.exp1.execute(table, tree)} * {self.exp2.execute(table, tree)}'
            if self.operator == OpArithmetic.DIVIDE:
                return f'{self.exp1.execute(table, tree)} / {self.exp2.execute(table, tree)}'
            if self.operator == OpArithmetic.MODULE:
                return f'{self.exp1.execute(table, tree)} % {self.exp2.execute(table, tree)}'
            if self.operator == OpArithmetic.POWER:
                return f'{self.exp1.execute(table, tree)} ^ {self.exp2.execute(table, tree)}'
        else:  # TAC
            # Classes who return scalar values NOT expressions: Numeric, Text, BoolAST, ColumnName for ID's, expressions_math.py, expressions_trig.py
            arg1 = None
            arg2 = None
            gen_exp1 = self.exp1.generate(table, tree)
            if isinstance(gen_exp1, Quadruple):
                arg1 = gen_exp1.res
            else:
                arg1 = gen_exp1  # if isn´t Cuadrupe must be scallar value such as 1,45,'OLC2 100 pts', False
            # same as arg2 but with ternary operator syntax ;)
            gen_exp2 = self.exp2.generate(table, tree)
            arg2 = gen_exp2.res if isinstance(gen_exp2, Quadruple) else gen_exp2

            this_tac = Quadruple(self.operator, arg1, arg2, generate_tmp(), OpTAC.ASSIGNMENT)
            tree.append(this_tac)
            return this_tac


class RelationalExpression(ASTNode):
    # Class that handles every relational expression

    def __init__(self, exp1, exp2, operator, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.operator == OpRelational.GREATER:
            return self.exp1.execute(table, tree) > self.exp2.execute(table, tree)
        if self.operator == OpRelational.LESS:
            return self.exp1.execute(table, tree) < self.exp2.execute(table, tree)
        if self.operator == OpRelational.EQUALS:
            return self.exp1.execute(table, tree) == self.exp2.execute(table, tree)
        if self.operator == OpRelational.NOT_EQUALS:
            return self.exp1.execute(table, tree) != self.exp2.execute(table, tree)
        if self.operator == OpRelational.GREATER_EQUALS:
            return self.exp1.execute(table, tree) >= self.exp2.execute(table, tree)
        if self.operator == OpRelational.LESS_EQUALS:
            return self.exp1.execute(table, tree) <= self.exp2.execute(table, tree)
        if self.operator == OpRelational.LIKE:  # TODO add execution to [NOT] LIKE, Regex maybe?
            return self.exp1.execute(table, tree) == self.exp2.execute(table, tree)
        if self.operator == OpRelational.NOT_LIKE:
            return self.exp1.execute(table, tree) != self.exp2.execute(table, tree)

    def generate(self, table, tree):
        super().generate(table, tree)
        if tree is None:
            if self.operator == OpRelational.GREATER:
                return f'{self.exp1.generate(table, tree)} > {self.exp2.execute(table, tree)}'
            if self.operator == OpRelational.LESS:
                return f'{self.exp1.generate(table, tree)} < {self.exp2.execute(table, tree)}'
            if self.operator == OpRelational.EQUALS:
                return f'{self.exp1.generate(table, tree)} = {self.exp2.execute(table, tree)}'
            if self.operator == OpRelational.NOT_EQUALS:
                return f'{self.exp1.generate(table, tree)} != {self.exp2.execute(table, tree)}'
            if self.operator == OpRelational.GREATER_EQUALS:
                return f'{self.exp1.generate(table, tree)} >= {self.exp2.execute(table, tree)}'
            if self.operator == OpRelational.LESS_EQUALS:
                return f'{self.exp1.generate(table, tree)} <= {self.exp2.execute(table, tree)}'
            if self.operator == OpRelational.LIKE:
                return f'{self.exp1.generate(table, tree)} LIKE {self.exp2.execute(table, tree)}'
            if self.operator == OpRelational.NOT_LIKE:
                return f'{self.exp1.generate(table, tree)} NOT LIKE {self.exp2.execute(table, tree)}'
        else:
            arg1 = None
            arg2 = None
            gen_exp1 = self.exp1.generate(table, tree)
            arg1 = gen_exp1.res if isinstance(gen_exp1, Quadruple) else gen_exp1
            gen_exp2 = self.exp2.generate(table, tree)
            arg2 = gen_exp2.res if isinstance(gen_exp2, Quadruple) else gen_exp2
            this_tac = Quadruple(self.operator, arg1, arg2, generate_tmp(), OpTAC.ASSIGNMENT)
            tree.append(this_tac)
            return this_tac


class PredicateExpression(ASTNode):  # TODO check operations and call to exceute function
    # Class that handles every logic expression

    def __init__(self, exp1, exp2, operator, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.operator == OpPredicate.NULL:
            return self.exp1.execute(table, tree) is None
        if self.operator == OpPredicate.NOT_NULL:
            return self.exp1.execute(table, tree) is not None
        if self.operator == OpPredicate.DISTINCT:  # Improve logic in order to allow null and 0 to be the same
            return self.exp1.execute(table, tree) != self.exp2.execute(table, tree)
        if self.operator == OpPredicate.NOT_DISTINCT:  # Improve logic in order to allow null and 0 to be the same
            return self.exp1.execute(table, tree) == self.exp2.execute(table, tree)
        if self.operator == OpPredicate.TRUE:
            return self.exp1.execute(table, tree) is True
        if self.operator == OpPredicate.NOT_TRUE:
            return self.exp1.execute(table, tree) is False
        if self.operator == OpPredicate.FALSE:
            return self.exp1.execute(table, tree) is False
        if self.operator == OpPredicate.NOT_FALSE:
            return self.exp1.execute(table, tree) is True
        if self.operator == OpPredicate.UNKNOWN:  # TODO do actual comparison to Unknown... No ideas right now
            return False
        if self.operator == OpPredicate.NOT_UNKNOWN:  # Same as previous comment about Unknown
            return False

    def generate(self, table, tree):
        super().generate(table, tree)
        if tree is None:
            if self.operator == OpPredicate.NULL:
                return f'{self.exp1.generate(table, tree)} IS NULL'
            if self.operator == OpPredicate.NOT_NULL:
                return f'{self.exp1.generate(table, tree)} IS NOT NULL'
            if self.operator == OpPredicate.DISTINCT:
                return f'{self.exp1.generate(table, tree)} IS DISTINCT FROM {self.exp1.generate(table, tree)}'
            if self.operator == OpPredicate.NOT_DISTINCT:
                return f'{self.exp1.generate(table, tree)} IS NOT DISTINCT FROM {self.exp1.generate(table, tree)}'
            if self.operator == OpPredicate.TRUE:
                return f'{self.exp1.generate(table, tree)} IS TRUE'
            if self.operator == OpPredicate.NOT_TRUE:
                return f'{self.exp1.generate(table, tree)} IS NOT TRUE'
            if self.operator == OpPredicate.FALSE:
                return f'{self.exp1.generate(table, tree)} IS FALSE'
            if self.operator == OpPredicate.NOT_FALSE:
                return f'{self.exp1.generate(table, tree)} IS NOT FALSE'
            if self.operator == OpPredicate.UNKNOWN:
                return f'{self.exp1.generate(table, tree)} IS UNKNOWN'
            if self.operator == OpPredicate.NOT_UNKNOWN:
                return f'{self.exp1.generate(table, tree)} IS NOT UNKNOWN'
        else:
            pass


class BoolExpression(ASTNode):
    def __init__(self, exp1, exp2, operator, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exec1 = self.exp1.execute(table, tree)
        exec2 = self.exp2.execute(table, tree)

        if isinstance(exec1, bool) and isinstance(exec2, bool):
            if self.operator == OpLogic.AND:
                return exec1 and exec2
            if self.operator == OpLogic.OR:
                return exec1 or exec2
        else:
            raise Exception("The result of operation isn't boolean value")

    def generate(self, table, tree):
        super().generate(table, tree)
        exec1 = self.exp1.generate(table, tree)
        exec2 = self.exp2.generate(table, tree)
        if tree is None:
            if self.operator == OpLogic.AND:
                return f'{exec1} AND {exec2}'
            if self.operator == OpLogic.OR:
                return f'{exec1} OR {exec2}'
        else:
            arg1 = None
            arg2 = None
            arg1 = exec1.res if isinstance(exec1, Quadruple) else exec1
            arg2 = exec2.res if isinstance(exec2, Quadruple) else exec2
            this_tac = Quadruple(self.operator, arg1, arg2, generate_tmp(), OpTAC.ASSIGNMENT)
            tree.append(this_tac)
            return this_tac


class Negation(ASTNode):
    def __init__(self, exp1, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exec1 = self.exp1.execute(table, tree)

        if isinstance(exec1, bool):
            return not exec1
        else:
            raise Exception("The result of operation isn't boolean value")

    def generate(self, table, tree):
        super().generate(table, tree)
        exec1 = self.exp1.generate(table, tree)
        if tree is None:
            if exec1 != 'TRUE' and exec1 != 'FALSE':
                raise Exception("The result of operation isn't boolean value")
            return 'TRUE' if exec1 == 'FALSE' else 'FALSE'
        else:
            arg1 = exec1.res if isinstance(exec1, Quadruple) else exec1
            this_tac = Quadruple(OpLogic.NOT, arg1, None, generate_tmp(), OpTAC.ASSIGNMENT)
            tree.append(this_tac)
            return this_tac


class Identifier(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    # Must return lexeme of ID
    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val

    def executeSTVal(self, table, tree):  # TODO: Symbol value from ST :S
        super().execute(table, tree)
        return self.val

    def generate(self, table, tree):
        super().generate(table, tree)
        return self.val


class TypeDef(ASTNode):
    def __init__(self, val, min_size, max_size, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val  # token name: CHAR, INTEGER,...
        self.min_size = min_size,
        self.max_size = max_size,
        self.graph_ref = graph_ref

    # Must return lexeme of ID
    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val

    def minSize(self, table, tree):
        super().execute(table, tree)
        return self.min_size

    def maxSize(self, table, tree):
        super().execute(table, tree)
        return self.max_size

    def generate(self, table, tree):
        super().generate(table, tree)
        return self.val


class Nullable(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val  # True: accept null values other wise False
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val

    def generate(self, table, tree):
        super().generate(table, tree)
        return 'TRUE' if self.val else 'FALSE'


class MD5_(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return hashlib.md5(exp.encode('utf-8')).hexdigest()
        except:
            raise (Error(self.line, self.column, ErrorType.SEMANTIC, 'MD5 error'))

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'MD5({self.exp.generate(table, tree)})'


class SUBSTRING_(ASTNode):
    def __init__(self, exp, str_pos, ext_char, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.str_pos = str_pos
        self.ext_char = ext_char
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        str_por = self.str_pos.execute(table, tree)
        ext_char = self.ext_char.execute(table, tree)
        try:
            str_por = int(str_por)
            ext_char = int(ext_char)
            if (str_por >= 0) and (ext_char >= 0) and (str_por < ext_char):
                str_por = str_por - 1
                r = exp[str_por: ext_char]
                return r
            else:
                raise (Error(self.line, self.column, ErrorType.SEMANTIC, 'SUBSTRING() function argument error'))
        except:
            raise (Error(self.line, self.column, ErrorType.SEMANTIC, 'SUBSTRING() function argument error'))

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'SUBSTRING({self.exp.generate(table, tree)})'


class LENGTH_(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            if type(exp) == str:
                return len(exp)
            else:
                raise (Error(self.line, self.column, ErrorType.SEMANTIC, 'LENGTH() function argument error'))
        except:
            raise (Error(self.line, self.column, ErrorType.SEMANTIC, 'LENGTH() function argument error'))

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'LENGTH({self.exp.generate(table, tree)})'


class LOWER_(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            if type(exp) == str:
                
                r = exp.lower()
                return r 
            else:
                raise (Error(self.line, self.column, ErrorType.SEMANTIC, 'LOWER() function argument error'))
        except:
            raise (Error(self.line, self.column, ErrorType.SEMANTIC, 'LOWER() function argument error'))

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'LOWER({self.exp.generate(table, tree)})'
