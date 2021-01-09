from Instrucciones.instruction import *
from funcionalidad import getTemp,getLabel,traduct


class Ins_Case(Instruccion):

    def __init__(self,condition, instruction, elseI, row, column):
        Instruccion.__init__(self, row, column)
        self.condition = condition
        self.instruction = instruction 
        self.elseI = elseI
        self.case = None

    def Traduct(self):
        caso = ''
        if self.case != None:
            caso = self.case
        codigo = ''
        cod = ''
        contador = 1
        for it in self.condition:
            val = traduct(it['valor'])
            cod += val['c3d']
            if it['tipo'] == 'prim':
                codigo += caso+' == '+val['temp']
            else:
                codigo += val['temp']
            if len(self.condition)>1:
                if contador != len(self.condition):
                    codigo += ' or '
            contador = contador + 1
            

        trueLabel = getLabel()
        falseLabel = getLabel()
        fueraIf = ''
        cod += 'if '+codigo+': \n\tgoto .'+trueLabel+'\n'
        cod += 'goto .'+falseLabel+'\n'
        cod += 'label .'+trueLabel+'\n'
        cod +=  '\t'+self.instruction + '\n'     
        if self.elseI != None:
            fueraIf = getLabel()
            cod += 'goto .'+fueraIf+'\n'
        cod += 'label .'+falseLabel+'\n'       
        if self.elseI != None:
            if isinstance(self.elseI,str):
                cod += '\t'+str(self.elseI) + '\n'
            else:
                self.elseI.case = self.case
                cod += self.elseI.Traduct()
                cod +='\n'
        if fueraIf != '':
            cod+= 'label. '+fueraIf
    
        return cod+'\n'
