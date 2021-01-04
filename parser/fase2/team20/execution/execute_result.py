class execute_result:

    def __init__(self, dotAST, printSymbolTable, errors, messagges, querys):
        self.dotAST = dotAST
        self.printSymbolTable = printSymbolTable
        self.errors = errors
        self.messages = messagges
        self.querys = querys