from analizer_pl.abstract.expression import Expression
from analizer_pl.abstract.expression import TYPE
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment


class FunctionCall(Expression):
    def __init__(self, id, params, isBlock, temp, row, column) -> None:
        super().__init__(row, column)
        self.id = id
        self.params = params
        self.isBlock = isBlock
        self.temp = temp

    def execute(self, environment):
        c3d = ""
        tab = ""
        # Si es para PL/SQL
        if self.isBlock:
            if isinstance(environment, Environment):
                tab += "\t"
                func = environment.globalEnv.getFunction(self.id)
            else:
                func = environment.getFunction(self.id)
            # Si es una funcion definida
            if func:
                if self.params:
                    if len(self.params) == func.params:
                        # Se meten al reves los parametros en la pila
                        self.params.reverse()
                        for p in self.params:
                            pval = p.execute(environment)
                            c3d += pval.value
                            c3d += tab + "stack.append(" + pval.temp + ")\n"
                        c3d += tab + self.id + "()\n"
                        c3d += tab + "t" + self.temp + " = stack.pop()\n"
                        self.temp = "t" + self.temp
                    else:
                        # TODO: ERROR: parametros no coinciden
                        pass
            # Si es una funcion matematica
            else:
                pass
        # Si es para el parser
        else:
            if isinstance(environment, Environment):
                tab += "\t"
                func = environment.globalEnv.getFunction(self.id)
            else:
                func = environment.getFunction(self.id)
            # Si es una funcion definida
            if func:
                if self.params:
                    if len(self.params) == func.params:
                        # Se meten al reves los parametros en la pila
                        self.params.reverse()
                        for p in self.params:
                            pval = p.execute(environment)
                            c3d += pval.value
                            c3d += tab + "stack.append(" + pval.temp + ")\n"
                        c3d += tab + self.id + "()\n"
                        c3d += tab + "t" + self.temp + " = stack.pop()\n"
                        self.temp = '"+t' + self.temp + '+"'
                    else:
                        # TODO: ERROR: parametros no coinciden
                        pass
            # Si es una funcion matematica
            else:
                pass
        return code.C3D(c3d, self.temp, self.row, self.column)
