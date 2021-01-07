from Instrucciones.instruction import *
from funcionalidad import getTemp,getLabel,traduct


class Ins_If(Instruccion):

    def __init__(self,condition, instruction, elseI, row, column):
        Instruccion.__init__(self, row, column)
        self.condition = condition
        self.instruction = instruction 
        self.elseI = elseI

    def Traduct(self):
        #print('LA CONDICION: '+str(self.condition.code))
        condi = traduct(self.condition)
        cod = ''
        cod += condi['c3d']
        trueLabel = getLabel()
        falseLabel = getLabel()
        fueraIf = ''
        cod += 'if '+condi['temp']+': \n\tgoto .'+trueLabel+'\n'
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
                cod += self.elseI.Traduct()
                cod +='\n'
        if fueraIf != '':
            cod+= 'label. '+fueraIf
    
        return cod+'\n'
