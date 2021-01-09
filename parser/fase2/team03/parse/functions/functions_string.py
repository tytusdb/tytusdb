from hashlib import md5, sha256
from parse.ast_node import ASTNode


# From here on, classes describing aggregate functions
# TODO: Convert, SetByte, Substr
class Convert(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class Decode(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.exp.decode('base64', 'strict')

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'Decode ({self.exp.generate(table, tree)})'


class Encode(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.exp.encode('base64', 'strict')

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'Encode({self.exp.generate(table, tree)})'


class GetByte(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return bytes(self.exp, 'utf-8')

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'GetByte({self.exp.generate(table, tree)})'


class Length(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return len(self.exp)

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'Length({self.exp.generate(table, tree)})'


class Md5(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return md5(self.exp.encode())

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'MD5({self.exp.generate(table, tree)})'


class SetByte(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class Sha256(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return sha256(self.exp)

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class Substr(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return len(self.exp)

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class Substring(ASTNode):
    def __init__(self, exp, start, end, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.start = start
        self.end = end

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.exp[self.start: self.end]

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'Substring({self.exp.generate(table, tree)},{self.start.generate(table, tree)}, {self.end.generate(table, tree)})'


class Trim(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.exp.strip()

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''
