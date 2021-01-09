from Instrucciones.Ifclass import Ifclass
from Instrucciones.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Expresion.Relacional import Relacional

class Case(Instruccion):
    def __init__(self,exp=None,cases=None,celse=None):
        self.exp=exp
        self.cases=cases
        self.celse=celse

    def ejecutar(self, ent):
        'ejecucion del case'
        if self.exp!=None:
            for case in self.cases:
                cond=Relacional(self.exp,case.exp,'=')
                if cond.getval(ent).valor:
                    newent = Entorno(ent)
                    for ins in case.instr:
                        val=ins.ejecutar(newent)
                        if val!=None:
                            return val
                    return
        else:
            for case in self.cases:
                if case.exp.getval(ent).valor:
                    newent = Entorno(ent)
                    for ins in case.instr:
                        val = ins.ejecutar(newent)
                        if val != None:
                            return val
                    return

        if self.celse!=None:
            newent = Entorno(ent)
            for ins in self.celse:
                val = ins.ejecutar(newent)
                if val != None:
                    return val



    def traducir(self,entorno):
        sql = 'case '
        if self.exp!=None:
            sql+=self.exp.traducir(entorno).stringsql+' '

        for case in self.cases:
            sql+='when '+case.exp.traducir(entorno).stringsql+' then '
            for inst in case.instr:
                sql+=inst.traducir(entorno).stringsql

        if self.celse != None:
            sql += ' else '
            for inst in self.celse:
                sql += inst.traducir(entorno).stringsql

        sql += 'end case;'
        self.stringsql = sql


        if self.exp != None:
            lelifs = []
            for case in self.cases:
                cond = Relacional(self.exp, case.exp, '=')
                lelifs.append(Ifclass(cond,case.instr,None,None))

            if self.celse!=None:
                tmp = None
                for i in range(len(lelifs) - 1, -1, -1):
                    inst = lelifs[i]
                    if i == len(lelifs) - 1:
                        inst = Ifclass(inst.exp, inst.cif, inst.elsif, self.celse)
                    else:
                        inst = Ifclass(inst.exp, inst.cif, inst.elsif, [tmp])
                    tmp = inst
                cad = tmp.traducir(entorno).codigo3d
                self.codigo3d = cad
            else:
                tmp = None
                for i in range(len(lelifs) - 1, -1, -1):
                    inst = Ifclass(inst.exp, inst.cif, inst.elsif, [tmp])
                tmp = inst
                cad = tmp.traducir(entorno).codigo3d
                self.codigo3d = cad
        else:
            lelifs = []
            for case in self.cases:
                lelifs.append(Ifclass(case.exp, case.instr, None, None))

            if self.celse != None:
                tmp = None
                for i in range(len(lelifs) - 1, -1, -1):
                    inst = lelifs[i]
                    if i == len(lelifs) - 1:
                        inst = Ifclass(inst.exp, inst.cif, inst.elsif, self.celse)
                    else:
                        inst = Ifclass(inst.exp, inst.cif, inst.elsif, [tmp])
                    tmp = inst
                cad = tmp.traducir(entorno).codigo3d
                self.codigo3d = cad
            else:
                tmp = None
                for i in range(len(lelifs) - 1, -1, -1):
                    inst = Ifclass(inst.exp, inst.cif, inst.elsif, [tmp])
                tmp = inst
                cad = tmp.traducir(entorno).codigo3d
                self.codigo3d = cad

        return self

class when():
    def __init__(self, exp,instr):
        self.exp = exp
        self.instr=instr
