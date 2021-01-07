from analizer.abstract import instruction
from analizer.reports.Nodo import Nodo
from analizer.reports.AST import AST

class IfSimple(instruction.Instruction):
    def __init__(self, if_exp , if_inst, row , column, else_inst = None):
        instruction.Instruction.__init__(self, row , column)
        self.if_exp = if_exp
        self.if_inst = if_inst
        self.else_inst = else_inst

    def execute(self, environment):
        pass

    def generate3d(self, environment, instanciaAux, etiquetaSalida = None):
        # creacion de etiquetas , true y false
        eTrue = instanciaAux.getNewLabel()
        eFalse = instanciaAux.getNewLabel()
        eSalida = None
        #IF
        condicional1 = self.if_exp.generate3d(environment,instanciaAux)
        instanciaAux.addToCode(f'\tif {condicional1}: goto .{eTrue}')
        instanciaAux.addToCode(f'\tgoto .{eFalse}')
        instanciaAux.addToCode(f'\tlabel .{eTrue} #etiqueta true')
        for ins in self.if_inst:
            ins.generate3d(environment,instanciaAux)
        # ELSE
        if etiquetaSalida != None:# un elif
            instanciaAux.addToCode(f'\tgoto .{etiquetaSalida} #EXIT\n')
        elif self.else_inst != None: # UN IF SIN ELSE
            eSalida =instanciaAux.getNewLabel()
            instanciaAux.addToCode(f'\tgoto .{eSalida} #EXIT\n')

        instanciaAux.addToCode(f'\tlabel .{eFalse} #etiqueta false')
        if self.else_inst != None:
            for ins in self.else_inst:
                ins.generate3d(environment,instanciaAux)
        if eSalida and self.else_inst:
            instanciaAux.addToCode(f'\n\tlabel .{eSalida} # SALE DEL IF')

    def Dot(self):
            texto = "ELSE IF"
            nuevo_nodo = Nodo(texto)
            expresion_texto = "EXPRESION"
            expresion_nodo = Nodo(expresion_texto)
            expresion_nodo.addNode(self.if_exp.dot())
            nuevo_nodo.addNode(expresion_nodo)
            instrucciones_texto = "INSTRUCCIONES"
            instrucciones_nodo = Nodo(instrucciones_texto)
            for instruccion in self.if_inst:
                instrucciones_nodo.addNode(instruccion.dot())
            nuevo_nodo.addNode(instrucciones_nodo)
            return nuevo_nodo
    
    def dot(self):
        nuevo_nodo = Nodo("IF")
        expresion_nodo = Nodo("EXPRESION")
        expresion_nodo.addNode(self.if_exp.dot())
        nuevo_nodo.addNode(expresion_nodo)
        instrucciones_nodo = Nodo("INSTRUCCIONES")
        for instruccion in self.if_inst:
            instrucciones_nodo.addNode(instruccion.dot())
        nuevo_nodo.addNode(instrucciones_nodo)
        if self.else_inst:
            else_nodo = Nodo("ELSE")
            for instruccion in self.else_inst:
                else_nodo.addNode(instruccion.dot())
            nuevo_nodo.addNode(else_nodo)
        return nuevo_nodo

class If_Elseif(instruction.Instruction):
    def __init__(self, if_exp , if_inst, lista_elifs , row , column, else_inst = None):
        instruction.Instruction.__init__(self, row , column)
        self.if_exp = if_exp
        self.if_inst = if_inst
        self.else_inst = else_inst
        self.lista_elifs = lista_elifs
    def execute(self, environment):
        pass
    def generate3d(self, environment, instanciaAux):

        eTrue = instanciaAux.getNewLabel()
        eFalse = instanciaAux.getNewLabel()
        eSalida =instanciaAux.getNewLabel()# ES LA DE SALIDA
        #IF
        condicional1 = self.if_exp.generate3d(environment,instanciaAux)
        instanciaAux.addToCode(f'\tif {condicional1}: goto .{eTrue}')
        instanciaAux.addToCode(f'\tgoto .{eFalse}')
        instanciaAux.addToCode(f'\tlabel .{eTrue} #etiqueta true')
        for ins in self.if_inst:
            ins.generate3d(environment,instanciaAux)
        instanciaAux.addToCode(f'\tgoto .{eSalida} #EXIT\n')
        # ELSE
        instanciaAux.addToCode(f'\tlabel .{eFalse} #etiqueta false')
        if self.lista_elifs != None:
            for ins in self.lista_elifs:
                ins.generate3d(environment,instanciaAux,eSalida) # * NO VA TRONAR CON UN TERCER PARAMETRO PORQUE EN ESTE CASO FIJO ACA TENGO SOLO OBJETOS IFS

        if self.else_inst != None:
            for ins in self.else_inst:
                ins.generate3d(environment,instanciaAux)

        instanciaAux.addToCode(f'\n\tlabel .{eSalida} # SALE DEL IF')

    def dot(self):
        texto = "IF"
        nuevo_nodo = Nodo(texto)
        expresion_texto  = "EXPRESION"
        expresion_nodo = Nodo(expresion_texto)
        expresion_nodo.addNode(self.if_exp.dot())
        instrucciones_texto = "INSTRUCCIONES"
        instrucciones_nodo = Nodo(instrucciones_texto)
        for instruccion in self.if_inst:
            instrucciones_nodo.addNode(instruccion.dot())
        nuevo_nodo.addNode(expresion_nodo)
        nuevo_nodo.addNode(instrucciones_nodo)
        for item in self.lista_elifs:
            nuevo_nodo.addNode(item.Dot())
        if self.else_inst:
            else_texto = "ELSE"
            else_nodo = Nodo(else_texto)
            instrucciones_else_texto = "INSTRUCCIONES"
            instrucciones_else_nodo = Nodo(instrucciones_else_texto)
            for instruccion in self.else_inst:
                instrucciones_else_nodo.addNode(instruccion.dot())
            else_nodo.addNode(instrucciones_else_nodo)
            nuevo_nodo.addNode(else_nodo)
        return nuevo_nodo