from analizer_pl.abstract.instruction import Instruction
from analizer_pl.abstract.expression import TYPE
from analizer_pl.statement.expressions import code
from analizer_pl.abstract.environment import Environment
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo

amb = 0


class Case(Instruction):
    def __init__(self, expBool, blockStmt, elseCase, elseStmt, row, column) -> None:
        super().__init__(row, column)
        self.expBool = expBool
        self.blockStmt = blockStmt
        self.elseCase = elseCase
        self.elseStmt = elseStmt
        self.codigo = ""
        self.ambito = amb

    def execute(self, environment):
        global amb
        amb += 1
        self.ambito = amb
        contLabel = 1
        c3d = ""
        var = self.expBool.execute(environment)
        c3d += var.value
        c3d += "\tif " + var.temp + ": goto .labelCase0" + str(self.ambito) + " \n"
        c3d += "\tgoto .labelCase1" + str(self.ambito) + "\n"

        if self.elseCase != None:
            for ec in self.elseCase:
                c3d += "\tlabel .labelCase" + str(contLabel) + str(self.ambito) + "\n"
                contLabel += 1
                cdtemp = ec[0].execute(environment)
                c3d += cdtemp.value
                c3d += (
                    "\tif "
                    + cdtemp.temp
                    + ": goto .labelCase"
                    + str(contLabel)
                    + str(self.ambito)
                    + "\n"
                )
                contLabel += 1
                c3d += "\tgoto .labelCase" + str(contLabel) + str(self.ambito) + "\n"

            contLabel = 0
        blockCad = ""
        for bs in self.blockStmt:
            blockCad += bs.execute(environment).value
        c3d += (
            "\tlabel .labelCase0"
            + str(self.ambito)
            + "\n"
            + blockCad
            + "\tgoto .labelCaseEnd"
            + str(self.ambito)
            + " \n"
        )  # contenido del primer case
        if self.elseCase != None:
            for ec2 in self.elseCase:
                contLabel += 2
                blockCad2 = ""
                for e in ec2[1]:
                    blockCad2 += e.execute(environment).value
                c3d += (
                    "\tlabel .labelCase"
                    + str(contLabel)
                    + str(self.ambito)
                    + "\n"
                    + blockCad2
                    + "\tgoto .labelCaseEnd"
                    + str(self.ambito)
                    + " \n"
                )  # contenido del case

            contLabel += 1
        els = ""

        if self.elseStmt:
            els += self.elseStmt.execute(environment).value

        c3d += (
            "\tlabel .labelCase" + str(contLabel) + str(self.ambito) + "\n" + els
        )  # contenido del else
        c3d += "\tlabel .labelCaseEnd" + str(self.ambito) + "\n"  # etiqueta final

        self.codigo = c3d
        return code.C3D(c3d, "case", self.row, self.column)

    def dot(self):
        new = Nodo("CASE")
        when = Nodo("WHEN")
        new.addNode(when)

        when.addNode(self.expBool.dot())
        then = Nodo("THEN")
        when.addNode(then)
        for bs in self.blockStmt:

            then.addNode(bs.dot())

        if self.elseCase:
            for ec in self.elseCase:
                w = Nodo("WHEN")
                new.addNode(w)
                w.addNode(ec[0].dot())
                t = Nodo("THEN")
                w.addNode(t)
                for i in ec[1]:
                    t.addNode(i.dot())
        if self.elseStmt:
            new.addNode(self.elseStmt.dot())
        return new