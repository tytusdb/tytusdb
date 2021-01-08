import optimization.abstract.optimize as opt
import re

class OptAssignment(opt.OptimizedInstruction):
    """
    Asignacion optimizada
    """
    def __init__(self,type_,id,assign,row) -> None:
        super().__init__(row) 
        self.type = type_
        self.id = id
        self.assign = assign

    def __str__(self) -> str:
        if self.type == opt.TEVAL.SINGLE:
            return f'{self.id} = {self.assign}'
        elif self.type == opt.TEVAL.OPERATION:
            return f'{self.id} = {self.assign[0]} {self.assign[1]} {self.assign[2]}'
        else:
            return f'{self.id} = {self.assign}()'

    def optimize(self, generador):
        idVal = self.id
        if self.type == opt.TEVAL.OPERATION:
            izq,operador,der = self.assign
            #Separamos por operador
            if operador == '+':
                if der == 0 or izq == 0:
                    if idVal == izq or idVal == der:
                        self.optimizable = opt.RULES.O8
                        self.toReport(generador)
                    elif re.match(r'^(\'.*?\'|\".*?\")$', str(izq)) == None and \
                    re.match(r'^(\'.*?\'|\".*?\")$', str(der)) == None:
                        if der == 0:
                            self.optimizable = opt.RULES.O12
                            self.toReport(generador)
                            self.assign = izq
                            self.type = opt.TEVAL.SINGLE
                        else:
                            self.optimizable = opt.RULES.O12
                            self.toReport(generador)
                            self.assign = der
                            self.type = opt.TEVAL.SINGLE      
            elif operador == '-':
                if der == 0:
                    if idVal == izq:
                        self.optimizable = opt.RULES.O9
                        self.toReport(generador)
                    elif re.match(r'^(\'.*?\'|\".*?\")$', str(izq)) == None and \
                    re.match(r'^(\'.*?\'|\".*?\")$', str(der)) == None:
                        self.optimizable = opt.RULES.O13
                        self.toReport(generador)
                        self.assign = izq
                        self.type = opt.TEVAL.SINGLE
            elif operador == '/':
                if idVal == izq and der == 1:
                    self.optimizable = opt.RULES.O11
                    self.toReport(generador)
                elif re.match(r'^(\'.*?\'|\".*?\")$', str(izq)) == None and \
                re.match(r'^(\'.*?\'|\".*?\")$', str(der)) == None:
                    if izq == 0:
                        self.optimizable = opt.RULES.O18
                        self.toReport(generador)
                        self.assign = izq
                        self.type = opt.TEVAL.SINGLE
                    elif der == 1:
                        self.optimizable = opt.RULES.O15
                        self.toReport(generador)
                        self.assign = izq
                        self.type = opt.TEVAL.SINGLE

            elif operador == '*':
                if idVal == izq or idVal == der:
                    if der == 1 or izq == 1:
                        self.optimizable = opt.RULES.O10
                        self.toReport(generador)
                    elif der == 2:
                        self.optimizable = opt.RULES.O16
                        self.toReport(generador)
                        self.assign = (izq, '+', izq)
                    elif izq == 2:
                        self.optimizable = opt.RULES.O16
                        self.toReport(generador)
                        self.assign = (der, '+', der)
                elif re.match(r'^(\'.*?\'|\".*?\")$', str(izq)) == None and \
                re.match(r'^(\'.*?\'|\".*?\")$', str(der)) == None:
                    if der == 2:
                        self.optimizable = opt.RULES.O16
                        self.toReport(generador)
                        self.assign = (izq, '+', izq)
                    elif izq == 2:
                        self.optimizable = opt.RULES.O16
                        self.toReport(generador)
                        self.assign = (der, '+', der)
                    elif der == 0 or izq == 0:
                            self.optimizable = opt.RULES.O17
                            self.toReport(generador)
                            self.assign = der
                            self.type = opt.TEVAL.SINGLE
                    elif der == 1:
                        self.optimizable = opt.RULES.O14
                        self.toReport(generador)
                        self.assign = izq
                        self.type = opt.TEVAL.SINGLE
                    elif izq == 1:
                        self.optimizable = opt.RULES.O14
                        self.toReport(generador)
                        self.assign = der
                        self.type = opt.TEVAL.SINGLE
        #TIPO SINGLE
        elif self.type == opt.TEVAL.SINGLE:
            if idVal == self.assign:
                self.optimizable = opt.RULES.OMISION

    def addToCode(self, generador) -> None:
        if self.id != 'stack':
            super().addToCode(generador)
            if not self.optimizable in (opt.RULES.OMISION,opt.RULES.O8, opt.RULES.O9, opt.RULES.O10, opt.RULES.O11):
                generador.addToCode(f'\t{str(self)}')
        else:
            generador.addToCode(f'{str(self)}')
