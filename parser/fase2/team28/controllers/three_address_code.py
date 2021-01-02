from utils.decorators import singleton
#from utils.analyzers.syntactic import parse


@singleton
class ThreeAddressCode(object):
    def __init__(self):
        self.__fileName = 'C3D.py'
        self.__content = ''
        self.__code = ''

        self.__tempCounter = 0

        self.__stack = []
        self.__stackCounter = 0

    def destroy(self):
        self.__content = ''
        self.__code = ''
        self.__tempCounter = 0

        self.__stack = []
        self.__stackCounter = 0

    def newTemp(self):
        tmp = f"t{self.__tempCounter}"
        self.__tempCounter += 1
        return tmp

    # ------------------------- Stack -------------------------
    @property
    def stack(self):
        return self.__stack

    @property
    def stackCounter(self):
        stackCounter = self.__stackCounter
        self.__stackCounter += 1
        return stackCounter

    def addStack(self, function):
        """
        Method to add to stack

        :param function: Function to add
        :return: Returns nothing
        """
        self.__stack.append(function)
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
        self.__code += f"\n\t{data}"

    def getCode(self):
        """
        Method to generate (write) and execute the file (report) with the three-address code

        :return: Returns nothing
        """
        self.__content = 'from goto import with_goto'
        self.__content += '\nfrom controllers.three_address_code import ThreeAddressCode'

        self.__content += '\n\n@with_goto'
        self.__content += '\ndef main():'
        self.__content += '\n\tstack = ThreeAddressCode()\n'
        self.__content += self.__code

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
