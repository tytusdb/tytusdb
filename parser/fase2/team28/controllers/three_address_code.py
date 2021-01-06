from utils.decorators import singleton
#from utils.analyzers.syntactic import parse


@singleton
class ThreeAddressCode(object):
    def __init__(self):
        self.__fileName = 'C3D.py'
        self.__content = ''
        self.__code = ''

        self.__tempCounter = 0
        self.__tempLabel = 0

        self.__stack = []
        self.__stackCounter = 0

        self.__function = ''
        self.__instructionList = ''
        self.__isCode = True
        self.__functions = []

    def destroy(self):
        self.__content = ''
        self.__code = ''

        self.__tempCounter = 0
        self.__tempLabel = 0

        self.__stack = []
        self.__stackCounter = 0

        self.__function = ''
        self.__instructionList = ''
        self.__isCode = True
        self.__functions = []

    def newTemp(self):
        tmp = f"t{self.__tempCounter}"
        self.__tempCounter += 1
        return tmp

    def newLabel(self):
        lbl = f"L{self.__tempLabel}"
        self.__tempLabel += 1
        return lbl

    # ------------------------- Stack -------------------------
    @property
    def stack(self):
        return self.__stack

    @property
    def stackCounter(self):
        stackCounter = self.__stackCounter
        # self.__stackCounter += 1
        return stackCounter

    def addStack(self, value):
        """
        Method to add to stack

        :param function: Function to add
        :return: Returns nothing
        """
        self.addCode(f"Stack[{self.__stackCounter}] = {value}")
        # self.__stack.append(function)
        self.__stackCounter += 1

    def incStackCounter(self):
        self.__stackCounter += 1

    def execute(self, tmp):
        # parse(tmp)
        self.__stack.pop(0).process(tmp)

    def push(self, tmp):
        pass

    # ------------------------- Report -------------------------
    def addCode(self, data):
        """
        Method to add Code or temp to three-address code 

        :param data: Code or temp 
        :return: Returns nothing
        """
        if self.__isCode:
            self.__code += f"\n\t{data}"
        else:
            self.__instructionList += f"\n\t{data}"

    def getCode(self):
        """
        Method to generate (write) and execute the file (report) with the three-address code

        :return: Returns nothing
        """
        self.__content = 'from goto import with_goto'
        self.__content += '\nfrom math import *'
        self.__content += '\nfrom controllers.three_address_code import ThreeAddressCode'
        self.__content += '\n\nStack = [None]*10000\nP = 0'

        self.__content += '\n\n@with_goto'
        self.__content += '\ndef main():'
        self.__content += '\n\tglobal Stack'
        self.__content += self.__code

        for functions in self.__functions:
            self.__content += functions['function']

        self.__content += '\n\nmain()'
        return self.__content

    def writeFile(self):
        """
        Method to write the file with the three-address code

        :return: Returns nothing
        """
        try:
            with open(self.__fileName, 'w') as f:
                f.write(self.getCode())
        except IOError:
            print('Error: File does not appear to exist.')

    def executeFile(self):
        """
        Method to execute the file with the three-address code

        :return: Returns nothing
        """
        try:
            with open(self.__fileName, 'r') as f:
                exec(f.read())
        except IOError:
            print('Error: File does not appear to exist.')
    # END---------------------- Report -------------------------

    def createFunction(self, name, params, variables):
        listParameters = ''

        for i, item in enumerate(params):
            if i:  # print a separator if this isn't the first element
                listParameters += ', '
            listParameters += str(item.id)

        self.__function = '\n\n@with_goto'
        self.__function += f"\ndef {name}():"
        self.__function += '\n\tglobal Stack, P'
        self.__function += self.__instructionList

        self.__functions.append({'name': name, 'function': self.__function,
                                 'variables': variables})
        self.__isCode = True

    def newFunction(self):
        self.__isCode = False

    def searchFunction(self, name):
        for fun in self.__functions:
            if name == fun['name']:
                return fun
        return None
