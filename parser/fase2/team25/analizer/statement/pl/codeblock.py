
from analizer.abstract import instruction
from analizer.reports.Nodo import Nodo
from analizer.reports.AST import AST

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
    
    def dot(self):
        nuevo_nodo = Nodo("CODEBLOCK")
        if self.lista_declaraciones:
            declaraciones_nodo = Nodo("DECLARACIONES")
            for declaracion in self.lista_declaraciones:
                declaraciones_nodo.addNode(declaracion.dot())
            nuevo_nodo.addNode(declaraciones_nodo)
        instrucciones_nodo = Nodo("INSTRUCCIONES")
        for instruccion in self.lista_instrucciones:
            if instruccion!=None:
                instrucciones_nodo.addNode(instruccion.dot())
        nuevo_nodo.addNode(instrucciones_nodo)
        return nuevo_nodo


