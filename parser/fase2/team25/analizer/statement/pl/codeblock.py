
from analizer.abstract import instruction


class CodeBlock(instruction.Instruction):
    def __init__(self, lista_instrucciones, row , column , lista_declaraciones = None ):
        instruction.Instruction.__init__(self, row , column)
        self.lista_instrucciones = lista_instrucciones
        self.lista_declaraciones = lista_declaraciones

    def execute(self, environment):
        pass

    def generate3d(self, environment, instanciaAux):
        # * LAS DECLARACIONES SE TRADUCEN ANTES QUE LAS INSTRUCCIONES
        if self.lista_declaraciones:
            for element in self.lista_declaraciones:
                element.generate3d(environment,instanciaAux)

        for element in self.lista_instrucciones:
            # * LAS INSTRUCCIONES NO DEVUELVEN nada solo se ejecuta su metodo generate 3d
            if element != None:
                element.generate3d(environment, instanciaAux)
            else:
                print('venia un null en codeblock')


