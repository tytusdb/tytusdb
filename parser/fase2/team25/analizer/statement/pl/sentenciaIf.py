from analizer.abstract import instruction


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