from parse.expressions.expression_enum import *
from TAC.tac_enum import *
import copy
import os
from tabulate import tabulate


class Quadruple(object):
    def __init__(self, op: Enum, arg1: str, arg2: str, res: str, instType: Enum):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.res = res
        self.instType = instType  # type of the intruction

    def isEqual(self, c_Quadruple, c_op: bool, c_arg1: bool, c_arg2: bool, c_res: bool):
        if c_Quadruple is None:
            raise 'You are trying to compare a Quadruplee passing None value, please check you code [quadruple.py]'
        isequal = False
        if self.instType != c_Quadruple.instType:
            return False
        if c_op:
            if self.op == c_Quadruple.op:
                isequal = True
            else:
                return False

        if c_arg1:
            if self.arg1 == c_Quadruple.arg1:
                isequal = True
            else:
                return False

        if c_arg2:
            if self.arg2 == c_Quadruple.arg2:
                isequal = True
            else:
                return False

        if c_res:
            if self.res == c_Quadruple.res:
                isequal = True
            else:
                return False

        return isequal

    def isAsigment(self):
        return self.instType == '=' or self.instType == OpTAC.ASSIGNMENT

    def isLabel(self):
        return self.instType == OpTAC.LABEL

    def labelName(self):
        if not self.isLabel() and not self.isGoTo():
            raise 'You ar trying to get a label name for a intruction that isn´t a label or goto'
        return self.arg1

    def isGoTo(self):
        return self.instType == OpTAC.GOTO

    def isEqualOperator(self):
        return self.op == OpRelational.EQUALS or self.op == '=='

    def isConditional(self):
        return self.instType == OpTAC.CONDITIONAL

    def allWaysFalse(self):  # TODO: check > < >= <= = for strings excuding if args are temporals Tn
        try:
            if self.op == OpLogic.OR:
                return (str(self.arg1).lower() == 'false') and (str(self.arg2).lower() == 'false')
            elif self.op == OpLogic.AND:
                return (str(self.arg1).lower() == 'false') or (str(self.arg2).lower() == 'false')
            elif self.op == OpLogic.NOT:
                return str(self.arg1).lower() == 'True'
            elif self.op == OpRelational.EQUALS:
                return int(self.arg1) != int(self.arg2)
            elif self.op == OpRelational.GREATER:
                return int(self.arg1) <= int(self.arg2)
            elif self.op == OpRelational.GREATER_EQUALS:
                return int(self.arg1) < int(self.arg2)
            elif self.op == OpRelational.LESS:
                return int(self.arg1) >= int(self.arg2)
            elif self.op == OpRelational.LESS_EQUALS:
                return int(self.arg1) > int(self.arg2)
            elif self.op == OpRelational.NOT_EQUALS:
                return int(self.arg1) == int(self.arg2)
            elif self.op is None:
                return str(self.arg1).lower() == 'false'

        except expression as identifier:
            return False

        return False

    # this function aply for rules 8, 9, 10, 11,
    # return true if the rule must be removed or false if no removed, (you ust remove it in other function)
    # use it in assigments type x = x + 0, x = x / 1, ...
    def neutralElement(self):
        if self.isAsigment():
            if self.op == OpArithmetic.PLUS:
                return (self.res == self.arg1 and self.arg2 == '0') or (self.res == self.arg2 and self.arg1 == '0')
            elif self.op == OpArithmetic.MINUS:
                return self.res == self.arg1 and self.arg2 == '0'
            elif self.op == OpArithmetic.TIMES:
                return (self.res == self.arg1 and self.arg2 == '1') or (self.res == self.arg2 and self.arg1 == '1')
            elif self.op == OpArithmetic.DIVIDE:
                return self.res == self.arg1 and self.arg2 == '1'
        return False

    def __str__(self):
        if self.instType == OpTAC.ASSIGNMENT:
            oper = self.op.strSymbol() if self.op else ''
            arg2_ = self.arg2 if self.arg2 else ''
            return f'{self.res} = {self.arg1} {oper} {arg2_}'
        elif self.instType == OpTAC.GOTO:
            return f'goto {self.arg1}'
        elif self.instType == OpTAC.LABEL:
            return f'{self.arg1}:'
        elif self.instType == OpTAC.CONDITIONAL:
            oper = self.op.strSymbol() if self.op else ''
            ar2 = self.arg2 if self.arg2 else ''
            return f'if {self.arg1} {oper} {ar2}: goto {self.res}'
        else:
            return f'arg1:{self.arg1}, arg2:{self.arg2}, op:{self.op}'

    def strpy(self):
        if str(self.arg1).lower() == 'false':
            self.arg1 = 'False'
        if str(self.arg1).lower() == 'true':
            self.arg1 = 'True'
        if str(self.arg2).lower() == 'false':
            self.arg1 = 'False'
        if str(self.arg2).lower() == 'true':
            self.arg1 = 'True'

        if self.instType == OpTAC.ASSIGNMENT:
            oper = self.op.strSymbol() if self.op else ''
            arg2_ = self.arg2 if self.arg2 else ''
            return f'{self.res} = {self.arg1} {oper} {arg2_}'
        elif self.instType == OpTAC.GOTO:
            return f'goto.{self.arg1}'
        elif self.instType == OpTAC.LABEL:
            return f'label.{self.arg1}'
        elif self.instType == OpTAC.CONDITIONAL:
            oper = self.op.strSymbol() if self.op else ''
            ar2 = self.arg2 if self.arg2 else ''
            return f'if {self.arg1} {oper} {ar2}: goto.{self.res}'
        elif self.instType == OpTAC.POP:
            return f'{self.res} = pop()'
        elif self.instType == OpTAC.PUSH:
            return f'push({self.arg1})'
        elif self.instType == OpTAC.CALL:
            return f'{self.res} = {self.arg1}({self.arg2})'


# This Funtion will unquewe each TAC (Quadruplees) from param list, aply each rule for each TAC and push that TAC to reslut
# Ohh and save a log for wich rule was applied
# return [result, reoved items]
def DoOptimization(quadL: list):
    # We need an list for the optiization result, a list for the log of the optimization
    # Each Rule function modifi the current Quadruple (changing its values) and the list (remoing items)
    # Each Rule function returns the elemens removed fro list (for log)
    result = []
    str_result = []
    while len(quadL) > 0:
        tmp = quadL.pop(0)
        res = Rule1(quadL, tmp)
        if len(res) > 0:
            in_str = ''
            for item in res:
                in_str = f'{in_str}{item},'
            str_result.append(['#1', f'To remove --> {in_str[:-1]}', tmp])

        res = Rule2(quadL, tmp)
        if len(res) > 0:
            in_str = ''
            for item in res:
                in_str = f'{in_str}{item},'
            str_result.append(['#2', f'To remove --> {in_str[:-1]}', tmp])

        res = Rule3(quadL, tmp)
        if len(res) > 0:
            in_str = ''
            for item in res:
                in_str = f'{in_str}{item},'
            str_result.append(['#3', f'To remove --> {in_str[:-1]}', tmp])

        res = Rule4(quadL, tmp)
        if len(res) > 0:
            in_str = ''
            for item in res:
                in_str = f'{in_str}{item},'
            str_result.append(['#4', f'To remove --> {in_str[:-1]}', tmp])

        res = Rule5(quadL, tmp)
        if len(res) > 0:
            in_str = ''
            for item in res:
                in_str = f'{in_str}{item},'
            str_result.append(['#5', f'To remove --> {in_str[:-1]}', tmp])

        res = Rule6(quadL, tmp)
        if len(res) > 0:
            in_str = ''
            for item in res:
                in_str = f'{in_str}{item},'
            str_result.append(['#6', f'To remove --> {in_str[:-1]}', tmp])

        res = Rule7(quadL, tmp)
        if len(res) > 0:
            in_str = ''
            for item in res:
                in_str = f'{in_str}{item},'
            str_result.append(['#7', f'To remove --> {in_str[:-1]}', tmp])

        # Rule 8 - 11
        if tmp.neutralElement():
            # res.append(tmp)
            str_result.append(['#8,9,10,11', f'Neutral Element. To remove --> {tmp}', ''])
            continue

        res = Rule12(tmp)
        if res:
            str_result.append(['#12', res, tmp])

        res = Rule13(tmp)
        if res:
            str_result.append(['#13', res, tmp])

        res = Rule14_16_17(tmp)
        if res:
            str_result.append(['#14,16,17', res, tmp])

        res = Rule15_18(tmp)
        if res:
            str_result.append(['#15,18', res, tmp])

        result.append(tmp)
    return [result, [], tabulate(str_result, ['Regla', 'De (Original)', 'Optimizado'], tablefmt="psql")]


def printL(quadL: list):
    for q in quadL:
        print(q)


def strTAC(quadL: list, ntabs):
    r = ''
    tabs = ''
    for i in range(ntabs):
        tabs += getFileTab()
    for q in quadL:
        r += f'{tabs}{q.__str__()}\n'
    return r


def strTAC_pySyntax(quadL: list, ntabs):
    r = ''
    tabs = ''
    for i in range(ntabs):
        tabs += getFileTab()
    for q in quadL:
        tacstr = q.strpy()
        tacstr = tacstr.replace(getFileTab(), f'{getFileTab()}{tabs}')
        r += f'{tabs}{q.strpy()}\n'
    return r


def getHeader():
    return f'from goto import with_goto\nfrom wrapper import *\n\n@with_goto\ndef all_code():\n'


def getFooter():
    return f'#all_code()\n#report_stored_st()\n'


def getFileTab():
    return '    '


def getPlpgFolder():
    if not os.path.exists('data'): os.makedirs('data')
    if not os.path.exists('data/plpgObj'):
        os.makedirs('data/plpgObj')

    # return 'data/plpgObj/'#comment to use the root
    return ''


def getParamNameFormat():
    return '___sys_param_'


# Takes a list of Quadrupes (TAC) aply optimization rules
# Write files .py for DB objects
def Save_TAC_obj(objname: str, quadL: list):
    optimiR = DoOptimization(quadL)
    result = optimiR[0]

    # Writing Report
    opt_report = optimiR[2]
    f = open(f'opt_report.txt', "a")
    # str_report = ''
    # for item_report in opt_report:
    #     str_report = f'{str_report}{item_report}\n'
    content = f'\n+------------- {objname} --------------+\n {opt_report}'
    f.write(content)
    f.close()

    # Writing TAC File
    f = open(f'{getPlpgFolder()}{objname}.py', "w")
    content = getHeader() + strTAC_pySyntax(result, 1) + getFooter()
    f.write(content)
    f.close()


def Rule1(quadL: list, currQuad: Quadruple):
    # Si existe una asignación de valor de la forma a = b y posteriormente existe una asignación de forma b = a,
    # se eliminará la segunda asignación siempre que a no haya cambiado su valor. Se deberá tener la seguridad de que
    # no exista el cambio de valor y no existan etiquetas entre las 2 asignaciones
    removed = []
    if currQuad.isAsigment() and currQuad.arg2 is None:
        for q in quadL:
            # check for tn changed value
            if q.res == currQuad.res:
                return removed
            elif q.isAsigment() and q.arg2 is None and q.arg1 == currQuad.res and q.res == currQuad.arg1:
                quadL.remove(q)
                removed.append(q)
            elif q.isLabel() or q.isGoTo():  # TODO: verifi if goto validation stays here
                return removed
    return removed


def Rule2(quadL: list, currQuad: Quadruple):
    # Si  existe  un  salto  condicional  de  la  forma  Lx  y  exista  una  etiqueta  Lx:,
    # todo  código  contenido entre el goto Lx y la etiqueta Lx, podrá ser eliminado siempre y cuando 
    # no exista una etiqueta en dicho código.
    removed = []
    if currQuad.isGoTo():
        for q in quadL:
            removed.append(q)
            if q.isLabel():
                if q.labelName() == currQuad.labelName():  # remove all instructions between
                    currQuad.instType = OpTAC.LABEL  # TODO store into history
                    for rem in removed:
                        quadL.remove(rem)
                    return removed
                else:  # undo removals
                    return []

    return removed


def Rule3(quadL: list, currQuad: Quadruple):
    # Si existe un alto condicional de la forma if <cond> goto Lv; goto Lf; inmediatamente después de sus  etiquetas
    # Lv:  <instrucciones>Lf:  se  podrá  reducir  el  número  de  saltos  negando  la condición,  cambiando  el  salto
    # condicional  hacia  la  etiqueta  falsa  Lf:  y  eliminando  el  salto condicional innecesario a goto Lf
    # y quitando la etiqueta Lv:.
    removed = []
    if currQuad.isConditional() and 'goto' in currQuad.res:
        if quadL[0].isGoTo() and quadL[1].isLabel():
            currQuad.op = OpRelational.NOT_EQUALS
            currQuad.res = quadL[1].labelName()
            removed.append(quadL.pop(1))
            removed.append(quadL.pop(0))  # two times for indexes 0  and 1

    return removed


def Rule4(quadL: list, currQuad: Quadruple):
    # Si se utilizan valores constantes dentro de las condiciones de la forma if <cond>goto Lv;
    # goto Lf; y el resultado de la condición es una constante verdadera, 
    # se podrá transformar en un salto incondicional y eliminarse el salto hacia la etiqueta falsa Lf.
    removed = []
    if currQuad.isConditional() and currQuad.arg1 == currQuad.arg2 and currQuad.op == OpRelational.EQUALS:
        currQuad.arg1 = currQuad.res.replace('goto', '').replace(' ', '')
        currQuad.arg2 = None
        currQuad.res = None
        currQuad.op = None
        currQuad.instType = OpTAC.GOTO
        if quadL[0].isGoTo():
            removed.append(quadL.pop(0))
    return removed


def Rule5(quadL: list, currQuad: Quadruple):
    # Si se utilizan valores constantes dentro de las condiciones de la forma if <cond> goto Lv; goto Lf;
    # y  el  resultado  de  la  condición  es  una  constante  falsa,  se  podrá  transformar  en  un  
    # salto incondicional y eliminarse el salto hacia la etiqueta verdadera Lv.
    removed = []
    if currQuad.isConditional() and currQuad.allWaysFalse():
        temp = copy.deepcopy(currQuad)
        removed.append(temp)
        poped = quadL.pop(0)
        currQuad.op = poped.op
        currQuad.arg1 = poped.arg1
        currQuad.arg2 = poped.arg2
        currQuad.res = poped.res
        currQuad.instType = poped.instType
    return removed


def Rule6(quadL: list, currQuad: Quadruple):
    # Si  existe  un  salto  incondicional  de  la  forma  goto  Lx  donde  existe  la  etiqueta  Lx:
    # y  la  primera instrucción,  luego  de  la  etiqueta,  es  otro  salto,  de  la  forma  goto  Ly;
    # se  podrá  realizar  la modificación  al  primer  salto  para  que  sea  dirigido  hacia  la  
    # etiqueta  Ly:  ,  para  omitir  el  salto condicional hacia Lx.        
    removed = []
    prev = None
    if currQuad.isGoTo():
        for q in quadL:
            if prev is not None and prev.isLabel() and prev.labelName() == currQuad.labelName():
                if q.isGoTo():
                    currQuad.arg1 = q.arg1
                    removed.append(prev)
                else:
                    break
            prev = q
    return removed


def Rule7(quadL: list, currQuad: Quadruple):
    # Si  existe  un  salto  incondicional  de  la  forma  if  <cond>goto  Lx;  y  existe  la  etiqueta  Lx:
    # y  la primera instrucciones luego de la etiqueta es otro salto, de la forma goto Ly; se podrá realizar
    # la modificación  al  primer  salto  para  que  sea  dirigido  hacia  la  etiqueta  Ly:  , 
    # para  omitir  el  salto condicional hacia Lx
    removed = []
    prev = None
    if currQuad.isConditional():
        for q in quadL:
            if prev is not None and prev.isLabel() and prev.labelName() == currQuad.res:
                if q.isGoTo():
                    currQuad.res = q.arg1
                    removed.append(prev)
                else:
                    break
            prev = q
    return removed


def Rule12(currQuad: Quadruple):
    oldRule = None
    if currQuad.isAsigment() and currQuad.op == OpArithmetic.PLUS:
        if currQuad.arg2 == '0':
            oldRule = copy.copy(currQuad)
            currQuad.arg2 = None
            currQuad.op = None
        elif currQuad.arg1 == '0':
            oldRule = copy.copy(currQuad)
            currQuad.arg1 = currQuad.arg2
            currQuad.arg2 = None
            currQuad.op = None
    return oldRule


def Rule13(currQuad: Quadruple):
    oldRule = None
    if currQuad.isAsigment() and currQuad.op == OpArithmetic.MINUS:
        if currQuad.arg2 == '0':
            oldRule = copy.copy(currQuad)
            currQuad.arg2 = None
            currQuad.op = None
    return oldRule


def Rule14_16_17(currQuad: Quadruple):
    oldRule = None
    if currQuad.isAsigment() and currQuad.op == OpArithmetic.TIMES:
        if currQuad.arg2 == '1':
            oldRule = copy.copy(currQuad)
            currQuad.arg2 = None
            currQuad.op = None
        elif currQuad.arg1 == '1':
            oldRule = copy.copy(currQuad)
            currQuad.arg1 = currQuad.arg2
            currQuad.arg2 = None
            currQuad.op = None
        elif currQuad.arg2 == '2':
            oldRule = copy.copy(currQuad)
            currQuad.arg2 = currQuad.arg1
            currQuad.op = OpArithmetic.PLUS
        elif currQuad.arg1 == '2':
            oldRule = copy.copy(currQuad)
            currQuad.arg1 = currQuad.arg2
            currQuad.op = OpArithmetic.PLUS
        elif currQuad.arg2 == '0' or currQuad.arg1 == '0':
            oldRule = copy.copy(currQuad)
            currQuad.arg2 = None
            currQuad.arg1 = '0'
            currQuad.op = None
    return oldRule


def Rule15_18(currQuad: Quadruple):
    oldRule = None
    if currQuad.isAsigment() and currQuad.op == OpArithmetic.DIVIDE:

        if currQuad.arg2 == '1' or currQuad.arg1 == '0':  # R15, R18
            oldRule = copy.copy(currQuad)
            currQuad.arg2 = None
            currQuad.op = None

    return oldRule


def Rule16(currQuad: Quadruple):
    oldRule = None
    if currQuad.isAsigment() and currQuad.op == OpArithmetic.TIMES:
        if currQuad.arg2 == '1':
            oldRule = copy.copy(currQuad)
            currQuad.arg2 = None
            currQuad.op = None
        elif currQuad.arg1 == '1':
            oldRule = copy.copy(currQuad)
            currQuad.arg1 = currQuad.arg2
            currQuad.arg2 = None
            currQuad.op = None
    return oldRule


# Testing...
'''#Rule 15:
a = Quadruple(OpArithmetic.DIVIDE,'t5','1','t1', OpTAC.ASSIGNMENT)
r = Rule15_18(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.DIVIDE,'1','t6','t1', OpTAC.ASSIGNMENT)
r = Rule15_18(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.DIVIDE,'t5','t7','t1', OpTAC.ASSIGNMENT)
r = Rule15_18(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.DIVIDE,'0','t7','t1', OpTAC.ASSIGNMENT)
r = Rule15_18(a)
print (r,'-->',a)

#Rule 14:
print ('Rule 14:')
a = Quadruple(OpArithmetic.TIMES,'t5','1','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.TIMES,'1','t6','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.TIMES,'t5','t7','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
print ('Rule 16:')
a = Quadruple(OpArithmetic.TIMES,'2','1','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.TIMES,'3','2','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.TIMES,'t5','2','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.TIMES,'2','tx','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
print ('Rule 17:')
a = Quadruple(OpArithmetic.TIMES,'0','1','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.TIMES,'1','0','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.TIMES,'t3','0','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.TIMES,'0','t1','t1', OpTAC.ASSIGNMENT)
r = Rule14_16_17(a)
print (r,'-->',a)
#Rule 13:
a = Quadruple(OpArithmetic.MINUS,'t5','0','t1', OpTAC.ASSIGNMENT)
r = Rule13(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.MINUS,'0','t6','t1', OpTAC.ASSIGNMENT)
r = Rule13(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.MINUS,'t5','t7','t1', OpTAC.ASSIGNMENT)
r = Rule13(a)
print (r,'-->',a)
#Rule 12:
a = Quadruple(OpArithmetic.PLUS,'t5','0','t1', OpTAC.ASSIGNMENT)
r = Rule12(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.PLUS,'0','t6','t1', OpTAC.ASSIGNMENT)
r = Rule12(a)
print (r,'-->',a)
a = Quadruple(OpArithmetic.PLUS,'t5','t7','t1', OpTAC.ASSIGNMENT)
r = Rule12(a)
print (r,'-->',a)
#Rules 8-11
a = Quadruple(OpArithmetic.PLUS,'t1','0','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())
a = Quadruple(OpArithmetic.PLUS,'0','t1','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())
a = Quadruple(OpArithmetic.PLUS,'t1','2','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())
a = Quadruple(OpArithmetic.MINUS,'t1','0','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())
a = Quadruple(OpArithmetic.MINUS,'t1','t34','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())
print('+++++++++')
a = Quadruple(OpArithmetic.TIMES,'t1','1','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())
a = Quadruple(OpArithmetic.TIMES,'1','t1','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())
a = Quadruple(OpArithmetic.TIMES,'t1','0','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())
a = Quadruple(OpArithmetic.DIVIDE,'t1','1','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())
a = Quadruple(OpArithmetic.DIVIDE,'t1','t34','t1', OpTAC.ASSIGNMENT)
print(a.neutralElement())


quad_list = []
#rule2:
#quad_list.append(Quadruple(None,'L3',None,None, OpTAC.GOTO))
#rule3: 
quad_list.append(Quadruple(OpRelational.EQUALS,'t1','10','L1', OpTAC.CONDITIONAL))
quad_list.append(Quadruple(None,'3',None,'t22', OpTAC.ASSIGNMENT))
quad_list.append(Quadruple(None,'2',None,'t33', OpTAC.ASSIGNMENT))

quad_list.append(Quadruple(None, 'L11', None, None, OpTAC.LABEL))
quad_list.append(Quadruple(None, 'L2', None, None, OpTAC.GOTO))
#rule1:
quad_list.append(Quadruple(None,'b',None,'t2', OpTAC.ASSIGNMENT))
quad_list.append(Quadruple(None,'b',None,'t3', OpTAC.ASSIGNMENT))
quad_list.append(Quadruple(None, 'L3', None, None, OpTAC.LABEL))
quad_list.append(Quadruple(None, 'L4', None, None, OpTAC.GOTO))
quad_list.append(Quadruple(None,'t2',None,'b', OpTAC.ASSIGNMENT))
quad_list.append(Quadruple(None,'b',None,'t2', OpTAC.ASSIGNMENT))
quad_list.append(Quadruple(None,'t2',None,'b', OpTAC.ASSIGNMENT))

peephole = quad_list.pop(0)
op = Rule7(quad_list,peephole)
#op = Rule1(quad_list,peephole)
#op = Rule3(quad_list,peephole)
print('Optimizado: ',op)
print(peephole)
for q in quad_list:
    print (q)

'''
